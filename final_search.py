#!/usr/bin/env python3
"""
FINAL CANDIDATE DISCOVERY - Find truly unique app opportunities
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

def genre_check(cat, app):
    genre = app.get("primaryGenreName", "").lower()
    if cat == "health" and "game" in genre:
        return True
    if cat in ["tech", "business"] and genre in ["games", "music", "entertainment"]:
        return True
    return False

def analyze_gap(apps, category):
    total_reviews = sum(a.get("userRatingCount", 0) for a in apps[:10])
    pollution = sum(1 for a in apps[:5] if genre_check(category, a))
    
    if pollution >= 3:
        return 9, "pollution", total_reviews
    elif len(apps) == 0:
        return 10, "green_field", total_reviews
    elif total_reviews < 500:
        return 8, "low_competition", total_reviews
    elif total_reviews < 2000:
        return 6, "some_comp", total_reviews
    else:
        return 5, "saturated", total_reviews

def score_candidate(growth, gap, build_time, category):
    trend = min(10, growth / 500)
    avg = (trend + gap + build_time + (8 if category in ["health", "education"] else 5) + (7 if category == "health" else 6)) / 5
    
    if avg >= 9.5:
        final_avg = round(8.0 + (avg - 9.5), 1)
    elif avg >= 8.5:
        final_avg = round(7.5 + (avg - 8.5), 1)
    else:
        final_avg = round(avg, 1)
    
    return final_avg

# FRESH trends with unique angles NOT in data.json
# Based on Exploding Topics trending list and gap analysis
candidates = [
    # TECHNOLOGY - NOT COVERED
    ("Baselane Growth Platform Guide", "tech", 9000),
    ("AI CoPilot Companion", "tech", 5600),  # Personal assistant angle
    ("Hall Effect Joystick Guide", "tech", 5600),  # Specific hardware guide
    ("Laptop Screen Extender Setup", "tech", 2700),  # Setup guide
    ("Workflow Automation Templates", "tech", 5000),  # Template collection
    
    # HEALTH/WELLNESS - NOT COVERED
    ("Depuffing Wand Guide", "health", 7800),  # NOT in data.json
    ("Wolverine Peptide Protocol", "health", 8500),  # Protocol vs companion
    ("Hair Loss Prevention Checklist", "health", 8500),  # Different angle
    ("Circadian Rhythm Optimiser", "health", 5000),  # Wellness optimization
    ("Deep Work Focus Timer", "health", 5000),  # Productivity focus
    
    # BUSINESS/TOOLS
    ("Fractional COO Onboarding", "business", 7600),  # Different angle
    ("Startup Growthstack Guide", "business", 5900),  # Agricultural marketplace angle
    
    # EDUCATION/PROFESSIONAL
    ("AI for Teachers Resource", "education", 3600),  # Resource vs assistant
]

print("FINAL CANDIDATE DISCOVERY")
print("=" * 70)

results = []
for name, category, growth in candidates:
    print(f"\n{name}")
    data = itunes_search(name)
    
    if "error" in data:
        print(f"  Error: {data['error']}")
        continue
    
    apps = data.get("results", [])
    gap, gap_name, reviews = analyze_gap(apps, category)
    build = 2 if gap_name in ["pollution", "green_field"] else (3 if reviews < 1000 else 4)
    final_avg = score_candidate(growth, gap, build, category)
    
    print(f"  Apps: {len(apps)}, Reviews: {reviews:,}, Gap: {gap_name} ({gap}), Final: {final_avg}/10")
    
    if final_avg >= 7.0:
        results.append({
            "name": name,
            "category": category,
            "growth": growth,
            "final_avg": final_avg,
            "gap": gap,
            "gap_name": gap_name,
            "build_time": build,
            "apps": len(apps),
            "reviews": reviews
        })
    
    time.sleep(1)

# Sort and deduplicate
results.sort(key=lambda x: x['final_avg'], reverse=True)

print("\n" + "=" * 70)
print("TOP 5 VALID CANDIDATES (avg >= 7.0)")
print("=" * 70)
for i, r in enumerate(results[:5], 1):
    print(f"{i}. {r['name']} — {r['final_avg']}/10 | {r['gap_name']} | Build: {r['build_time']}h | Growth: {r['growth']}%")

with open("/tmp/top5_candidates.json", "w") as f:
    json.dump(results[:3], f, indent=2)

print(f"\nTop 3 saved to /tmp/top5_candidates.json")