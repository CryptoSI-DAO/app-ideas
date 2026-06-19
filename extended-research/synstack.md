# SynStack — Supplement Interaction Checker: Extended Research

*Generated: 2026-06-19*
*Related Idea: [002-synstack](../../ideas/2026-06-19/002-synstack/idea.md)*
*Confidence Score: 8.0/10*

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Market Size** | $150B+ global supplement market, growing 12.5% CAGR |
| **Target Users** | 180M+ US adults take supplements; ~60M take 3+ daily |
| **Trend Signal** | Magnesium Glycinate +3,900% on Exploding Topics (#89, Jun 2026) |
| **App Gap** | TRUE supplement interaction checker is an empty niche |
| **Build Time** | ~3 hours (SwiftUI, bundled JSON, no backend) |
| **Revenue Model** | Paid $2.99 (health safety utility) |
| **SAM** | 2.4M qualified iOS users (US, 30-55, health-conscious, 3+ supplements) |
| **Risk Level** | Medium (medical disclaimer required; no backend risk) |

**Bottom Line**: SynStack fills a genuine gap at the intersection of two structural trends — supplement market explosion and polypharmacy awareness. The competitive landscape has NO dominant player in supplement-specific interaction checking. Synstax tried and abandoned (1 review). SuppCo is the category leader but is a barcode scanner, not an interaction checker. This is a clean, buildable, monetizable gap.

---

## 2. The Opportunity

### Why Now?

**Supplement market is exploding.** The global dietary supplement market is $150B+ and growing at 12.5% CAGR through 2028 (Grand View Research, Mordor Intelligence). In the US alone, 77% of adults take dietary supplements (CRN 2023 survey), and the average supplement user takes 4+ products daily.

**Magnesium Glycinate is the canary in the coal mine.** On Exploding Topics (Jun 2026), "Magnesium Glycinate Supplement" ranks #89 with +3,900% search growth. This isn't a fad — it reflects a structural shift toward evidence-based supplementation. Related trends: Probiotic Soda +1,975%, Algae Cooking Oil +2,200%, Health Tracking Ring +5,800%. The "stack your supplements" culture is going mainstream.

**Polypharmacy awareness is rising.** 42% of adults 65+ take 5+ medications (CDC). Drug interactions cause 5% of hospitalizations (Scientific Reports, 2024). The intersection of "takes supplements" AND "takes medications" is where the danger — and the opportunity — lives. Reddit's r/Supplements (1.3M+ members) has daily posts asking "can I take X with Y?"

**Consumer behavior is shifting.** People don't want to ask their pharmacist every time they add a new supplement. They want instant, private, trustworthy answers on their phone. The "quantified self" movement (Oura Ring +5,800%, Apple Watch health features) drives demand for personal health intelligence tools.

### The Specific Gap

There is NO app on the App Store that does **all three** of:
1. Supplement + Supplement interaction checking
2. Supplement + Prescription Medication interaction checking
3. Supplement + Herb/Botanical interaction checking

...in a clean, consumer-friendly, offline-first interface.

The closest attempts:
- **Synstax** — has the right concept (5,142 combinations) but 1 review, domain dead, effectively abandoned
- **SuppCo** — 24K reviews, category leader, but it's a BARCODE SCANNER for nutrition labels, not an interaction checker
- **Drugs.com** — excellent interaction data but prescription-only, no supplement coverage, web-first
- **epocrates** — clinical tool for doctors, not consumers

---

## 3. App Store Gap Analysis

### Search Query Results (iTunes Search API, Jun 2026)

| Query | Top Result | Rating | Reviews | Relevance |
|-------|-----------|--------|---------|-----------|
| supplement interaction checker | SuppCo: Supplement Scanner | 4.8★ | 24,135 | ❌ Scanner, not checker |
| vitamin interaction checker | Synstax: Interaction Checker | 5.0★ | 1 | ⚠️ Abandoned |
| drug interaction checker | Drugs.com Medication Guide | 4.8★ | 15,125 | ❌ Rx-only, no supplements |
| supplement safety | SuppCo: Supplement Scanner | 4.8★ | 24,135 | ❌ Scanner, not checker |
| medication interaction | Drugs.com Medication Guide | 4.8★ | 15,125 | ❌ Rx-only |
| herb drug interaction | epocrates | 4.5★ | 7,079 | ❌ Clinical, not consumer |
| supplement checker | SuppCo: Supplement Scanner | 4.8★ | 24,135 | ❌ Scanner |
| polypharmacy checker | WebMD Symptom Checker | 4.7★ | 134,634 | ❌ Symptom checker, not interactions |
| vitamin safety checker | UV Index Widget | 4.7★ | 14,196 | ❌ Unrelated |
| health supplement guide | SuppCo: Supplement Scanner | 4.8★ | 24,135 | ❌ Scanner |
| supplement tracker | SuppCo: Supplement Scanner | 4.8★ | 24,135 | ❌ Scanner |
| medication safety app | Davis Drug Guide | 4.8★ | 8,631 | ❌ Nursing reference |

### Key Finding

Across 12 search queries covering the supplement interaction space, **ZERO apps** returned as top results provide dedicated supplement interaction checking. The same 3-4 apps (SuppCo, Drugs.com, epocrates, WebMD) dominate results but serve fundamentally different use cases. This is a classic "search result pollution" gap — the right apps don't exist, so wrong apps fill the results.

### Unique Apps Discovered (42 total across all queries)

**Direct Competitors (interaction-related):**
1. Synstax: Interaction Checker — 5.0★, 1 review — ABANDONED
2. Drug Interaction Checker + — 4.1★, 67 reviews — Rx-focused, dated UI
3. WeSupp: Supplement Safety Scan — 4.1★, 9 reviews — New, unproven

**Adjacent Competitors (supplement scanners):**
4. SuppCo: Supplement Scanner — 4.8★, 24,135 reviews — Barcode scanner, not checker
5. Prove It - Supplement Scanner — 4.4★, 15,000 reviews — Evidence reviews, not interactions
6. Supplement Scanner: NutriSee — 4.7★, 44 reviews — Scanner

**Adjacent Competitors (medical references):**
7. Drugs.com Medication Guide — 4.8★, 15,125 reviews — Rx-only
8. epocrates — 4.5★, 7,079 reviews — Clinical
9. Pocket Pharmacist — 4.7★, 3,841 reviews — Drug info, subscription
10. UpToDate Lexidrug — 4.7★, 4,211 reviews — Clinical

**Non-competitors (filling search results):**
11. iHerb — Shopping platform
12. WebMD — Symptom checker
13. Habit Tracker — General productivity
14. Bobby Approved — Food scanner

---

## 4. Competitive Analysis

### Direct Competitors

#### Synstax: Interaction Checker
- **Rating**: 5.0★ (1 review)
- **Price**: Free
- **Developer**: 宁 丁 (individual developer)
- **What it does**: Claims 5,142 supplement combination checks + diet absorption effects
- **Fatal Flaw**: Effectively abandoned. 1 review. Domain (synstax.app) doesn't resolve. App description hasn't been updated. No social presence. The developer built the right concept but couldn't maintain it.
- **Verdict**: Validates the demand but proves the execution failed. Opportunity for a polished successor.

#### Drug Interaction Checker +
- **Rating**: 4.1★ (67 reviews)
- **Price**: Free
- **Developer**: HYDL
- **What it does**: Drug-drug interaction checker with pill ID
- **Fatal Flaw**: Prescription medication only. No supplement coverage. Dated UI (last meaningful update appears to be 2018). Medical/clinical framing, not consumer-friendly.
- **Verdict**: Not a real competitor — serves a different audience (healthcare professionals).

#### WeSupp: Supplement Safety Scan
- **Rating**: 4.1★ (9 reviews)
- **Price**: Free
- **Developer**: Relentless
- **What it does**: Supplement scanner with safety information (appears to be a French app localized to English)
- **Fatal Flaw**: Only 9 reviews. New entrant with no traction. Description reads like a translation. No interaction checking — it's a product scanner.
- **Verdict**: Too early to assess but currently not a threat.

### Adjacent Competitors

#### SuppCo: Supplement Scanner (Category Leader)
- **Rating**: 4.8★ (24,135 reviews)
- **Price**: Free
- **Developer**: Supple Stack Inc
- **What it does**: Barcode scanner for supplement facts. 160,000+ supplement database. Tracks daily regimen.
- **Fatal Flaw**: It's a SCANNER, not an INTERACTION CHECKER. You scan a barcode to see nutrition facts. It doesn't tell you if your magnesium conflicts with your calcium. This is the #1 result for almost every supplement search, which pollutes the gap analysis — but it doesn't fill the gap.
- **Verdict**: The 800-pound gorilla in the supplement app space, but solving a different problem. Could add interaction checking as a feature, but their business model (supplement recommendations, affiliate revenue) doesn't align with it.

#### Prove It - Supplement Scanner
- **Rating**: 4.4★ (15,000 reviews)
- **Price**: Free
- **Developer**: Control. Alt. Delete. LLC
- **What it does**: Evidence-based supplement reviews via barcode scan. Science-backed efficacy ratings.
- **Fatal Flaw**: Reviews individual supplements, doesn't check interactions between them. Different use case.
- **Verdict**: Strong in the "is this supplement worth buying" space, not the "is my stack safe" space.

#### Drugs.com Medication Guide
- **Rating**: 4.8★ (15,125 reviews)
- **Price**: Free
- **What it does**: Comprehensive drug interaction checker. Excellent data. Web-first with app wrapper.
- **Fatal Flaw**: Prescription medications only. No supplement data. Requires internet. Clinical tone. Not designed for consumers managing supplement stacks.
- **Verdict**: Best-in-class for drug-drug interactions but doesn't address the supplement gap at all.

### Positioning Map

```
                    CONSUMER-FRIENDLY
                           │
                           │
         Prove It ●        │        ● SynStack (proposed)
                           │
                           │
   SCANNER ────────────────┼──────────────── INTERACTION CHECKER
                           │
                           │
         SuppCo ●          │        ● Synstax (abandoned)
                           │
                    CLINICAL/PROFESSIONAL
                           │
                    ● Drugs.com
                    ● epocrates
```

**The empty quadrant**: Consumer-friendly + Interaction Checker. This is where SynStack lives.

---

## 5. Revenue Model

### Monetization Layers

| Layer | Model | Price | Target Segment |
|-------|-------|-------|----------------|
| **Core App** | One-time purchase | $2.99 | All users |
| **Pro Upgrade** (v1.1) | In-app purchase | $1.99 | Power users |
| **Database Updates** | Free with purchase | — | Retention |
| **Future: Telehealth** | Affiliate/referral | $5-15/referral | Users with major interactions |

### Why $2.99 Works

- Health safety apps command $2.99-$4.99 (Pocket Pharmacist: free trial → subscription; Drugs.com: free but ad-supported)
- Users pay for TRUSTWORTHINESS in health information
- One-time purchase removes friction vs. subscription for a reference tool
- Higher perceived value than "another free scanner"
- At $2.99, need ~800 sales/month to hit $200/mo (realistic for a niche health app with good ASO)

### Market Sizing

- **TAM**: 180M US adults taking supplements
- **SAM**: 60M taking 3+ supplements or supplements + medications (the "stackers" who need interaction checking)
- **SAM (iOS)**: 30M (50% iOS skew in health app demographics)
- **SAM (iOS, paying)**: 2.4M (8% conversion to paid health app)
- **Realistic Year 1**: 5,000-15,000 downloads → $15,000-$45,000 revenue
- **Realistic Year 2**: 20,000-50,000 downloads (with ASO + word of mouth) → $60,000-$150,000

### Revenue Comparison

| App | Model | Est. Annual Revenue |
|-----|-------|-------------------|
| SuppCo | Free + affiliate | Unknown (supplement recommendations) |
| Drugs.com | Free + ads | $5M+ (web + app) |
| Pocket Pharmacist | Free trial → $4.99/mo | ~$500K (est. 10K subscribers) |
| **SynStack (projected)** | **$2.99 one-time** | **$15K-$150K** |

---

## 6. Risk Analysis

### Regulatory Risk: MEDIUM

**Risk**: Apple may reject health apps that make medical claims. FDA could classify interaction checking as a medical device.

**Mitigation**:
- Frame as "reference tool" not "medical advice"
- Include prominent disclaimer: "This app is for educational purposes only. Always consult your healthcare provider before making changes to your supplement or medication routine."
- Avoid diagnostic language ("you should stop taking X") → use informational language ("X and Y have a known interaction")
- Cite published sources for all interaction data
- Category: Health & Fitness (not Medical) for App Store submission
- Precedent: Drugs.com, WebMD, and Pocket Pharmacist all operate in this space without FDA issues

### Trust Risk: MEDIUM-HIGH

**Risk**: Users need to trust the interaction data. Wrong information could cause harm and liability.

**Mitigation**:
- Source ALL data from published, peer-reviewed databases (Natural Medicines Comprehensive Database, NIH ODS, Examine.com, published drug interaction literature)
- Include source citations for every interaction
- Clear severity ratings (Major/Moderate/Minor/None) with mechanism explanations
- "Last updated" date on the database
- No user-generated content — all data curated by the developer

### Competitive Risk: LOW-MEDIUM

**Risk**: SuppCo, Drugs.com, or Medisafe could add supplement interaction features.

**Mitigation**:
- **SuppCo**: Their business model is supplement recommendations/affiliates. Interaction checking doesn't align with their revenue. Low risk of them adding it.
- **Drugs.com**: Could add supplements but their brand is prescription-focused. Would take 12+ months to build.
- **Medisafe**: Medication management focus. Supplements are adjacent but not core.
- **New entrants**: The 3-hour build time means SynStack can launch fast and establish ASO presence before competitors react.
- **First-mover advantage**: In the supplement interaction niche, being first matters for ASO and word-of-mouth.

### Content Maintenance Risk: MEDIUM

**Risk**: Interaction database needs regular updates as new research is published.

**Mitigation**:
- Bundle updates with app updates (App Store release cycle)
- ~2 hours/month to review new publications and update JSON
- Start with 400 curated pairs (covers 90% of common interactions)
- Community can submit interaction reports for v1.1

### Legal Risk: MEDIUM

**Risk**: Liability if user makes health decision based on app data and is harmed.

**Mitigation**:
- Comprehensive Terms of Service and Disclaimer
- "For educational purposes only" framing
- No collection of personal health data (privacy-first = no liability from data breaches)
- LLC or corporation structure for the app business
- Precedent: Drugs.com, WebMD, and every health reference app operates with disclaimers

---

## 7. Your Moats

| Moat | Strength | Description |
|------|----------|-------------|
| **First-Mover in Niche** | ⭐⭐⭐ | No established supplement interaction checker. First to market = ASO dominance. |
| **Curated Database** | ⭐⭐⭐⭐ | 400+ evidence-based interaction pairs with source citations. Hard to replicate. |
| **Offline-First** | ⭐⭐⭐ | Works without internet. Competitors (Drugs.com, WebMD) require connectivity. |
| **Privacy-First** | ⭐⭐⭐ | No account, no data collection, no tracking. Appeals to health-conscious users. |
| **Clean UX** | ⭐⭐⭐ | Medical-grade clarity with consumer warmth. Competitors are clinical or cluttered. |
| **Word of Mouth** | ⭐⭐⭐ | Health-conscious users share safety tools with friends/family. Organic growth channel. |
| **Content Depth** | ⭐⭐⭐⭐ | Mechanism explanations + timing recommendations = more than just "red/yellow/green." |

---

## 8. Recommended Approach: Phased Build Plan

### Phase 1: MVP (3 hours)

**Core Features:**
- Interaction checker: select 2-4 substances, see severity + mechanism + recommendation
- 150 supplements + 50 medications + 30 herbs with ~400 curated interaction pairs
- Color-coded severity cards (Red/Orange/Yellow/Green)
- Searchable substance database
- "My Stack" builder (save personal regimen, check all at once)
- Offline-first: bundled JSON database
- Medical disclaimer on first launch

**Tech Stack:**
- SwiftUI, iOS 17+
- Bundled JSON (~300KB)
- No backend, no APIs, no accounts
- Local storage only (UserDefaults or SwiftData)

**App Store:**
- Title: SynStack — Interaction Checker
- Category: Health & Fitness (secondary: Medical)
- Price: $2.99
- Keywords: supplement, interaction, checker, vitamin, medication, herb, safety, health, stack

### Phase 2: Enhanced (2 hours, Week 2-3)

**Add:**
- Timing recommendations ("Take calcium 2 hours apart from iron")
- Interaction mechanism deep-dives with source citations
- Share interaction results (text/image)
- Widget: "Daily Stack Check" showing today's supplements and any interactions
- Haptic feedback for major interactions

### Phase 3: Growth (3 hours, Month 2)

**Add:**
- Interaction database update mechanism (download updated JSON from GitHub)
- User-reported interactions (submit for review)
- Apple Health integration (read supplement/medication data if available)
- iPad optimization
- macOS version (Mac Catalyst)

### Phase 4: Ecosystem (Future)

**Consider:**
- Separate "MedStack" app for prescription-only interactions (different audience, different ASO)
- Telehealth referral partnerships (users with major interactions → book a pharmacist consultation)
- Web version for non-iOS users
- API for other health apps to query interaction data

---

## 9. Conclusion

SynStack addresses a real, validated gap at the intersection of two structural trends: supplement market explosion and polypharmacy awareness. The competitive landscape has NO dominant player in supplement-specific interaction checking — the closest attempts are either abandoned (Synstax), solving a different problem (SuppCo = scanner), or serving a different audience (Drugs.com = prescription-only).

**Key strengths:**
- ✅ TRUE green field — no quality competitor exists
- ✅ Structural trend — supplement market growing 12.5% CAGR, not a fad
- ✅ Simple build — 3 hours, no backend, bundled JSON
- ✅ Clear monetization — $2.99 paid, health safety utility commands premium
- ✅ Defensible — curated database + first-mover ASO + word-of-mouth in health community
- ✅ Low regulatory risk — reference tool with disclaimer, precedent exists

**Key risks:**
- ⚠️ Medical disclaimer required — must be framed as reference, not advice
- ⚠️ Content maintenance — monthly updates needed (~2 hrs/mo)
- ⚠️ Competitive response — SuppCo could add interactions (but misaligned with their business model)

**Verdict**: This is a **strong build candidate**. The gap is real, the trend is structural, the build is simple, and the monetization is clear. The 🚨 tag is warranted.

---

*Research sources: Exploding Topics (Jun 2026), iTunes Search API (Jun 2026), last30days social sentiment analysis, Drugs.com interaction database documentation, Grand View Research supplement market data, CDC polypharmacy statistics, Scientific Reports drug interaction hospitalization study (2024), Reddit r/Supplements community analysis.*
