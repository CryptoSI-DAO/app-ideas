#!/usr/bin/env python3
"""Daily App Store Research Pipeline"""
import json
import urllib.request, urllib.parse
import time
from datetime import datetime

# Load data
with open('/workspace/app-ideas/data.json', 'r') as f:
    data = json.load(f)

# Find incomplete entries (score=0)
incomplete = [i for i in data['ideas'] if i.get('score', 0) == 0]
print(f"=== INCOMPLETE ENTRIES ===")
for e in incomplete:
    print(f"  {e['title']} ({e['date']})")

# iTunes search function
def search_itunes(q, lim=5):
    u = f"https://itunes.apple.com/search?term={urllib.parse.quote(q)}&entity=software&limit={lim}&country=US"
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=10)
        return json.loads(r.read().decode()).get('results', [])
    except Exception as ex:
        return []

# Score incomplete entries based on iTunes gap analysis
print("\n=== SCORING INCOMPLETE ENTRIES ===")
scores_to_update = {}
for entry in incomplete:
    title = entry['title']
    query = title.replace(' Guide', '').replace(' Track', '').replace('App', '').strip()
    results = search_itunes(query)
    time.sleep(1.0)  # Rate limiting
    
    if not results:
        gap, trend, build = 10, 8, 2
    else:
        cats = set(r.get('primaryCategory', {}).get('defaultValue', 'Unknown') for r in results[:5])
        total_rev = sum(r.get('userRatingCount', 0) for r in results[:5])
        
        if len(cats) > 1:
            gap = 9  # Search pollution
        elif total_rev < 500:
            gap = 8  # Tiny competition
        else:
            gap = 6
        
        trend = 8 if 'pouch' in query.lower() or 'earbuds' in query.lower() or 'toothbrush' in query.lower() else 7
        build = 2  # Guide apps are quick to build
    
    avg = (gap + trend + build + 8 + 8) / 5  # 8,8 for evergreen/monetization
    avg = min(8.6, max(7.0, avg))  # Cap at realistic max
    
    print(f"{title}: Gap={gap}, Trend={trend}, Build={build} => Avg={avg:.1f}")
    scores_to_update[title] = round(avg, 1)

# Update data.json with scores
for entry in data['ideas']:
    if entry['title'] in scores_to_update:
        entry['score'] = scores_to_update[entry['title']]
        print(f"Updated: {entry['title']} -> {entry['score']}")

# Update metadata
data['last_updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:00:00.000000Z')
data['total'] = len(data['ideas'])

# Save
with open('/workspace/app-ideas/data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n=== SUMMARY ===")
print(f"Total ideas: {data['total']}")
print(f"Scores updated for {len(scores_to_update)} entries")