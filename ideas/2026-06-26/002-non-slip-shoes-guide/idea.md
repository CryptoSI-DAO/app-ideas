# Non-Slip Shoes Guide — Find the Right Slip-Resistant Footwear

## App Specification

- **App Name**: Grip — Non-Slip Shoes Guide
- **Bundle ID**: com.cryptosi.grip-shoes-guide
- **Target Platform**: iOS 16.0+
- **Orientation**: Portrait only
- **Minimum Device**: iPhone SE (2nd gen) through iPhone 15 Pro Max
- **Category**: Health & Fitness / Lifestyle

## Concept

A practical, comprehensive guide to non-slip and slip-resistant shoes. Helps workers in kitchens, healthcare, construction, and other hazardous environments find the right footwear. Covers materials, tread patterns, safety certifications, and brand comparisons — organized by profession and use case.

## Why This Works

- **Trend**: "Non-Slip Shoes" at #65 on Exploding Topics, 6,800% growth (Jun 2026)
- **App Gap**: ZERO dedicated non-slip shoe guide apps. App Store returns only shopping apps (Nike, DSW, Foot Locker) — nobody is solving the "which shoe for which job" problem.
- **Evergreen**: 3+ million restaurant workers, 2M+ healthcare workers, 1M+ construction workers in the US alone need slip-resistant footwear. OSHA requires it.
- **Build**: Pure content app. No backend, no API, no internet required. ~2.5 hours.
- **Monetization**: $2.99 one-time purchase. Could also license to restaurants/employers.

## Trend Data

| Source | Signal | Value |
|--------|--------|-------|
| Exploding Topics | Growth | 6,800% |
| Exploding Topics | Rank | #65 |
| Exploding Topics | Status | Regular |
| App Store | Direct competitors | 0 |
| App Store | Note | All results are retail/shopping apps, not guides |

## Feature Breakdown

### Feature 1: Shoe Guide by Profession (P0)
- **User Story**: As a restaurant worker, I want to see the best non-slip shoes for my job so that I can stay safe and comfortable during long shifts.
- **Acceptance Criteria**:
  - 6+ profession categories: Kitchen/Restaurant, Healthcare, Construction, Warehouse, Cleaning/Janitorial, Outdoor/Weather
  - Each category shows 4-8 recommended shoes with ratings
  - Sort by: rating, price, comfort, durability
- **Dependencies**: Shoe data model (bundled JSON)
- **Complexity**: M

### Feature 2: Shoe Detail (P0)
- **User Story**: As a shopper, I want to see detailed specs and slip-resistance ratings so that I can compare options intelligently.
- **Acceptance Criteria**:
  - Each shoe shows: name, brand, price, slip-resistance rating (1-5 stars), tread material, upper material, weight, waterproof, oil-resistant, chemical-resistant, safety certifications
  - Sizing notes and fit guidance
  - Pros/cons list
  - Where to buy link
- **Dependencies**: Shoe data model
- **Complexity**: S

### Feature 3: Slip-Resistance Education (P0)
- **User Story**: As a first-time buyer, I want to understand what makes a shoe slip-resistant so that I can evaluate claims.
- **Acceptance Criteria**:
  - Explains: tread pattern design, rubber compound types, SRC vs. SRA/SRB testing
  - Visual comparison of tread patterns
  - "What to look for" checklist
  - OSHA requirements summary
- **Dependencies**: None
- **Complexity**: S

### Feature 4: Tread Pattern Visual Guide (P1)
- **User Story**: As a visual learner, I want to see tread pattern examples so that I can compare them side-by-side.
- **Acceptance Criteria**:
  - 8+ tread pattern diagrams with descriptions
  - Pattern types: chevron, hexagonal, circular, channel, lugged
  - Each pattern rated for: wet floors, oily surfaces, outdoor terrain
- **Dependencies**: None
- **Complexity**: S

### Feature 5: Favorites & Comparison (P1)
- **User Story**: As a buyer, I want to compare 2-3 shoes side-by-side so that I can make a final decision.
- **Acceptance Criteria**:
  - Heart to favorite (persisted with UserDefaults)
  - Compare screen with same layout as toothbrush app
  - Share sheet for individual shoes
- **Dependencies**: Feature 1
- **Complexity**: S

## Screen-by-Screen Specification

### Screen 1: Home
- **Purpose**: Entry point. Show profession categories and let users find shoes for their job.
- **Layout**: Header, search bar, profession category cards (2-column grid), "All Shoes" button.
- **Elements**:
  - App title ("Grip")
  - Search bar
  - Profession cards (image icon + name): Restaurant, Healthcare, Construction, Warehouse, Cleaning, Outdoor
  - "Browse All Shoes" button at bottom
  - Tab bar: Home, Compare, Learn, Favorites
- **Interactions**:
  - Tap profession card → Profession Detail
  - Tap "Browse All Shoes" → All Shoes list
  - Tap search → Search
  - Tap tab bar → switch screen
- **Data**: Category array from bundled JSON

### Screen 2: Profession Detail
- **Purpose**: Shows recommended shoes for a specific profession with context about that job's needs.
- **Layout**: Hero image of profession, brief description of safety needs, horizontal scroll of shoe cards.
- **Elements**:
  - Profession name + illustration
  - Safety context text (e.g., "Kitchen workers face wet, greasy floors for 8+ hour shifts...")
  - Stat cards: "Average shift: 8 hours", "Common hazards: Water, oil, grease"
  - Recommended shoes horizontal scroll: card image, name, slip-rating badge, price
  - "See All" link → full list
- **Interactions**:
  - Tap shoe card → Shoe Detail
  - Swipe horizontal shoes → scroll
- **Data**: Category + related shoes from bundled JSON

### Screen 3: Shoe Detail
- **Purpose**: Full specs and details for a single shoe.
- **Layout**: Scrollable. Shoe image, slip-rating badge, specs grid, pros/cons, certifications, buy button.
- **Elements**:
  - Shoe image
  - Name + brand
  - Slip-resistance rating (5-star, large)
  - Price
  - Specs grid: "Tread Pattern", "Upper Material", "Sole Material", "Weight", "Waterproof", "Oil-Resistant", "Chemical-Resistant", "Safety Toe"
  - Certifications row: SRC, ASTM, OSHA
  - Pros list (green checkmarks)
  - Cons list (orange warnings)
  - Sizing notes
  - "Where to buy" button (URL)
  - Favorite heart button
- **Interactions**:
  - Tap favorite → toggle + haptic
  - Tap "Where to buy" → open URL
  - Swipe down → dismiss
- **Data**: Single shoe object from bundled JSON

### Screen 4: Compare
- **Purpose**: Side-by-side comparison of 2-3 shoes.
- **Layout**: Same as toothbrush app. Slots at top, comparison table below.
- **Elements**:
  - 3 selection slots
  - Table rows: Price, Slip Rating, Tread Material, Upper, Weight, Waterproof, Oil-Resist, Chemical-Resist, Safety Toe, Comfort
  - Best value highlighted
- **Interactions**: Tap slot → picker
- **Data**: Shoe array from bundled JSON

### Screen 5: Learn
- **Purpose**: Slip-resistance education.
- **Layout**: Article cards grouped by category.
- **Elements**:
  - Sections: "Understanding Slip Resistance", "Tread Patterns Explained", "Safety Standards", "Care & Maintenance"
  - Article cards with icons
  - Full article view
- **Interactions**: Tap card → detail
- **Data**: Articles from bundled JSON

### Screen 6: Favorites
- **Purpose**: View saved shoes.
- **Layout**: Grid of favorited shoes. Empty state if none.
- **Elements**: Same as Home grid but filtered
- **Interactions**: Tap → detail, swipe to delete
- **Data**: Filtered array from UserDefaults

### Screen 7: Search
- **Purpose**: Search all shoes and articles.
- **Layout**: Search bar + results list.
- **Elements**: Search field, results (mixed shoes + articles), no-results state
- **Interactions**: Live filter
- **Data**: Shoe array + article array from bundled JSON

## Data Model

### Shoe Entity
```json
{
  "id": "s1",
  "name": "Skechers Workrelax 7.0",
  "brand": "Skechers",
  "priceUSD": 74.99,
  "categories": ["restaurant", "healthcare", "cleaning"],
  "slipRating": 4.5,
  "treadPattern": "Channel drain",
  "treadMaterial": "Rubber (oil-resistant compound)",
  "upperMaterial": "Synthetic mesh",
  "weightOz": 14,
  "isWaterproof": false,
  "isWaterResistant": true,
  "isOilResistant": true,
  "isChemicalResistant": false,
  "hasSafetyToe": false,
  "certifications": ["SRC", "ASTM F2913"],
  "sizingNotes": "Runs slightly wide. Size down if between sizes.",
  "pros": ["All-day cushioning", "Excellent oil grip", "Breathable"],
  "cons": ["Not waterproof", "Not for heavy chemicals"],
  "whereToBuyURL": "https://www.skechers.com",
  "imageName": "skechers_workrelax"
}
```

### Sample Data (3 items)
```json
[
  {
    "id": "s1",
    "name": "Skechers Work Relax 7.0",
    "brand": "Skechers",
    "priceUSD": 74.99,
    "categories": ["restaurant", "healthcare"],
    "slipRating": 4.5,
    "treadPattern": "Channel drain",
    "treadMaterial": "Oil-resistant rubber",
    "upperMaterial": "Synthetic mesh",
    "weightOz": 14,
    "isWaterproof": false,
    "isWaterResistant": true,
    "isOilResistant": true,
    "isChemicalResistant": false,
    "hasSafetyToe": false,
    "certifications": ["SRC"],
    "sizingNotes": "True to size. Wide fit available.",
    "pros": ["Memory foam insole", "Excellent oil grip", "Lightweight", "Slip-on design"],
    "cons": ["Not waterproof", "Sole wears after 6-8 months of heavy use"],
    "whereToBuyURL": "https://www.skechers.com",
    "imageName": "skechers_workrelax"
  },
  {
    "id": "s2",
    "name": "Shoes for Crews Falcon II",
    "brand": "Shoes for Crews",
    "priceUSD": 59.98,
    "categories": ["restaurant", "kitchen", "cleaning"],
    "slipRating": 4.8,
    "treadPattern": "TripGuard (spill-repellent)",
    "treadMaterial": "Proprietary slip-resistant compound",
    "upperMaterial": "Leather",
    "weightOz": 16,
    "isWaterproof": true,
    "isWaterResistant": true,
    "isOilResistant": true,
    "isChemicalResistant": false,
    "hasSafetyToe": false,
    "certifications": ["SRC", "ASTM F2913"],
    "sizingNotes": "Size up half for thick socks.",
    "pros": ["Industry-leading spill repellent", "Waterproof", "Durable leather", "12+ month lifespan"],
    "cons": ["Heavier than mesh options", "Break-in period required"],
    "whereToBuyURL": "https://www.shoesforcrews.com",
    "imageName": "sfc_falcon"
  },
  {
    "id": "s3",
    "name": "Trellus Ultimate Cushion",
    "brand": "Trellus",
    "priceUSD": 69.99,
    "categories": ["healthcare", "restaurant", "warehouse"],
    "slipRating": 4.3,
    "treadPattern": "Multi-directional lug",
    "treadMaterial": "High-traction rubber",
    "upperMaterial": "Microfiber knit",
    "weightOz": 11,
    "isWaterproof": false,
    "isWaterResistant": true,
    "isOilResistant": true,
    "isChemicalResistant": false,
    "hasSafetyToe": false,
    "certifications": ["SRC"],
    "sizingNotes": "Narrow fit. Size up half width.",
    "pros": ["Ultra-lightweight", "Insole rivals running shoes", "Machine washable", "Quick-dry"],
    "cons": ["Narrow toe box", "Less durable than leather"],
    "whereToBuyURL": "https://www.trellus.com",
    "imageName": "trellus_ultimate"
  }
]
```

### Article Entity
```json
{
  "id": "a1",
  "title": "What Is SRC? Understanding Slip-Resistance Ratings",
  "subtitle": "The safety certification that matters for workplace footwear",
  "readTimeMinutes": 3,
  "category": "standards",
  "icon": "shield.checkered",
  "bodyMarkdown": "..."
}
```

**Data Source**: All data bundled as JSON in the app bundle.

## Design Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #1E3A5F | Headers, buttons (industrial blue) |
| Secondary | #4A90D9 | Secondary text, highlights |
| Accent | #E7F900 | CTA buttons, Lisa Kim brand |
| Background | #FFFFFF | Screen backgrounds |
| Surface | #F4F6F8 | Cards |
| Text Primary | #1A1A2E | Body text |
| Text Secondary | #6B7280 | Captions |
| Success | #22C55E | High slip rating (4+ stars) |
| Warning | #F59E0B | Medium slip rating (3-4 stars) |
| Error | #EF4444 | Low slip rating (<3 stars) |

### Typography
| Style | Font | Size | Weight |
|-------|------|------|--------|
| Title (Large) | SF Pro Display | 34px | Bold |
| Title 1 | SF Pro Display | 28px | Semibold |
| Title 2 | SF Pro Display | 22px | Semibold |
| Headline | SF Pro Text | 17px | Semibold |
| Body | SF Pro Text | 17px | Regular |
| Caption | SF Pro Text | 13px | Regular |
| Rating Number | SF Pro Display | 48px | Bold |

### Spacing
- Base unit: 4px
- Card padding: 16px
- Section spacing: 24px
- Screen margin: 16px

### Corner Radius
- Cards: 12px
- Buttons: 8px
- Rating badge: 25px (rounded rectangle)

### Shadows
- Card shadow: offset (0, 2), blur 8, opacity 0.08

### Icons (SF Symbols)
- Home: `house.fill`
- Compare: `square.split.2x1`
- Learn: `book.fill`
- Favorites: `heart.fill`
- Search: `magnifyingglass`
- Slip rating: `shield.fill`
- Categories: `fork.knife`, `stethoscope`, `hammer.fill`, `shippingbox.fill`, `sparkles`, `sun.max.fill`

## App Store Metadata

- **Title**: Grip — Non-Slip Shoes Guide (27 chars)
- **Subtitle**: Find safe, slip-resistant footwear (30 chars)
- **Keywords**: non slip shoes, slip resistant shoes, kitchen shoes, restaurant shoes, work shoes, safety shoes, osha footwear, chef shoes, nurse shoes, slip proof (99 chars)
- **Description**: 
  ```
  Find the right non-slip shoes for your job.
  
  Grip helps workers in restaurants, healthcare, construction, and beyond find footwear that actually prevents slips and falls. No brand sponsorships. Just safety data.
  
  WHAT YOU GET:
  • Shoe recommendations by profession
  • Slip-resistance ratings (1-5 stars)
  • Detailed specs: tread material, oil resistance, waterproofing
  • Safety certification guide (SRC, ASTM, OSHA)
  • Side-by-side shoe comparison
  • Tread pattern visual guide
  
  WHY SLIPS MATTER:
  Slips, trips, and falls cause 15% of all workplace injuries — and they're preventable. The right footwear makes the difference between a safe shift and a trip to the ER.
  
  Whether you're a chef on greasy kitchen floors, a nurse rushing between patients, or a warehouse worker on concrete, Grip helps you find shoes rated for YOUR environment.
  
  FEATURES:
  • Works offline
  • No ads, no tracking, no account
  • $2.99 one-time — lifetime access
  • Updated with new brands and models
  
  Download Grip and step safely.
  ```
- **Promotional text**: The only footwear guide rated by slip-resistance, not brand budget. (66 chars)
- **What's New (v1.0)**: Initial launch! Get slip-resistance ratings for 20+ shoes across 6 professions. Stay safe on the job.
- **Screenshots needed**:
  1. Home — profession category cards
  2. Shoe Detail — Skechers Workrelax with specs
  3. Compare — 3 shoes side-by-side
  4. Learn — safety standards article
  5. Search — filtered shoe results
- **App Category**: Health & Fitness (primary), Lifestyle (secondary)
- **Age Rating**: 4+
- **Privacy**: No data collected. No tracking. All content bundled locally.

## Build Instructions

### Framework
- SwiftUI (iOS 16.0+)
- No third-party dependencies
- SF Symbols for all icons

### Build Order
1. **Data Layer**: Create `shoes.json` and `articles.json`. Models with Codable.
2. **Data Manager**: Load/filter/sort methods.
3. **Home Screen**: Category grid with search bar.
4. **Profession Detail**: Hero + safety context + shoe cards.
5. **Shoe Detail**: Full specs, slip rating, certifications, pros/cons.
6. **Compare Screen**: Side-by-side table.
7. **Learn Screen**: Article list + detail.
8. **Favorites**: UserDefaults persistence.
9. **Search**: Live filtering.
10. **Tab Bar**: Wire up all screens.

### Testing Checklist
- [ ] App launches on iPhone SE simulator
- [ ] All screens render correctly
- [ ] Shoe detail shows all spec fields
- [ ] Compare highlights best values correctly
- [ ] Favorites persist between launches
- [ ] Search works across shoes + articles
- [ ] No network requests
- [ ] Dark mode renders correctly
- [ ] VoiceOver labels present

### Estimated Build Time
2.5 hours
