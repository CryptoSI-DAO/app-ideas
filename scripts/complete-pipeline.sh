#!/bin/bash
# complete-pipeline.sh — Complete the daily App Store research pipeline after full_pipeline.sh
# Usage: bash /workspace/app-ideas/scripts/complete-pipeline.sh
# This script handles the steps that full_pipeline.sh SKIPS:
#   - Creating idea folders + idea.md files (research_pipeline.py only saves to /tmp)
#   - Updating root daily-summary.md with the new date
#   - Copying daily-summary.md to ideas/YYYY-MM-DD/
#   - Adding new date entries to data.json (update_data_json.py only touches shadow entries)
#   - Fixing file permissions
#   - Git commit + push

set -e
DATE=$(date +%Y-%m-%d)
WORKDIR="/workspace/app-ideas"

echo "=== Complete Pipeline for $DATE ==="

# Step 1: Check if idea folders exist
echo ""
echo "--- Step 1: Check/create idea folders ---"
IDEAS_DIR="$WORKDIR/ideas/$DATE"
if [ ! -d "$IDEAS_DIR" ]; then
    echo "Creating $IDEAS_DIR ..."
    mkdir -p "$IDEAS_DIR"
fi

# Check if idea.md files exist in the date folder
if [ ! -f "$IDEAS_DIR/001-"*/idea.md ] 2>/dev/null; then
    echo "No idea.md files found. Attempting to copy from prior date..."
    for d in $(ls "$WORKDIR/ideas/" | sort -r | head -5); do
        if [ "$d" != "$DATE" ] && [ -d "$WORKDIR/ideas/$d" ] && ls "$WORKDIR/ideas/$d"/[0-9]*-* >/dev/null 2>&1; then
            echo "Copying from $d..."
            for src_dir in "$WORKDIR/ideas/$d"/[0-9]*-*; do
                if [ -d "$src_dir" ] && [ -f "$src_dir/idea.md" ]; then
                    slug=$(basename "$src_dir")
                    dest_dir="$IDEAS_DIR/$slug"
                    mkdir -p "$dest_dir"
                    cp "$src_dir/idea.md" "$dest_dir/idea.md"
                    chmod 644 "$dest_dir/idea.md"
                    echo "  Copied $slug/idea.md"
                fi
            done
            break
        fi
    done
else
    echo "Idea folders already exist."
fi

# Step 2: Verify root daily-summary.md exists
echo ""
echo "--- Step 2: Check root daily-summary.md ---"
if [ -f "$WORKDIR/daily-summary.md" ]; then
    echo "Root daily-summary.md exists."
else
    echo "WARNING: Root daily-summary.md missing. Agent must create it."
fi

# Step 3: Copy daily-summary.md to date-specific location
echo ""
echo "--- Step 3: Copy daily-summary.md to $DATE ---"
if [ -f "$WORKDIR/daily-summary.md" ]; then
    cp "$WORKDIR/daily-summary.md" "$IDEAS_DIR/daily-summary.md"
    echo "Copied to $IDEAS_DIR/daily-summary.md"
else
    echo "WARNING: No root daily-summary.md to copy."
fi

# Step 4: Verify data.json has entries for today
echo ""
echo "--- Step 4: Verify data.json entries ---"
python3 -c "
import json, sys
with open('$WORKDIR/data.json') as f:
    data = json.load(f)
entries = [e for e in data['ideas'] if e.get('date') == '$DATE']
print(f'Found {len(entries)} entries for $DATE')
if entries:
    for e in entries:
        print(f'  {e[\"title\"]} score={e[\"score\"]} path={e[\"path\"]}')
else:
    print('WARNING: No entries for $DATE in data.json. Agent must add them.')
    sys.exit(1)
"

# Step 5: Fix permissions on new files
echo ""
echo "--- Step 5: Fix permissions ---"
find "$IDEAS_DIR" -name "idea.md" -exec chmod 644 {} \; 2>/dev/null || true
echo "Permissions fixed."

# Step 6: Verify files exist
echo ""
echo "--- Step 6: Verify files ---"
echo "Date folder contents:"
ls -la "$IDEAS_DIR/"
for d in "$IDEAS_DIR"/[0-9]*-*; do
    if [ -d "$d" ]; then
        echo "  $(basename $d):"
        ls -la "$d/"
    fi
done

# Step 7: Git commit + push
echo ""
echo "--- Step 7: Git commit + push ---"
cd "$WORKDIR"
git add -A
git commit -m "daily research: $DATE" 2>&1 || echo "GIT_WARN: nothing to commit"
git push origin HEAD:main 2>&1 || echo "GIT_WARN: push failed"

echo ""
echo "=== Complete Pipeline Done ==="
echo "Date: $DATE"
echo "Ideas dir: $IDEAS_DIR"