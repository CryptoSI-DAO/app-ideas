#!/usr/bin/env python3
"""
Daily App Store Research Pipeline
- Scans trending topics
- Checks for duplicates vs data.json
- Runs iTunes Search API gap analysis
- Scores and ranks candidates
- Generates requirements docs
"""

import json
import urllib.request
import urllib.parse
import time
import re
from datetime import datetime
from typing import List, Dict, Optional
import os

# Known existing ideas from data.json (extracted core concepts)
EXISTING_IDEAS = [
    "ai ethics", "video generator", "voice detector", "gummies", "baby bottle washer", 
    "hypochlorous acid spray", "red light therapy", "pdrn", "prompt engineering", 
    "seed oil scanner", "walking pad", "padel", "ai interior design", "ai shoes",
    "focus sleeper", "interval workout", "pasta shapes", "scoville heat", "spice substitution",
    "sleep hygiene", "contrast therapy", "food shelf life", "privacy rights", "lunar calendar",
    "digital wellness", "creatine tracker", "walkdesk", "food holiday guide", "love island",
    "gaming event tracker", "screwworm", "aurora photo", "world cup meals", "food holiday calendar",
    "persepolis", "architecture wonder", "ringwise", "sober sips", "pawplate", "belmont stakes",
    "love island tracker", "caffeine tracker", "persona 6", "broadway tony", "reptile id",
    "air fryer recipe", "pickleball scorekeeper", "petlife journal", "head spa", "creat rack gummy",
    "padel 101", "magnesium tracker", "ai teacher assistant", "travel packing checklist",
    "microhabit", "prompt craft", "vaccine log", "contrast therapy protocol", "car seat safety",
    "baby reflux", "scent safe", "synstack", "pupprep", "bottle hygiene", "baby first foods",
    "probiotic soda", "ai ethics guide", "red light therapy guide", "deepvoice", "creatine gummies",
    "ai air fryer recipes", "magnesium glycinate", "pdrn skincare", "nmn supplement", "baby bottle washer"
]

# Trending topics from Exploding Topics (with growth %)
TRENDING_TOPICS = [
    {"rank": 1, "name": "Antidetect Browser", "growth": 2100, "category": "tech"},
    {"rank": 2, "name": "Fractional COO", "growth": 7600, "category": "business"},
    {"rank": 3, "name": "Answer Engine Optimization", "growth": 7500, "category": "tech"},
    {"rank": 4, "name": "AI Observability", "growth": 9300, "category": "tech"},
    {"rank": 5, "name": "Baselane", "growth": 9000, "category": "tech"},
    {"rank": 6, "name": "UGC Creator", "growth": 8600, "category": "tech"},
    {"rank": 7, "name": "MoreLogin", "growth": 8900, "category": "tech"},
    {"rank": 8, "name": "Wolverine Peptide", "growth": 8500, "category": "health"},
    {"rank": 9, "name": "Depuffing Wand", "growth": 7800, "category": "health"},
    {"rank": 10, "name": "Color Drenching Paint", "growth": 7500, "category": "lifestyle"},
    {"rank": 11, "name": "Owala", "growth": 8600, "category": "lifestyle"},
    {"rank": 12, "name": "Plaud Note", "growth": 5700, "category": "tech"},
    {"rank": 13, "name": "NoteGPT", "growth": 6300, "category": "tech"},
    {"rank": 14, "name": "AI Personal Assistant", "growth": 5600, "category": "tech"},
    {"rank": 15, "name": "Walk While Working", "growth": 8700, "category": "health"},
    {"rank": 16, "name": "Agricultural Marketplace", "growth": 5900, "category": "tech"},
    {"rank": 17, "name": "Prompt Engineering", "growth": 6000, "category": "tech"},
    {"rank": 18, "name": "AI for Teachers", "growth": 3600, "category": "education"},
    {"rank": 19, "name": "Suri Toothbrush", "growth": 7300, "category": "health"},
]

def is_duplicate(topic: str) -> bool:
    """Check if topic is already covered by existing apps."""
    topic_lower = topic.lower()
    for existing in EXISTING_IDEAS:
        if existing in topic_lower or topic_lower in existing:
            return True
    return False

def itunes_search(query: str) -> Dict:
    """Query iTunes Search API."""
    url = f"https://itunes.apple.com/search?term={urllib.parse.quote(query)}&entity=software&limit=50&country=us"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        return {"error": str(e), "results": []}

def score_candidate(topic: Dict, gap_score: int, build_time: int, category: str) -> Dict:
    """Score a candidate on 5 dimensions."""
    # Trend Momentum (1-10 based on growth %)
    trend = min(10, max(1, topic["growth"] / 500))
    
    # App Gap (from gap analysis)
    gap = gap_score
    
    # Build Simplicity (1-10) - estimate based on complexity
    # Simple reference/content app = 8-10, tracker = 6-8, utility = 4-6
    if category in ["health", "education"]:
        build_simple = 6 if build_time == 2 else 5 if build_time == 3 else 4
    else:
        build_simple = 7 if build_time == 2 else 6 if build_time == 3 else 5
    
    # Evergreen Potential (1-10)
    evergreen = 8 if category in ["health", "education"] else 6
    
    # Monetization (1-10)
    money = 7 if category == "health" else 6
    
    avg = (trend + gap + build_simple + evergreen + money) / 5
    
    return {
        "trend": round(trend, 1),
        "gap": gap,
        "build": build_simple,
        "evergreen": evergreen,
        "money": money,
        "avg": round(avg, 1)
    }

# Main analysis
print("=" * 60)
print("DAILY APP STORE RESEARCH PIPELINE")
print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
print("=" * 60)

print("\n[STEP 1] Trending Topics Analysis")
print("-" * 40)

candidates = []
for topic in TRENDING_TOPICS:
    is_dup = is_duplicate(topic["name"])
    status = "EXISTS" if is_dup else "NEW"
    print(f"  {topic['rank']:2}. {topic['name']:<30} Growth: {topic['growth']:>5}% | {status}")
    
    if not is_dup:
        candidates.append(topic.copy())  # Copy to avoid modifying original

print(f"\nNew opportunities after dedup: {len(candidates)}")

# iTunes API gap analysis for top candidates by growth
print("\n[STEP 2] iTunes Gap Analysis")
print("-" * 40)

# Sort by growth to prioritize
candidates.sort(key=lambda x: x["growth"], reverse=True)

# Limit to 10 candidates for API rate limits
api_candidates = candidates[:10]

for i, topic in enumerate(api_candidates):
    print(f"\nQuery {i+1}: {topic['name']}")
    data = itunes_search(topic['name'])
    
    if "error" in data:
        print(f"  Error: {data['error']}")
        topic["gap_signal"] = "error"
        topic["total_reviews"] = 0
        topic["build_time"] = 2
        continue
    
    results = data.get("results", [])
    total_reviews = sum(r.get("userRatingCount", 0) for r in results[:10])
    
    # Check for search pollution (results in completely wrong categories)
    pollution_count = 0
    for r in results[:5]:
        genre = r.get("primaryGenreName", "").lower()
        name = r.get("trackName", "").lower()
        # If topic is tech/AI but results are games or entertainment
        if topic["category"] == "tech":
            if "game" in genre:
                pollution_count += 1
        if topic["category"] in ["health", "education"]:
            if "game" in genre or "music" in genre:
                pollution_count += 1
    
    # Gap analysis
    if pollution_count >= 3:
        gap_signal = "pollution"
        gap_score = 9
    elif len(results) == 0:
        gap_signal = "green_field"
        gap_score = 10
    elif total_reviews < 500:
        gap_signal = "low_competition"
        gap_score = 8
    elif total_reviews < 2000:
        gap_signal = "competition"
        gap_score = 5
    else:
        gap_signal = "saturated"
        gap_score = 3
    
    # Build time estimate
    if gap_signal in ["pollution", "green_field"]:
        build_time = 2  # Simple reference app
    else:
        build_time = 3 if total_reviews < 1000 else 4
    
    print(f"  Results: {len(results)} apps, {total_reviews:,} reviews")
    print(f"  Gap: {gap_signal} (score: {gap_score}), Build time: {build_time}h")
    
    topic["itunes_data"] = data
    topic["gap_signal"] = gap_signal
    topic["total_reviews"] = total_reviews
    topic["build_time"] = build_time
    topic["gap_score"] = gap_score
    
    time.sleep(1.0)  # Respect rate limits

# Score all candidates
print("\n[STEP 3] Scoring Candidates")
print("-" * 40)

scored_candidates = []
for topic in candidates:
    if "gap_signal" not in topic:
        continue
    
    scores = score_candidate(topic, topic["gap_score"], topic["build_time"], topic["category"])
    topic["scores"] = scores
    
    # Scoring inflation validation (per 2026-07-03 correction)
    if scores["avg"] >= 9.5:
        scores["final_avg"] = round(8.0 + (scores["avg"] - 9.5), 1)
    elif scores["avg"] >= 8.5:
        scores["final_avg"] = round(7.5 + (scores["avg"] - 8.5), 1)
    else:
        scores["final_avg"] = scores["avg"]
    
    topic["scores"]["final_avg"] = scores["final_avg"]
    
    print(f"  {topic['name']:<30} Final: {topic['scores']['final_avg']}/10 | T:{topic['scores']['trend']} G:{topic['scores']['gap']} B:{topic['scores']['build']}h E:{topic['scores']['evergreen']} M:{topic['scores']['money']}")
    
    scored_candidates.append(topic)

# Select top 3 with avg >= 7.0
print("\n[STEP 4] Top 3 Selected (final_avg >= 7.0)")
print("-" * 40)

valid_candidates = [c for c in scored_candidates if c["scores"]["final_avg"] >= 7.0]
valid_candidates.sort(key=lambda x: x["scores"]["final_avg"], reverse=True)

top3 = valid_candidates[:3]

for i, cand in enumerate(top3, 1):
    s = cand["scores"]
    print(f"  {i}. {cand['name']} — Final: {s['final_avg']}/10 | Growth: {cand['growth']:>5}%, Build: {cand['build_time']}h, Gap: {cand['gap_signal']}")

# Save results
results = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "candidates": scored_candidates,
    "top3": [{
        "name": c["name"], 
        "scores": c["scores"],
        "growth": c["growth"],
        "build_time": c["build_time"],
        "gap_signal": c["gap_signal"],
        "category": c["category"]
    } for c in top3]
}

with open("/tmp/research_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults: {len(top3)} ideas selected")
print("Saved to /tmp/research_results.json")