# App Idea: MagTrack — Magnesium Bisglycinate Guide & Tracker

*Generated: 2026-09-01*
*Confidence Score: 7.2/10*

---

## Pitch

MagTrack is a focused guide to magnesium bisglycinate — the fastest-growing supplement form in 2026 — with a simple tracker for dosage, timing, and effects. Built for the 1,550% search growth trend, it's pure on-device content with a logging workflow, shipping in ~2 hours.

## Target Audience
- Primary: People struggling with sleep, anxiety, muscle cramps, or low energy who've heard of magnesium bisglycinate
- Secondary: Biohackers, wellness enthusiasts, and supplement curious consumers
- Demographics: 25-55, US, health-conscious, already shopping at supplement retailers

## Problem Statement

Magnesium bisglycinate has exploded 1,550% in search volume, driven by its reputation as the "calm magnesium" — gentle on the stomach, supports sleep and anxiety. But there's no dedicated mobile resource: the App Store has only one tiny tracker (2 reviews, likely abandoned), and everything else is retail apps or giant supplement scanners. People don't know what dose to take, when to take it, what to expect, or how to tell if it's working.

## Trend Evidence
- **Exploding Topics**: "Magnesium Bisglycinate" at #50 with 1,550% search growth, status "Exploding"
- **iTunes Gap**: "magnesium bisglycinate" → 8 results, only 21 combined reviews. Top result: "Magnesium Counter and Tracker" (2 reviews). Strong green-field signal.
- **Reddit**: r/Biohackers, r/sleep, r/anxiety all have active magnesium discussion threads
- **Momentum**: Rising — supplement trends typically have 2-3 year lifecycles, still early

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Magnesium Counter and Tracker | N/A | Free | 2 reviews — abandoned, no content |
| SuppCo: Supplement Scanner | 4.8 | Free | Retail scanner, not educational |
| Sleepiest Meditation | 4.8 | Free | Sleep app, not magnesium-specific |

**App Gap**: Only one tiny tracker exists with virtually no reviews. No educational guide, no dosage context, no effect tracking. Quality gap — build the actually useful one.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Magnesium Bisglycinate Guide** — What it is, how it differs from other magnesium forms (citrate, oxide, glycinate), benefits by use case (sleep, anxiety, muscle, energy)
2. **Dosage Calculator** — Simple input: weight, goal (sleep/anxiety/muscle), experience level → recommended dose range with explanation
3. **Daily Tracker** — Log dose, time taken, and rate sleep quality / anxiety level / muscle comfort on a 1-5 scale
4. **Timing Guide** — When to take it (morning vs night), with food vs empty stomach, what to avoid combining with
5. **Side Effect Awareness** — What's normal (loose stools, stomach upset) vs what's not, when to contact a doctor

### Nice-to-Have (v1.1+)
- Supplement interaction checker (cross-reference with other supplements/medications)
- Progress charts (sleep quality over time, anxiety trends)
- Batch reminder notifications

## Content & Data
- ~40 entries covering: magnesium forms comparison, benefits by use case, dosage ranges, timing rules, side effect guide, food interactions, drug interactions summary
- ~10 sample tracking logs for demonstration
- Data sourced from published NIH/NCBI summaries, Examine.com, and mainstream health publications
- All bundled as JSON — no API calls, no backend

## Design Direction
- **Style**: Clean, calm, trustworthy — like a premium wellness journal
- **Color Palette**: Deep teal (#0D7377), cream (#F5F1E6), soft sage (#A3B18A), warm amber (#C4A574)
- **Typography**: SF Pro Display / SF Pro Rounded
- **Key Screens**: Home (today's dose + quick log), Guide (readable articles), Tracker (timeline + charts), Dosage Calculator, Settings
- **Navigation**: Tab bar (Home, Guide, Tracker, Settings)
- **Reference Apps**: Headspace (wellness calm), MyFitnessPal (tracking UX), Sleep Cycle (sleep tracking)

## Technical Notes
- **Platform**: iOS (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON in app bundle
- **Estimated Build Time**: ~2 hours
- **Complexity**: Low

## App Store Listing

### Title
MagTrack — Magnesium Guide (27 chars)

### Subtitle
Bisglycinate Dosage & Tracker (31 chars — must trim to 30)

Actually: "Bisglycinate Tracker" (21 chars)

### Keywords
magnesium, bisglycinate, magnesium glycinate, sleep aid, anxiety relief, muscle cramps, supplement tracker, wellness guide, dosage calculator, sleep quality, stress relief, mineral supplement, health tracker, magnesium deficiency, calm, relaxation

### Description
MagTrack is your personal magnesium bisglycinate companion — the fastest-growing supplement form in 2026. Whether you're using it for better sleep, less anxiety, fewer muscle cramps, or just overall wellness, MagTrack helps you understand what to take, when to take it, and whether it's actually working.

With a curated guide covering forms, benefits, dosages, and timing, plus a simple daily tracker for dose, timing, and how you feel, MagTrack turns supplement guesswork into an actual plan. No accounts. No ads. No backend. Everything lives on your phone.

### Category
Health & Fitness (primary), Reference (secondary)

### Age Rating
4+

### Privacy
No data collected. Fully on-device.

---