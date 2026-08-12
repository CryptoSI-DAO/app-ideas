#!/usr/bin/env python3
"""Rebuild data.json from local idea files AND sync to Supabase (dual-write).
GitHub remains the source of truth for markdown; Supabase is the fast-read cache.
"""
import json
import os
import re
import sys
import urllib.request

# ── Config ──
ideas_dir = 'ideas'
SUPABASE_URL = os.environ.get('SUPABASE_URL', '')
SUPABASE_ANON_KEY = os.environ.get('SUPABASE_ANON_KEY', '')

# ── Parse idea.md ──
def parse_idea_md(content):
    """Extract title, score, and pitch from idea.md markdown."""
    title_match = re.search(r'^#\s+(?:App Idea:\s*)?(.+)$', content, re.MULTILINE)
    title = title_match.group(1).replace('**', '').strip() if title_match else ''

    score = 0
    score_match = re.search(r'Confidence Score:\s*([\d.]+)', content)
    if score_match:
        try:
            score = float(score_match.group(1))
        except ValueError:
            pass

    pitch_match = re.search(r'##\s+Pitch\s*\n+([\s\S]+?)(?=\n##|\n---)', content)
    pitch = ''
    if pitch_match:
        pitch = pitch_match.group(1).replace('**', '').replace('\n+', ' ').strip()

    return title, score, pitch

# ── Supabase REST helpers ──
def supabase_upsert(table, data, conflict_cols=None):
    """Upsert a row to Supabase via REST API. Returns True on success.
    conflict_cols: list of column names that define the conflict (for ON CONFLICT).
    """
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        return False
    try:
        body = json.dumps(data).encode('utf-8')
        # Build URL with on_conflict query param for upsert support
        endpoint = f"{SUPABASE_URL}/rest/v1/{table}"
        if conflict_cols:
            endpoint += f"?on_conflict={','.join(conflict_cols)}"
        req = urllib.request.Request(
            endpoint,
            data=body,
            headers={
                'apikey': SUPABASE_ANON_KEY,
                'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
                'Content-Type': 'application/json',
                'Prefer': 'resolution=merge-duplicates',
            },
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status in (200, 201)
    except Exception as e:
        print(f"  ⚠ Supabase upsert failed for {table}: {e}", file=sys.stderr)
        return False

def push_to_supabase(date, slug, num, title, score, pitch, full_content, github_path):
    """Push a single idea to Supabase."""
    data = {
        'date': date,
        'slug': slug,
        'num': num,
        'title': title,
        'score': score,
        'pitch': pitch,
        'full_content': full_content,
        'github_path': github_path,
    }
    return supabase_upsert('app_ideas', data, conflict_cols=['date', 'slug'])

def push_daily_summary_to_supabase(date, content):
    """Push daily summary to Supabase."""
    data = {
        'date': date,
        'summary': {'has_summary': True, 'content': content},
    }
    return supabase_upsert('app_ideas_daily', data, conflict_cols=['date'])

# ── Main ──
days = sorted(os.listdir(ideas_dir)) if os.path.exists(ideas_dir) else []
data = []
supabase_pushed = 0
supabase_failed = 0

for day in days:
    day_path = os.path.join(ideas_dir, day)
    if not os.path.isdir(day_path):
        continue

    # Push daily summary to Supabase
    summary_path = os.path.join(day_path, 'daily-summary.md')
    if os.path.exists(summary_path):
        with open(summary_path) as f:
            summary_content = f.read()
        push_daily_summary_to_supabase(day, summary_content)

    ideas = sorted(os.listdir(day_path))
    for idea in ideas:
        if idea == 'daily-summary.md':
            continue
        idea_path = os.path.join(day_path, idea, 'idea.md')
        if os.path.exists(idea_path):
            with open(idea_path) as f:
                content = f.read()

            title, score, pitch = parse_idea_md(content)
            num = idea.split('-')[0] if '-' in idea else idea
            github_path = 'ideas/' + day + '/' + idea + '/idea.md'

            data.append({
                'date': day,
                'slug': idea,
                'num': num,
                'title': title,
                'score': score,
                'path': github_path
            })

            # Dual-write: push to Supabase
            if push_to_supabase(day, idea, num, title, score, pitch, content, github_path):
                supabase_pushed += 1
            else:
                supabase_failed += 1

# Write data.json
out = {'ideas': data, 'last_updated': __import__('datetime').datetime.now().isoformat() + 'Z', 'total': len(data)}
with open('data.json', 'w') as f:
    json.dump(out, f, indent=2)

print(f'data.json rebuilt: {len(data)} ideas')
print(f'Supabase dual-write: {supabase_pushed} pushed, {supabase_failed} failed')
for i in data:
    print(f'  {i["date"]}/{i["slug"]} - score: {i["score"]}')
