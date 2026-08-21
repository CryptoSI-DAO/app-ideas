#!/usr/bin/env python3
import urllib.request, urllib.parse, json, time

def search(q, lim=5):
    u = f"https://itunes.apple.com/search?{urllib.parse.urlencode({'term': q, 'entity': 'software', 'limit': lim, 'country': 'US'})}"
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=10)
        return json.loads(r.read().decode()).get('results', [])
    except: return []

topics = [("Suri Toothbrush", "suri toothbrush"), ("Non-Slip Shoes", "slip resistant"), ("AI Earbuds", "ai earbuds")]
for n, q in topics:
    res = search(q); time.sleep(1.0)
    if not res: g, a = 10, "GREEN FIELD"
    else: g = 9 if len(set(r.get('primaryCategory',{}).get('defaultValue','Unknown') for r in res[:5])) > 1 or sum(r.get('userRatingCount',0) for r in res[:5]) < 500 else 7
    print(f'{n}: Gap {g}/10')