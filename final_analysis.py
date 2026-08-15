#!/usr/bin/env python3
"""
Final Candidate Scoring and Selection
"""
import json
import urllib.request
import urllib.parse
import time
from datetime import datetime

def itunes_search(query):
    url = f"https://itunes.apple.com/search?term={urllib.parse.quote(query)}&entity=software&limit=50&country=us"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        return {"error": str(e), "results": []}

def score_candidate(name, growth, gap_score, build_time, category):
    """Score on 5 dimensions."""
    trend = min(10, max(1, growth / 500))
    gap = gap_score
    build_simple = 7 if build_time <= 2 else 5 if build_time <= 3 else 3
    evergreen = 8 if category in ["health", "education"] else 5
    money = 7 if category == "health" else 6
    
    avg = (trend + gap + build_simple + evergreen + money) / 5
    
    # Validate scoring inflation
    if avg >= 9.5:
        final_avg = round(8.0 + (avg - 9.5), 1)
    elif avg >= 8.5:
        final_avg = round(7.5 + (avg - 8.5), 1)
    else:
        final_avg = round(avg, 1)
    
    return {
        "trend": round(trend, 1),
        "gap": gap,
        "build": build_simple,
        "evergreen": evergreen,
        "money": money,
        "final_avg": final_avg
    }

def analyze_gap(apps, category):
    """Analyze gap signal from iTunes results."""
    total_reviews = sum(a.get("userRatingCount", 0) for a in apps[:10])
    
    # Check for search pollution
    pollution = 0
    for a in apps[:5]:
        genre = a.get("primaryGenreName", "").lower()
        if category == "health" and "game" in genre:
            pollution += 1
        if category in ["tech", "business"] and genre in ["games", "music", "entertainment"]:
            pollution += 1
    
    if pollution >= 3:
        return 9, "pollution", total_reviews
    elif len(apps) == 0:
        return 10, "green_field", total_reviews
    elif total_reviews < 500:
        return 8, "low_competition", total_reviews
    elif total_reviews < 2000:
        return 6, "some_competition", total_reviews
    else:
        return 5, "saturated", total_reviews

# Candidate topics with app angles
candidates = [
    # Health/Supplement guides
    {"name": "Wolverine Peptide Guide", "growth": 8500, "category": "health", "query": "Wolverine Peptide"},
    {"name": "Depuffing Wand Guide", "growth": 7800, "category": "health", "query": "Depuffing Wand"},
    {"name": "Hypochlorous Acid Spray Guide", "growth": 8000, "category": "health", "query": "Hypochlorous Acid Spray Guide"},
    {"name": "PDRN Skincare Protocol", "growth": 7600, "category": "health", "query": "PDRN skincare protocol"},
    
    # Tech/Business tools
    {"name": "Fractional COO Finder", "growth": 7600, "category": "business", "query": "Fractional COO business"},
    {"name": "Antidetect Browser Guide", "growth": 2100, "category": "tech", "query": "Antidetect Browser privacy"},
    
    # Education
    {"name": "AI Teacher Assistant App", "growth": 3600, "category": "education", "query": "AI teacher assistant app"},
    
    # Consumer angles
    {"name": "Hair Loss Peptide Tracker", "growth": 8500, "category": "health", "query": "hair loss peptide app"},
    {"name": "Facial Wand Efficacy", "growth": 7800, "category": "health", "query": "facial depuffing wand results"},
]

print("Comprehensive Candidate Analysis")
print("=" * 70)

valid_candidates = []

for c in candidates:
    print(f"\nQuery: {c['name']}")
    data = itunes_search(c['query'])
    
    if "error" in data:
        print(f"  Error: {data['error']}")
        continue
    
    apps = data.get("results", [])
    gap_score, gap_signal, reviews = analyze_gap(apps, c['category'])
    
    # Build time estimate
    if gap_signal in ["pollution", "green_field"]:
        build_time = 2
    elif reviews < 500:
        build_time = 3
    else:
        build_time = 3  # Still viable if focused
    
    scores = score_candidate(c['name'], c['growth'], gap_score, build_time, c['category'])
    
    print(f"  Apps: {len(apps)}, Reviews: {reviews:,}, Gap: {gap_signal} ({gap_score})")
    print(f"  Score: {scores['final_avg']}/10 | Trend:{scores['trend']} Gap:{gap_score} Build:{build_time}h")
    
    if scores['final_avg'] >= 7.0:
        valid_candidates.append({
            "name": c['name'],
            "scores": scores,
            "growth": c['growth'],
            "build_time": build_time,
            "gap_signal": gap_signal,
            "gap_score": gap_score,
            "category": c['category'],
            "total_reviews": reviews
        })
    
    time.sleep(1)

# Sort by final score
valid_candidates.sort(key=lambda x: x['scores']['final_avg'], reverse=True)

print("\n" + "=" * 70)
print("TOP VALID CANDIDATES (avg >= 7.0)")
print("=" * 70)
for i, c in enumerate(valid_candidates[:5], 1):
    s = c['scores']
    print(f"{i}. {c['name']}")
    print(f"   Final: {s['final_avg']}/10 | Growth: {c['growth']}% | Build: {c['build_time']}h | Gap: {c['gap_signal']}")

# Save for next step
with open("/tmp/final_candidates.json", "w") as f:
    json.dump(valid_candidates, f, indent=2)

print(f"\n{len(valid_candidates)} valid candidates saved")