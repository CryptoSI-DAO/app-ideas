#!/usr/bin/env python3
"""iTunes Gap Analysis for New Trend Candidates"""
import urllib.request, urllib.parse, json, time

def search_iTunes(query, lim=5):
    url = f"https://itunes.apple.com/search?term={urllib.parse.quote(query)}&entity=software&limit={lim}&country=US"
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=10)
        return json.loads(r.read().decode()).get('results', [])
    except:
        return []

def analyze_gap(results):
    """Analyze search results for app gap signal"""
    if not results:
        return 10, "ZERO RESULTS - TRUE GREEN FIELD"
    
    cats = [r.get('primaryCategory', {}).get('defaultValue', 'Unknown') for r in results[:5]]
    total_rev = sum(r.get('userRatingCount', 0) for r in results[:5])
    unique_cats = set(cats)
    
    # Check for search pollution (all different categories)
    if len(unique_cats) > 1 and all(c not in ['Book', 'News'] for c in unique_cats):
        return 9, f"SEARCH POLLUTION - Categories: {list(unique_cats)[:3]}"
    
    if total_rev < 500:
        return 9, f"TINY COMPETITION - {total_rev} reviews"
    
    return 7, f"Crowded - {len(results)} apps, {total_rev} reviews"

# New candidates from Exploding Topics
candidates = [
    ("Wolverine Peptide", "wolverine peptide supplement"),
    ("Hypochlorous Acid Spray", "hypochlorous acid spray device"),
    ("Depuffing Wand", "depuffing skin wand"),
    ("Cold Plunge Sauna", "cold plunge sauna app"),
    ("Fractional COO", "fractional coo tool"),
    ("Answer Engine Optimizer", "answer engine optimization tool"),
    ("Color Drenching Paint", "color drenching paint guide"),
]

print("iTunes Gap Analysis for New Trends")
print("=" * 60)

results = []
for name, query in candidates:
    apps = search_iTunes(query)
    time.sleep(1.5)  # Rate limiting
    gap_score, analysis = analyze_gap(apps)
    
    # Get top 3 app names if any
    top_apps = [r.get('trackName', 'N/A') for r in apps[:3]] if apps else []
    
    print(f"\n{name}:")
    print(f"  Query: '{query}'")
    print(f"  Gap Score: {gap_score}/10")
    print(f"  Analysis: {analysis}")
    if top_apps:
        print(f"  Top apps: {', '.join(top_apps)}")
    
    results.append({
        'name': name,
        'query': query,
        'gap_score': gap_score,
        'analysis': analysis,
        'top_apps': top_apps
    })

# Output JSON
print("\n" + "=" * 60)
print("JSON_RESULTS")
print(json.dumps(results, indent=2))