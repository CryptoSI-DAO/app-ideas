# App Ideas 🚀

Daily validated App Store opportunities — researched, scored, and packaged for rapid development.

## Structure

```
ideas/
  YYYY-MM-DD/
    001-idea-slug/
      README.md          # Full idea + requirements document
      validation.md      # Scoring & validation checklist
    002-idea-slug/
    ...
    daily-summary.md     # Top 3 picks with reasoning
templates/
  idea-template.md       # Standard requirements document format
  validation-template.md # Scoring rubric
ARCHIVE.md               # Ideas that were built or killed
```

## Workflow

1. **Data agent** runs daily research cycle
2. Top 3 ideas saved here with full requirements docs
3. Pick an idea → hand off to Claude Code / Codex for building
4. Move built/killed ideas to ARCHIVE.md

## Scoring Rubric

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Trend Momentum | 20% | Is the topic actively rising? |
| App Gap | 25% | How underserved is the App Store? |
| Build Simplicity | 20% | Can MVP be built in 1-3 hours? |
| Evergreen Potential | 15% | Will the trend last? |
| Monetization | 20% | Revenue potential (paid/freemium/ad)? |

## Agent

Built with [Hermes Agent](https://github.com/NousResearch/hermes-agent) running Owl Alpha via OpenRouter.
