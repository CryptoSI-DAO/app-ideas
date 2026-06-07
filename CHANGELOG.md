# Changelog

All notable changes to the App Ideas research repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] — 2026-06-07

### Added
- Initial repository structure with `ideas/`, `templates/`, and `ARCHIVE.md`
- Daily research pipeline: trend discovery → scoring → requirements docs → git push
- 27+ app ideas researched and scored (May 26 — Jun 7, 2026)
- `data.json` flat index for programmatic access to all ideas
- Top 3 ideas per day with full requirements documents
- `extended-research/` folder for deep-dive competitive analysis and proposals
  - First entry: **Racing Tips Marketplace** — full competitive analysis + revenue model + build plan (8 sections)
- Semantic versioning scheme (starting at `0.1.0`)
- `CHANGELOG.md` (this file)

### Scoring Rubric (current)
| Dimension | Weight | Description |
|-----------|--------|-------------|
| Trend Momentum | 20% | Is the topic actively rising? |
| App Gap | 25% | How underserved is the App Store? |
| Build Simplicity | 20% | Can MVP be built in 1–3 hours? |
| Evergreen Potential | 15% | Will the trend last? |
| Monetization | 20% | Revenue potential (paid/freemium/ad)? |

### Idea Status Key
| Emoji | Meaning |
|-------|---------|
| ⏳ | Pending — awaiting decision |
| 🏗️ | Built — developed and published |
| 📈 | Live — published and generating revenue |
| ⛔ | Killed — abandoned after validation |

---

## Versioning Scheme

This repo uses [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0) — Structural changes: new scoring rubric, schema changes, workflow redesign
- **MINOR** (0.X.0) — New features: extended research section, new templates, site redesigns
- **PATCH** (0.0.X) — Bug fixes, content updates, typo corrections, individual idea additions

Ideas added during daily research are **patch** releases.
New sections, features, or structural changes are **minor** releases.
Scoring rubric or fundamental workflow changes are **major** releases.

The changelog documents minor and major releases. Patch-level changes (individual idea additions) are tracked via git commits.

[Unreleased]: https://github.com/CryptoSI-DAO/app-ideas/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/CryptoSI-DAO/app-ideas/releases/tag/v0.1.0
