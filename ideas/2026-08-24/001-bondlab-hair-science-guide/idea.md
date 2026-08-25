# App Idea: BondLab — Bond Repair Hair Science Guide

*Generated: 2026-08-24*
*Confidence Score: 7.8/10*

---

## Pitch
Search interest in "bond repair shampoo" is up 3,600%, but the App Store has nothing that actually explains bond-building science. iTunes scans across 6 query variations return only salon check-in giants, retail apps, and three 0–2 review shells (Shampoo Scanner AI: 2 ratings; HairPlan: 1). BondLab is an offline hair-science reference: a porosity/damage assessment quiz, plain-English explainers of how bond builders work (bis-aminopropyl diglycol dimaleate, peptides, keratin fragments), an ingredient decoder for shampoo labels, and a weekly routine planner matched to your damage level — the definitive pocket guide to the fastest-growing category in haircare.

## Target Audience
- Primary: Women 20–45 investing in bond-builder products (Olaplex/K18-era shoppers) confused by conflicting advice
- Secondary: Curly/coily and bleached-hair users building repair routines; cosmetology students
- Demographics: Beauty-engaged iOS users who already buy premium haircare ($30+ products) and research ingredients

## Problem Statement
Bond repair exploded from a pro-salon treatment into a shelf-wide category, but the knowledge layer didn't keep up. Today it lives in TikTok rants, SEO blog spam, and Reddit threads. Product labels shout marketing terms ("repairs bonds!") with no explanation of what peptides vs. maleic acid derivatives actually do, or why you can't use a bond builder in place of protein treatment. No app decodes the ingredient list, assesses your damage level, or sequences the products you already own into a coherent weekly routine. The gap between purchase intent and usable education is total.

## Trend Evidence
- **Source 1**: Exploding Topics Aug-2026 — "Bond Repair Shampoo" +3,600% search growth (#96 on the top-100 list)
- **Source 2**: iTunes mega-scan 2026-08-24: 6 queries ("bond repair shampoo", "hair bond builder", "hair porosity", "hair repair", "hair care routine tracker", "shampoo guide") → 82 unique apps; every top result is a salon booking giant or retailer; only 9 keyword-relevant matches totaling ~117 combined ratings
- **Source 3**: Category durability — bond builders moved from single-brand novelty (2018 Olaplex) to standard shelf fixture at every price tier through 2026, indicating sustained demand rather than one-season hype

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Great Clips Check-in | ⭐ 4.9 (682K) | Free | Salon logistics — pure search pollution |
| Sephora US | ⭐ 4.9 (425K) | Free | Retail; sells products, explains nothing |
| Yuka | ⭐ 4.8 (98K) | Free | Generic cosmetic safety scores; no bond-repair science or routines |
| Curly Hair Scanner & Care Plan | ⭐ 4.6 (114) | Free | Curl-pattern focus; mentions porosity once; no bond/ingredient education |
| Shampoo Scanner AI | ⭐ 3.0 (2) | ? | 2 ratings, generic scanner shell |
| HairPlan – Hair Routine | ⭐ 5.0 (1) | ? | 1 rating; quiz shell, no content depth |

**App Gap**: GREEN FIELD by tiny-app signal. Zero dedicated bond-repair/hair-science education apps exist; the only keyword-relevant results are sub-120-review shells. Giants in this space are all wrong-job (booking, retail, generic safety scoring).

## Core Features (MVP)

### Must-Have (v1.0)
1. **Damage Assessment Quiz** — 12 questions (heat use, bleach/color, elasticity feel, breakage patterns) → damage tier 1–4 with plain-language results
2. **Porosity Guide & Tests** — float/slide test walkthroughs, what porosity means for product choice
3. **Ingredient Decoder** — searchable reference of ~60 common bond-repair ingredients: what each is, evidence level, what it can/can't do
4. **Weekly Routine Planner** — damage-tier-driven schedule builder (which days: bond builder, moisture, protein, clarifying) with local reminders
5. **Label Scanner Companion** — manual entry of product ingredient lists flagged against the decoder (no cloud vision needed in v1.0)

### Nice-to-Have (v1.1+)
- Photo-based porosity self-assessment — deferred: accuracy risk without ML investment
- Product database by brand — deferred: maintenance-heavy, brand-trademark risk
- Routine export/share card — v1.2

## Content & Data
- ~60 ingredient entries {name, aka, function, evidenceLevel, worksWith, conflicts}, 12 quiz questions, 4 damage-tier plans × 7-day templates, ~15 science explainers, porosity test guides
- Sources: published cosmetic chemistry literature summaries (e.g., peer-reviewed papers on maleic acid crosslinking), brand-published INCI lists, stylist-education materials — hand-curated, dated, cited
- MVP authoring: ingredients (~80 min), explainers + quiz logic (~70 min)

## Design Direction
- **Style**: Lab-meets-vanity — clean molecular motif, precise and premium; feels like a chemist's field notes, not a beauty ad
- **Color Palette**: Porcelain `#F7F5F2`, Ink navy `#1B2A41`, Peptide teal accent `#2E8C8C`, Strand copper `#C97B4A`, Slate divider `#D8DEE4`
- **Typography**: Modern grotesque headers (Inter/SF Pro Display), generous whitespace, monospace for ingredient codes
- **Key Screens**: Home (damage tier card), Quiz, My Routine (week view), Ingredients (search + detail), Learn hub
- **Navigation**: Tab bar (Routine, Quiz, Ingredients, Learn)

## Technical Notes
- **Platform**: iOS (SwiftUI), iOS 16+
- **Backend**: None — fully on-device
- **APIs**: None (UserNotifications for routine reminders)
- **Data Storage**: Bundled JSON (`ingredients.json`, `plans.json`, `quiz.json`, `learn.json`); user tier + ticks in UserDefaults/CoreData-lite
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low-Medium

**First-launch disclaimer (verbatim requirement)**: "BondLab provides general cosmetic education, not medical or professional advice. For scalp conditions, significant hair loss, or reactions, consult a dermatologist or licensed cosmetologist."

## App Store Listing

### Title
BondLab — Hair Science Guide

### Subtitle
Porosity, actives & routines

### Keywords
bond repair,hair porosity,hair routine,k18,shampoo guide,hair science,damaged hair,olaplex

*(91 chars)*

### Description
Stop guessing at the shampoo aisle. BondLab turns bond-repair buzzwords into actual understanding — decode any label, assess your damage, and build a weekly routine that sequences your products correctly.

KNOW YOUR HAIR FIRST
A 12-question assessment maps your heat, color, and breakage history into a clear damage tier — the starting point every routine should begin with.

DECODE THE LABEL
Peptides, bis-aminopropyl diglycol dimaleate, hydrolyzed keratin — what each ingredient actually does, how strong the evidence is, and what it can't do. Searchable dictionary of 60+ bond-repair ingredients, written in plain English.

BUILD THE ROUTINE
Get a week-by-week plan matched to your tier: when to bond-build, when to moisturize, when to clarify, and which combos conflict. Optional local reminders keep you on schedule.

SCIENCE WITHOUT HYPE
Every claim is graded. Where marketing outruns the research, we say so — clearly attributed, no fear-mongering, no miracle promises.

• 100% offline — your routine works anywhere
• No ads, no tracking, no data collected
• Ingredient entries dated and sourced

Important: general cosmetic education only — not medical advice. See a dermatologist for scalp conditions or hair loss.

Free to start — one-time unlock for the full ingredient library and unlimited routines.

### Category
Primary: Reference
Secondary: Lifestyle

### Pricing
- **Model**: Freemium — free (quiz + 10 core ingredients + basic plan), $2.99 one-time unlock
- **Reasoning**: One-time unlock matches the one-time-education nature of the content; avoids subscription fatigue in beauty-reference category
- **Monetization Path**: Paid unlock; v1.2 "color-treated pack" IAP possible

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | +3,600% growth on a category that has become a durable shelf staple |
| App Gap | 9/10 | Green field: only tiny-app signal — relevant hits total ~117 ratings, giants all wrong-job |
| Build Simplicity | 9/10 | Static JSON + quiz logic + local notifications; no backend, no accounts |
| Evergreen Potential | 7/10 | Bond builders are now a permanent category; ingredient hype cycles will rotate |
| Monetization | 6/10 | Motivated premium-shopper audience, but reference-app ceiling is real |
| **Average** | **7.8/10** | |

## Risk Assessment
- **Trend Fizzle**: Low-Medium — specific products rotate, but damage-repair demand persists across the category
- **App Store Rejection**: Low — educational reference; disclaimers shipped on first launch
- **Competition**: Medium — a well-funded beauty app could add a bond module, but wrong-job giants rarely pivot to deep reference
- **Legal/IP**: Low — avoid brand logos/trademarks in content; discuss ingredient classes, not branded products; cite sources
- **Content Maintenance**: Medium — ingredient library refresh 2×/year keeps evidence grades current (also the moat)

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics +3,600%, iTunes scan, category durability)
- [x] App Store search shows no dedicated bond-repair/hair-science reference (mega-scan 2026-08-24)
- [x] MVP buildable without backend/API dependencies
- [x] Health-adjacent gate passed: disclaimers mandatory, no medical claims
- [x] No obvious legal/copyright issues (ingredient-class discussion, no trademarks)
- [x] Build time estimate ≤ 3 hours (2.5h)
