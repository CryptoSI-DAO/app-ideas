#!/usr/bin/env python3
"""
Broad Candidate Discovery - Find diverse app opportunities
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

# Broader range of topics
candidates = [
    # Health/Supplement topics (high growth)
    ("Suri Toothbrush Guide", "health", 7300),
    ("Nicotine Pouches Tracker", "health", 863),
    ("Pupscle Dog Treat Toy Guide", "health", 2300),
    # Tech topics with gaps
    ("AI Personal Assistant Companion", "tech", 5600),
    ("Backlink Building Guide", "tech", 220),
    ("Passwordless Auth Setup", "tech", 386),
    ("Workflow Automation Templates", "tech", 5000),
    # Education
    ("AI for Teachers Handbook", "education", 3600),
    ("Teacher Assistant App", "education", 3600),
    # Creative/Supplement
    ("Lash Cluster Application Guide", "health", 6000),
    ("Ionic Hair Dryer Tips", "health", 9200),
    # Shopping/Lifestyle
    ("Barrel Leg Pants Guide", "lifestyle", 8500),
    ("Low Rise Sweatpants Guide", "lifestyle", 1275),
    ("Satin Bonnet Styling Tips", "lifestyle", 214),
    # Unique angles
    ("Airplane Phone Holder Guide", "tech", 4200),
    ("Laptop Screen Extender Setup", "tech", 2700),
    ("Hall Effect Joystick Guide", "tech", 5600),
]

print("BROAD CANDIDATE DISCOVERY")
print("=" * 70)

results = []
for name, category, growth in candidates:
    data = itunes_search(name)
    apps = data.get("results", [])
    
    if "error" in data:
        continue
    
    gap, gap_name, reviews = analyze_gap(apps, category)
    build = 2 if gap_name in ["pollution", "green_field"] else (3 if reviews < 1000 else 4)
    final_avg = score_candidate(growth, gap, build, category)
    
    print(f"{name}: {final_avg}/10 | Gap:{gap}({gap_name}) | Build:{build}h | {len(apps)} apps, {reviews} reviews")
    
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
    
    time.sleep(0.5)

# Sort and deduplicate
seen = set()
unique_results = []
for r in results:
    key = r['name'][:30]
    if key not in seen:
        seen.add(key)
        unique_results.append(r)

unique_results.sort(key=lambda x: x['final_avg'], reverse=True)

print("\n" + "=" * 70)
print("TOP 5 VALID CANDIDATES")
print("=" * 70)
for i, r in enumerate(unique_results[:5], 1):
    print(f"{i}. {r['name']} — {r['final_avg']}/10 | Build: {r['build_time']}h | Gap: {r['gap_name']}")

with open("/tmp/broad_results.json", "w") as f:
    json.dump(unique_results, f, indent=2)