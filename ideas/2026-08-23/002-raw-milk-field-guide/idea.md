# App Idea: Raw Milk Field Guide

*Generated: 2026-08-23*
*Confidence Score: 7.8/10*

---

## Pitch
Search interest in non-homogenized/raw milk is up 4,000%, and Google is full of 2026-dated "raw milk laws by state" blog posts — but the App Store has nothing. Every existing app is either a farm-finder requiring live backend data or a breast-milk tracker (search pollution). Raw Milk Field Guide is a fully offline reference: 50-state legality breakdown (retail/farm/herd-share status), safe handling & storage protocols, what to ask a farmer, pasteurization science explained neutrally, and a glossary — the definitive pocket companion for a fast-growing food movement.

## Target Audience
- Primary: Health-focused adults 25–45 exploring raw dairy; homesteaders and regenerative-agriculture curious
- Secondary: Travelers/movers who need to know their new state's rules; farmers selling raw milk who want a neutral explainer to share
- Demographics: Rural + suburban US, overlaps with Seed Oil Scout/weston-price-style audiences, strong iOS presence

## Problem Statement
Raw milk legality is genuinely confusing: some states allow retail sale, some only on-farm purchases, some herd-shares only, some ban it entirely — and federal guidance differs from state law. Today this knowledge lives in SEO blogs (rawmilklookup.com, realmilk.com map, Farm-to-Consumer Legal Defense Fund map) that are ad-cluttered, inconsistent, and impossible to use offline at a farm stand. Farm-finder apps need live databases and location services; nobody offers the *reference layer*: rules + safety + questions-to-ask, in your pocket, always available.

## Trend Evidence
- **Source 1**: Exploding Topics — Non-Homogenized Milk +4,000% search growth
- **Source 2**: Multiple 2026-dated state-law guides ranking on Google (rawmilklookup.com, milkshelf.com Feb 2026, unanswered.io Feb 2026, sureshotfatloss.com May 2026) — publishers race to cover it because demand is fresh
- **Source 3**: Active Reddit threads ("Best place to buy raw milk" on r/AnimalBased) asking sourcing questions the app answers
- **Momentum**: Rising — sustained multi-year climb with renewed 2025–2026 acceleration

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Localize - Farmers Market | ⭐ 4.81 (12.1K) | Free | Farm finder w/ live data; no legality/safety reference |
| Organised | ⭐ 4.95 (73) | Free | Lists raw-milk farms but needs backend + location; tiny |
| Seed Oil Scout | ⭐ 4.81 (27.3K) | Free | Restaurant dining focus; different job |
| Pump Log / DairyBar etc. | ⭐ ~4.8 | Free | Breast-milk trackers — pure search pollution |
| Longmont Dairy / delivery apps | ⭐ ~4.8 | Free | Single-brand commerce apps |

**App Gap**: Fragmented-adjacent. Finder apps exist but serve discovery (and need live infrastructure); zero apps provide the offline legality-by-state + safety education reference. The core concept — "is raw milk legal here, is it safe to handle, what do I ask the farmer" — is unclaimed on the App Store.

## Core Features (MVP)

### Must-Have (v1.0)
1. **50-State Legality Map/List** — per state: sale type allowed (retail/farm-gate/herd-share/not permitted), notes on restrictions, last-reviewed date, plain-language summary
2. **Safety & Handling Protocols** — cold chain, shelf life, container hygiene, who should avoid raw milk (verbatim medical disclaimer shipped on first launch), H5N1 awareness note
3. **Farmer Questions Checklist** — 12 questions to vet a source (testing, herd health, licensing, insurance) as an interactive tick-list
4. **Science, Neutrally** — pasteurization explained (what it does/doesn't do), homogenization, nutrition claims presented with both perspectives cited

### Nice-to-Have (v1.1+)
- Herd-share agreement primer (legal concepts, not legal advice) — deferred: needs careful review
- Personal tasting/journal log — deferred: v1.0 stays pure-reference
- State law-change changelog — deferred: annual content refresh process first

## Content & Data
- 50 state entries {code, name, retailSale, farmSale, herdShare, petOnly?, summary, notes, reviewed}, ~15 safety protocol entries, 12 farmer questions, ~18 glossary/science entries
- Source: state agriculture department publications, FDA/CDC guidance, Farm-to-Consumer Legal Defense Fund summaries — hand-curated, dated, sourced
- MVP: full 50-state dataset (~90 min authoring) + safety/glossary content (~60 min). Future: annual legal-status review

## Design Direction
- **Style**: Rustic-modern field guide — cream paper texture feel, stamped-label cards, utilitarian and trustworthy
- **Color Palette**: Cream background `#FAF6EE`, Milk white `#FFFFFF`, Barn red accent `#A63D2F`, Meadow green `#5F7355`, Charcoal ink `#33302B`, Sand divider `#E5DCC9`
- **Typography**: Rockwell-style slab serif for headers; SF Pro body; monospace accents for state codes
- **Key Screens**: Home (disclaimer + search), State Map/List, State Detail, Safety Hub, Farmer Checklist, Science Glossary
- **Navigation**: Tab bar (States, Safety, Checklist, Learn) + stack detail pushes
- **Reference Apps**: Screwworm Watch (public-health guide pattern), Food Shelf Life Guide

## Technical Notes
- **Platform**: iOS (SwiftUI), iOS 16+
- **Backend**: None — fully on-device
- **APIs**: None
- **Data Storage**: Bundled JSON (`states.json`, `safety.json`, `questions.json`, `learn.json`); checklist ticks in UserDefaults
- **Estimated Build Time**: 3 hours (content-heaviest of today's three)
- **Complexity**: Low-Medium

**First-launch disclaimer (verbatim requirement)**: "This app is for general information only and is not legal, medical, or food-safety advice. Raw milk can contain harmful bacteria regardless of source. Laws change — always verify with your state's agriculture department and consult a healthcare provider before consuming raw milk, especially if pregnant, immunocompromised, very young, or elderly."

## App Store Listing

### Title
Raw Milk Field Guide

### Subtitle
Laws, safety & smart sourcing

### Keywords
raw milk,dairy farm,pasteurization,homestead,state laws,herd share,food safety,A2 milk

*(86 chars)*

### Description
Your offline companion to America's fastest-growing dairy movement — laws for all 50 states, safe handling protocols, and the exact questions to ask before you buy.

KNOW YOUR STATE'S RULES
Raw milk law is a patchwork: retail sale, on-farm purchase, herd shares — or none of the above. Get a clear, plain-language summary for every US state, with restriction notes and review dates. Moving or traveling? Your answer travels with you — no internet required.

HANDLE IT SAFELY
If you choose to drink raw milk, handling matters. Cold-chain guidance, shelf-life tables, container hygiene, and honest risk information — including who should avoid raw milk entirely. We present both sides: the movement's claims AND regulator warnings, clearly attributed.

VET YOUR SOURCE LIKE A PRO
A 12-point farmer checklist covering testing routines, herd health, licensing and insurance. Tick items off right at the farm stand.

UNDERSTAND THE SCIENCE
Pasteurization and homogenization explained without hype — what each process actually does, what studies suggest, and where genuine uncertainty remains.

BUILT TO BE TRUSTED
• 100% offline — works at the farmers market, on the farm, in a dead zone
• No ads, no tracking, no data collected
• Sources dated and cited; annual legal review planned

Important: this app provides general information, not legal, medical, or food-safety advice. Always verify current laws with your state agriculture department and consult a healthcare provider about raw milk consumption.

Download free to explore — upgrade once to unlock the full 50-state reference.

### Category
Primary: Reference
Secondary: Food & Drink

### Pricing
- **Model**: Freemium — free (5 sample states + safety basics), $2.99 one-time unlock
- **Reasoning**: Legality content carries annual maintenance burden; one-time fee funds reviews without subscription friction in a trust-sensitive niche
- **Monetization Path**: Paid unlock; potential v1.2 "homestead pack" (goat/sheep milk laws) IAP

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | +4,000% search growth; 2026 publisher gold-rush confirms fresh demand |
| App Gap | 8/10 | Finders exist (backend-bound); zero offline legality/safety references |
| Build Simplicity | 9/10 | Static reference JSON; freemium paywall is the only added complexity |
| Evergreen Potential | 8/10 | Multi-year movement, growing; needs annual law-review upkeep |
| Monetization | 6/10 | Niche ceiling but motivated buyers; freemium beats flat paid here |
| **Average** | **7.8/10** | |

## Risk Assessment
- **Trend Fizzle**: Low — underlying interest predates the spike and keeps growing
- **App Store Rejection**: Low-Medium — educational reference with prominent disclaimers; avoid giving specific legal advice; no sourcing instructions for bypassing laws
- **Competition**: Low-Medium — finder startups would need to pivot from live-data model to reference
- **Legal/IP**: Low — summarize public law; label everything "not legal advice"; cite sources
- **Content Maintenance**: Medium — state laws change; commit to annual review cycle (this is also the moat)

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics, 2026 guides, Reddit)
- [x] App Store search shows no dedicated legality/safety reference apps
- [x] MVP can be built without backend/API dependencies
- [x] Content handled neutrally with mandatory disclaimers (health-adjacent gate passed)
- [x] No obvious legal/copyright issues (summarized public law, cited)
- [x] Build time estimate ≤ 3 hours (3h)
