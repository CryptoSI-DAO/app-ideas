# App Idea: Magnesium Tracker

*Generated: 2026-06-16*
*Confidence Score: 7.6/10*

---

## Pitch
A clean, offline-first magnesium supplement tracker that helps users log daily intake, track different forms (glycinate, citrate, oxide), set dosing reminders, and avoid interactions with other supplements or medications. No ads, no subscriptions — just a simple wellness companion for the 50%+ of Americans who are magnesium deficient.

## Target Audience
- Primary: Health-conscious adults 25-55 supplementing with magnesium
- Secondary: People managing migraines, sleep issues, muscle cramps, or anxiety with magnesium
- Demographics: US/Canada, 25-55, wellness-oriented, iOS users skew female 60%

## Problem Statement
Magnesium supplementation is surging (glycinate searches up 3,900% on Exploding Topics) but there's no dedicated tracking app. Users either use generic pill reminders (too basic) or full health trackers (too complex). Nobody answers: "Am I taking too much?" "Should I take it with food?" "What form is best for sleep vs. muscle recovery?" Existing apps like "Magnesium Counter and Tracker" have 2 reviews and 5 stars — clearly abandoned. Thorne (a major supplement brand) has a 1.9-star app. The gap is real.

## Trend Evidence
- **Exploding Topics**: "Magnesium Glycinate Supplement" at #89, +3,900% 5-year search growth, "Regular" growth status (sustained, not a spike)
- **Google Trends**: "Magnesium glycinate" shows sustained upward interest over 12 months, with related queries like "magnesium glycinate dosage" and "magnesium for sleep" trending upward
- **Health context**: 50-60% of US adults don't get enough magnesium; supplementation recommendations rising across functional medicine
- **Momentum**: Sustained — driven by clinical research on magnesium's role in sleep, anxiety, and metabolic health

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Magnesium Counter and Tracker | ⭐5.0 | $2.99 | 2 reviews, abandoned, no updates |
| Thorne | ⭐1.9 | Free | Brand-specific, poor UX, 53 reviews |
| Magnesium Athletes | ⭐0.0 | Free | 0 reviews, placeholder app |
| Generic Pill Reminders | ⭐4.2-4.8 | Free | No magnesium-specific features, no form tracking, no dosage guidance |

**App Gap**: TRUE GREEN FIELD. The only dedicated magnesium tracker has 2 reviews and hasn't been updated. No app tracks different magnesium forms (glycinate vs. citrate vs. oxide), their specific use cases, or provides evidence-based dosage guidance. The supplement tracking category is dominated by either brand-specific apps (Thorne) or generic pill reminders.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Supplement Log** — Quick-log magnesium intake with form type (glycinate, citrate, oxide, threonate, malate), dosage (mg), and time. One-tap repeat for daily users.
2. **Form Guide** — Reference card for each magnesium form: best use case (sleep, muscles, digestion, anxiety), absorption rate, recommended dosage range, food interactions.
3. **Daily Dosing Reminder** — Customizable notification to take magnesium, with smart scheduling (e.g., "take with dinner" or "split AM/PM dose").
4. **Weekly Summary** — Simple chart showing weekly intake vs. target, adherence streak, and form breakdown.

### Nice-to-Have (v1.1+)
- Interaction checker — warns about common magnesium interactions (calcium, zinc, certain medications)
- Symptom correlation — optional logging of sleep quality, muscle cramps, mood to correlate with supplementation
- Export data — CSV export for sharing with healthcare provider

## Content & Data
- Magnesium form reference data (glycinate, citrate, oxide, threonate, malate, taurate) — ~10 entries with dosage ranges, absorption rates, best use cases, food interactions
- Recommended daily allowances by age/gender (public data from NIH Office of Dietary Supplements)
- All content is factual, sourced from NIH, Mayo Clinic, and peer-reviewed research
- Content can be curated in <1 hour from public sources

## Design Direction
- **Style**: Clean, clinical-minimal — think Apple Health meets supplement packaging
- **Color Palette**: 
  - Primary: #2D6A4F (deep sage green — wellness, calm)
  - Secondary: #52B788 (lighter green — positive actions)
  - Accent: #F4A261 (warm amber — highlights, CTAs)
  - Background: #FAFAF9 (warm white)
  - Text: #1B1B1B (near-black)
  - Error/Warning: #E76F51 (soft red)
- **Typography**: SF Pro Display for headings, SF Pro Text for body, SF Mono for numbers
- **Key Screens**: Home (today's log + streak), Log Entry (form picker + dosage), Form Guide (reference cards), Weekly Summary (chart), Settings
- **Navigation**: Tab bar — Home, Guide, History, Settings
- **Reference Apps**: WaterMinder (clean tracking UI), Apple Health (data presentation), Pill Reminder apps (notification patterns)

## Technical Notes
- **Platform**: iOS (SwiftUI), minimum iOS 16
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: SwiftData / Core Data, bundled JSON for form reference data
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
Magnesium Tracker

### Subtitle
Track your daily magnesium intake

### Keywords
magnesium, supplement tracker, magnesium glycinate, health tracker, vitamin tracker, pill reminder, wellness, sleep aid, muscle recovery, dosage tracker

### Description
Track your magnesium supplementation with precision.

Magnesium Tracker helps you log daily intake, understand different forms (glycinate, citrate, oxide, and more), and stay consistent with evidence-based dosing guidance.

Whether you take magnesium for better sleep, muscle recovery, anxiety relief, or general wellness — this app keeps you on track without the clutter.

FEATURES:
• Quick-log your daily magnesium with form type and dosage
• Comprehensive form guide — know which form fits your needs
• Smart reminders — take with food, split doses, whatever works
• Weekly summary — see your adherence at a glance
• 100% on-device — no account, no internet, no ads

No subscriptions. No ads. No data collection. Just a clean tracker that respects your privacy.

Download Magnesium Tracker and take control of your supplementation.

### Category
Primary: Health & Fitness
Secondary: Medical

### Pricing
- **Model**: Free with optional Pro unlock ($2.99 one-time)
- **Reasoning**: Free core (logging + reminders) attracts users; Pro unlocks form guide, weekly summary, and interaction checker
- **Monetization Path**: One-time Pro purchase for power users; potential future: custom supplement tracking beyond magnesium

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | 3,900% growth on Exploding Topics, sustained "Regular" status, NIH data supports rising awareness |
| App Gap | 9/10 | Only 1 dedicated app with 2 reviews; all competitors are brand-specific or generic pill reminders |
| Build Simplicity | 8/10 | Static reference data, simple logging UI, no backend, no APIs |
| Evergreen Potential | 8/10 | Magnesium supplementation is a permanent wellness habit, not a fad; 50%+ of adults are deficient |
| Monetization | 6/10 | Free + one-time Pro model is viable but not high-revenue; better as portfolio app |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: Low — magnesium research is growing, not peaking; "Regular" growth status on Exploding Topics indicates sustained interest
- **App Store Rejection**: Low — no medical claims, purely informational + tracking; disclaimers included
- **Competition**: Medium — a generic health tracker could add magnesium features, but the form-specific angle is defensible
- **Legal/IP**: Low — all data from public NIH sources; include "not medical advice" disclaimer
- **Content Maintenance**: Low — reference data is stable; update only when new research emerges

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics, Google Trends, NIH data)
- [x] App Store search shows ≤ 3 relevant apps OR top apps have < 3 stars (only 1 app with 2 reviews)
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours
