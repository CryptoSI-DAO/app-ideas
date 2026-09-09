# Low Rise Sweatpants

## 1. App Specification
- **App name**: Low Rise Sweatpants
- **Bundle ID suggestion**: com.lisa.low-rise-sweatpants
- **Target platform**: iOS (minimum iOS 16)
- **Orientation**: Portrait
- **Minimum device**: iPhone SE through iPhone 15 Pro Max

## 2. Feature Breakdown
### Feature 1: Core Functionality
- **User Story**: As a user interested in Low Rise Sweatpants, I want to easily access information and tools related to Low Rise Sweatpants so that I can stay informed and productive.
- **Acceptance Criteria**: 
  - The app loads and displays relevant Low Rise Sweatpants information within 2 seconds.
  - Users can perform the core Low Rise Sweatpants-related action with no more than 3 taps.
  - All data is displayed accurately and up-to-date.
- **Priority**: P0
- **Dependencies**: None (bundled data or on-device calculations)
- **Complexity**: M

### Feature 2: Settings & Preferences
- **User Story**: As a user, I want to customize the app to my preferences so that the experience is tailored to my needs.
- **Acceptance Criteria**:
  - Settings screen is accessible from the main menu.
  - Users can toggle at least 3 different preferences.
  - Preferences persist across app launches.
- **Priority**: P1
- **Dependencies**: None
- **Complexity**: S

## 3. Screen-by-Screen Specification
### Screen 1: Home Screen
- **Purpose**: Display the main Low Rise Sweatpants information and entry points to core features.
- **Layout**: Standard iOS layout with navigation bar at top, tab bar at bottom (if multiple tabs), or single view.
- **Elements**:
  - Title label: "Low Rise Sweatpants"
  - Main content area showing Low Rise Sweatpants data or tool
  - Button to access core feature
  - Button to access settings
- **Interactions**:
  - Tap core feature button → navigates to Core Feature Screen
  - Tap settings button → navigates to Settings Screen
- **Data**: Displays current Low Rise Sweatpants information (either bundled or computed on-device)
- **Navigation**: 
  - Entry point: App launch
  - Exits: To Core Feature Screen, Settings Screen

### Screen 2: Core Feature Screen
- **Purpose**: Allow the user to perform the main Low Rise Sweatpants-related action.
- **Layout**: Focused view with input fields and action button.
- **Elements**:
  - Input fields relevant to Low Rise Sweatpants (e.g., text entry, selectors, etc.)
  - Primary action button (e.g., "Calculate", "Scan", "Track")
  - Results display area
- **Interactions**:
  - Tap action button → processes input and displays results
  - Tap outside input → dismiss keyboard
- **Data**: Takes user input, processes it, displays output
- **Navigation**:
  - Entry point: From Home Screen via core feature button
  - Exits: Back to Home Screen

### Screen 3: Settings Screen
- **Purpose**: Allow users to customize app behavior and preferences.
- **Layout**: List-style settings screen.
- **Elements**:
  - Toggle switches for various options
  - Slider for adjustable settings
  - Text field for user input (if needed)
- **Interactions**:
  - Toggle switch → immediately updates setting
  - Slider → updates setting in real-time
  - Text field → saves on return key or when focus leaves
- **Data**: Stores user preferences in UserDefaults
- **Navigation**:
  - Entry point: From Home Screen via settings button
  - Exits: Back to Home Screen

## 4. Data Model
- **Entity**: TopicData
  - Fields:
    - id: String (unique identifier)
    - title: String
    - description: String
    - value: Double (if applicable)
    - timestamp: Date (when data was relevant)
  - Sample data (3 items):
    - id: "001", title: "Sample Low Rise Sweatpants Item 1", description: "First sample item for Low Rise Sweatpants", value: 42.5, timestamp: "2026-09-08T10:00:00Z"
    - id: "002", title: "Sample Low Rise Sweatpants Item 2", description: "Second sample item for Low Rise Sweatpants", value: 38.2, timestamp: "2026-09-08T11:00:00Z"
    - id: "003", title: "Sample Low Rise Sweatpants Item 3", description: "Third sample item for Low Rise Sweatpants", value: 45.1, timestamp: "2026-09-08T12:00:00Z"
- **Data source**: Bundled JSON in the app bundle (data/topic_data.json)
- **Relationships**: None (standalone entities)

## 5. Design Tokens
- **Colors**:
  - Primary: #FF6B6B (a vibrant red)
  - Secondary: #4ECDC4 (a teal accent)
  - Background: #FFFFFF (white)
  - Text: #333333 (dark gray)
  - Success: #6BCB77 (green)
  - Warning: #FFD93D (yellow)
  - Error: #FF6B6B (red, same as primary for simplicity)
- **Typography**:
  - Font family: SF Pro Rounded (system font)
  - h1: 34pt, weight Bold
  - h2: 24pt, weight SemiBold
  - body: 17pt, weight Regular
  - caption: 12pt, weight Regular
- **Spacing**:
  - Base unit: 8 points
  - Padding/margin: 8, 16, 24, 32 points (multiples of base unit)
- **Corner radius**:
  - Card radius: 12 points
  - Button radius: 8 points
  - Input radius: 6 points
- **Shadows**:
  - Card shadow: offset x=0, y=2, blur=4, opacity=0.25
  - Button shadow: offset x=0, y=1, blur=2, opacity=0.15
- **Icons**: 
  - Use SF Symbols: for core feature, use "doc.text.magnifyingglass" (or appropriate symbol based on topic)

## 6. App Store Metadata
- **Title**: Low Rise Sweatpants
- **Subtitle**: Essential Low Rise Sweatpants Tool
- **Keywords**: Low Rise Sweatpants, tool, guide, reference, utility (example, must be under 100 chars)
- **Description**: Discover the ultimate Low Rise Sweatpants companion app. Designed for enthusiasts and professionals, this app provides instant access to essential Low Rise Sweatpants information, tools, and resources. With a clean, intuitive interface and powerful features, you'll stay ahead in the world of Low Rise Sweatpants. Whether you're a beginner or an expert, this app is your go-to reference for all things Low Rise Sweatpants.
- **Promotional text**: Your essential Low Rise Sweatpants companion.
- **What's New**: Initial release with core Low Rise Sweatpants features and tools.
- **Screenshots needed**: 
  1. Home screen showing main Low Rise Sweatpants information
  2. Core feature screen in action
  3. Settings screen showing customization options
- **App Category**: 
  - Primary: Utilities
  - Secondary: Reference (if applicable) or Lifestyle
- **Age Rating recommendation**: 4+ (no questionable content)
- **Privacy**: No data collected (fully on-device, no networking required)

## 7. Build Instructions
For the coding agent receiving this document:
- Use SwiftUI for iOS development.
- No third-party dependencies (prefer Swift standard library + SF Symbols).
- Bundle the sample data as JSON in the app bundle at `Resources/data/topic_data.json`.
- Minimum Xcode version: 15.0
- Step-by-step build order:
  1. Set up the project and app structure.
  2. Create the data model and bundle the sample data.
  3. Implement the Home Screen with navigation.
  4. Implement the Core Feature Screen with user interactions.
  5. Implement the Settings Screen with persistence.
  6. Integrate design tokens and styling.
  7. Test in simulator on various device sizes.
  8. Prepare App Store metadata and screenshots.
- Testing checklist:
  - [ ] App launches without crashes on iPhone SE and iPhone 15 Pro Max simulators.
  - [ ] Core feature produces correct results for sample inputs.
  - [ ] Settings persist across app launches.
  - [ ] All text is legible and properly aligned.
  - [ ] App Store metadata is complete and within character limits.

## 8. Multi-Platform Companion Specs (Android)
When the user asks for an Android version, generate a SEPARATE `requirements-android.md` companion doc.
- **applicationId**: com.lisa.low-rise-sweatpants
- **Stack**: Kotlin 2.x + Jetpack Compose + Material 3, minSdk 26 / targetSdk 35, portrait locked, androidx-only.
- **Include a platform-mapping table**: UserDefaults→SharedPreferences, SF Symbols→Material Icons, SF Pro Rounded→system Roboto.
- **Extra Android acceptance criteria**: process-death persistence, usable at 200% font scale, zero `<uses-permission>` entries.
- **Play metadata differs**: title 30 chars, short description 80 chars, Data Safety form ("no data collected"), content-rating questionnaire → Everyone expected.

## 9. PWA Decision Rule
Default answer for paid apps is NO full PWA — a free web clone cannibalizes the $ price. Instead spec a static landing page (~1h, free hosting): free interactive top-of-funnel tool ONLY (e.g., the checklist — catches buyers mid-purchase-decision), core product locked behind store links.

