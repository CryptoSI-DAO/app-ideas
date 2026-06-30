# App Idea: ScentSafe — Non-Toxic Perfume & Ingredient Safety Guide

*Generated: 2026-06-30*
*Confidence Score: 8.1/10*
*Status: idea_generated | Gap: OPEN (GREEN FIELD)*

---

## Pitch
ScentSafe is a fragrance safety reference app that helps users identify harmful ingredients in perfumes, colognes, and body sprays. With a searchable database of 200+ fragrance ingredients — each rated for safety, allergen risk, and endocrine disruption potential — users can quickly check products before buying. No more mystery "parfum" or "fragrance" labels. Just scan or search, and know exactly what you're spraying on your skin.

## Target Audience
- Primary: Health-conscious women 25-45 shopping for clean beauty products
- Secondary: Allergy sufferers, pregnant women avoiding phthalates, clean beauty enthusiasts
- Demographics: US/UK/CA, iOS-skewing, $50K+ household income, interested in wellness

## Problem Statement
The fragrance industry is notoriously opaque. The term "fragrance" or "parfum" on a label can hide dozens of undisclosed chemicals including phthalates, formaldehyde releasers, and synthetic musks linked to hormone disruption. Consumers who care about ingredient safety have no dedicated mobile reference tool. EWG Healthy Living covers food and general cosmetics but NOT perfume specifically. Yuka/Think Dirty focus on skincare ingredients, not fragrance compounds. There is literally NO app on the App Store dedicated to perfume ingredient safety.

## Trend Evidence
- **Exploding Topics #66**: Non-Toxic Perfume (+1,050% search growth) — current list
- **Exploding Topics Trend**: Clean beauty / non-toxic personal care (multi-year mega-trend)
- **Reddit signals**: Active threads on r/Perfumes, r/NaturalBeauty, r/fragrance asking for non-toxic recommendations and ingredient guidance
- **Google search results**: Multiple 2026 blog articles (greenwashingindex.com, thefiltery.com, sustainablykindliving.com) ranking "best non-toxic fragrances" — commercial demand confirmed
- **Momentum**: Rising — clean beauty market projected to hit $11.6B by 2027
- **Cross-signal**: Prequel Skincare (+8,400%), Milky Toner (+6,500%), Peptide Lip Balm (+6,400%) all on same Exploding Topics list confirming clean beauty ingredient awareness wave

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| EWG Healthy Living | 3.7★ | $0.00 | Covers food + general cosmetics, NOT perfume-specific. Low rating (3.7★) indicates UX issues. |
| PERFUMIST | 4.4★ | $0.00 | Ratings database (457 reviews), not safety-focused. Community reference only. |
| Parfumo | 4.85★ | $0.00 | Reference database, not safety/ingredient analysis. German-centric. |
| Think Dirty | 4.8★ | $0.00 | Skincare/cosmetics scanner, limited fragrance-specific data. |
| Yuka | 4.8★ | $0.00 | Food + cosmetics scanner, no perfume ingredient safety ratings. |

**App Gap**: TRUE GREEN FIELD. Zero apps exist specifically for perfume ingredient safety. All competitors are either general cosmetics scanners (miss fragrance-specific compounds) or perfume reference databases (don't rate safety). User reviews for the closest alternatives frequently ask: "What ingredients should I avoid?" — signaling unmet need.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Ingredient Database** — 200+ fragrance ingredients with safety ratings (Green/Yellow/Red), allergen flags, and endocrine disruption warnings. Searchable by name or browse by category (solvent, fixative, synthetic musk, etc.)
2. **Safety Lookup** — User types or pastes an ingredient list from any perfume label. App highlights red-flag ingredients, explains risks in plain language, and gives an overall safety score (A-F).
3. **Brand Directory** — 80+ clean fragrance brands with safety ratings. Brands sorted by "cleanest" first. Includes price range, scent family, and where to buy.
4. **Learn Section** — 12 articles explaining key topics: phthalates, synthetic musks, formaldehyde releasers, IFRA standards, "fragrance loophole," how to read labels, pregnancy safety, etc.

### Nice-to-Have (v1.1+)
- Barcode scanner for quick product lookup (requires product database expansion)
- Personal "safe list" of saved brands/ingredients
- Community reviews/ratings for fragrances
- Allergen profile: user sets allergies, app filters recommendations
- Seasonal scent recommendations

## Content & Data
- Ingredient safety data: EWG Skin Deep database (public), IFRA standards (public), PubChem toxin data (public)
- Brand directory: Curated from clean beauty blogs, brand transparency reports (publicly available)
- Educational content: Compiled from EWG, Campaign for Safe Cosmetics, academic fragrance toxicology reviews
- MVP content: ~200 ingredients + 80 brands + 12 articles (approximately 1.5 hours to compile)
- Data source: Bundled JSON in app bundle, updated via app updates quarterly

## Design Direction
- **Style**: Clean, minimal, editorial — think Headspace meets The Ordinary. Trustworthy and science-forward.
- **Color Palette**:
  - Primary: #2D3436 (dark charcoal)
  - Accent: #00B894 (clean green for "safe")
  - Warning: #FDCB6E (amber for "caution")
  - Danger: #E17055 (coral for "harmful")
  - Background: #FAFAFA (off-white)
  - Card: #FFFFFF
- **Typography**: SF Pro Display (headings), SF Pro Text (body). H1: 28pt Bold, H2: 20pt Semibold, Body: 16pt Regular, Caption: 13pt Regular
- **Key Screens**: Home (search + trending), Ingredient Detail, Lookup Results, Brand Directory, Learn
- **Navigation**: Tab bar — Home (search), Browse, Learn, Saved
- **Reference Apps**: Yuka, Think Dirty, OnSkin (UX patterns); Headspace (clean editorial feel)

## Technical Notes
- **Platform**: iOS (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON files
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
ScentSafe — Clean Fragrance Guide

### Subtitle
Check perfume ingredients for safety

### Keywords
clean perfume, fragrance safety, non toxic perfume, perfume ingredients, phthalate free, clean beauty, scent safe, fragrance guide, ingredient checker, perfume scanner

### Category
Primary: Health & Fitness
Secondary: Lifestyle

### Description
Stop spraying mystery chemicals on your skin.

ScentSafe is the only app dedicated to perfume ingredient safety. Paste any perfume's ingredient list and instantly see which ingredients are linked to hormone disruption, allergies, or irritation. Get a clear A-F safety rating for any fragrance.

WHAT YOU GET:
• Safety ratings for 200+ fragrance ingredients
• Red-flag ingredient alerts with plain-language explanations
• 80+ clean fragrance brand recommendations
• Educational guides on phthalates, synthetic musks, and the "fragrance loophole"
• Endocrine disruption and allergen warnings
• Pregnancy-safe filtering

Whether you're switching to clean beauty, managing fragrance allergies, or just want to know what's in your favorite scent — ScentSafe gives you the transparency the fragrance industry won't.

No account. No tracking. Just honest ingredient safety.
Breathe easier. Smell amazing. Stay safe.

### Pricing
- **Model**: Free with Premium unlock ($2.99 one-time)
- **Reasoning**: Free tier covers ingredient safety lookup (core utility). Premium unlocks full brand directory, save/view history, and all educational content.
- **Monetization Path**: Could extend to affiliate links to clean fragrance retailers (Scentbird, Dossier, etc.)

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | Non-Toxic Perfume +1,050% on Exploding Topics; clean beauty mega-trend; multiple Reddit communities discussing |
| App Gap | 10/10 | ZERO dedicated perfume ingredient safety apps exist — TRUE GREEN FIELD |
| Build Simplicity | 8/10 | Pure content/reference app. No backend, no real-time data, no camera/scanner complexity. JSON + SwiftUI lists. |
| Evergreen Potential | 8/10 | Ingredient safety is permanent need. Clean beauty trend is multi-year. No trend dependency. |
| Monetization | 7/10 | $2.99 paid feasible. Could add affiliate revenue. Not recurring subscription material but strong one-time purchase. |
| **Average** | **8.2/10** | |

## Risk Assessment
- **Trend Fizzle**: LOW — Clean beauty is a multi-year structural shift, not a fad. Ingredient transparency regulations (MoCRA in US, EU cosmetics regulation) are accelerating demand.
- **App Store Rejection**: LOW — No health claims, just publicly sourced ingredient data. Educational reference app.
- **Competition**: MEDIUM — Yuka or Think Dirty could add perfume ingredients to their scanner. First-mover advantage matters.
- **Legal/IP**: LOW — All data from public sources (EWG, IFRA, PubChem). Trademark-safe name "ScentSafe."
- **Content Maintenance**: MEDIUM — Ingredient database needs quarterly updates. Brand directory needs periodic refresh. Low effort (< 2 hours/quarter).

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics, Reddit, multiple blogs)
- [x] App Store search shows 0 relevant apps (only shopping apps and general scanners)
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial (safety is universally desired)
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours (2.5 hours)

---

## Build Instructions for Coding Agent

### Step-by-Step Build Order

1. **Create Xcode project** — SwiftUI iOS app, minimum iOS 16.0, project name "ScentSafe"
2. **Set up data models** — Create `Ingredient`, `Brand`, `Article` structs conforming to Codable
3. **Add bundled JSON** — Create `ingredients.json` (200 items), `brands.json` (80 items), `articles.json` (12 items)
4. **Build Home screen** — Search bar at top, "Quick Safety Check" CTA, recently browsed ingredients
5. **Build Ingredient Detail screen** — Safety badge (green/amber/red), description, risks, alternatives
6. **Build Lookup screen** — Text input for paste-in ingredient list, parse and highlight results
7. **Build Brand Directory screen** — List view with safety score badges, filter by scent family/price
8. **Build Learn screen** — Article list with markdown
9. **Add tab bar navigation** — Home, Browse, Learn, Saved tabs
10. **Polish** — Colors, spacing, empty states, dark mode support
11. **Premium gating** — Add StoreKit purchase flow (or simple "Pro" unlock for MVP)

### Data Model (Codable Swift Structs)

```swift
struct Ingredient: Codable, Identifiable {
    let id: String  // e.g., "phthalate-dehp"
    let name: String  // e.g., "Diethylhexyl Phthalate (DEHP)"
    let category: String  // e.g., "Plasticizer, Solvent"
    let safetyRating: String  // "Red" | "Amber" | "Green"
    let allergenRisk: Bool
    let endocrineDisruptor: Bool
    let summary: String  // 1-2 sentence plain-language explanation
    let risks: [String]  // Bullet list of specific concerns
    let alternatives: [String] // Safer substitute ingredients
    let sources: [String]  // EWG, IFRA, PubMed references
}

struct Brand: Codable, Identifiable {
    let id: String  // e.g., "hermes"
    let name: String  // e.g., "Hermès"
    let safetyScore: String  // "A" | "B" | "C" | "D" | "F"
    let priceRange: String  // "$" | "$$" | "$$$"
    let scentFamilies: [String]  // e.g., ["Floral", "Woody"]
    let description: String
    let fullIngredientDisclosure: Bool
    let website: String
}

struct Article: Codable, Identifiable {
    let id: String  // e.g., "phthalates-101"
    let title: String
    let category: String  // "Science" | "Guide" | "Regulations"
    let readMinutes: Int
    let bodyMarkdown: String
}
```

### Testing Checklist
- [ ] App launches on iPhone SE (smallest screen)
- [ ] Search returns results for ingredient names
- [ ] Lookup parses pasted ingredient lists correctly
- [ ] Ingredient detail shows correct safety color
- [ ] Brand directory sortable/filterable
- [ ] Learn articles render properly
- [ ] Dark mode works on all screens
- [ ] No network calls required (fully offline)
- [ ] App works in Airplane mode
