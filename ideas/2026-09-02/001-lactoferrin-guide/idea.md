# App Idea: Lactoferrin Guide — Immune Support & Iron Absorption Supplement

*Generated: 2026-09-02*
*Confidence Score: 7.2/10*

---

## Pitch

Lactoferrin Guide is a focused educational resource on lactoferrin — the milk-derived immune protein exploding in popularity as a supplement — with dosage guidance, brand comparisons, and a simple tracker. Built for the 210% search growth trend, it's pure on-device content with zero backend, shipping in ~2 hours.

## Target Audience

- Primary: Health-conscious consumers 25-55 interested in immune support, iron absorption, and natural supplements
- Secondary: People with iron deficiency, athletes, biohackers, and postpartum mothers
- Demographics: US, health-store shoppers, supplement subscription recipients

## Problem Statement

Lactoferrin is a glycoprotein found in milk with documented immune-supporting and iron-absorbing properties. Search growth is rising (210% on Exploding Topics), but the App Store has zero dedicated lactoferrin resources. The top results for "lactoferrin supplement" are retail scanners (SuppCo, iHerb, Prove It) — useful for buying but useless for education. People want to know: what is lactoferrin, how is it different from whey protein, what dose do I take, does it actually work for immunity, and which brand is worth buying.

## Trend Evidence

- **Exploding Topics**: "Lactoferrin" at #23 with 210% search growth, status "Regular"
- **iTunes Gap**: "lactoferrin supplement guide" → 9 results, all retail/giant pollution (SuppCo 28K reviews, iHerb 176K reviews, Prove It 15K reviews). Zero dedicated lactoferrin apps.
- **Reddit**: r/Biohackers, r/supplements, r/HealthAnxiety have active lactoferrin discussion threads
- **Momentum**: Rising — still early in the category lifecycle

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| SuppCo: Supplement Scanner | 4.8 | Free | Retail scanner, not educational |
| iHerb: Vitamins & Supplements | 4.8 | Free | Retail marketplace, not a guide |
| Prove It - Supplement Scanner | 4.4 | Free | Retail scanner, not educational |
| Probiotic Guide USA | 4.7 | Free | Abandoned (9 reviews, 2018), wrong topic |

**App Gap**: Zero dedicated lactoferrin apps. All top results are retail/giant pollution. This is a green field — build the first actually useful lactoferrin guide.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Lactoferrin 101** — What it is, how it differs from whey protein and other milk proteins, how it's extracted
2. **Benefits Guide** — Immune support, iron absorption, gut health, anti-inflammatory properties, skin health — with simple explanations
3. **Dosage Calculator** — Input: goal (immunity/iron/skin), weight, experience level → recommended dose range
4. **Brand Comparison** — Side-by-side of popular lactoferrin brands on price per serving, purity, sourcing, flavor options
5. **Simple Tracker** — Log dose, date, and rate how you feel (immune energy, digestion, overall wellness)

### Nice-to-Have (v1.1+)
- Barcode scanner for supplement bottles
- Interaction checker (cross-reference with other supplements/medications)
- Progress charts over time

## Content & Data

- ~30 entries covering: lactoferrin basics, benefits by use case, dosage ranges, brand comparisons, extraction methods, what to look for on labels
- ~10 brand comparison cards
- Data sourced from published NIH/NCBI summaries, Examine.com, and mainstream health publications
- All bundled as JSON — no API calls, no backend

## Design Direction

- **Style**: Clean, clinical but trustworthy — like a premium wellness reference
- **Color Palette**: Deep navy (#1B3A5C), cream (#F5F1E6), soft sage (#A3B18A), warm amber (#C4A574)
- **Typography**: SF Pro Display / SF Pro Rounded
- **Key Screens**: Home (today's dose + quick log), Guide (readable articles), Brand Comparison (side-by-side), Tracker (timeline), Settings
- **Navigation**: Tab bar (Home, Guide, Tracker, Settings)
- **Reference Apps**: Headspace (wellness calm), MyFitnessPal (tracking UX), Examine.com (reference aesthetic)

## Technical Notes

- **Platform**: iOS (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON in app bundle
- **Estimated Build Time**: ~2 hours
- **Complexity**: Low

## App Store Listing

### Title
Lactoferrin Guide (18 chars)

### Subtitle
Immune Support & Iron Absorption (38 chars — trim to 30)

Actually: "Lactoferrin Supplement Guide" (28 chars)

### Keywords
lactoferrin, immune support, iron absorption, supplement guide, lactoferrin benefits, milk protein, immune health, supplement tracker, wellness guide, natural immunity, lactoferrin dosage, biohackers, postpartum, iron deficiency, supplement comparison, health tracker, immune booster, lactoferrin brand, wellness supplement, evidence-based

### Description
Meet Lactoferrin Guide — your personal resource on the milk-derived protein exploding in the supplement world. Whether you're looking for immune support, better iron absorption, or just want to understand what all the buzz is about, this app cuts through the marketing noise.

With a curated guide covering what lactoferrin actually does, how to dose it, and which brands are worth your money, plus a simple tracker for what you try and how you feel, Lactoferrin turns supplement guesswork into an actual plan. No accounts. No ads. No backend. Everything lives on your phone.

### Category
Health & Fitness (primary), Reference (secondary)

### Age Rating
4+

### Privacy
No data collected. Fully on-device.

---

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 6/10 | 210% growth on ET, "Regular" status — solid but not exploding |
| App Gap | 8/10 | Zero dedicated apps; all top results are retail/giant pollution |
| Build Simplicity | 9/10 | Pure on-device content, ~2 hour build, no backend |
| Evergreen Potential | 7/10 | Supplement interest is sustained; lactoferrin has staying power as a wellness category |
| Monetization | 6/10 | Limited — affiliate links to supplement retailers, maybe IAP for premium brand comparisons |
| **Average** | **7.2/10** | |

## Risk Assessment

- **Trend Fizzle**: Low — lactoferrin has scientific backing beyond trend-hopping; immune support is evergreen
- **App Store Rejection**: Low — educational content, no medical claims beyond published research
- **Competition**: Medium — a retail giant could build a lactoferrin section, but they rarely do niche educational content
- **Legal/IP**: Low — lactoferrin is a naturally occurring protein, not trademarkable
- **Content Maintenance**: Low — supplement science evolves slowly; annual updates sufficient