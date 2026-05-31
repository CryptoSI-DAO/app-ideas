import json, os

ideas_dir = 'ideas'
days = sorted(os.listdir(ideas_dir)) if os.path.exists(ideas_dir) else []
data = []

for day in days:
    day_path = os.path.join(ideas_dir, day)
    if not os.path.isdir(day_path):
        continue
    ideas = sorted(os.listdir(day_path))
    for idea in ideas:
        if idea == 'daily-summary.md':
            continue
        idea_path = os.path.join(day_path, idea, 'idea.md')
        if os.path.exists(idea_path):
            with open(idea_path) as f:
                content = f.read()
            title_line = next((l for l in content.split('\n') if l.startswith('# App Idea:')), '')
            title = title_line.replace('# App Idea: ', '').strip()
            score = 0
            for line in content.split('\n'):
                if 'Confidence Score:' in line:
                    try:
                        score = float(line.split(':')[1].strip().split('/')[0])
                    except:
                        pass
            num = idea.split('-')[0] if '-' in idea else idea
            data.append({
                'date': day,
                'slug': idea,
                'num': num,
                'title': title,
                'score': score,
                'path': 'ideas/' + day + '/' + idea + '/idea.md'
            })

out = {'ideas': data, 'last_updated': '2026-05-31T07:27:00Z', 'total': len(data)}
with open('data.json', 'w') as f:
    json.dump(out, f, indent=2)
print('data.json rebuilt: ' + str(len(data)) + ' ideas')
for i in data:
    print('  ' + i['date'] + '/' + i['slug'] + ' - score: ' + str(i['score']))
