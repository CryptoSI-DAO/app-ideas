# Requirements: Scoville Heat Guide

*Version: 1.0*
*Date: 2026-05-27*
*Target: SwiftUI iOS App*

---

## 1. App Specification

- **App Name**: Scoville Heat Guide
- **Bundle ID**: com.owl.scovilleheat
- **Target Platform**: iOS 16.0+ (SwiftUI)
- **Orientation**: Portrait only
- **Minimum Device**: iPhone SE (2nd gen) through iPhone 15 Pro Max
- **Design Mode**: Dark theme by default (heat/dark aesthetic)

---

## 2. Feature Breakdown

### F1: Scoville Scale Visualization (Screen: Home)
- **User Story**: As a hot sauce fan, I want to see peppers and sauces arranged on a visual Scoville scale so I can instantly compare heat levels
- **Acceptance Criteria**:
  - Horizontal scroll view with colored gradient background (green → yellow → orange → red → dark red)
  - Each pepper/sauce shown as a named marker at its SHU position on the scale
  - Logarithmic scale (SHU ranges from 0 to 2,200,000+)
  - Tapping any marker opens Pepper/Sauce Detail
  - Scale markers show: name, emoji thumbnail, SHU number badge
- **Priority**: P0
- **Dependencies**: Bundled pepper + sauce data
- **Complexity**: M (custom scale UI)

### F2: Pepper Detail Screen
- **User Story**: As a user, I want to see comprehensive information about each pepper including flavor profile and uses, so I know how to cook with it
- **Acceptance Criteria**:
  - Shows: name, SHU range (e.g., "2,500-8,000 SHU"), Scoville category badge (color-coded), flavor profile, origin, image, common uses, "where to find it" note
  - Visual SHU bar graphic showing where this pepper sits relative to others
  - Color-coded category system
- **Priority**: P0
- **Dependencies**: Pepper data model
- **Complexity**: S

### F3: Hot Sauce Database
- **User Story**: As a hot sauce buyer, I want to look up commercial hot sauces and their estimated SHU, so I know how hot my purchase will be
- **Acceptance Criteria**:
  - List view of 20+ commercial hot sauces
  - Each entry: brand, sauce name, estimated SHU range, flavor notes
  - Search bar to filter
  - Grouped by heat category (mild, medium, hot, extreme)
- **Priority**: P0
- **Dependencies**: Hot sauce data
- **Complexity**: S

### F4: Heat Tolerance Meter
- **User Story**: As a user who isn't sure of their spice tolerance, I want to set my comfort level and see which peppers/sauces fit, so I avoid buying something too hot
- **Acceptance Criteria**:
  - Screen with 5-level selector: "No Heat" → "Mild" → "Medium" → "Hot" → "Extreme"
  - Selecting a level highlights/masks peppers and sauces in the user's range
  - Persist selection in UserDefaults
  - Visual feedback: peppers in range glow, peppers above range are greyed out
- **Priority**: P1
- **Dependencies**: F1, F3
- **Complexity**: S

### F5: Burn Treatment Guide
- **User Story**: As someone who ate something too spicy, I want quick first aid tips to cool down the burn
- **Acceptance Criteria**:
  - Simple screen with 5-7 tips (dairy, sugar, bread, citrus, etc.)
  - Each tip has explanation of WHY it works (capsaicin is fat-soluble)
  - Fun, light-hearted tone
- **Priority**: P1
- **Dependencies**: None (static content)
- **Complexity**: S

---

## 3. Screen-by-Screen Specification

### Screen 1: Scoville Scale (Home)
- **Purpose**: Visual heat comparison of all peppers and sauces
- **Layout**:
  - Header: "SCOVILLE SCALE" (large, bold, fire-colored)
  - Subtitle: Color legend bar (green→red gradient with category labels)
  - Main: Horizontal scrollable scale with pepper markers
  - Bottom: Tab bar (Scale, Sauces, My Heat, Burn Tips)
- **Elements**:
  - Label: "SCOVILLE SCALE" (h1, SF Pro Display, 28pt, bold, #FF4500)
  - View: Gradient legend bar (horizontal, 40pt height, rounded, showing color zones)
  - ScrollView (horizontal): Scale visualization
  - Scale background: full-width, positioned vertical markers
  - Pepper/Sauce markers: capsule-shaped buttons at correct SHU positions
  - Each marker: emoji icon (🌶️), name label, SHU badge (e.g., "5K SHU")
- **Interactions**:
  - Scroll horizontally → browse the full scale
  - Tap marker → push to Pepper/Sauce Detail
  - Pinch to zoom → no action (fixed scale)
  - Tap gradient zone header → scroll to that heat category
- **Data**: All peppers and sauces from bundled JSON, sorted by SHU
- **Navigation**: Push to detail view

### Screen 2: Pepper/Sauce Detail
- **Purpose**: Full details on one pepper or sauce
- **Layout**:
  - Header: "< Back" button
  - Hero section: Pepper/sauce name + SHU display + category badge
  - Content: Scrollable info cards
  - Visual: SHU bar graphic (mini scale showing position)
- **Elements**:
  - Label: Pepper/sauce name (h1, 30pt, bold, white)
  - Label: SHU range (e.g., "2,500-8,000 SHU") (h2, 22pt, monospaced, #FF4500)
  - Badge: Heat category (capsule pill, color-coded, e.g., "HOT" in red)
  - View: Mini SHU bar (horizontal bar, colored gradient, position indicator dot)
  - Card: Flavor profile (text + 5 dimension pills: Sweet/Savory/Bitter/Heat/Aroma)
  - Card: Origin (text)
  - Card: Common uses (bullet list)
  - Card: Where to buy (text)
- **Interactions**:
  - Back to previous
  - Tap "Similar peppers" → jump to others at similar heat (v1.1)
- **Data**: Single pepper/sauce object
- **Navigation**: Pop back to scale or sauces list

### Screen 3: Hot Sauce List
- **Purpose**: Browse commercial hot sauces by heat
- **Layout**:
  - Header: Title + search bar
  - Category sections (expandable/collapsible)
  - List of sauces in each section
- **Elements**:
  - Label: "Hot Sauces"
  - SearchBar: System search
  - Section headers: Mild | Medium | Hot | Extreme (as Section headers)
  - Rows: Brand name (bold), SHU badge, flavor notes
- **Interactions**:
  - Filter by search
  - Tap row → push to Sauce Detail (same view as Pepper Detail)
- **Data**: Hot sauce array from JSON
- **Navigation**: Push to detail

### Screen 4: My Heat Tolerance
- **Purpose**: Set heat tolerance, see matching peppers
- **Layout**:
  - Header: "What's your heat tolerance?"
  - 5-level picker (vertical list or slider)
  - Preview: Show matching peppers/sauces count
  - List of peppers in range
- **Elements**:
  - 5 selectable options (large tap targets, emoji + label):
    - 😇 No Heat (0-100 SHU)
    - 😊 Mild (100-2,500 SHU)
    - 😐 Medium (2,500-30,000 SHU)
    - 😅 Hot (30,000-100,000 SHU)
    - 🤯 Extreme (100,000+ SHU)
  - Count badge: "12 peppers in your range"
  - List: filtered peppers
- **Interactors**:
  - Tap level → update filter, haptic feedback
  - Tap pepper in list → detail view
- **Data**: Tolerance level from UserDefaults, filtered pepper array
- **Navigation**: Push to detail

### Screen 5: Burn Treatment
- **Purpose**: First aid tips for too-spicy food
- **Layout**:
  - Static content screen with cards
- **Elements**:
  - Header: "🔥 Burn Treatment" (large)
  - List of 6-7 tip cards, each: emoji, title, description
  - Tips: Dairy (🥛), Sugar (🍬), Bread (🍞), Citrus (🍋), Alcohol (🍺), Oil (🫒)
- **Interactions**: Scroll content
- **Data**: Static content (no JSON needed)
- **Navigation**: None (leaf screen)

---

## 4. Data Model

```swift
struct Pepper: Codable, Identifiable {
    let id: String
    let name: String               // "Jalapeño"
    let shuMin: Int              // 2500
    let shuMax: Int              // 8000
    let category: HeatCategory   // mild, medium, hot, veryHot, extreme
    let flavorProfile: FlavorProfile
    let origin: String           // "Mexico"
    let uses: [String]           // ["salsas", "pickling", "poppers"]
    let whereToFind: String      // "Any grocery store"
    let emoji: String            // "🌶️"
    
    enum HeatCategory: String, Codable, CaseIterable {
        case noHeat = "No Heat"
        case mild = "Mild"
        case medium = "Medium"
        case hot = "Hot"
        case veryHot = "Very Hot"
        case extreme = "Extreme"
    }
}

struct FlavorProfile: Codable {
    let sweet: Int       // 0-5
    let savory: Int      // 0-5
    let bitter: Int      // 0-5
    let heat: Int        // 0-5 (intensity of heating sensation)
    let aroma: Int       // 0-5 (fruity, smoky, etc.)
    let description: String // "Bright, vegetal, with grassy notes"
}

struct HotSauce: Codable, Identifiable {
    let id: String
    let brand: String           // "Cholula"
    let name: String            // "Original"
    let shuMin: Int            // 500
    let shuMax: Int            // 1000
    let category: HeatCategory  // same as Pepper
    let flavorNotes: String    // "Tangy, garlicky, with mild heat"
    let emoji: String           // "🥫"
}
```

### Sample Data:

```json
{
  "peppers": [
    {
      "id": "bell_pepper",
      "name": "Bell Pepper",
      "shuMin": 0,
      "shuMax": 0,
      "category": "noHeat",
      "flavorProfile": {
        "sweet": 4, "savory": 2, "bitter": 1, "heat": 0, "aroma": 2,
        "description": "Sweet, crunchy, zero heat"
      },
      "origin": "Central & South America",
      "uses": ["salads", "roasting", "stuffed", "stir-fry"],
      "whereToFind": "Every grocery store",
      "emoji": "🫑"
    },
    {
      "id": "jalapeno",
      "name": "Jalapeño",
      "shuMin": 2500,
      "shuMax": 8000,
      "category": "mild",
      "flavorProfile": {
        "sweet": 2, "savory": 3, "bitter": 1, "heat": 3, "aroma": 3,
        "description": "Bright, vegetal, grassy heat that builds"
      },
      "origin": "Mexico (Jalapa)",
      "uses": ["salsas", "nachos", "poppers", "relishes"],
      "whereToFind": "All grocery stores",
      "emoji": "🌶️"
    },
    {
      "id": "habanero",
      "name": "Habanero",
      "shuMin": 100000,
      "shuMax": 350000,
      "category": "veryHot",
      "flavorProfile": {
        "sweet": 3, "savory": 1, "bitter": 2, "heat": 5, "aroma": 5,
        "description": "Fruity, floral, with intense delayed heat"
      },
      "origin": "Amazon / Yucatan",
      "uses": ["hot sauces", "Caribbean dishes", "marinades", "salsas"],
      "whereToFind": "Specialty stores, farmers markets",
      "emoji": "🔥"
    }
  ],
  "hotSauces": [
    {
      "id": "cholula_original",
      "brand": "Cholula",
      "name": "Original",
      "shuMin": 500,
      "shuMax": 1000,
      "category": "mild",
      "flavorNotes": "Tangy, garlicky, with mild chili heat",
      "emoji": "🥫"
    }
  ]
}
```

**Data Source**: Bundled scoville_data.json in app bundle
**Estimated Size**: ~150KB JSON for 60 peppers + 20 sauces
**Relationships**: None (flat lists). Same detail view for both peppers and sauces.
**SHU Scale Positioning**: Use logarithmic positioning for scroll view — position = log10(SHU) / log10(2200000) * scrollWidth

---

## 5. Design Tokens

### Colors (Dark Theme)
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #FF4500 | Fire orange, SHU numbers, accent text |
| Secondary | #1A1A2E | Deep navy-dark, card backgrounds |
| Accent Green | #00FF7F | No Heat / Mild category |
| Accent Yellow | #FFD700 | Medium category |
| Accent Orange | #FF8C00 | Hot category |
| Accent Red | #FF2222 | Very Hot / Extreme category |
| Background | #0D0D1A | Main app background (near-black) |
| Surface | #1A1A2E | Card backgrounds |
| Text Primary | #FFFFFF | Main text |
| Text Secondary | #A0A0B8 | Subtitles, metadata |
| Border | #2A2A3E | Card borders |
| Scale Gradient | See below | Scoville scale background |

### Scoville Scale Gradient
The horizontal scale uses a 5-stop gradient:
- 0%: #00FF7F (No Heat green)
- 25%: #FFD700 (Mild yellow)
- 50%: #FF8C00 (Hot orange)
- 75%: #FF4500 (Very Hot fire)
- 100%: #8B0000 (Extreme dark red)

### Typography
| Style | Font | Size | Weight | Usage |
|-------|------|------|--------|-------|
| h1 | SF Pro Display | 30pt | Bold | Screen titles |
| h2 | SF Pro Display | 22pt | Semibold | Section headings, SHU ranges |
| h3 | SF Pro | 17pt | Semibold | Card titles |
| Body | SF Pro Text | 16pt | Regular | Descriptions |
| Caption | SF Pro Text | 13pt | Regular | Metadata, badges |
| SHU Number | SF Mono | 18pt | Medium | SHU display (monospaced for alignment) |

### Spacing
| Token | Value |
|-------|-------|
| xs | 4pt |
| sm | 8pt |
| md | 12pt |
| lg | 16pt |
| xl | 24pt |
| xxl | 32pt |

### Corner Radius
| Token | Value | Usage |
|-------|-------|-------|
| card | 12pt | Info cards |
| pill | 16pt | Category badges, heat level buttons |
| scale | 8pt | Scrollable scale container |

### Icons (SF Symbols)
| Usage | Icon Name |
|-------|-----------|
| Tab: Scale | thermometer |
| Tab: Sauces | drop.fill |
| Tab: My Heat | person.fill.questionmark |
| Tab: Burn Tips | cross.case.fill |
| Heat category badges | Same color coding as text |
| Back | chevron.left |

---

## 6. App Store Metadata

- **Title**: Scoville Heat Guide (21 chars ✅)
- **Subtitle**: Pepper heat scale & hot sauces (30 chars ✅)
- **Keywords**: scoville,heat,pepper,hot sauce,spicy,chili,capsicum,Carolina Reaper,Jalapeno,habanero,SHU,scale,food (96 chars ✅)
- **Description**: See idea.md
- **Promotional Text**: Know your heat before you eat. 🌶️ From mild to nuclear — the complete Scoville scale.
- **What's New (v1.0)**: Initial launch — 60+ peppers & 20+ hot sauces on the visual Scoville scale
- **Screenshots Needed**:
  1. Scoville scale (full horizontal, showing peppers at different heat levels)
  2. Pepper detail (e.g., Habanero with SHU display)
  3. Hot sauce list
  4. Heat tolerance meter
  5. Burn treatment tips
- **Category**: Food & Drink (Primary), Reference (Secondary)
- **Age Rating**: 4+
- **Privacy**: No data collected. Fully on-device. No network requests.

---

## 7. Build Instructions

### Framework: SwiftUI
### No third-party dependencies
### Data: Bundled scoville_data.json
### Minimum Xcode: Xcode 15.0+

### Step-by-Step Build Order:

1. **Create Xcode project** (iOS App, SwiftUI)
   - Product Name: ScovilleHeatGuide
   - Bundle ID: com.owl.scovilleheat

2. **Create data model** (Pepper.swift, HotSauce.swift, FlavorProfile.swift)
   - Load JSON from bundle
   - DataManager with loadData(), search(), filterByCategory()

3. **Create Scoville Scale UI** (the main challenge)
   - Horizontal ScrollView with gradient background background (LinearGradient with 5 color stops)
   - Position each pepper marker using logarithmic SHU positioning:
     ```swift
     func xPosition(for shu: Int, in width: CGFloat) -> CGFloat {
         let logSHU = log10(Double(max(shu, 1)))
         let logMax = log10(2_200_000)
         return CGFloat(logSHU / logMax) * width
     }
     ```
   - Each marker is a Button with name + emoji + SHU badge

4. **Create Pepper Detail screen / Sauce Detail screen** (one reusable view)
   - Pass either Pepper or HotSauce via enum wrapping
   - Show all info fields
   - Mini SHU bar showing position

5. **Create Hot Sauce List screen**
   - Grouped List by category
   - Search bar

6. **Create Heat Tolerance screen**
   - 5 selectable options
   - Store selection in UserDefaults
   - Filter peppers/sauces in list below

7. **Create Burn Treatment screen** (static, no data)
   - Simple List with static text

8. **Add tab bar with 4 tabs**
   - Scale | Sauces | My Heat | Burn Tips

9. **Theme consistently dark**
   - Set `preferredColorScheme(.dark)` on root view
   - Ensure all colors match dark theme tokens

10. **Test and polish**
    - Verify layout on iPhone SE simulator
    - Ensure SHU scale scrolls smoothly
    - Add haptic feedback on pepper tap
    - Create app icon (🌶️ on dark red background)

### Testing Checklist:
- [ ] App launches on iPhone SE simulator
- [ ] Scoville scale scrolls smoothly with all peppers visible
- [ ] Tapping peppers/sauces opens correct detail
- [ ] Search filters work on both peppers and sauces
- [ ] Heat tolerance selection persists across launches
- [ ] Burn tips screen loads instantly (static content)
- [ ] Dark theme applied consistently (no light mode flash)
- [ ] No network calls
- [ ] No console errors
