#!/usr/bin/env python3
"""
Final Candidate Discovery - Find NEW unique app opportunities
"""
import json
import urllib.request
import urllib.parse
import time

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
    if cat == "tech" and genre in ["games", "music", "entertainment"]:
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
    avg = (trend + gap + build_time + (8 if category == "health" else 5) + 6) / 5
    
    # Scoring inflation correction
    if avg >= 9.5:
        final_avg = round(8.0 + (avg - 9.5), 1)
    elif avg >= 8.5:
        final_avg = round(7.5 + (avg - 8.5), 1)
    else:
        final_avg = round(avg, 1)
    
    return final_avg

# NEW opportunities NOT in data.json
# Checking specific angles to avoid existing ideas
new_ideas = [
    # Trending topics with unique app angles
    ("Depuffing Wand Guide", "health", 7800),  # NOT in data.json
    ("Wolverine Peptide Protocol", "health", 8500),  # Protocol angle is different from existing companion
    ("Hair Loss Prevention Checklist", "health", 8500),  # Different from "Hair Loss Peptide Tracker"
    ("Circadian Rhythm Optimiser", "health", 5000),  # New wellness angle
    ("Deep Work Timer Pro", "health", 5000),  # Similar to Focus Sleeper but productivity-focused
    # Tech with consumer angles
    ("AI Observability Dashboard App", "tech", 9300),  # Dashboard angle
    ("Programmatic SEO Builder", "tech", 8300),  # Builder/tool angle
]

print("NEW CANDIDATE DISCOVERY")
print("=" * 70)

results = []
for name, category, growth in new_ideas:
    print(f"\nQuery: {name}")
    data = itunes_search(name)
    apps = data.get("results", [])
    
    if "error" in data:
        print(f"  Error: {data['error']}")
        continue
    
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

# Sort and show top 3
results.sort(key=lambda x: x['final_avg'], reverse=True)
print("\n" + "=" * 70)
print("TOP 3 CANDIDATES (avg >= 7.0)")
print("=" * 70)
for i, r in enumerate(results[:3], 1):
    s = r['scores'] if 'scores' in r else {}
    print(f"{i}. {r['name']} — Score: {r['final_avg']}/10")
    print(f"   Growth: {r['growth']}%, Build: {r['build_time']}h, Gap: {r['gap_name']}")

# Save top 3
top3 = results[:3]
with open("/tmp/top3_candidates.json", "w") as f:
    json.dump(top3, f, indent=2)

print(f"\nReady top 3 candidates loaded")