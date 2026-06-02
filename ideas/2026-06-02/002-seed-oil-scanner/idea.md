# App Idea: SeedOilScan

*Generated: 2026-06-02*
*Confidence Score: 8.0/10*

---

## Pitch
SeedOilScan is a beautifully curated reference app that helps users identify and avoid seed oils (canola, soybean, sunflower, safflower, corn, cottonseed) in packaged foods. It includes a searchable database of 300+ common products with their oil content, a barcode-by-text search, and a clean "safe/avoid" food categorization. Inspired by the explosive "seed oil free" movement on TikTok, Reddit, and mainstream wellness circles. Built with 100% offline bundled content — no camera, no barcode scanning, just pure reference data.

## Target Audience
- Primary: Health-conscious consumers (ages 22–45) following the "seed oil free" dietary movement on social media
- Secondary: Biohackers, carnivore/low-tox diet followers, parents researching better food options for kids
- Demographics: US/Canada/UK, health-focused, higher-than-average spending on organic/natural foods

## Problem Statement
The "avoid seed oils" movement is one of the biggest dietary trends of 2024–2026, with massive traction on TikTok (#seedoilfree has 200M+ views), Reddit (multiple growing communities), and YouTube. But there's no simple, beautiful reference app that bundles everything in one place. Existing options: Seed Oil Scout requires internet for its database and has a cluttered Food & Drink store listing. Yuka and Olive scan cosmetics, not food oil content accurately. A well-organized, offline-first reference guide targeting this specific need has a gap wide enough to drive a truck through.

## Trend Evidence
- **Source 1 (Exploding Topics)**: "Seed oil free" and "PDRN" are both on the June 2026 top 40 trending topics list (5,900%+ growth)
- **Source 2 (TikTok)**: #seedoilfree has 200M+ views; "what I eat in a day seed oil free" videos regularly hit millions
- **Source 3 (Google Trends)**: Google Trends Explore for US 7-day shows sustained upward trajectory for "seed oil free" and "no seed oils" queries
- **Momentum**: Rising — the movement is still accelerating as mainstream media coverage increases

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Seed Oil Scout | ⭐4.8 (25,330 ratings) | Free | Good but cluttered UX, requires internet connection for full functionality, focused on restaurants not grocery |
| Seed Oil Scanner (by Jessie Maxwell) | ⭐0 (0 ratings) | Free | Abandoned — zero ratings means never launched properly |
| Yuka - Food & Cosmetic Scanner | ⭐4.8 (93,738 ratings) | Free | Not focused on seed oils; too broad, requires barcode scanning, French-centric |
| Olive - Holistic Food Scanner | ⭐4.8 (34,721 ratings) | Free | Not focused on seed oils; AI-based scanner overkill for this use case |

**App Gap**: Seed Oil Scout is good but focused on restaurant dining and requires internet. There's no clean, offline-first, grocery-store-focused seed oil reference app that doesn't need a camera or connection. The concept of a simple curated reference (like a beautifully designed "Which foods contain seed oils?" guide) is wide open.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Seed Oil Database** — Bundled JSON with 300+ common packaged food products categorized as "Contains Seed Oils" / "Seed Oil Free" / "Check Label". Each entry includes brand, product name, specific oils listed in ingredients, and a brief why-it-matters note. Searchable by product name or brand.
2. **Educational Content** — Five bundled information screens explaining: What are seed oils? (the 7 to avoid: canola, soybean, sunflower, safflower, corn, cottonseed, grapeseed), Why avoid them? (science summary), Seed oil free alternatives (olive oil, avocado oil, coconut oil, butter, tallow), How to read labels (hidden names), and Seed oil free cooking oils ranked. All offline.
3. **Category Browser** — Browse safe/avoid products by grocery category: Snacks, Breads & Baked Goods, Cooking Oils, Condiments, Frozen Meals, Cereals, Salad Dressings, Crackers & Chips, Protein Bars, Candy & Chocolate, Baby Food, Pet Food.
4. **Favorites / Personal Safe List** — Users can mark products as "safe for me" and access them from a dedicated favorites tab. Persisted locally.
5. **Daily Tip** — A "Tip of the Day" card on home screen with a rotating fact about seed oils, label reading, or ingredient alternatives (30 tips bundled).

### Nice-to-Have (v1.1+)
- Barcode lookup (requires API — defer)
- Seasonal "seed oil free" holiday meal guides
- Shopping list integration
- Community voting on products
- "Where to find seed oil free X in [city]" crowd-sourced data

## Content & Data
- 300+ food products sourced from: Seed Oil Scout's public database, label scans from popular brands, Reddit's r/seedoilfree community wiki
- 30 daily tips (written in-app)
- 5 educational content pages (~2500 words total)
- 12 grocery product categories
- All bundled as JSON assets in the app bundle — zero internet required at launch
- Estimated content preparation: 2 hours of research + data entry

## Design Direction
- **Style**: Warm, clean, friendly — like a premium wellness magazine. Not clinical, not alarmist. Green-forward to signal "healthy/natural."
- **Color Palette**:
  - Primary: #2D5016 (forest green — nature, health)
  - Secondary: #8B4513 (brown — whole foods, earthiness)
  - Accent: #FF6347 (tomato red — "avoid" indicators)
  - Safe Badge: #22C55E (green — "seed oil free!")
  - Background: #FFFEF7 (warm white — not sterile)
  - Card Background: #F5F0E8 (warm cream)
  - Text Primary: #1C1917
  - Text Secondary: #6B7280

- **Typography**: SF Pro Display for headings, SF Pro Text for body. Rounded corners on all cards. SF Symbols for iconography.
- **Key Screens**: Home (today's tip + quick search), Search/Browse, Product Detail, Categories, Education, Favorites
- **Navigation**: Tab bar (Home / Browse / Learn / Favorites), with top search bar always accessible
- **Reference Apps**: Yuka (food scanning reference UX), Water tracker apps (simple home screen card design), Headspace (educational content presentation)

## Technical Notes
- **Platform**: iOS 16.0+ (SwiftUI)
- **Backend**: None — fully offline with bundled JSON
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON files read at launch; Favorites stored in UserDefaults/AppStorage
- **Estimated Build Time**: 3 hours
- **Complexity**: Low-Medium (content-heavy but technically simple)

## App Store Listing

### Title
Seed Oil Scan — Food Guide

### Subtitle
Identify seed oils in your food fast

### Keywords
seed oil,seed oil free,canola oil,soybean oil,healthy eating,food guide,diet,wellness,biohacking,clean eating,food scanner

### Description
Stop guessing. Know exactly which foods contain seed oils.

SeedOilScan is your pocket guide to the seed oil free lifestyle. With over 300 common products in our bundled database, you'll know in seconds whether that snack, sauce, or frozen meal contains inflammatory seed oils.

THE 7 SEED OILS TO AVOID:
Canola, soybean, sunflower, safflower, corn, cottonseed, and grapeseed oils. They're in almost everything — unless you know where to look.

WHAT YOU GET:
✅ 300+ products rated: Contains Seed Oils / Seed Oil Free / Check Label
✅ Browse by grocery category (12 categories)
✅ Learn WHY seed oils matter (science-based summaries)
✅ Daily tips and label-reading hacks
✅ Track your personal safe products list
✅ 100% offline — works anywhere, no account needed

WHO IS THIS FOR:
→ The person who just learned about seed oils and wants to start today
→ Anyone frustrated by hidden oils in "healthy" foods
→ Parents keeping seed oils out of their kids' diets
→ Biohackers and health-conscious foodies

Seed Oil Scout hikers the restaurant angle. We're focused on what's IN YOUR KITCHEN and at the GROCERY STORE.

No camera needed. No internet required. Just open and search.

### Category
Primary: Health & Fitness
Secondary: Food & Drink

### Pricing
- **Model**: Paid $1.99
- **Reasoning**: Health reference apps in this category consistently perform well at $0.99–$2.99. The target audience is willing to pay for health tools. A paid price signals quality and avoids the need for ads. Reference data has lasting value doesn't go stale fast.
- **Monetization Path**: Quarterly or biannual "content update" IAP (free for existing buyers during a window, or paid grandfathered at lower price). v1.1 could add premium categories (restaurant chains, international foods, baby food focus).

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 9/10 | Massive across TikTok, Reddit, and Google. Multiple data points confirm sustained rising interest. |
| App Gap | 8/10 | One good competitor (Seed Oil Scout) but it's restaurant-focused and online-required. Curation and grocery-store focus is open. |
| Build Simplicity | 8/10 | JSON data, static content views, no networking. Slightly more complex than creatine tracker due to 300+ products to curate. |
| Evergreen Potential | 7/10 | The "avoid seed oils" movement could peak and fade (many diet trends do). But the core reference value (what oils are in what foods) degrades slowly. |
| Monetization | 7/10 | Paid app at $2.99 narrows reach but targets a health-willingness-to-pay audience. Content updates provide long-tail revenue. |
| **Average** | **8.0/10** | |

## Risk Assessment
- **Trend Fizzle**: Medium. The "seed oil free" movement could decline if mainstream medical consensus pushes back. However, even if the trend fades, the factual data (what oils are in what foods) remains useful informationally. Build a factual reference, not a preachy manifesto.
- **App Store Rejection**: Low. The app is a factual reference, not medical advice. Include standard disclaimer.
- **Competition**: Medium. Seed Oil Scout could add grocery features. Yuka could add oil detection. Speed matters.
- **Legal/IP**: Low. Public facts about food composition. No copyrighted content needed.
- **Content Maintenance**: Medium. Packaged food formulations change. Plan quarterly content update pass.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics, TikTok views, Google Trends)
- [x] App Store shows 1 relevant good competitor but with different focus (restaurants) — grocery gap confirmed
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual (ingredients lists are public facts)
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours (content curation is the bottleneck, not code)
