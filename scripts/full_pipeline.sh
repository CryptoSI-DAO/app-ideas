#!/bin/bash
# Efficient daily research pipeline - runs the heavy lifting as a script
# so the agent only needs a few tool calls for git push + delivery

set -e
DATE=$(date +%Y-%m-%d)
WORKDIR="/workspace/app-ideas"

echo "=== STEP 1: Run research pipeline ==="
cd "$WORKDIR"
python3 research_pipeline.py 2>&1 || echo "PIPELINE_WARN: research_pipeline.py exited non-zero"

echo ""
echo "=== STEP 2: Check for date-specific summary ==="
IDEAS_DIR="$WORKDIR/ideas/$DATE"
if [ ! -f "$IDEAS_DIR/daily-summary.md" ]; then
    echo "Creating date-specific summary..."
    mkdir -p "$IDEAS_DIR"
    if [ -f "$WORKDIR/daily-summary.md" ]; then
        cp "$WORKDIR/daily-summary.md" "$IDEAS_DIR/daily-summary.md"
    fi
fi

echo ""
echo "=== STEP 3: Update data.json ==="
python3 scripts/update_data_json.py 2>&1 || echo "DATA_WARN: update_data_json.py exited non-zero"

echo ""
echo "=== STEP 4: Sync app-archive ==="
cd "$WORKDIR"
python3 scripts/sync_data_json.py 2>&1 || echo "SYNC_WARN: sync_data_json.py exited non-zero"

echo ""
echo "=== STEP 5: Git commit ==="
cd "$WORKDIR"
git add -A
git commit -m "daily research: $DATE" 2>&1 || echo "GIT_WARN: nothing to commit"

echo ""
echo "=== STEP 6: Git push ==="
git push 2>&1 || echo "GIT_WARN: push failed (will retry next run)"

echo ""
echo "=== PIPELINE COMPLETE ==="
echo "Date: $DATE"
echo "Ideas dir: $IDEAS_DIR"
