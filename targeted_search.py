#!/usr/bin/env python3
"""
Targeted Green Field Search - Find specific health/wellness niches
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

def analyze_gap(query, apps, category, growth):
    total_reviews = sum(a.get("userRatingCount", 0) for a in apps[:10])
    
    # Check for pollution (wrong categories)
    pollution = 0
    for a in apps[:5]:
        genre = a.get("primaryGenreName", "").lower()
        if category == "health" and "game" in genre:
            pollution += 1
    
    if pollution >= 3:
        return 9, "pollution", total_reviews, 2  # Build 2h for pollution
    elif len(apps) == 0:
        return 10, "green_field", 0, 2
    elif total_reviews < 500:
        return 8, "low_competition", total_reviews, 3
    elif total_reviews < 2000:
        return 6, "some_competition", total_reviews, 3
    else:
        return 5, "saturated", total_reviews, 4

# HEALTH & WELLNESS niches with specific angles
health_niches = [
    ("Facial Depuffing Protocol", "health", 7800, "depuffing wand protocol"),
    ("Hypochlorous Acid Spray Scheduling", "health", 8000, "hypochlorous spray schedule"),
    ("Wolverine Peptide Dosing Guide", "health", 8500, "wolverine peptide dosing"),
    ("Biohacker Peptide Tracker", "health", 8500, "biohacker peptide"),
    ("Hair Loss Peptide Cycle", "health", 8500, "hair loss peptide cycle"),
    ("Circadian Rhythm Lighting App", "health", 5000, "circadian lighting"),
    ("Deep Work Session Optimizer", "health", 5000, "deep work optimizer"),
    ("Blue Light Screen Time Manager", "health", 3800, "blue light screen manager"),
]

# TECH niches
tech_niches = [
    ("Antidetect Browser Setup Guide", "tech", 2100, "antidetect browser guide"),
    ("Answer Engine SEO Tool", "tech", 7500, "answer engine seo tool"),
    ("AI Agent Orchestration Guide", "tech", 5600, "ai agent orchestration"),
    ("Programmatic SEO Builder", "tech", 8300, "programmatic seo builder"),
    ("Fractional COO Operations Manual", "business", 7600, "fractional coo manual"),
    ("AI Token Cost Optimizer", "tech", 3600, "ai token optimizer"),
    ("Workflow Automation Playbook", "tech", 5000, "workflow automation playbook"),
]

print("TARGETED GREEN FIELD SEARCH")
print("=" * 70)

results = []

for name, category, growth, query in health_niches + tech_niches:
    print(f"\n{name}")
    data = itunes_search(query)
    
    if "error" in data:
        continue
    
    apps = data.get("results", [])
    gap, gap_name, reviews, build = analyze_gap(query, apps, category, growth)
    
    # Score calculation
    trend = min(10, growth / 500)
    if category == "health":
        evergreen = 8
        money = 7
    elif category == "education":
        evergreen = 8
        money = 6
    else:
        evergreen = 5
        money = 6
    
    build_simple = 7 if build <= 2 else 5
    avg = (trend + gap + build_simple + evergreen + money) / 5
    
    # Scoring inflation correction
    if avg >= 9.5:
        final_avg = round(8.0 + (avg - 9.5), 1)
    elif avg >= 8.5:
        final_avg = round(7.5 + (avg - 8.5), 1)
    else:
        final_avg = round(avg, 1)
    
    print(f"  Gap: {gap_name} ({gap}), Reviews: {reviews:,}, Build: {build}h, Score: {final_avg}/10")
    
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
            "reviews": reviews,
            "query": query
        })
    
    time.sleep(0.5)

# Sort by score
results.sort(key=lambda x: x['final_avg'], reverse=True)

print("\n" + "=" * 70)
print("VALID CANDIDATES (avg >= 7.0)")
print("=" * 70)
for i, r in enumerate(results, 1):
    print(f"{i}. {r['name']} — {r['final_avg']}/10 | {r['gap_name']} | Build: {r['build_time']}h")

# Save top 3
top3 = results[:3]
with open("/tmp/greenfield_candidates.json", "w") as f:
    json.dump(top3, f, indent=2)

print(f"\n{len(top3)} candidates ready")