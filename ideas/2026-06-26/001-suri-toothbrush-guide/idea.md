# Suri Toothbrush Guide — Sustainable Oral CareBuying Guide

## App Specification

- **App Name**: Suri — Sustainable Toothbrush Guide
- **Bundle ID**: com.cryptosi.suri-toothbrush-guide
- **Target Platform**: iOS 16.0+
- **Orientation**: Portrait only
- **Minimum Device**: iPhone SE (2nd gen) through iPhone 15 Pro Max
- **Category**: Health & Fitness / Lifestyle

## Concept

A beautiful, science-backed guide to sustainable toothbrushes and eco-friendly oral care. Helps users compare materials (bamboo, recycled plastic, plant-based bristles), understand environmental impact, and find the best eco-friendly toothbrush for their needs. No brand affiliation — purely educational.

## Why This Works

- **Trend**: Suri Toothbrush at #9 on Exploding Topics, 8,500% growth (Jun 2026)
- **App Gap**: ZERO dedicated toothbrush comparison/buying guide apps exist. App Store returns only brand companion apps (Oral-B, Philips Sonicare, Colgate) that lock users into their ecosystem.
- **Evergreen**: Oral care is a $50B+ global market. Sustainability is a permanent shift, not a fad.
- **Build**: Pure content app. No backend, no API, no internet required. ~2.5 hours to build.
- **Monetization**: $2.99 one-time purchase. No subscriptions needed.

## Trend Data

| Source | Signal | Value |
|--------|--------|-------|
| Exploding Topics | Growth | 8,500% |
| Exploding Topics | Rank | #9 |
| Exploding Topics | Status | Regular (sustained) |
| App Store | Direct competitors | 0 |
| App Store | Related (brand apps) | Oral-B (197K rev), Philips (55K), Colgate (46K) — NOT competitors |

## Feature Breakdown

### Feature 1: Toothbrush Comparison Guide (P0)
- **User Story**: As an eco-conscious consumer, I want to compare sustainable toothbrushes side-by-side so that I can make an informed purchase decision.
- **Acceptance Criteria**:
  - Shows at least 8 toothbrush brands with comparison table
  - Each toothbrush has: materials, bristle type, handle material, price range, eco-score, where to buy
  - Filter by: price, material type, bristle hardness, vegan
  - Sort by: eco-score, price, rating
- **Dependencies**: Toothbrush data model (bundled JSON)
- **Complexity**: M

### Feature 2: Materials Education (P0)
- **User Story**: As a confused shopper, I want to understand what "sustainable" means for toothbrushes so that I can evaluate claims critically.
- **Acceptance Criteria**:
  - 6+ material cards: bamboo, recycled plastic, plant-based bristles, biodegradable packaging, etc.
  - Each card explains: what it is, environmental impact, durability, end-of-life disposal
  - Visual comparison of biodegradability timelines
- **Dependencies**: None
- **Complexity**: S

### Feature 3: Eco Score Calculator (P0)
- **User Story**: As a user, I want to see a clear eco-score for each toothbrush so that I can quickly identify the most sustainable option.
- **Acceptance Criteria**:
  - 5-factor scoring: materials, manufacturing, packaging, end-of-life, company ethics
  - Score displayed as 0-100 with color coding (red/yellow/green)
  - Detailed breakdown viewable on tap
- **Dependencies**: Toothbrush data model
- **Complexity**: S

### Feature 4: Oral Care Tips (P1)
- **User Story**: As a user, I want to learn proper brushing technique and oral care best practices so that I can maintain good dental health.
- **Acceptance Criteria**:
  - 10+ tips covering: brushing technique, brush head replacement, recycling old brushes, composting bamboo handles
  - Tips organized by category
  - Beautiful illustrations/icons
- **Dependencies**: None
- **Complexity**: S

### Feature 5: Favorites & Share (P1)
- **User Story**: As a user, I want to save my favorite toothbrushes and share recommendations with friends.
- **Acceptance Criteria**:
  - Heart icon to favorite any toothbrush
  - Favorites persist between launches (UserDefaults)
  - Share sheet integration for sharing a specific toothbrush card
- **Dependencies**: Feature 1
- **Complexity**: S

## Screen-by-Screen Specification

### Screen 1: Home
- **Purpose**: Entry point. Showcases the guide's value and lets users browse toothbrushes by category.
- **Layout**: Header with app name, search bar, horizontal category chips, scrollable grid of toothbrush cards.
- **Elements**:
  - App title text ("Suri")
  - Search bar (text input)
  - Category chips (horizontal scroll): "All", "Bamboo", "Recycled Plastic", "Plant-Based", "Kids", "Premium"
  - Toothbrush cards (2-column grid): image, name, eco-score badge, price
  - Tab bar at bottom: Home, Compare, Learn, Favorites
- **Interactions**:
  - Tap card → Toothbrush Detail
  - Tap search bar → Search screen
  - Tap category chip → filter grid
  - Tap tab bar → switch screens
- **Data**: Toothbrush array from bundled JSON

### Screen 2: Toothbrush Detail
- **Purpose**: Deep dive into a single toothbrush. All specs, eco-score breakdown, where to buy.
- **Layout**: Scrollable. Hero image at top, eco-score card, specs grid, materials breakdown, purchase links.
- **Elements**:
  - Hero image (toothbrush product image)
  - Name + brand text
  - Eco-score badge (large, circular, color-coded)
  - Price text
  - Specs grid (2 columns): "Handle Material", "Bristle Type", "Bristle Hardness", "Vegan", "Packaging", "Made In"
  - Materials breakdown section (expandable cards)
  - Sustainability notes text
  - "Where to buy" button (opens affiliate URL/website)
  - Heart button (favorite)
- **Interactions**:
  - Tap eco-score → full breakdown modal
  - Tap favorite → toggle + haptic feedback
  - Tap "Where to buy" → open URL in Safari
  - Swipe down → dismiss
- **Data**: Single toothbrush object from bundled JSON

### Screen 3: Compare
- **Purpose**: Side-by-side comparison of multiple toothbrushes.
- **Layout**: Horizontal columns. Select up to 3 toothbrushes to compare. Table-style layout scrolling vertically.
- **Elements**:
  - "Select toothbrushes to compare" header
  - 3 slots (tap to select from picker — bottom sheet)
  - Comparison table rows: Price, Eco-Score, Handle Material, Bristle Type, Hardness, Vegan, Packaging, Weight
  - Highlight best value in each row (green checkmark)
- **Interactions**:
  - Tap slot → picker bottom sheet with all toothbrushes
  - Tap "Clear" → reset comparison
- **Data**: Toothbrush array from bundled JSON

### Screen 4: Learn
- **Purpose**: Educational content about sustainable oral care.
- **Layout**: Scrollable list of article cards grouped by category.
- **Elements**:
  - Section headers: "Materials Guide", "Care Tips", "Sustainability 101"
  - Article cards: title, subtitle, estimated read time, icon
  - Article detail view (push): title, body text, images
- **Interactions**:
  - Tap card → Article detail
  - Tap back → return to Learn list
- **Data**: Articles array from bundled JSON

### Screen 5: Favorites
- **Purpose**: View and manage favorited toothbrushes.
- **Layout**: Grid (same as Home) but filtered to favorites only. Empty state if no favorites.
- **Elements**:
  - Same toothbrush cards as Home
  - Empty state illustration + text: "No favorites yet. Tap the heart on any toothbrush to save it here."
  - "Clear All" button
- **Interactions**:
  - Tap card → Toothbrush Detail
  - Swipe left on card → delete from favorites
  - Tap "Clear All" → confirmation alert, then clear
- **Data**: Filtered toothbrush array (from UserDefaults favorites)

### Screen 6: Search
- **Purpose**: Search across all toothbrushes and articles.
- **Layout**: Search bar at top, results list below.
- **Elements**:
  - Search text field (auto-focus)
  - Results list: toothbrush cards + article cards mixed
  - No results state: "No results for 'X'. Try 'bamboo' or 'electric'."
  - Recent searches (last 5, persisted)
- **Interactions**:
  - Type → live filter results
  - Tap recent search → fill search + filter
  - Tap "Clear" → reset
- **Data**: Toothbrush array + articles array from bundled JSON

## Data Model

### Toothbrush Entity
```json
{
  "id": "t1",
  "name": "Suri Sustainable Sonic",
  "brand": "Suri",
  "priceUSD": 79,
  "category": "electric",
  "handleMaterial": "Aluminum (recyclable)",
  "bristleMaterial": "Plant-based nylon (castor oil)",
  "bristleHardness": "Medium",
  "isVegan": true,
  "isCrueltyFree": true,
  "packaging": "Plastic-free, recyclable cardboard",
  "endOfLife": "Heads recyclable via mail-back program; handle infinitely recyclable",
  "manufacturingLocation": "China (audited facility)",
  "ecoScore": 92,
  "ecoScoreBreakdown": {
    "materials": 20,
    "manufacturing": 16,
    "packaging": 20,
    "endOfLife": 18,
    "companyEthics": 18
  },
  "keyFeatures": ["Sonic vibration", "2-hour charge", "Travel case", "60-day battery"],
  "whereToBuyURL": "https://www.trysuri.com",
  "imageName": "suri_sonic"
}
```

### Sample Data (3 items)
```json
[
  {
    "id": "t1",
    "name": "Suri Sustainable Sonic",
    "brand": "Suri",
    "priceUSD": 79,
    "category": "electric",
    "handleMaterial": "Recyclable aluminum",
    "bristleMaterial": "Castor oil-based nylon",
    "bristleHardness": "Medium",
    "isVegan": true,
    "isCrueltyFree": true,
    "packaging": "Plastic-free cardboard",
    "endOfLife": "Heads recyclable via mail-back; handle infinitely recyclable",
    "manufacturingLocation": "China (audited)",
    "ecoScore": 92,
    "ecoScoreBreakdown": {"materials": 20, "manufacturing": 16, "packaging": 20, "endOfLife": 18, "companyEthics": 18},
    "keyFeatures": ["Sonic vibration", "USB-C charging", "2-min timer", "60-day battery"],
    "whereToBuyURL": "https://www.trysuri.com",
    "imageName": "suri_sonic"
  },
  {
    "id": "t2",
    "name": "Brush with Bamboo",
    "brand": "Brush with Bamboo",
    "priceUSD": 8.99,
    "category": "bamboo",
    "handleMaterial": "Organic bamboo (compostable)",
    "bristleMaterial": "Nylon-4 (partially biodegradable)",
    "bristleHardness": "Soft",
    "isVegan": false,
    "isCrueltyFree": true,
    "packaging": "Recyclable paper sleeve",
    "endOfLife": "Handle compostable; remove bristles before composting",
    "manufacturingLocation": "USA",
    "ecoScore": 88,
    "ecoScoreBreakdown": {"materials": 20, "manufacturing": 20, "packaging": 18, "endOfLife": 16, "companyEthics": 14},
    "keyFeatures": ["Biodegradable handle", "Charcoal-infused bristles", "BPA-free"],
    "whereToBuyURL": "https://www.brushwithbamboo.com",
    "imageName": "brush_with_bamboo"
  },
  {
    "id": "t3",
    "name": "Gusto Bamboo Manual",
    "brand": "Gusto",
    "priceUSD": 5.99,
    "category": "bamboo",
    "handleMaterial": "Moso bamboo",
    "bristleMaterial": "Nylon",
    "bristleHardness": "Medium",
    "isVegan": false,
    "isCrueltyFree": true,
    "packaging": "Compostable bag",
    "endOfLife": "Handle home-compostable in 6 months",
    "manufacturingLocation": "Canada",
    "ecoScore": 84,
    "ecoScoreBreakdown": {"materials": 18, "manufacturing": 19, "packaging": 19, "endOfLife": 16, "companyEthics": 12},
    "keyFeatures": ["Ergonomic handle", "Minimal packaging", "Natural antimicrobial"],
    "whereToBuyURL": "https://gusto.com",
    "imageName": "gusto_bamboo"
  }
]
```

### Article Entity
```json
{
  "id": "a1",
  "title": "Bamboo vs. Recycled Plastic: Which Is Greener?",
  "subtitle": "A lifecycle analysis of the two most popular eco toothbrush materials",
  "readTimeMinutes": 4,
  "category": "materials",
  "icon": "leaf.arrow.circlepath",
  "bodyMarkdown": "..."
}
```

**Data Source**: All data bundled as JSON in the app bundle. No network requests.

**Relationships**: Toothbrushes have a one-to-many relationship with categories. Articles are categorized independently.

## Design Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #2D6A4F | Headers, buttons, eco-score (high) |
| Secondary | #52B788 | Secondary text, eco-score (med) |
| Accent | #E7F900 | Highlights, CTAs (Lisa Kim brand) |
| Background | #FFFFFF | Screen backgrounds |
| Surface | #F7F9F9 | Cards, backgrounds |
| Text Primary | #1B1B1B | Body text |
| Text Secondary | #6B7280 | Captions, subtitles |
| Success | #22C55E | Eco-score 80+, positive |
| Warning | #F59E0B | Eco-score 50-79 |
| Error | #EF4444 | Eco-score <50 |

### Typography
| Style | Font | Size | Weight |
|-------|------|------|--------|
| Title (Large) | SF Pro Display | 34px | Bold |
| Title 1 | SF Pro Display | 28px | Semibold |
| Title 2 | SF Pro Display | 22px | Semibold |
| Headline | SF Pro Text | 17px | Semibold |
| Body | SF Pro Text | 17px | Regular |
| Caption | SF Pro Text | 13px | Regular |
| Eco Score Number | SF Pro Display | 48px | Bold |

### Spacing
- Base unit: 4px
- Card padding: 16px
- Section spacing: 24px
- Screen edge margin: 16px
- Tab bar height: 49px

### Corner Radius
- Cards: 12px
- Buttons: 8px
- Eco-score badge: 50px (full circle)
- Images: 8px

### Shadows
- Card shadow: offset (0, 2), blur 8, opacity 0.08
- Button shadow: offset (0, 1), blur 4, opacity 0.1

### Icons (SF Symbols)
- Home: `house.fill`
- Compare: `square.split.2x1`
- Learn: `book.fill`
- Favorites: `heart.fill`
- Search: `magnifyingglass`
- Eco score: `leaf.fill`
- Back: `chevron.left`
- Share: `square.and.arrow.up`
- Favorite (empty): `heart`
- Favorite (filled): `heart.fill`

## App Store Metadata

- **Title**: Suri — Eco Toothbrush Guide (28 chars)
- **Subtitle**: Compare sustainable toothbrushes (30 chars)
- **Keywords**: eco toothbrush, sustainable toothbrush, bamboo toothbrush, oral care, green living, eco friendly, zero waste, dental health, toothbrush comparison, suri (99 chars)
- **Description**: 
  ```
  Find the most sustainable toothbrush for your routine.
  
  Suri helps you compare eco-friendly toothbrushes side-by-side — from bamboo handles to plant-based bristles, recycled aluminum to compostable packaging. No brand bias. Just facts.
  
  WHAT YOU GET:
  • Compare 10+ sustainable toothbrush brands
  • Eco-Score rating (0-100) for each brush
  • Materials breakdown: what's actually eco-friendly
  • Side-by-side comparison tool
  • Educational guides on sustainable oral care
  • Save favorites for later
  
  WHY SURI?
  The oral care industry produces over 1 billion plastic toothbrushes per year — most end up in landfills for 400+ years. Switching to a sustainable toothbrush is one of the easiest zero-waste swaps you can make. But with so many options, how do you choose?
  
  Suri cuts through the greenwashing. We rate each toothbrush on 5 factors: materials, manufacturing, packaging, end-of-life, and company ethics. Get a clear Eco-Score so you can make an informed choice in seconds.
  
  FEATURES:
  • Beautiful, fast, works offline
  • No ads, no tracking, no account needed
  • One-time purchase — lifetime access
  • Updated regularly with new brands
  
  Download Suri and make your next toothbrush a sustainable one.
  ```
- **Promotional text**: Compare eco toothbrushes with clear Eco-Scores. No greenwashing, just facts. (79 chars)
- **What's New (v1.0)**: Initial launch! Compare 10+ sustainable toothbrushes, learn about eco materials, and find your perfect green brush.
- **Screenshots needed**:
  1. Home screen — grid of toothbrush cards with eco-scores
  2. Toothbrush Detail — Suri Sonic with 92/100 eco-score
  3. Compare screen — 3 toothbrushes side-by-side
  4. Learn screen — article list
  5. Search — filtered results
- **App Category**: Health & Fitness (primary), Lifestyle (secondary)
- **Age Rating**: 4+
- **Privacy**: No data collected. No tracking. No account required. All data is bundled locally.

## Build Instructions

### Framework
- SwiftUI (iOS 16.0+)
- No third-party dependencies
- SF Symbols for all icons

### Build Order
1. **Data Layer**: Create `toothbrushes.json` and `articles.json` in the bundle. Create `Toothbrush.swift` and `Article.swift` models with Codable conformance.
2. **Data Manager**: Create `DataManager.swift` — loads bundled JSON, provides filtering/sorting methods.
3. **Home Screen**: Implement `HomeView.swift` with grid layout, category chips, search bar.
4. **Toothbrush Detail**: Implement `ToothbrushDetailView.swift` with eco-score display, specs grid, materials breakdown.
5. **Compare Screen**: Implement `CompareView.swift` with picker and comparison table.
6. **Learn Screen**: Implement `LearnView.swift` with article list and detail.
7. **Favorites**: Implement `FavoritesView.swift` with UserDefaults persistence.
8. **Search**: Implement `SearchView.swift` with live filtering.
9. **Tab Bar**: Wire up all screens with `TabView`.
10. **Polish**: Add haptics, animations, empty states, share sheet.

### Testing Checklist
- [ ] App launches without errors on iPhone SE (3rd gen) simulator
- [ ] All 5 tab bar screens render correctly
- [ ] Toothbrush detail shows all data fields
- [ ] Compare screen correctly highlights best values
- [ ] Favorites persist between app launches
- [ ] Search filters correctly across toothbrushes and articles
- [ ] Share sheet works on toothbrush detail
- [ ] No network requests made (verify with Network Link Conditioner)
- [ ] Dark mode renders correctly
- [ ] Accessibility: VoiceOver reads all labels

### Estimated Build Time
2.5 hours
