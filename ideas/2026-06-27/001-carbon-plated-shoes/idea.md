# App Idea: CarbonPlate — Running Shoe Finder

*Generated: 2026-06-27*
*Confidence Score: 8.2/10*

---

## Pitch

CarbonPlate is a buyer's guide app for carbon-plated running shoes. It helps runners compare the latest carbon-plate models side-by-side — weight, stack height, price, ride feel, and best race distance — so they can pick the perfect shoe without scrolling through 47 YouTube reviews or DTC brand pages. No account, no tracking, no fluff. Just data.

## Target Audience

- **Primary**: Competitive and serious amateur runners (25-45) shopping for carbon-plated racers or trainers
- **Secondary**: Running coaches, gym owners, fitness enthusiasts researching gear
- **Demographics**: US-based, 25-45, skews male but growing female segment, disposable income ($80-$250 shoe purchase)

## Problem Statement

Carbon-plated running shoes are dominating the market (Nike Vaporfly, Adidas Adizero, Asics Metaspeed, New Balance Fuelcell, etc.), but there's no neutral, independent app to compare them. Runners must rely on:
- YouTube reviews (biased by sponsorships)
- Brand marketing (not neutral)
- Reddit threads (outdated, scattered)
- retailer sites (no comparison tools)

A dedicated comparison guide with up-to-date specs fills a clear gap. Runners spend $180-$250 on these shoes and want data before buying.

## Trend Evidence

- **Exploding Topics**: "Carbon-Plated Running Shoes" at +9,100% 5-year search growth, "Exploding" status (rank #7)
- **Google Trends**: Rising steadily since 2020, seasonal peaks align with marathon season (Mar-Apr, Sep-Oct)
- **Market Context**: Carbon plate shoe market projected $4.2B by 2028. Nike Vaporfly alone generated $2B+ revenue.
- **Community**: r/running (2.3M members), r/AdvancedRunning (180K) regularly discuss shoe choices. "Which carbon plate should I buy?" appears weekly.
- **Momentum**: Rising — not peaking yet. New models released 2-3x per year by major brands.

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Nike Run Club | ⭐4.77 | Free | Only Nike shoes, not neutral |
| ASICS Runkeeper | ⭐4.83 | Free | Only ASICS shoes, not neutral |
| StockX | ⭐4.78 | Free | Sneaker trading marketplace, zero spec info |
| On: Shop Shoes | ⭐4.93 | Free | On-brand shopping, not a guide |

**App Gap**: ZERO independent/buyer-guide apps exist. All results are either brand-specific apps or trading platforms. No app provides neutral comparison data across brands.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Shoe Database** — Browse 25+ carbon-plate running shoes with detailed specs (weight, stack height, drop, price, plate type, best distance, release year, image)
2. **Compare Tool** — Select 2-4 shoes to see specs side-by-side with differences highlighted
3. **Recommendation Quiz** — "Find My Plate" — 5-question quiz (race distance, weight, pronation, budget) → ranked recommendations
4. **Favorites** — Save shoes to a personal list

### Nice-to-Have (v1.1+)
- Price alerts (scrape retailer APIs or user-reported)
- User reviews/ratings within the app
- Shoe durability tracker (miles logged on your pair)
- New release calendar

## Content & Data

- **Shoe specs** for 25-30 models (Nike, Adidas, Asics, New Balance, Saucony, Hoka, Brooks, Puma)
- **Data sources**: Manufacturer spec pages, Runner's World reviews, RSS running database
- **Content effort**: ~4-6 hours to curate initial database from public sources
- **Update frequency**: Quarterly (new shoe releases)

## Design Direction

- **Style**: Clean, data-dense, athletic. Think Strava meets Wirecutter.
- **Color Palette**: 
  - Primary: `#FF6B35` (energetic orange — running energy)
  - Secondary: `#1A1A2E` (dark navy — premium feel)
  - Accent: `#E94560` (coral red — highlights)
  - Background: `#F8F9FA` (light gray)
  - Text: `#16213E` (near-black)
- **Typography**: SF Pro Display (bold for headers), SF Pro Body
- **Key Screens**: Home (featured shoes + quiz CTA), Browse (filterable list), Detail (full specs + image), Compare (side-by-side), Results (quiz recommendations)
- **Navigation**: Tab bar (Home, Browse, Compare, Favorites)
- **Reference Apps**: Strava, Wirecutter, Headspace (clean card-based layouts)

## Technical Notes

- **Platform**: iOS (SwiftUI), minimum iOS 16
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON file with shoe database
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
CarbonPlate — Shoe Finder

### Subtitle
Compare Carbon Running Shoes

### Keywords
carbon plate,running shoes,marathon shoes,nike vaporfly,adidas adizero,shoe comparison,running gear,footwear guide,race day,carbon fiber

### Description
Find the perfect carbon-plated running shoe for YOUR race.

CarbonPlate makes it easy to compare the latest carbon-plate running shoes side-by-side. Whether you're chasing a marathon PR or your first 5K, our neutral, unbiased database helps you pick the right shoe.

FEATURES:
• Comprehensive specs for 25+ carbon-plate models
• Side-by-side comparison (up to 4 shoes)
• "Find My Plate" quiz — answer 5 questions, get personalized recommendations
• Filter by brand, price, distance, weight
• Save favorites for later
• No account needed. No tracking. No ads.

Shoes included: Nike Vaporfly & Alphafly, Adidas Adizero Pro & Boston, Asics Metaspeed, New Balance Fuelcell, Hoka Rocket X, Saucony Endorphin, Brooks Hyperion, Puma Deviate, and more.

Updated quarterly with the latest releases.

### Category
Primary: Health & Fitness
Secondary: Sports

### Pricing
- **Model**: Paid $2.99 one-time
- **Reasoning**: Runners invest in $200+ shoes; $2.99 for a buyer's guide is a no-brainer. Paid model avoids ad-supported clutter.
- **Monetization Path**: Future: affiliate links to retailers (disclosed), premium tier with user reviews

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 9/10 | 9,100% growth, "Exploding" status, market growing |
| App Gap | 9/10 | Zero neutral comparison apps exist |
| Build Simplicity | 8/10 | Static JSON data, no backend, standard SwiftUI |
| Evergreen Potential | 8/10 | Running is evergreen, carbon plate trend is multi-year |
| Monetization | 7/10 | $2.99 one-time, clear value prop for the price |
| **Average** | **8.2/10** | |

## Risk Assessment

- **Trend Fizzle**: Low. Carbon plate technology is still evolving (Vaporfly just 3rd gen). Even if hype fades, the shoe market remains.
- **App Store Rejection**: Low risk. No user-generated content, no health claims, factual specs only.
- **Competition**: Medium. A large player (like Runner's World) could build this, but they haven't yet. First-mover advantage.
- **Legal/IP**: Low. Using publicly available specs and brand names for comparison is nominative fair use. No trademark logos.
- **Content Maintenance**: Low. Quarterly updates needed (new shoe releases). ~1 hour per quarter.

## Validation Checklist
- [x] At least 3 sources confirm rising trend
- [x] App Store search shows ≤ 3 relevant apps OR top apps have < 3 stars
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours
