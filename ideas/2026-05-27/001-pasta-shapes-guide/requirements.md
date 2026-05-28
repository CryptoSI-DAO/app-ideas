# Requirements: Pasta Shapes Guide

*Version: 1.0*
*Date: 2026-05-27*
*Target: SwiftUI iOS App*

---

## 1. App Specification

- **App Name**: Pasta Shapes Guide
- **Bundle ID**: com.owl.pastashapes
- **Target Platform**: iOS 16.0+ (SwiftUI)
- **Orientation**: Portrait only
- **Minimum Device**: iPhone SE (2nd gen) through iPhone 15 Pro Max

---

## 2. Feature Breakdown

### F1: Pasta Shape Catalog (Screen: Home)
- **User Story**: As a home cook, I want to browse all pasta shapes in a visual grid so I can discover varieties I didn't know existed
- **Acceptance Criteria**:
  - Grid displays at minimum 50 pasta shapes on first launch
  - Each grid cell shows: shape thumbnail (SVG/emoji), Italian name, cooking time
  - Grid is scrollable and responsive (2 columns on iPhone SE, 3 on larger iPhones)
  - Pull-to-refresh is NOT needed (static data)
- **Priority**: P0
- **Dependencies**: Bundled pasta data JSON
- **Complexity**: S

### F2: Shape Detail Screen
- **User Story**: As a user looking at a pasta shape, I want to see detailed information including cooking times, sauce pairings, and origin, so I can decide if this shape fits my recipe
- **Acceptance Criteria**:
  - Tapping a grid cell opens a full detail screen
  - Detail screen shows: large shape illustration, Italian name (headline), English name (subheadline), description paragraph, cooking time (with visual timer icon), texture description, origin region (with Italian flag emoji or map pin icon), recommended sauces (each with emoji), and Facts section
  - "Favorite" heart button in top-right corner
  - "Back" navigation via swipe or navigation bar
- **Priority**: P0
- **Dependencies**: Pasta data model
- **Complexity**: S

### F3: Search
- **User Story**: As a cook who heard a pasta name on a cooking show, I want to search by name so I can find that specific shape instantly
- **Acceptance Criteria**:
  - Search bar at top of Home + dedicated Search tab
  - Searches Italian name, English name, and aliases
  - Real-time filtering as user types (minimum 1 character)
  - No results state with "No shapes found for 'xyz'" message
  - Clear button (X) to reset search
- **Priority**: P0
- **Dependencies**: F1
- **Complexity**: S

### F4: Category Filter
- **User Story**: As a user looking for a specific type of pasta (e.g., short pasta for baked dishes), I want to filter by category so I only see relevant shapes
- **Acceptance Criteria**:
  - Category pills/icons in a horizontal scroll: All, Long, Short, Filled, Soup, Egg, Stuffed
  - Tapping a category filters the grid instantly
  - Active category is visually highlighted (filled pill, others are outline)
  - Category + search work together (intersection, not union)
- **Priority**: P1
- **Dependencies**: F1, F3
- **Complexity**: S

### F5: Favorites
- **User Story**: As a user, I want to bookmark my favorite pasta shapes so I can quickly reference them later
- **Acceptance Criteria**:
  - Heart icon on each grid cell and on detail screen
  - Toggling heart saves/removes from Favorites
  - Favorited state shown with filled heart (red #FF6B6B)
  - Favorites tab shows only favorited shapes in grid format
  - Empty state for Favorites: "Tap any heart to add favorites" with icon
  - Favorites persist across app launches (UserDefaults)
- **Priority**: P1
- **Dependencies**: F1, F2
- **Complexity**: S

---

## 3. Screen-by-Screen Specification

### Screen 1: Home (Catalog Grid)
- **Purpose**: Browse and discover all pasta shapes
- **Layout**:
  - Header: App title "Pasta Shapes" (large bold) + subtitle "80+ varieties"
  - Category filter pills (horizontal scroll, below header)
  - Main: 2-3 column grid of pasta cards
  - Bottom: Tab bar (Catalog, Search, Favorites)
- **Elements**:
  - Label: "Pasta Shapes" (h1, New York font, 34pt, bold)
  - Label: "80+ varieties" (caption, SF Pro, 14pt, secondary color)
  - ScrollView: Category filter chips
  - LazyVGrid: Pasta cards (each: 140pt height, 12pt corner radius, white bg with shadow)
  - Each card: Shape thumbnail area (60x60pt), Italian name label, cooking time badge
  - TabBar: 3 tabs with SF Symbols (tray.full, magnifyingglass, heart.fill)
- **Interactions**:
  - Tap card → navigate to Shape Detail
  - Tap category pill → filter grid
  - Scroll → load more (lazy)
  - Pull down → no action (static data)
- **Data**: All pasta shapes from bundled JSON
- **Navigation**: Root of Catalog tab → push to Shape Detail

### Screen 2: Shape Detail
- **Purpose**: Full information about one pasta shape
- **Layout**:
  - Header: "< Back" button (system back)
  - Hero: Large shape illustration area (200pt height)
  - Content: Scrollable details sections
  - Footer: Favorite button (floating heart top-right)
- **Elements**:
  - Button: Back chevron (system)
  - Image/View: Shape illustration (200pt, centered, aspect fit)
  - Label: Italian name (h1, New York, 32pt, bold, terracotta #C75B39)
  - Label: English name (h2, SF Pro, 18pt, regular)
  - Label: Description (body, SF Pro, 16pt, regular, max 3 lines)
  - Card: Cooking time info (icon + text, e.g., "8-10 min")
  - Card: Texture description
  - Card: Origin region (with flag/map pin)
  - Card: "Best with" — sauce pairings list (each with emoji + name + brief note)
  - Button: Heart (favorite toggle, 28pt, SF Symbol heart/heart.fill)
- **Interactions**:
  - Tap back → pop to previous
  - Tap heart → toggle favorite (haptic feedback)
  - Scroll → content scrolls
- **Data**: Single pasta shape object from JSON
- **Navigation**: Push from Home grid → pop back. No further navigation (could add "Similar shapes" in v1.1)

### Screen 3: Search
- **Purpose**: Find pasta by name
- **Layout**:
  - Header: Search bar (magnifying glass icon, placeholder "Search pasta shapes...")
  - Main: Grid of results (same card style as Home)
  - Empty state: Centered message + icon
  - Bottom: Tab bar
- **Elements**:
  - SearchBar: System search bar, auto-focused
  - LazyVGrid: Same pasta cards as Home
  - Label: "No shapes found" (centered, secondary color, shown when empty)
- **Interactions**:
  - Type → real-time filter
  - Tap result → push to Shape Detail
  - Clear button → reset to full catalog
  - Cancel → dismiss keyboard, show full catalog
- **Data**: Filtered pasta shapes based on search text
- **Navigation**: Push to Shape Detail from results

### Screen 4: Favorites
- **Purpose**: Quick access to saved shapes
- **Layout**:
  - Header: "Favorites" title + count badge
  - Main: Grid (same as Home but filtered to favorites only)
  - Empty state: Centered illustration + message
  - Bottom: Tab bar
- **Elements**:
  - Label: "Favorites" (h1)
  - Badge: Count of favorites (e.g., "(12)")
  - LazyVGrid: Favorite pasta cards
  - Empty state: Heart icon + "No favorites yet" + "Tap any heart on a shape to save it here"
- **Interactions**:
  - Tap card → Shape Detail
  - Edit mode: None in v1.0 (swipe to delete, edit button)
- **Data**: Filtered shapes where isFavorite == true
- **Navigation**: Push to Shape Detail

---

## 4. Data Model

```swift
struct PastaShape: Codable, Identifiable {
    let id: String              // "spaghetti", "penne", "orecchiette"
    let italianName: String     // "Spaghetti", "Penne", "Orecchiette"
    let englishName: String     // "Spaghetti", "Penne", "Little Ears"
    let aliases: [String]       // ["Spaghettini", "Fettuccine"]
    let category: Category      // long, short, filled, soup
    let description: String     // 2-3 sentence description
    let cookingTimeMin: Int     // 8 (minutes)
    let cookingTimeMax: Int     // 12 (minutes)
    let texture: String         // "firm, chewy"
    let origin: String          // "Lazio (Rome)"
    let originRegion: String     // "Central Italy"
    let sauces: [SaucePairing]  // 2-3 recommended sauces
    let emojiThumbnail: String   // "🍝" or custom Unicode
    
    enum Category: String, Codable, CaseIterable {
        case long = "Long"
        case short = "Short"
        case filled = "Filled"
        case soup = "Soup"
        case egg = "Egg"
        case stuffed = "Stuffed"
    }
}

struct SaucePairing: Codable {
    let name: String            // "Carbonara"
    let emoji: String           // "🥚"
    let note: String            // "Classic Roman pairing"
}
```

### Sample Data (minimum 3 items):

```json
[
  {
    "id": "spaghetti",
    "italianName": "Spaghetti",
    "englishName": "Spaghetti",
    "aliases": ["Spaghettini", "Capellini"],
    "category": "long",
    "description": "The world's most iconic pasta. Long, thin, cylindrical strands that are the backbone of Italian-American cuisine.",
    "cookingTimeMin": 8,
    "cookingTimeMax": 12,
    "texture": "firm, chewy when al dente",
    "origin": "Lazio (Rome)",
    "originRegion": "Central Italy",
    "sauces": [
      {"name": "Carbonara", "emoji": "🥚", "note": "Classic Roman with egg, pecorino, guanciale"},
      {"name": "Aglio e Olio", "emoji": "🧄", "note": "Simple garlic and olive oil"},
      {"name": "Bolognese", "emoji": "🍖", "note": "Meat sauce (though purists prefer tagliatelle)"}
    ],
    "emojiThumbnail": "🍝"
  },
  {
    "id": "orecchiette",
    "italianName": "Orecchiette",
    "englishName": "Little Ears",
    "aliases": [],
    "category": "short",
    "description": "Small, dome-shaped pasta with a rough exterior and thin center. Hails from Puglia and is perfect for holding chunky sauces.",
    "cookingTimeMin": 10,
    "cookingTimeMax": 14,
    "texture": "chewy, sauce-absorbing",
    "origin": "Puglia (Bari)",
    "originRegion": "Southern Italy",
    "sauces": [
      {"name": "Broccoli Rabe & Sausage", "emoji": "🥬", "note": "Classic Pugliese combination"},
      {"name": "Tomato Ricotta", "emoji": "🧀", "note": "Light, creamy pairing"}
    ],
    "emojiThumbnail": "👂"
  },
  {
    "id": "rigatoni",
    "italianName": "Rigatoni",
    "englishName": "Rigatoni",
    "aliases": [],
    "category": "short",
    "description": "Large, ridged tubes of pasta. The ridges are designed to hold thick sauces, and the open ends capture chunks of meat and vegetables.",
    "cookingTimeMin": 10,
    "cookingTimeMax": 14,
    "texture": "hearty, substantial bite",
    "origin": "Campania",
    "originRegion": "Southern Italy",
    "sauces": [
      {"name": "Amatriciana", "emoji": "🥓", "note": "Tomato with guanciale and pecorino"},
      {"name": "Arrabbiata", "emoji": "🌶️", "note": "Spicy tomato sauce"},
      {"name": "Baked Pasta (Al Forno)", "emoji": "🧀", "note": "Perfect for baked dishes with cheese"}
    ],
    "emojiThumbnail": "🍜"
  }
]
```

**Data Source**: Bundled pasta_shapes.json file in app bundle (target membership: yes)
**Relationships**: Sauces are embedded array on each pasta. No inter-pasta relationships in v1.0.
**Estimated Size**: ~200KB JSON for 80 shapes

---

## 5. Design Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #C75B39 | Accent text, active states, spahetti icon tint |
| Secondary | #F5E6D0 | Section backgrounds, cards |
| Accent | #2D5F3E | Olive green, success states, sauce pairing tags |
| Background | #FFFDF8 | Main screen background |
| Surface | #FFFFFF | Card backgrounds |
| Text Primary | #2C2C2C | Body text, descriptions |
| Text Secondary | #8B7355 | Subtitles, captions |
| Border | #E8DCC8 | Card borders, dividers |
| Favorite | #FF6B6B | Heart icon, favorite state |
| Shadow | #2C2C2C12 | Card shadow (2pt y-offset, 8pt blur, 7% opacity) |

### Typography
| Style | Font | Size | Weight | Usage |
|-------|------|------|--------|-------|
| h1 | New York | 34pt | Bold | Screen titles |
| h2 | New York | 22pt | Semibold | Section headings, Italian pasta names |
| h3 | SF Pro Display | 17pt | Semibold | Card titles |
| Body | SF Pro Text | 16pt | Regular | Descriptions, detail text |
| Caption | SF Pro Text | 13pt | Regular | Cooking times, metadata |
| Mini | SF Pro Text | 11pt | Medium | Category pills, badges |

### Spacing
| Token | Value | Usage |
|-------|-------|-------|
| baseUnit | 4pt | All spacing divisible by 4 |
| xs | 4pt | Inline spacing |
| sm | 8pt | Icon-to-label spacing |
| md | 12pt | Card internal padding |
| lg | 16pt | Section padding, list item spacing |
| xl | 24pt | Screen edge margins |
| xxl | 32pt | Major section breaks |

### Corner Radius
| Token | Value | Usage |
|-------|-------|-------|
| card | 12pt | Pasta shape cards |
| button | 8pt | Category pills, buttons |
| search | 10pt | Search bar |
| detailCard | 16pt | Info cards on detail screen |

### Icons (SF Symbols)
| Usage | Icon Name |
|-------|-----------|
| Tab: Catalog | tray.full |
| Tab: Search | magnifyingglass |
| Tab: Favorites | heart |
| Category: Long | line.diagonal |
| Category: Short | circle.grid.3x3 |
| Category: Filled | circle.fill |
| Category: Soup | bowl |
| Category: Egg | egg |
| Detail: Timer | timer |
| Detail: Origin | mappin.and.ellipse |
| Detail: Sauce | fork.knife |
| Favorite (empty) | heart |
| Favorite (filled) | heart.fill |
| Back | chevron.left |

### Shadows
| Element | Offset | Blur | Color |
|---------|--------|------|-------|
| Cards | 0, 2pt | 8pt | #2C2C2C at 7% opacity |
| Floating buttons | 0, 4pt | 12pt | #2C2C2C at 10% opacity |

---

## 6. App Store Metadata

- **Title**: Pasta Shapes Guide (20 chars ✅)
- **Subtitle**: 80+ shapes, sauces & cook times (30 chars ✅)
- **Keywords**: pasta,shapes,cooking,guide,Italian,food,recipe,sauce,cook time,orecchiette,penne,fusilli,spaghetti,linguine,recipes (under 100 chars ✅)
- **Description**: See idea.md (within 1700 chars)
- **Promotional Text**: Never wonder about pasta shapes again. Cook with confidence, not guesswork. 🍝
- **What's New (v1.0)**: Initial launch — 50+ pasta shapes with full detail, search, favorites
- **Screenshots Needed**:
  1. Home grid (showing diverse pasta cards)
  2. Shape detail (showing a cool shape like orecchiette with all info)
  3. Search results
  4. Favorites tab
  5. Category filter in action
- **Category**: Food & Drink (Primary), Reference (Secondary)
- **Age Rating**: 4+
- **Privacy**: No data collected. All content on-device. No network requests.

---

## 7. Build Instructions

### Framework: SwiftUI
### No third-party dependencies
### Data: Bundled pasta_shapes.json
### Minimum Xcode: Xcode 15.0+
### Minimum iOS: 16.0

### Step-by-Step Build Order:

1. **Create Xcode project** (iOS App, SwiftUI, no Core Data, no tests yet)
   - Product Name: PastaShapesGuide
   - Organization: OWL
   - Bundle ID: com.owl.pastashapes

2. **Create data model** (PastaShape.swift + SaucePairing.swift)
   - Define struct conforming to Codable
   - Create bundled pasta_shapes.json with 10 shapes (minimum viable)
   - Write a DataManager class:
     ```swift
     class PastaDataManager: ObservableObject {
         @Published var shapes: [PastaShape] = []
         func loadData() { /* load from bundle */ }
         func search(_ query: String) -> [PastaShape] { ... }
         func filter(by category: PastaShape.Category?) -> [PastaShape] { ... }
     }
     ```

3. **Create Home screen** (CatalogView)
   - NavigationView with LazyVGrid
   - 2-column adaptive grid (GridItem(.flexible()), GridItem(.flexible()))
   - Category filter as horizontal ScrollView with capsule buttons
   - Pull data from DataManager

4. **Create PastaCard component**
   - Small reusable view: emoji + italianName + cookingTime
   - 12pt corner radius, shadow, white background
   - Tap gesture to navigate to detail

5. **Create ShapeDetailView**
   - Large shape illustration area
   - All text fields from data model
   - Heart button in navigation bar
   - Pass PastaShape object via navigation

6. **Create Search tab**
   - Searchable modifier on CatalogView (iOS 15+ minimal is 16)
   - Filter data based on search text
   - Reuse same cards and grid

7. **Create Favorites tab and functionality**
   - UserDefaults for persistence
   - Filter shapes where isFavorite == true
   - Empty state view

8. **Add favorites toggle to cards and detail**
   - Heart SF Symbol that toggles
   - Haptic feedback (UIImpactFeedbackGenerator)
   - Save to UserDefaults

9. **Polish design**
   - Apply all design tokens
   - Add warm color palette
   - Set correct fonts (New York for headings)
   - Add app icon (simple pasta emoji on terracotta background)

10. **Create app icon** (simple: 🍝 emoji on #C75B39 background, 1024x1024)

### Testing Checklist:
- [ ] App launches without errors on iPhone SE (3rd gen) simulator
- [ ] All 10+ shapes display in grid
- [ ] Search finds shapes by Italian name, English name, and aliases
- [ ] Category filter works correctly
- [ ] Shape detail screen shows all information fields
- [ ] Heart toggle persists across app restarts
- [ ] Empty favorites state displays correctly
- [ ] No console errors or warnings
- [ ] Dark mode works (bonus — ensure colors adapt)
- [ ] Tab bar navigation works smoothly
- [ ] No network calls in the app (verify with Network Link Conditioner)
