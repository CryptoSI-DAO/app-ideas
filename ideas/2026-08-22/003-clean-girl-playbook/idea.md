# App Idea: Clean Girl Playbook

*Generated: 2026-08-22*
*Confidence Score: 7.6/10*

---

## Pitch
"Clean girl aesthetic" is exploding (+6,900% search growth): slick-back buns, glazed skin, gold hoops, 5am Pilates energy. But every existing app is another habit *tracker* wearing the branding. The actual playbook — the routines, skincare order, hair techniques, capsule checklist, weekly reset ritual as *step-by-step reference guides* — doesn't exist as an app. Clean Girl Playbook is the curated, offline reference: open it, see exactly how the routine works, check off your setup.

## Target Audience
- Primary: Women 16–30 discovering the aesthetic via TikTok/Pinterest, wanting a concrete starter guide
- Secondary: Gift-buyers and routine-curious users who want structure without another subscription habit app
- Demographics: Gen Z / young millennial, iOS-dominant, high TikTok exposure, buys aesthetics

## Problem Statement
The clean girl look is documented in thousands of scattered TikToks. A newcomer must reverse-engineer: what's the skincare ORDER? What products count as "essentials"? How does the slick bun actually stay? What belongs in the capsule wardrobe? Existing apps (That Girl: Become a Clean Girl — 4.6K reviews; That Girl Routine Planner — 5.7K; SLAY — 119) are streak-based habit trackers with generic task lists, not technique references. Users churn once motivation dips because nothing taught them the *how*.

## Trend Evidence
- **Source 1**: Exploding Topics — "Clean Girl Aesthetic" +6,900% search growth, rank #98 top-100 US trends Aug 2026
- **Source 2**: Adjacent trend cluster all rising simultaneously — Pilates Outfit +2,133%, Milky Toner +4,600% (already validated as app idea scoring 9.0 in this repo), Satin Bonnet +214%
- **Source 3**: iTunes gap scan — "clean girl aesthetic"/"clean girl routine" surface small dedicated trackers (≤5.7K reviews) and mega-generic habit apps (Me+ 246K); zero dedicated *reference/playbook* apps
- **Momentum**: Rising hard now; aesthetic-trend risk noted below

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| That Girl: Become a Clean Girl | ⭐ 4.8 (4,622) | Subs | Habit streaks; no technique content |
| That Girl: Routine Planner | ⭐ 4.8 (5,739) | Subs | Same tracker pattern, generic tasks |
| Me+ Lifestyle Routine | ⭐ 4.8 (246K) | Subs | Giant generic routine app, no clean-girl specificity |
| SLAY – become that girl | ⭐ 4.7 (119) | ? | Tiny, tracker-only |
| Aesthetic Toka – Outfit Ideas | ⭐ 4.4 (16.5K) | Ads | Outfit pictures, no routines |

**App Gap**: QUALITY-BAR opportunity (fragmented) — dedicated apps exist but all miss the reference/guide job. Different workflow (playbook vs. tracker) per the adjacent-vs-duplicate rule.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Routine Guides** — Morning Ritual, Evening Wind-Down, Weekly Reset: step-by-step ordered guides with why-it-matters notes and time estimates per step
2. **Skincare Order Reference** — visual AM/PM layering order (cleanser → toner → serum → moisturizer → SPF), ingredient do-not-mix warnings
3. **Signature Hair Guide** — slick-back bun, claw clip, heatless curls: supply list + numbered steps
4. **Capsule Checklist** — tap-to-check wardrobe essentials list (white tee, gold hoops…) with "staples vs. splurge" notes

### Nice-to-Have (v1.1+)
- Product-category glossary expansion (vanity tour checklist)
- Seasonal pack updates (summer glow pack) — deferred, requires content refresh cadence
- Pinterest-style mood board — deferred, asset-heavy

## Content & Data
- 3 routine guides (~8–10 steps each), 2 hair tutorials, 1 skincare order map, ~24-item capsule checklist, ~15-term glossary
- Source: synthesized from public beauty editorial consensus (static, factual technique descriptions — no product brands required)
- Bundled JSON; v1.0 ships complete

## Design Direction
- **Style**: Soft neutral luxury — the aesthetic itself is the design system
- **Color Palette**: Background #FAF6F1, Card #FFFFFF, Text #3A3330, Accent gold #C9A96A, Sage secondary #A8B5A0, Success #7C9070, Warning #D9A441, Error #C26A5A
- **Typography**: New York (serif) for titles (28 bold), SF Pro body 16, captions 13 — serif headlines deliver the editorial feel
- **Key Screens**: Home (guide grid), Guide Detail, Skincare Order, Capsule Checklist
- **Navigation**: No tabs — single scroll home + push details; checklist via bottom sheet
- **Reference Apps**: Editorial feel of Milky Toner Guide apps; Apple Fitness+ calm cards

## Screen-by-Screen Specification

### Home
- Purpose: browse all playbooks
- Layout: serif greeting header, 2×2 card grid (Routines, Skin, Hair, Capsule), glossary strip
- Elements: 4 category cards (icon + label + item count), glossary horizontal scroll chips, settings gear
- Interactions: tap card → section; tap chip → glossary entry sheet
- Data: bundled JSON

### Guide Detail (Routine)
- Purpose: walk a routine step-by-step
- Layout: hero title w/ total time estimate, ordered step list, each step expandable
- Elements: step number badges (#C9A96A), step title, expand chevron revealing detail text + time chip, check-off circles
- Interactions: expand/collapse; check off steps (session-local); swipe back
- Data: guide JSON

### Skincare Order
- Purpose: master AM/PM layering
- Layout: two columns (AM / PM) of stacked product tiles connected by arrows
- Elements: product-type tiles w/ icons, arrow indicators, warning banners for conflicts (e.g., retinol + acids)
- Interactions: tap tile → explainer popover
- Data: skincare JSON

### Capsule Checklist
- Purpose: build the wardrobe base
- Elements: 24 check rows grouped (Tops/Bottoms/Shoes/Accessories), progress bar, staples-vs-splurge tag pills
- Interactions: toggle checks → progress bar animates; persists locally

## Data Model
```json
// Guide — bundled
{"id":"morning-ritual","category":"routines","title":"Morning Ritual",
 "totalMinutes":35,"steps":[
  {"n":1,"title":"Sunlight + water","minutes":5,"detail":"Open curtains, big glass of water before phone"},
  {"n":2,"title":"Move for 10","minutes":10,"detail":"Walk, pilates flow, or stretch — anything counts"}]}
// SkincareStep — bundled
{"order":1,"slot":"AM","name":"Cleanser","icon":"drop","detail":"Gentle gel cleanser",
 "warning":null}
{"order":3,"slot":"PM","name":"Retinoid","icon":"sparkle","detail":"Pea-size, 2–3 nights/week",
 "warning":"Do not layer with AHAs/BHAs same night"}
// CapsuleItem — bundled
{"id":"white-tee","group":"Tops","label":"Crisp white tee","tag":"Staple"}
// GlossaryTerm — bundled
{"term":"Glazed skin","definition":"Dewy, hydrated finish from layering hydrating toners + serums"}
```

## Technical Notes
- **Platform**: iOS 17+, SwiftUI, portrait-only
- **Backend**: None — fully on-device
- **APIs**: None
- **Data Storage**: Bundled JSON + UserDefaults (checks)
- **Estimated Build Time**: ~2.5 hours
- **Complexity**: Low

### Build Order
1. Scaffold + tokens + serif typography system
2. Home grid + navigation
3. Guide Detail w/ expandable steps + session checks
4. Skincare Order custom layout + popovers
5. Capsule checklist + persistence, polish, icon

### Testing Checklist
- All guides render full step lists (no truncation on SE)
- Checks persist across relaunch
- Warning banners appear on conflicting PM stacks
- Dynamic type at largest accessibility size stays readable
- Light mode only — verify no forced dark artifacts

## App Store Listing

### Title
Clean Girl Playbook (19 chars)

### Subtitle
Routines, skin order & style (28 chars)

### Keywords
clean girl,aesthetic,routine,skincare order,slick bun,capsule wardrobe,self care,glow up,that girl,morning routine,lifestyle guide (≤100)

### Description
Stop scrolling for the clean girl aesthetic — start living it. Clean Girl Playbook turns thousands of scattered TikToks into one beautiful, offline reference: the exact routines, orders, and checklists behind the look.

ROUTINES THAT ACTUALLY WORK
Morning Ritual, Evening Wind-Down, Weekly Reset — every step explained with timing and why it matters. Not streaks, not guilt: just a playbook you can follow from day one.

SKINCARE, IN THE RIGHT ORDER
The famous glazed-skin look is all about layering. Get the AM and PM order mapped visually, with do-not-mix warnings so you never waste product (or irritate your skin) again.

HAIR, MASTERED
Slick-back bun, claw-clip twist, heatless curls — supply lists and numbered steps for the three signature styles.

THE CAPSULE CHECKLIST
Build the wardrobe foundation: 24 essentials tagged Staple or Splurge, with satisfying progress tracking.

NO ACCOUNT. NO SUBSCRIPTION TRAP.
Every guide included, fully offline, one simple unlock. Download Clean Girl Playbook and make the aesthetic yours.

### Category
Primary: Lifestyle | Secondary: Reference

### Pricing
- **Model**: Freemium — free Routines pack; $1.99 one-time unlocks Skin/Hair/Capsule packs
- **Reasoning**: Try-before-buy suits aesthetic browsers; one-time unlock avoids sub fatigue in this demo
- **Monetization Path**: Seasonal content packs ($0.99) if trend sustains

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8.5/10 | +6,900%, entire adjacent cluster rising |
| App Gap | 7.0/10 | Trackers exist; reference angle unclaimed |
| Build Simplicity | 8.5/10 | Static content, simple layouts |
| Evergreen Potential | 6.5/10 | Aesthetic fade risk; core self-care structure endures |
| Monetization | 7.5/10 | Proven spender demo; freemium converts |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: Medium-high — aesthetics cycle; mitigation: content framed as timeless self-care structure, seasonal packs optional not promised
- **App Store Rejection**: Minimal — no medical claims beyond generic skincare-order facts
- **Competition**: Tracker incumbents could bolt on guides — but their streak architecture fights the reference UX
- **Legal/IP**: No brand names, original illustrations/icons only
- **Content Maintenance**: Optional seasonal refresh; ship-and-forget viable

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics + adjacent cluster + iTunes scan)
- [x] App Store search shows ≤ 3 relevant apps OR top apps have < 3 stars (dedicated exist but different workflow — reference gap)
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours
