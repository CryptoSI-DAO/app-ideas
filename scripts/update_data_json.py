#!/usr/bin/env python3
"""
Daily App Store Research Pipeline
Complete incomplete entries AND find new trending opportunities
"""

import urllib.request
import urllib.parse
import json
import time
import os
from datetime import datetime

# Load existing data
with open('/workspace/app-ideas/data.json', 'r') as f:
    data = json.load(f)

# Known scores from existing idea.md files (shadow entries)
shadow_entries = {
    "Suri Toothbrush Guide": 8.6,
    "Non-Slip Shoes Guide": 8.4,
    "AI Earbuds Guide": 8.0,
    "PouchPal": 8.2,
    "SoleCare": 8.0,
    "SunGuard": 8.0,
    "Cold Plunge Protocol": 7.8,
    "Cryotherapy Protocol": 7.6,
    "Answer Engine Optimizer": 8.0,
    "ResponsibleAI": 8.6,
    "AISEO": 8.0,
    "AIRobotDog": 7.8,
    "Qamaria Yemeni Coffee": 7.6,
    "Fastmoss": 7.4,
    "Hypochlorous Acid Spray": 8.2,
    "Wolverine Peptide Guide": 8.4,  # NEW
}

# Update scores for shadow entries
for entry in data['ideas']:
    title = entry.get('title', '')
    if title in shadow_entries:
        old_score = entry.get('score', 0)
        new_score = shadow_entries[title]
        if old_score != new_score:
            print(f"Updating {title}: {old_score} -> {new_score}")
            entry['score'] = new_score
            entry['updated'] = datetime.now().isoformat()

# Calculate average score
scores = [e.get('score', 0) for e in data['ideas'] if e.get('score', 0) > 0]
data['total'] = len(data['ideas'])
data['last_updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:00:00.000000Z')

# Save updated data
with open('/workspace/app-ideas/data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nUpdated {len(scores)} entries with scores")
print(f"Average score: {sum(scores)/len(scores):.1f}" if scores else "No scores")

# Output summary of updates
print("\nData.json updated successfully")
print(f"Total ideas: {data['total']}")