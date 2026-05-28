# Requirements: Spice Substitution Guide

*Version: 1.0*
*Date: 2026-05-27*
*Target: SwiftUI iOS App*

---

## 1. App Specification

- **App Name**: Spice Sub Guide
- **Bundle ID**: com.owl.spicesub
- **Target Platform**: iOS 16.0+ (SwiftUI)
- **Orientation**: Portrait only
- **Minimum Device**: iPhone SE (2nd gen) through iPhone 15 Pro Max

---

## 2. Feature Breakdown

### F1: Spice Search & Substitution Results (Home)
- **User Story**: As a cook who is out of a spice, I want to type the spice name and instantly see substitution options so I can continue cooking without a store run
- **Acceptance Criteria**:
  - Search bar auto-focused on launch
  - Type any spice/hero name → see substitution results in real-time
  - Each result shows: substitute name, conversion ratio (e.g., "¾ tsp ground"), flavor similarity note
  - Results appear within 100ms (local data, no API)
  - No results state: "No substitutions found for 'xyz'"
  - Clear button to reset
- **Priority**: P0
- **Dependencies**: Bundled spice data with bidirectional substitution mapping
- **Complexity**: S

### F2: Spice Detail Screen
- **User Story**: As a user looking at a specific spice, I want to understand its flavor profile and all its substitution options (both what it can replace, and what can replace it), so I have complete context
- **Acceptance Criteria**:
  - Shows: spice name, aliases, description, flavor profile (5-dimension horizontal bars), cuisines, origin
  - "This can be replaced BY" section (list of substitutes with ratios)
  - "This can replace" section (list of spices this one substitutes for)
  - Storage tips: "Store whole in airtight container, 2-3 years"
  - Whole ↔ Ground conversion ratio
- **Priority**: P0
- **Dependencies**: Spice data model with bidirectional relationships
- **Complexity**: S

### F3: Browse by Cuisine
- **User Story**: As a cook preparing a specific cuisine (e.g., Indian), I want to see spices organized by cuisine so I can explore substitutions within a flavor profile
- **Acceptance Criteria**:
  - Filter spices by cuisine: Indian, Mexican, Mediterranean, Asian, Middle Eastern, French, Caribbean
  - Show spices in that cuisine as a list
  - Tapping a spice opens detail
  - Cuisine count badge shows number of spices per cuisine
- **Priority**: P1
- **Dependencies**: Spice data model with cuisine tags
- **Complexity**: S

### F4: "What Can I Make?" Reverse Lookup
- **User Story**: As a user with a limited spice rack, I want to pick a spice I HAVE and see what it can substitute FOR, so I can maximize what I can cook
- **Acceptance Criteria**:
  - From any detail screen or from a dedicated "Reverse Lookup" tab
  - Select spice → show all spices it can replace
  - Same conversion ratios and notes
- **Priority**: P1
- **Dependencies**: F2
- **Complexity**: S

### F5: My Spice Rack (Favorites/Inventory)
- **User Story**: As a user, I want to check off the spices I have in my kitchen, so the app can help me find recipes based on my actual inventory
- **Acceptance Criteria**:
  - Toggle spices as "have" or "don't have"
  - "My Rack" tab shows only owned spices
  - "What can I make?" button → aggregates all possible recipes (v1.1+, static list in v1.0)
  - Persist in UserDefaults
- **Priority**: P1
- **Dependencies**: F1
- **Complexity**: S

---

## 3. Screen-by-Screen Specification

### Screen 1: Home (Search)
- **Purpose**: Quick substitution search
- **Layout**:
  - Header: App icon + "Spice Sub Guide" title
  - Search bar (large, centered, auto-focused)
  - Results list below
  - Bottom: tab bar (Search, Cuisines, My Rack)
- **Elements**:
  - Image: App icon (small, 40x40)
  - Label: "Spice Sub Guide" (h1, 28pt, bold, Primary brown)
  - Label: "Type any spice to find substitutions" (caption, secondary)
  - SearchBar: Large search field, auto-focus, placeholder "e.g., cardamum, cumin, za'atar"
  - List: Substitution results (each row: substitute name + ratio + similarity note + cuisine tag)
  - Empty state: "No substitutions found" message
- **Interactions**:
  - Type → real-time search with results list
  - Tap result → navigate to Spice Detail
  - Clear → reset search
- **Data**: Filtered suggestions based on search text
- **Navigation**: Push to Spice Detail

### Screen 2: Spice Detail
- **Purpose**: Complete spice information and substitution relationships
- **Layout**:
  - Header: "< Back" button + "<spice name>"
  - Scrollable content with info cards
- **Elements**:
  - Label: Spice name (h1, 30pt, bold)
  - Label: Aliases (caption, secondary, e.g., "Also called: dhaniya")
  - Label: Description (body, 16pt, regular)
  - Card: Flavor Profile (5 horizontal bars: Sweet/Savory/Bitter/Heat/Aroma)
  - Card: Cuisines (capsule pills: Indian, Middle Eastern)
  - Card: Origin (text)
  - Section Header: "🔄 This can be replaced BY" (bold, accent color)
  - List: substitutes (each row: name + ratio + note)
  - Section Header: "🔁 This can replace" (bold, accent color)
  - List: reversed substitutions (each row: name + ratio)
  - Card: Storage Tips (icon + text)
  - Card: Whole ↔ Ground Ratio (e.g., "1 tsp ground = 1.5 tsp whole")
  - Button: "Add to My Rack" (full width, outlined)
- **Interactions**:
  - Back → pop
  - Tap substitution → open that spice's detail (linked navigation)
  - Toggle "Add to My Rack" → save to UserDefaults, haptic
  - Scroll → read all info
- **Data**: Single spice object + related substitutes (from JSON)
- **Navigation**: Pop back, or push to another Spice Detail

### Screen 3: Browse by Cuisine
- **Purpose**: Explore spices organized by culinary tradition
- **Layout**:
  - Header: "Browse by Cuisine"
  - Grid/List of cuisine options with spice counts
  - Detail: Spices in selected cuisine
- **Elements**:
  - Label: "Browse by Cuisine" (h1)
  - Grid: 3x2 grid of cuisine cards (Indian 🇮🇳, Mexican 🇲🇽, Mediterranean, Asian, Middle Eastern, French)
  - Each card: flag emoji + cuisine name + count (e.g., "18 spices")
  - Section view: List of spices in selected cuisine
  - Each spice row: name + flavor icon
- **Interactions**:
  - Tap cuisine card → expand/show spices in that cuisine
  - Tap spice → push to detail
  - Back → return to cuisine grid
- **Data**: Spices array filtered by cuisine
- **Navigation**: Detail drill-down

### Screen 4: My Spice Rack
- **Purpose**: Track owned spices
- **Layout**:
  - Header: "My Spice Rack" + count badge
  - List of owned spices
  - "Add more" button
  - Browse cuisines -> track -> view suggestions
- **Elements**:
  - Label: "My Spice Rack" (h1)
  - Badge: Count of owned spices (e.g., "12 spices")
  - List: Owned spices (compact rows)
  - Empty state: "Your rack is empty. Search for spices and tap '+ Rack' to add them."
  - Button: "Find spices by cuisine" (link)
- **Interactions**:
  - Tap spice → detail
  - Swipe to delete → remove from rack
  - Tap "+ Rack" from any spice detail → add
- **Data**: Owned spice IDs from UserDefaults
- **Navigation**: Push to spice detail

---

## 4. Data Model

```swift
struct Spice: Codable, Identifiable {
    let id: String                  // "cumin"
    let name: String                // "Cumin"
    let aliases: [String]           // ["Jeera", "Comino"]
    let description: String         // Brief description
    let origin: String              // "Mediterranean"
    let cuisines: [String]          // ["Indian", "Mexican", "Middle Eastern"]
    let wholeGroundRatio: String    // "1 tsp ground = 1.25 tsp whole"
    let storageTips: String         // "Whole: 2 yrs airtight. Ground: 6 months."
    let flavorProfile: FlavorProfile
    let substitutions: [Substitution] // Substitutes FOR this spice (what can replace IT)
    let canReplace: [String]        // IDs of spices this can replace (reverse lookup)
}

struct Substitution: Codable {
    let substituteSpiceId: String    // ID of the substitute spice
    let ratio: String                // "¾ tsp ground for 1 tsp cumin"
    let note: String                 // "Similar earthy warmth, less smoky"
    let similarity: Int              // 1-5 (1=loose, 5=very close)
}

struct FlavorProfile: Codable {
    let sweet: Int        // 0-5
    let savory: Int       // 0-5
    let bitter: Int       // 0-5
    let heat: Int         // 0-5
    let aroma: Int        // 0-5
    let description: String // "Earthy, smoky, warm with slight bitterness"
}
```

### Sample Data:

```json
[
  {
    "id": "cumin",
    "name": "Cumin (Ground)",
    "aliases": ["Jeera", "Comino", "Zeera"],
    "description": "A warm, earthy spice essential to Indian, Mexican, and Middle Eastern cumin. The dried seeds of the Cuminum cyminum plant.",
    "origin": "Mediterranean / Middle East",
    "cuisines": ["Indian", "Mexican", "Middle Eastern", "North African"],
    "wholeGroundRatio": "1 tsp ground = 1.25 tsp whole seeds",
    "storageTips": "Whole seeds: 2 years in airtight container. Ground: 6 months max.",
    "flavorProfile": {
      "sweet": 1, "savory": 4, "bitter": 2, "heat": 1, "aroma": 5,
      "description": "Earthy, smoky, warm with slight bitterness"
    },
    "substitutions": [
      {
        "substituteSpiceId": "coriander_ground",
        "ratio": "Use 1 tsp coriander + ½ tsp chili powder",
        "note": "Flatter flavor, needs heat component added",
        "similarity": 3
      },
      {
        "substituteSpiceId": "chili_powder",
        "ratio": "Use ¾ tsp chili powder",
        "note": "Similar warmth but adds more heat",
        "similarity": 3
      },
      {
        "substituteSpiceId": "caraway",
        "ratio": "Use ¾ tsp caraway seeds, ground",
        "note": "Close flavor family, more European profile",
        "similarity": 3
      }
    ],
    "canReplace": ["coriander_ground"]
  },
  {
    "id": "coriander_ground",
    "name": "Coriander (Ground)",
    "aliases": ["Dhaniya", "Cilantro seed"],
    "description": "The dried seeds of the cilantro plant. Citrusy, slightly sweet, and warming — very different from fresh cilantro leaves.",
    "origin": "Mediterranean / Southern Europe",
    "cuisines": ["Indian", "Middle Eastern", "Mediterranean", "North African"],
    "wholeGroundRatio": "1 tsp ground = 1.5 tsp whole seeds",
    "storageTips": "Whole seeds: 2 years. Ground: 3-4 months.",
    "flavorProfile": {
      "sweet": 2, "savory": 2, "bitter": 1, "heat": 0, "aroma": 4,
      "description": "Citrusy, floral, slightly sweet"
    },
    "substitutions": [
      {
        "substituteSpiceId": "cumin",
        "ratio": "Use ¾ tsp cumin + pinch of citrus zest",
        "note": "More earthy than citrusy, adds warmth",
        "similarity": 3
      },
      {
        "substituteSpiceId": "garam_masala",
        "ratio": "Use ½ tsp garam masala",
        "note": "Complex blend that includes coriander",
        "similarity": 3
      }
    ],
    "canReplace": ["cumin"]
  },
  {
    "id": "cardamom",
    "name": "Cardamom (Ground)",
    "aliases": ["Elaichi", "True cardamom"],
    "description": "One of the world's most expensive spices. Intensely aromatic with notes of eucalyptus, citrus, and mint. Essential in Indian and Scandinavian baking.",
    "origin": "India / Guatemala",
    "cuisines": ["Indian", "Middle Eastern", "Scandinavian", "North African"],
    "wholeGroundRatio": "1 tsp ground = 10-12 whole pods, ground",
    "storageTips": "Whole pods: 1 year airtight. Ground: 3 months. Grind fresh for best flavor.",
    "flavorProfile": {
      "sweet": 3, "savory": 1, "bitter": 1, "heat": 1, "aroma": 5,
      "description": "Intensely aromatic: eucalyptus, citrus, mint, floral"
    },
    "substitutions": [
      {
        "substituteSpiceId": "cinnamon",
        "ratio": "Use ½ tsp cinnamon + pinch of nutmeg",
        "note": "Similar warmth but loses the bright aromatics",
        "similarity": 2
      },
      {
        "substituteSpiceId": "vanilla",
        "ratio": "Use 1 tsp vanilla extract (only in sweet dishes)",
        "note": "Only works in desserts, completely different flavor",
        "similarity": 2
      }
    ],
    "canReplace": []
  }
]
```

**Data Source**: Bundled spice_substitutions.json in app bundle
**Estimated Size**: ~80KB JSON for 50 spices with 3-5 substitutions each
**Relationships**: Bidirectional substitution graph. `substitutions` array links to other spice IDs. `canReplace` array for reverse lookup.
**Data Loading**: Parse substitutions at startup, build lookup dictionaries for O(1) access.

---

## 5. Design Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #8B4513 | Saddle brown, active states, key text |
| Secondary | #FFF8E7 | Warm cream, section backgrounds |
| Accent | #D4A574 | Cinnamon, highlight cards, spice-colored accents |
| Background | #FDFCFA | Main screen background (clean white) |
| Surface | #FFFFFF | Card backgrounds |
| Text Primary | #2C1810 | Dark brown text |
| Text Secondary | #8B7355 | Subtitles, metadata |
| Border | #E8DCC8 | Card borders |
| Substitution Green | #4A7C59 | Similarity ratings, positive notes |
| Warning Red | #C1666B | Low similarity warnings |
| Cuisine Tag BG | #FFF0E0 | Cuisine tag background |

### Typography
| Style | Font | Size | Weight | Usage |
|-------|------|------|--------|-------|
| h1 | New York | 30pt | Bold | Screen titles |
| h2 | New York | 22pt | Semibold | Spice names, section headers |
| h3 | SF Pro Display | 17pt | Semibold | Card titles, substitutions |
| Body | SF Pro Text | 16pt | Regular | Descriptions |
| Caption | SF Pro Text | 13pt | Regular | Conversion ratios, notes |
| Ratio | SF Mono | 15pt | Medium | Conversion ratios (monospaced for clarity) |

### Spacing
| Token | Value |
|-------|-------|
| xs | 4pt |
| sm | 8pt |
| md | 12pt |
| lg | 16pt |
| xl | 24pt |

### Corner Radius
| Token | Value | Usage |
|-------|-------|-------|
| card | 12pt | Info cards |
| pill | 16pt | Cuisine tags, similarity badges |
| button | 10pt | Action buttons |

### Icons (SF Symbols)
| Usage | Icon Name |
|-------|-----------|
| Tab: Search | magnifyingglass |
| Tab: Cuisines | globe |
| Tab: My Rack | truffle (if available), else basket |
| Flavor: Sweet | leaf.fill |
| Flavor: Savory | fork.knife |
| Flavor: Bitter | drop.triangle.fill |
| Flavor: Heat | flame |
| Flavor: Aroma | wind |
| Substitution section | arrow.triangle.swap |
| Storage | archivebox |
| Rack (empty) | heart |
| Rack (filled) | heart.fill |
| Back | chevron.left |

---

## 6. App Store Metadata

- **Title**: Spice Sub Guide (15 chars ✅)
- **Subtitle**: Substitute spices with confidence (30 chars ✅)
- **Keywords**: spice,substitute,cooking,recipe,herb,flavor,cumin,coriander,cardamom,turmeric,paprika,kitchen,food,replace,swap (98 chars ✅)
- **Description**: See idea.md
- **Promotional Text**: Never abandon a recipe again. 🌿 100+ spices, 300+ substitutions, 100% offline.
- **What's New (v1.0)**: Initial launch — 50+ spices with 3-5 substitutions each, search, browse by cuisine, rack tracking
- **Screenshots Needed**:
  1. Search results (typing "cumin" showing substitution options)
  2. Spice detail (cumin with flavor bars and substitution lists)
  3. Browse by cuisine (Indian spices list)
  4. My Spice Rack
  5. Conversion ratio close-up
- **Category**: Food & Drink (Primary), Reference (Secondary)
- **Age Rating**: 4+
- **Privacy**: No data collected. Fully on-device. No network requests.

---

## 7. Build Instructions

### Framework: SwiftUI
### No third-party dependencies
### Data: Bundled spice_substitutions.json
### Minimum Xcode: Xcode 15.0+

### Step-by-Step Build Order:

1. **Create Xcode project** (iOS App, SwiftUI)
   - Product Name: SpiceSubGuide
   - Bundle ID: com.owl.spicesub

2. **Create data model** (Spice.swift, Substitution.swift, FlavorProfile.swift)
   - Define structs with Codable
   - Create bundled spice_substitutions.json with 10 spices
   - Write DataManager:
     ```swift
     class SpiceDataManager: ObservableObject {
         @Published var spices: [Spice] = []
         private var spiceDict: [String: Spice] = [:]
         
         func loadData() { /* bundle decode + build dict */ }
         func search(_ query: String) -> [Substitution] { ... }
         func getSubstitutions(for spiceId: String) -> [Substitution] { ... }
         func getReverseSubstitutions(for spiceId: String) -> [Spice] { ... }
         func filter(by cuisine: String) -> [Spice] { ... }
     }
     ```

3. **Create Home search screen**
   - Search bar at top (Searchable modifier or custom UITextField-wrapper)
   - Real-time results in List below
   - Result row: substitute name, ratio (monospaced), similarity capsule, note

4. **Create Spice Detail screen**
   - ScrollView with cards
   - Flavor profile: 5 horizontal progress bars (SwiftUI ProgressView)
   - Substitution sections: two lists (can replace, can be replaced by)
   - Storage card
  5. **Create Browse by Cuisine screen**
   - NavigationSplitView (iPad) or List (iPhone)
   - Cuisine sections with counts
   - Drill-down to spice list

6. **Create My Spice Rack screen**
   - List of owned spices
   - Empty state
   - Add/remove functionality

7. **Wire up links between screens**
   - Substitutions on detail screen → tap → open that spice's detail
   - "Add to Rack" button → toggle → UserDefaults

8. **Apply warm brown/cream design theme**
   - Set colors per tokens
   - New York font for spice names
   - Monospace font for ratios
   - Cream/warm white backgrounds

9. **Create app icon** (simple: 🌿 or spice jar on warm background)

### Testing Checklist:
- [ ] App launches on iPhone SE simulator
- [ ] Search finds spices by name and aliases
- [ ] Substitution results show with correct ratios
- [ ] Spice detail shows all sections (flavor bars, both substitution sections, storage)
- [ ] Tapping a substitution link opens the correct spice detail
- [ ] Cuisine filter shows correct spices
- [ ] "Add to Rack" persists across launches
- [ ] Empty rack state displays correctly
- [ ] No console errors or warnings
- [ ] Full search from home: "cumin" → 3+ substitutions shown → tap → substitution detail
- [ ] Performance: search results show within 100ms
