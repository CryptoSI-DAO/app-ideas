# High Speed Hair Dryer App Requirements

## 1. App Specification
- **App Name**: High Speed Hair Dryer
- **Bundle ID Suggestion**: com.cryptoai.hairdryerpro
- **Target Platform**: iOS (minimum iOS version 16.0)
- **Orientation**: Portrait
- **Minimum Device**: iPhone SE through iPhone 15 Pro Max

## 2. Feature Breakdown
| Feature | User Story | Acceptance Criteria | Priority | Dependencies | Complexity |
|---------|------------|---------------------|----------|--------------|------------|
| Hair Dryer Types Guide | As a user, I want to learn about different high-speed hair dryer technologies so that I can choose the right one for my hair type. | - Display list of dryer types (ionic, ceramic, tourmaline, etc.) with descriptions.<br>- Include pros/cons and best use cases.<br>- Allow filtering by hair type (fine, thick, curly, color-treated). | P0 | None | L |
| Heat & Speed Settings Guide | As a user, I want to understand optimal heat and speed settings for my hair so that I can avoid damage and achieve desired style. | - Interactive chart showing recommended settings based on hair type and goal (dry, smooth, voluminous).<br>- Explain effects of high heat vs. low heat.<br>- Warn about heat damage risks. | P0 | None | L |
| Drying Timer & Tips | As a user, I want to time my drying sessions and get tips so that I can dry my hair efficiently without over-drying. | - Start/stop timer for drying sessions.<br>- Show elapsed time and suggest when to lower heat.<br>- Display rotating tips (e.g., "Use cool shot to set style"). | P1 | None | L |
| Style Tutorials | As a user, I want to follow step-by-step tutorials for popular hairstyles so that I can achieve salon-like results at home. | - Video-less tutorials with images and text for styles like blowout, curls, straightening.<br>- List required tools (brush, comb) and products.<br>- Mark steps as completed. | P1 | None | L |
| Product Recommendations | As a user, I want to see recommended high-speed hair dryers so that I can make an informed purchase. | - List of top-rated dryers with key features and prices.<br>- Link to retailer sites (affiliate links disclaimed).<br>- Allow sorting by price, rating, or features. | P2 | None | L |

## 3. Screen-by-Screen Specification
### Home Screen
- **Purpose**: Navigate to different sections of the app.
- **Layout**:
  - Header: App title.
  - Content: Grid of feature icons and labels (Guide, Settings, Timer, Tutorials, Products).
  - Footer: Tab bar (not used in this simple app; we'll use bottom navigation bar with 5 items).
- **Elements**:
  - Header: Title (Text)
  - Feature Item: Icon (SF Symbols), Label (Text)
  - Tab Bar: 5 items (Home, Guide, Timer, Tutorials, Products) – but we'll implement as a single view with sections for simplicity.
- **Interactions**:
  - Tap Feature Item: Navigate to corresponding section.
- **Data**:
  - Displayed: Static text and icons.
  - Source: Hardcoded in SwiftUI.
- **Navigation**:
  - Get here: Launch app.
  - Go next: To selected section.

### Guide Screen (Hair Dryer Types & Settings)
- **Purpose**: Educate user on dryer technologies and optimal settings.
- **Layout**:
  - Header: Title and back button.
  - Content: Two tabs: Dryer Types and Settings Guide.
  - No footer tab bar (we'll use navigation view).
- **Elements**:
  - Header: Back Button (Button), Title (Text)
  - Dryer Types Tab: List of dryer types, each with name, icon, description, pros/cons.
  - Settings Guide Tab: Interactive picker for hair type and goal, showing recommended heat/speed settings.
- **Interactions**:
  - Tap Back Button: Return to Home.
  - Tap dryer type: Show detailed view (optional, for simplicity we'll keep list).
  - Change picker: Update settings display.
- **Data**:
  - Displayed: Dryer type names, descriptions, icons; recommended settings.
  - Source: Bundled JSON data.
- **Navigation**:
  - Get here: From Home (tap Guide).
  - Go next: Back to Home.

### Timer Screen
- **Purpose**: Time drying sessions and receive tips.
- **Layout**:
  - Header: Title and back button.
  - Content: Large timer display, start/pause/reset buttons, tip label.
  - No footer.
- **Elements**:
  - Header: Back Button (Button), Title (Text)
  - Timer Display: Large Text showing MM:SS
  - Buttons: Start/Pause (Button), Reset (Button)
  - Tip Label: Text (rotating tips array)
- **Interactions**:
  - Tap Start/Pause: Begin or pause timer.
  - Tap Reset: Reset timer to 00:00.
  - Timer ticks: Update display and show new tip every 30 seconds.
- **Data**:
  - Displayed: Elapsed time, current tip.
  - Source: Timer state, tips array.
- **Navigation**:
  - Get here: From Home (tap Timer).
  - Go next: Back to Home.

### Tutorials Screen
- **Purpose**: View step-by-step hairstyle tutorials.
- **Layout**:
  - Header: Title and back button.
  - Content: List of tutorials, each with thumbnail, title, and difficulty.
  - Tapping a tutorial shows step-by-step steps.
- **Elements**:
  - Header: Back Button (Button), Title (Text)
  - Tutorial Item: Thumbnail (Image), Title (Text), Difficulty (Text)
  - Tutorial Detail Screen: Step number, image description (placeholder), text description.
- **Interactions**:
  - Tap Back Button: Return to Home.
  - Tap Tutorial Item: Navigate to tutorial detail.
  - Tap Next/Previous Step: Navigate through steps.
- **Data**:
  - Displayed: Tutorial metadata and step details.
  - Source: Bundled JSON data (images as assets, but we'll use placeholder text descriptions for MVP).
- **Navigation**:
  - Get here: From Home (tap Tutorials).
  - Go next: To Tutorial Detail (tap item), Back to Home.

### Products Screen
- **Purpose**: Show recommended high-speed hair dryers.
- **Layout**:
  - Header: Title and back button.
  - Content: List of products, each with image, name, rating, price, and key features.
  - Tapping a product shows more details.
- **Elements**:
  - Header: Back Button (Button), Title (Text)
  - Product Item: Thumbnail (Image), Name (Text), Rating (Stars), Price (Text), Features (Text list)
  - Product Detail Screen: Full description, more features, link to retailer (opens Safari).
- **Interactions**:
  - Tap Back Button: Return to Home.
  - Tap Product Item: Navigate to product detail.
  - Tap retailer link: Open URL in Safari.
- **Data**:
  - Displayed: Product name, rating, price, features, image.
  - Source: Bundled JSON data (affiliate links as strings).
- **Navigation**:
  - Get here: From Home (tap Products).
  - Go next: To Product Detail (tap item), Back to Home.

## 4. Data Model
### Hair Dryer Type (bundled JSON)
```json
[
  {
    "id": "type_001",
    "name": "Ionic Hair Dryer",
    "description": "Emits negative ions to break down water molecules, reducing drying time and frizz.",
    "pros": ["Faster drying", "Less frizz", "Shinier hair"],
    "cons": ["Can be more expensive", "Ionic effect may diminish over time"],
    "bestFor": ["Fine hair", "Thick hair", "Frizz-prone hair"]
  },
  {
    "id": "type_002",
    "name": "Ceramic Hair Dryer",
    "description": "Uses ceramic heating elements for even heat distribution, reducing hot spots.",
    "pros": ["Even heat", "Gentle on hair", "Affordable"],
    "cons": ["May take longer to dry than ionic", "Ceramic coating can chip"],
    "bestFor": ["All hair types", "Color-treated hair", "Daily use"]
  }
]
```

### Heat/Speed Settings Recommendation (bundled JSON)
```json
{
  "settings": {
    "fine": {
      "dry": { "heat": "low", "speed": "low" },
      "smooth": { "heat": "medium", "speed": "medium" },
      "voluminous": { "heat": "medium", "speed": "high" }
    },
    "thick": {
      "dry": { "heat": "high", "speed": "high" },
      "smooth": { "heat": "high", "speed": "medium" },
      "voluminous": { "heat": "high", "speed": "high" }
    }
  }
}
```

### Timer State (in-memory)
```json
{
  "isRunning": false,
  "startTime": null,
  "elapsedTime": 0,
  "lastTipUpdate": null
}
```

### Tutorial (bundled JSON)
```json
[
  {
    "id": "tut_001",
    "title": "Classic Blowout",
    "difficulty": "Intermediate",
    "steps": [
      { "description": "Towel-dry hair until damp, not wet." },
      { "description": "Apply heat protectant serum." },
      { "description": "Section hair into 4 parts." },
      { "description": "Using round brush, dry each section from roots to ends with medium heat." },
      { "description": "Finish with cool shot to set style." }
    ]
  }
]
```

### Product (bundled JSON)
```json
[
  {
    "id": "prod_001",
    "name": "Dyson Supersonic™ Hair Dryer",
    "rating": 4.7,
    "price": "$429.99",
    "features": ["Fast drying", "Intelligent heat control", "Magnetic attachments"],
    "description": "Engineered for fast drying and precise styling.",
    "affiliateLink": "https://example.com/dyson-supersonic"
  }
]
```

## 5. Design Tokens
- **Colors**:
  - Primary: #FF6B6B (coral)
  - Secondary: #FFD166 (yellow)
  - Accent: #06D6A0 (green)
  - Background: #FFF9F0 (very light peach)
  - Text: #2E294E (dark purple)
  - Success: #06D6A0
  - Warning: #FF9F1C (orange)
  - Error: #EF233C (pink)
- **Typography**:
  - Font Family: SF Pro Display
  - H1: 34pt, weight Bold
  - H2: 24pt, weight SemiBold
  - Body: 17pt, weight Regular
  - Caption: 12pt, weight Regular
- **Spacing**:
  - Base unit: 8pt
  - Padding/Margin: 8, 16, 24, 32, 48
- **Corner Radius**:
  - Card: 12pt
  - Button: 8pt
  - Input: 8pt
- **Shadows**:
  - Card: offset x=0, y=2, blur=8, opacity=0.1
  - Button: offset x=0, y=1, blur=3, opacity=0.2
- **Icons**: SF Symbols
  - Guide: book.fill
  - Timer: timer
  - Tutorials: video.fill
  - Products: cart.fill
  - Heat: thermometer
  - Speed: gauge.medium
  - Hair: face.smiling

## 6. App Store Metadata
- **Title**: High Speed Hair Dryer (22 chars)
- **Subtitle**: Guides, Timer & Tutorials (30 chars)
- **Keywords**: hair dryer, styling, tutorial, timer, tips, heat settings, ionic, ceramic, blowout, hair care (96 chars)
- **Description**: 
  High Speed Hair Dryer is your complete guide to mastering fast drying techniques without damaging your hair. Learn about different dryer technologies (ionic, ceramic, tourmaline) and find the perfect settings for your hair type and style goals. Use the built-in timer to avoid over-drying and get helpful tips throughout your session. Follow step-by-step tutorials for popular hairstyles like blowouts, curls, and straightening. Get product recommendations for top-rated high-speed dryers. All content is available offline – no internet connection required.
- **Promotional Text**: Learn to dry your hair faster and safer with expert guides and tools.
- **What's New**: Initial release with dryer guides, settings recommendations, drying timer, tutorials, and product suggestions.
- **Screenshots Needed**: 
  1. Home screen with feature grid
  2. Guide screen showing dryer types and settings picker
  3. Timer screen with active timer and tips
  4. Tutorials screen and tutorial detail
  5. Products screen showing recommended dryers
- **App Category**: Lifestyle (primary), Health & Fitness (secondary)
- **Age Rating**: 4+
- **Privacy**: No data collected (all data bundled, no networking, no user data stored beyond app state in memory)

## 7. Build Instructions
- **Framework**: SwiftUI
- **Dependencies**: None (Swift standard library + SF Symbols)
- **Data**: Bundled JSON files in app bundle for all static content.
- **Minimum Xcode Version**: 15.0
- **Build Order**:
  1. Create data model structs for dryer types, settings, timer, tutorials, products.
  2. Create bundled JSON files and load them at startup.
  3. Build Home screen with navigation to sections.
  4. Build Guide screen with tabs for dryer types and settings guide.
  5. Build Timer screen with start/pause/reset logic and rotating tips.
  6. Build Tutorials screen with list and detail view.
  7. Build Products screen with list and detail view.
  8. Implement navigation between screens.
  9. Add App Store metadata and icons.
  10. Test in simulator on various iPhone sizes.
- **Testing Checklist**:
  - [ ] Home screen loads and shows feature grid.
  - [ ] Guide screen shows dryer types and settings picker.
  - [ ] Changing hair type and goal updates recommended settings.
  - [ ] Timer starts, pauses, and resets correctly.
  - [ ] Timer updates tip every 30 seconds.
  - [ ] Tutorials list loads and tapping a tutorial shows steps.
  - [ ] Products list loads and tapping a product shows details.
  - [ ] All content is accessible offline (disable network and verify).
  - [ ] App respects portrait orientation only.
  - [ ] No network requests are made.
  - [ ] App builds and runs on iPhone SE (2nd gen) and iPhone 15 Pro Max simulators.

## 8. Multi-Platform Companion Specs (Android)
When building for Android, generate a separate `requirements-android.md` file with the following adaptations:
- **applicationId**: com.cryptoai.hairdryerpro (matches iOS bundle ID)
- **Stack**: Kotlin 2.x + Jetpack Compose + Material 3, minSdk 26 / targetSdk 35
- **Shared content JSONs**: copied byte-for-byte into `assets/`; never edit locally — report content issues instead.
- **Platform-mapping table**:
  - iOS UserDefaults → Android SharedPreferences (not used in this app, all data bundled)
  - iOS SF Symbols → Android Material Icons (guide: menu_book, timer: timer, tutorials: video_library, products: shopping_cart)
  - iOS SF Pro Rounded → Android system Roboto font
  - iOS drop shadows → Android tonal elevation 2dp
  - iOS bundled JSON → Android via `assets.open()` and parsing
- **Extra Android acceptance criteria**:
  - Process-death persistence: not applicable (no user data stored beyond transient state).
  - Predictive-back pop order: works correctly with Compose navigation.
  - Usable at 200% font scale: layouts adapt to large text sizes.
  - Zero `<uses-permission>` entries: manifest declares no permissions for offline privacy claim.
- **Play Store metadata**:
  - Title: High Speed Hair Dryer (30 chars)
  - Short displays: Guides, timer & tutorials (80 chars)
  - Description: Reuse iOS description if ≤4000 chars (it is).
  - Data Safety form: "No data collected" matches permission-free manifest.
  - Content rating: Everyone expected.
  - Screenshots: same as iOS, minimum 2.
- **Estimated build time**: ~+0.5h vs iOS build (Compose overhead).

## 9. PWA Decision Rule
Not applicable for paid utility app. Instead, specify a static landing page (~1h, free hosting) with:
- **Purpose**: Free interactive top-of-funnel tool ONLY (e.g., "Hair Dryer Quiz" – helps users identify their dryer needs).
- **Core product locked behind store links**.
- **Landing page doubles as App Store "marketing URL" field value**.
- **Tech stack**: Next.js 15 (App Router, TS, Tailwind, `output:'export'`), Vercel free.
- **Sequenced AFTER the iOS and Android apps ship** (store badges need live URLs).

**Agent guardrails**: 
- Author all entries explicitly; no placeholders.
- Localization-ready strings from day 1.
- No brand names in UI or store body copy.
- Total estimated build time ≤ 3 hours (iOS: ~2.0h, Android: ~2.5h).