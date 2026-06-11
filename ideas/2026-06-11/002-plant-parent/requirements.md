# Requirements Document: Plant Parent

*Generated: 2026-06-11*
*Version: 1.0*

---

## 1. App Specification

- **App Name:** Plant Parent - Care Guide
- **Bundle ID:** com.lisakim.plantparent
- **Target Platform:** iOS 16.0+
- **Orientation:** Portrait only
- **Minimum Device:** iPhone SE (3rd gen) through iPhone 15 Pro Max

---

## 2. Feature Breakdown

### F1: Plant Library
- **User Story:** As a new plant parent, I want to browse a visual guide of common houseplants so I can learn about their care needs.
- **Acceptance Criteria:**
  - 100+ plants with: name, illustration/photo, light needs, watering frequency, humidity, temperature range, toxicity, difficulty, care tips
  - Browse by category (All, Beginner, Low Light, Pet-Friendly, Air-Purifying)
  - Search by name
  - Each plant has a detail screen with full care information
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** M

### F2: My Garden
- **User Story:** As a user, I want to add my own plants to a personal collection so I can track what I own.
- **Acceptance Criteria:**
  - Add plant from library to personal collection
  - Assign nickname, room location, and optional photo
  - View all plants in a grid layout
  - See at a glance which plants need water today
  - Free tier: up to 10 plants. Premium: unlimited.
- **Priority:** P0
- **Dependencies:** F1
- **Complexity:** M

### F3: Watering Schedule
- **User Story:** As a user, I want to know which plants need water today so I don't forget.
- **Acceptance Criteria:**
  - "Today" screen shows list of plants needing water
  - Watering frequency auto-set from plant type, adjustable by user
  - Seasonal adjustment (less frequent in winter)
  - Tap "Watered" → marks as done, schedules next watering
  - Overdue plants shown with red indicator
- **Priority:** P0
- **Dependencies:** F1, F2
- **Complexity:** M

### F4: Care Calendar
- **User Story:** As a user, I want a weekly/monthly view of all plant care tasks.
- **Acceptance Criteria:**
  - Weekly view: shows each day's tasks (watering, fertilizing, repotting)
  - Monthly view: overview of all tasks
  - Tap a task → mark as complete
  - Color-coded by task type (blue = water, green = fertilize, orange = repot)
- **Priority:** P0
- **Dependencies:** F3
- **Complexity:** M

### F5: Care Guide
- **User Story:** As a beginner, I want to read articles about plant care so I can learn best practices.
- **Acceptance Criteria:**
  - 20+ bundled articles on plant care topics
  - Categories: Watering, Light, Soil, Pests, Seasonal Care, Propagation
  - Clean reading view with headings and body text
  - Search articles by keyword
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** S

### F6: Plant Detail
- **User Story:** As a user, I want to see complete care information for a specific plant.
- **Acceptance Criteria:**
  - Full plant info: light, water, humidity, temperature, toxicity, difficulty
  - Care tips section
  - "Add to My Garden" button
  - Visual icons for each care parameter
  - Toxicity warning prominently displayed if toxic to pets
- **Priority:** P0
- **Dependencies:** F1
- **Complexity:** S

---

## 3. Screen-by-Screen Specification

### Screen: Today
- **Purpose:** Show which plants need attention today
- **Layout:**
  - Header: "Today" + date
  - Section: "Needs Water" — list of plants with water button
  - Section: "All Caught Up" — empty state if nothing needs attention
  - Bottom: Tab bar
- **Elements:**
  - Plant row: small thumbnail, nickname, room, "Watered" button
  - Empty state: illustration + "All your plants are happy! 🌱"
  - Overdue badge (red dot)
- **Interactions:**
  - Tap "Watered" → marks as watered, removes from today list, haptic feedback
  - Tap plant row → navigates to Plant Detail
  - Pull to refresh
- **Data:** Filtered from user's garden where nextWaterDate <= today
- **Navigation:** Tab bar → Today tab

### Screen: Library
- **Purpose:** Browse and search the plant database
- **Layout:**
  - Header: Search bar + filter chips
  - Content: Grid of plant cards (2 columns)
- **Elements:**
  - Search bar (text field)
  - Filter chips: All, Beginner, Low Light, Pet-Friendly, Air-Purifying
  - Plant card: thumbnail, name, difficulty badge, water/light icons
- **Interactions:**
  - Type in search → filters plant list in real-time
  - Tap filter chip → filters by category
  - Tap plant card → navigates to Plant Detail
- **Data:** Bundled JSON plant database
- **Navigation:** Tab bar → Library tab. Plant card → Plant Detail

### Screen: Plant Detail
- **Purpose:** Show full care information for a plant
- **Layout:** Scrollable detail view
- **Elements:**
  - Plant image/illustration (large, top)
  - Plant name (large title)
  - Difficulty badge (Beginner/Intermediate/Advanced)
  - Toxicity warning banner (if toxic)
  - Care parameters grid: Light (icon + text), Water (icon + frequency), Humidity, Temperature
  - Care tips section (expandable)
  - "Add to My Garden" button (bottom, sticky)
- **Interactions:**
  - Scroll to see all info
  - Tap "Add to My Garden" → opens Add to Garden modal
  - Tap care tip → expands/collapses
- **Data:** From bundled JSON plant database
- **Navigation:** Push from Library or My Garden

### Screen: My Garden
- **Purpose:** View personal plant collection
- **Layout:**
  - Header: "My Garden" + plant count
  - Content: Grid of plant cards (2 columns)
  - FAB: "+" button
- **Elements:**
  - Plant card: thumbnail/photo, nickname, room, water status indicator (green = OK, red = needs water)
  - Empty state: "Your garden is empty. Add your first plant!" + illustration
  - FAB: "+" button
- **Interactions:**
  - Tap plant → Plant Detail
  - Tap "+" → navigates to Library to add plant
  - Long press → edit/delete options
- **Data:** Core Data user garden
- **Navigation:** Tab bar → My Garden tab

### Screen: Add to Garden
- **Purpose:** Add a plant from the library to personal collection
- **Layout:** Modal sheet
- **Elements:**
  - Plant name (pre-filled from library)
  - Nickname text field (optional, placeholder: "e.g., Steve")
  - Room picker (picker wheel: Living Room, Bedroom, Kitchen, Bathroom, Office, Balcony, Other)
  - Photo button (optional, camera roll only)
  - "Add" button, "Cancel" button
- **Interactions:**
  - Enter nickname (optional)
  - Select room
  - Tap "Add" → saves to garden, dismisses modal, shows confirmation
- **Data:** Saves to Core Data garden entity
- **Navigation:** Modal from Plant Detail or My Garden

### Screen: Calendar
- **Purpose:** View care tasks in calendar format
- **Layout:**
  - Header: Month/Week toggle + month name
  - Content: Calendar grid (week view) or month grid
- **Elements:**
  - Week view: horizontal scroll, each day shows task dots (blue = water, green = fertilize)
  - Month view: grid, task dots on dates
  - Task list below calendar for selected day
  - Color legend
- **Interactions:**
  - Toggle between week/month view
  - Tap day → shows task list below
  - Tap task → mark as complete
  - Swipe to change week/month
- **Data:** Computed from garden plants' care schedules
- **Navigation:** Tab bar → Calendar tab

### Screen: Guide
- **Purpose:** Read plant care articles
- **Layout:**
  - Header: "Care Guide"
  - Content: List of article cards
- **Elements:**
  - Article card: title, category badge, short excerpt
  - Category filter chips at top
- **Interactions:**
  - Tap article → opens reading view
  - Filter by category
- **Data:** Bundled JSON articles
- **Navigation:** Tab bar → Guide tab

---

## 4. Data Models

### Plant (Bundled Database)
```swift
struct Plant: Identifiable, Codable {
    let id: String // e.g., "monstera-deliciosa"
    let name: String // e.g., "Monstera"
    let scientificName: String // e.g., "Monstera deliciosa"
    let imageName: String // Asset catalog name
    let difficulty: Difficulty // enum: beginner, intermediate, advanced
    let light: LightLevel // enum: low, medium, bright, direct
    let waterFrequency: Int // Days between watering
    let humidity: HumidityLevel // enum: low, medium, high
    let temperatureRange: String // e.g., "60-80°F"
    let isToxic: Bool
    let toxicTo: [String] // e.g., ["cats", "dogs"]
    let careTips: [String]
    let categories: [PlantCategory]
}

enum PlantCategory: String, Codable, CaseIterable {
    case beginner, lowLight, petFriendly, airPurifying, trailing, flowering, succulent
}
```

### GardenPlant (User's Collection)
```swift
struct GardenPlant: Identifiable, Codable {
    let id: UUID
    let plantId: String // References bundled Plant.id
    var nickname: String?
    var room: String
    var dateAdded: Date
    var lastWatered: Date?
    var nextWaterDate: Date
    var wateringInterval: Int // Days (can override plant default)
    var photoName: String? // Optional user photo
    
    var isWateringDue: Bool {
        nextWaterDate <= Date()
    }
    
    var daysUntilWater: Int {
        Calendar.current.dateComponents([.day], from: Date(), to: nextWaterDate).day ?? 0
    }
}
```

### CareArticle
```swift
struct CareArticle: Identifiable, Codable {
    let id: String
    let title: String
    let category: String
    let excerpt: String
    let content: String // Markdown or plain text
}
```

### Sample Data (Plants - first 5 of 100+)
```json
[
  {
    "id": "monstera-deliciosa",
    "name": "Monstera",
    "scientificName": "Monstera deliciosa",
    "imageName": "monstera",
    "difficulty": "beginner",
    "light": "medium",
    "waterFrequency": 7,
    "humidity": "medium",
    "temperatureRange": "65-85°F",
    "isToxic": true,
    "toxicTo": ["cats", "dogs"],
    "careTips": ["Wipe leaves monthly to remove dust", "Provide a moss pole for climbing", "Water when top inch of soil is dry"],
    "categories": ["beginner", "trailing", "airPurifying"]
  },
  {
    "id": "pothos",
    "name": "Pothos",
    "scientificName": "Epipremnum aureum",
    "imageName": "pothos",
    "difficulty": "beginner",
    "light": "low",
    "waterFrequency": 7,
    "humidity": "low",
    "temperatureRange": "60-80°F",
    "isToxic": true,
    "toxicTo": ["cats", "dogs"],
    "careTips": ["Thrives in low light", "Trim vines to encourage bushiness", "Can grow in water or soil"],
    "categories": ["beginner", "lowLight", "trailing", "airPurifying"]
  },
  {
    "id": "snake-plant",
    "name": "Snake Plant",
    "scientificName": "Sansevieria trifasciata",
    "imageName": "snake-plant",
    "difficulty": "beginner",
    "light": "low",
    "waterFrequency": 14,
    "humidity": "low",
    "temperatureRange": "60-85°F",
    "isToxic": true,
    "toxicTo": ["cats", "dogs"],
    "careTips": ["Very drought tolerant", "Don't overwater", "Tolerates neglect well"],
    "categories": ["beginner", "lowLight", "airPurifying"]
  },
  {
    "id": "fiddle-leaf-fig",
    "name": "Fiddle Leaf Fig",
    "scientificName": "Ficus lyrata",
    "imageName": "fiddle-leaf-fig",
    "difficulty": "advanced",
    "light": "bright",
    "waterFrequency": 7,
    "humidity": "high",
    "temperatureRange": "65-75°F",
    "isToxic": true,
    "toxicTo": ["cats", "dogs"],
    "careTips": ["Needs consistent bright indirect light", "Don't move around often", "Clean leaves regularly"],
    "categories": ["airPurifying"]
  },
  {
    "id": "peace-lily",
    "name": "Peace Lily",
    "scientificName": "Spathiphyllum",
    "imageName": "peace-lily",
    "difficulty": "beginner",
    "light": "low",
    "waterFrequency": 5,
    "humidity": "high",
    "temperatureRange": "65-80°F",
    "isToxic": true,
    "toxicTo": ["cats", "dogs"],
    "careTips": ["Droops when thirsty — great indicator", "Loves humidity", "Blooms in bright indirect light"],
    "categories": ["beginner", "lowLight", "flowering", "airPurifying"]
  }
]
```

### Data Source
- Plant database: Bundled JSON (100+ plants)
- Care articles: Bundled JSON (20+ articles)
- User garden: Core Data
- No backend, no API, no internet required

---

## 5. Design Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #2D6A4F | Headers, buttons, active states |
| Secondary | #95D5B2 | Secondary elements, tags, progress |
| Accent | #F4A261 | Alerts, overdue indicators, CTAs |
| Water Blue | #48BFE3 | Water-related UI elements |
| Background | #F8FAF8 | Main background |
| Card Background | #FFFFFF | Cards, modals |
| Text Primary | #1B2D1B | Headings, body text |
| Text Secondary | #6B7280 | Captions, subtitles |
| Success | #40916C | Completed tasks, healthy plants |
| Warning | #F4A261 | Overdue, needs attention |
| Error | #EF4444 | Toxic warnings, errors |
| Divider | #E5E7EB | Separators |

### Typography
| Style | Font | Size | Weight |
|-------|------|------|--------|
| Large Title | SF Pro Display | 34pt | Bold |
| Title 1 | SF Pro Display | 28pt | Bold |
| Title 2 | SF Pro Display | 22pt | Semibold |
| Title 3 | SF Pro Text | 20pt | Semibold |
| Headline | SF Pro Text | 17pt | Semibold |
| Body | SF Pro Text | 17pt | Regular |
| Callout | SF Pro Text | 16pt | Regular |
| Caption | SF Pro Text | 12pt | Regular |

### Spacing
- Base unit: 4pt
- Scale: 4, 8, 12, 16, 20, 24, 32, 40
- Card padding: 16pt
- Screen edge margin: 16pt
- Grid spacing (2-col): 12pt

### Corner Radius
- Cards: 16pt
- Buttons: 12pt
- Plant thumbnails: 12pt
- Tags/chips: 8pt

### Icons (SF Symbols)
- Today: house.fill
- Library: leaf.fill
- My Garden: square.grid.2x2.fill
- Calendar: calendar
- Guide: book.fill
- Water: drop.fill
- Light: sun.max.fill
- Humidity: humidity.fill
- Temperature: thermometer
- Toxic: exclamationmark.triangle.fill
- Search: magnifyingglass
- Plus: plus.circle.fill
- Checkmark: checkmark.circle.fill

---

## 6. App Store Metadata

- **Title:** Plant Parent - Care Guide
- **Subtitle:** Keep Your Plants Thriving
- **Keywords:** plant care,houseplant,plant guide,watering schedule,plant parent,indoor plants,plant identifier,garden care,plant reminder,house plant care
- **Description:** Your beautiful plant care companion. Never kill a houseplant again. Plant Parent gives you everything you need to keep your green friends thriving. PLANT LIBRARY: Browse 100+ houseplants with complete care guides. MY GARDEN: Build your personal plant collection. SMART WATERING SCHEDULE: Personalized watering schedule for each plant. CARE CALENDAR: Weekly and monthly views of all plant care tasks. CARE GUIDE: 20+ articles on essential plant care. NO SUBSCRIPTIONS: Pay nothing. No ads.
- **Promotional Text:** 100+ plants, smart watering schedules, and care guides. All free, no subscriptions.
- **What's New (v1.0):** Initial release. Your beautiful plant care companion is here.
- **Screenshots needed:**
  1. Today screen with plants needing water
  2. Plant Library grid view
  3. Plant Detail screen with care info
  4. My Garden collection view
  5. Care Calendar week view
- **App Category:** Primary: Lifestyle, Secondary: Reference
- **Age Rating:** 4+
- **Privacy:** No data collected. All data stored on-device. No tracking.

---

## 7. Build Instructions

### Framework & Dependencies
- SwiftUI (no third-party dependencies)
- SF Symbols for all icons
- Core Data for garden storage
- UserDefaults for settings

### Minimum Xcode Version
- Xcode 15.0

### Build Order
1. **Project setup:** Create SwiftUI project, iOS 16 minimum, Core Data stack
2. **Data layer:** Create bundled JSON (plants database, articles). Create Core Data model (GardenPlant).
3. **Plant Library:** Build grid view with search and filters. Build Plant Detail screen.
4. **My Garden:** Build garden grid view. Build Add to Garden modal. Implement plant count limit (10 free).
5. **Watering Schedule:** Build Today screen with watering due list. Implement watering logic (mark watered → reschedule).
6. **Care Calendar:** Build week/month views. Implement task list for selected day.
7. **Care Guide:** Build article list and reading view.
8. **Polish:** Add haptic feedback, empty states, app icon, dark mode.

### Testing Checklist
- [ ] Plant library displays all 100+ plants
- [ ] Search filters correctly by name
- [ ] Category filters work (Beginner, Low Light, etc.)
- [ ] Adding plant to garden works
- [ ] Watering due calculation is correct
- [ ] Marking as watered reschedules correctly
- [ ] Seasonal adjustment reduces frequency in winter
- [ ] Calendar shows correct tasks
- [ ] Free tier limits at 10 plants
- [ ] App works in airplane mode
- [ ] Data persists across launches
- [ ] No crashes on iPhone SE (3rd gen)

### Estimated Build Time
2.5-3 hours
