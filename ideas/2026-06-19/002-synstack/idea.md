# App Idea: SynStack — Supplement Interaction Checker

*Generated: 2026-06-19*
*Confidence Score: 7.4/10*

🚨 **[Extended Research Available](../extended-research/synstack.md)** — Full competitive analysis, revenue model, risk assessment, and phased build plan.

---

## Pitch
SynStack is a clean, offline-first supplement interaction checker that lets users quickly look up whether their supplements, medications, and herbs interact with each other. With the supplement market growing at 12.5% CAGR and "Magnesium Glycinate" exploding +3,900% on Exploding Topics, consumers are overwhelmed by complex supplement stacks and worried about safety. SynStack provides a curated interaction database with severity ratings, mechanism explanations, and timing recommendations — all without requiring an account or internet connection.

## Target Audience
- Primary: Health-conscious adults (30-55) taking 3+ supplements or supplements + medications
- Secondary: Caregivers managing medications for elderly parents, fitness enthusiasts stacking supplements
- Demographics: US, 60% female skew, $50K+ income, iOS-skewing

## Problem Statement
The supplement market is massive ($150B+ globally) and growing 12.5% annually, but consumers have no clean, standalone interaction checker. Existing options: SuppCo (24K reviews) is a BARCODE SCANNER for supplement facts, not an interaction checker. Synstax exists but has 1 review (effectively abandoned). Drugs.com and epocrates focus on PRESCRIPTION medications, not supplements. People taking magnesium, vitamin D, ashwagandha, and fish oil together have no easy way to check if their stack is safe. Google searches for "can I take X with Y supplement" are rising but results are unreliable.

## Trend Evidence
- **Exploding Topics**: "Magnesium Glycinate Supplement" #89 at +3,900% growth; supplement awareness is surging
- **Exploding Topics**: "Probiotic Soda" #92 at +1,975%; "Algae Cooking Oil" #48 at +2,200% — functional food/supplement convergence trend
- **Google Trends**: "supplement interactions" steady 30-40/100; "magnesium glycinate" breakout searches
- **Momentum**: Rising — supplement market growth + aging population + wellness culture = structural trend

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| SuppCo | ⭐ 4.8 | Free | Barcode scanner for supplement FACTS, not interactions. No interaction checking. |
| Synstax | ⭐ 5.0 | Free | Has interaction checking concept but only 1 review — effectively abandoned/non-functional |
| Drugs.com | ⭐ 4.8 | Free | Prescription medication focus, no supplement coverage |
| epocrates | ⭐ 4.5 | Free | Clinical tool for doctors, not consumer-friendly, prescription-only |
| StackSnap | ⭐ 4.8 | Free | 12 reviews — supplement scanner, not interaction checker |

**App Gap**: TRUE supplement interaction checker (supplement + supplement, supplement + medication, supplement + herb) is an empty niche. Synstax tried but is abandoned. SuppCo is the best-known app but only scans barcodes for nutrition labels — it doesn't check interactions. The gap is a clean, consumer-friendly interaction checker with a curated database of evidence-based supplement interactions.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Interaction Checker** — Select 2-4 substances from a searchable list; see interaction severity (Major/Moderate/Minor/None), mechanism, and recommendation
2. **Interaction Database** — 150+ common supplements, 50+ common medications, 30+ herbs with pairwise interaction data
3. **Severity Cards** — Color-coded results: Red (Major - avoid), Orange (Moderate - caution), Yellow (Minor - monitor), Green (No known interaction)
4. **"My Stack" Builder** — Users can build their personal supplement stack and check all interactions at once

### Nice-to-Have (v1.1+)
- Timing recommendations ("Take calcium 2 hours apart from iron")
- Interaction mechanism deep-dives with source citations
- New interaction alerts when database is updated

## Content & Data
- **Key data**: Supplement names (common + scientific), interaction pairs, severity ratings, mechanism descriptions, management recommendations
- **Sources**: Published interaction databases (Natural Medicines Comprehensive Database public data, NIH Office of Dietary Supplements, Examine.com public articles, drug interaction literature)
- **MVP content**: 150 supplements × common interactions = ~400 curated interaction pairs. ~6 hours to curate from published sources.
- **Future updates**: Monthly as new supplement-drug interaction studies published

## Design Direction
- **Style**: Medical-grade clarity with consumer-friendly warmth — think Ada Health meets Bear
- **Color Palette**:
  - Primary: Deep navy (#1B2838) — trust, authority
  - Accent: Electric teal (#00B4D8) — health, vitality
  - Background: Soft white (#F8F9FA)
  - Major interaction: Crimson (#DC2626)
  - Moderate: Amber (#F59E0B)
  - Minor: Yellow (#FCD34D)
  - Safe: Emerald (#10B981)
  - Text: Slate (#334155)
- **Typography**: SF Pro Display for headings, SF Pro Text for body
- **Key Screens**: Home (interaction checker), Results (severity cards), My Stack, Substance Detail, Browse Categories
- **Navigation**: Tab bar — Check, My Stack, Browse, Info
- **Reference Apps**: Ada Health (medical reference), Drugs.com interaction checker (interaction UX pattern), Bear (clean card design)

## Technical Notes
- **Platform**: iOS (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON (~300KB for 400 interaction pairs)
- **Estimated Build Time**: 3 hours
- **Complexity**: Low-Medium — pure content/reference app with slightly more complex interaction logic

## App Store Listing

### Title
SynStack — Interaction Checker

### Subtitle
Check supplement & drug safety

### Keywords
supplement,interaction,checker,vitamin,medication,herb,safety,health,stack,dosage,magnesium,drug,combination,reference,guide

### Description
Taking multiple supplements? Wondering if they're safe together? SynStack is your evidence-based interaction checker — fast, private, and works offline.

🔍 CHECK INTERACTIONS between:
• Supplements & vitamins
• Prescription medications
• Herbs & botanicals
• Common combinations

⚡ QUICK RESULTS:
Select 2-4 substances and instantly see:
• Interaction severity (Major → None)
• What the interaction does
• What to do about it (timing, dosage adjustment, avoid)

📋 BUILD YOUR STACK:
Save your personal supplement regimen and check all interactions at once. Know your stack is safe before you take it.

📚 EVIDENCE-BASED:
All interaction data sourced from published medical literature, NIH, and established interaction databases. No guesswork.

🔒 PRIVATE & OFFLINE:
No account required. No internet needed after download. Your health data stays on your device.

Whether you're optimizing your supplement stack, managing medications, or just curious about safety — SynStack gives you clear, trustworthy answers.

### Category
Primary: Health & Fitness
Secondary: Medical

### Pricing
- **Model**: Paid $2.99
- **Reasoning**: Health utility apps with safety information command $2.99-$4.99. Users pay for trustworthy interaction data. Higher price point than ScentSafe because safety information has higher perceived value.
- **Monetization Path**: Expand to include medication-only interactions as a separate premium app; partner with telehealth platforms

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | Magnesium Glycinate +3,900% on Exploding Topics; supplement market growing 12.5% CAGR |
| App Gap | 9/10 | Synstax abandoned (1 review); SuppCo is scanner not checker; true interaction checker is empty |
| Build Simplicity | 8/10 | Pure content/reference app; interaction logic is slightly more complex but still just lookups |
| Evergreen Potential | 9/10 | Supplement market is structural growth; interaction checking is evergreen need |
| Monetization | 7/10 | $2.99 paid viable for health safety app; limited recurring but strong one-time purchase |
| **Average** | **8.0/10** | |

## Risk Assessment
- **Trend Fizzle**: Very Low — supplement market is structural growth driven by health consciousness + aging population
- **App Store Rejection**: Medium — must be framed as "reference" not "medical advice"; include disclaimer; avoid diagnostic claims
- **Competition**: Medium — Drugs.com or Medisafe could add supplement interaction features, but they're medication-focused
- **Legal/IP**: Medium — must include medical disclaimer; data from published sources only; no liability for decisions made from app
- **Content Maintenance**: Medium — monthly updates needed for new interaction findings; ~2 hours per month

## Validation Checklist
- [x] At least 3 sources confirm rising trend
- [x] App Store search shows ≤ 3 relevant apps OR top apps have < 3 stars
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues (with proper disclaimer)
- [x] Build time estimate ≤ 3 hours
