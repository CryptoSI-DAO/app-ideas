# Requirements Document: Sobriety Tracker+

*Generated: 2026-06-11*
*Version: 1.0*

---

## 1. App Specification

- **App Name:** Sobriety Tracker+
- **Bundle ID:** com.lisakim.sobrietytracker
- **Target Platform:** iOS 16.0+
- **Orientation:** Portrait only
- **Minimum Device:** iPhone SE (3rd gen) through iPhone 15 Pro Max

---

## 2. Feature Breakdown

### F1: Sobriety Clock
- **User Story:** As a person in recovery, I want to see exactly how long I've been sober so that I feel proud of my progress.
- **Acceptance Criteria:**
  - Displays days, hours, minutes, seconds since sobriety start date
  - Updates in real-time (every second)
  - Start date is customizable (can be set to any past date)
  - Large, prominent display on home screen
  - Tap to show additional stats (total hours, total days)
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** S

### F2: Milestone Tracker
- **User Story:** As a user, I want to see upcoming milestones and celebrate achieved ones so that I stay motivated.
- **Acceptance Criteria:**
  - Pre-loaded milestones: 24h, 3d, 1w, 2w, 1m, 3m, 6m, 1y, 2y, 5y, 10y
  - Each milestone shows: date achieved, days to go (for future ones)
  - Celebration animation (confetti) when milestone is reached
  - Custom milestones can be added with name and date
  - Milestone timeline view (past → future)
- **Priority:** P0
- **Dependencies:** F1 (Sobriety Clock)
- **Complexity:** M

### F3: Daily Motivation
- **User Story:** As a user, I want to see a new motivational message each day so that I feel supported.
- **Acceptance Criteria:**
  - One quote/affirmation shown per day on home screen
  - 365+ bundled quotes (different quote each day, cycles yearly)
  - Pull-to-refresh shows a random new quote
  - Quotes are recovery-focused, encouraging, non-religious
  - Text is shareable (long press → copy)
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** S

### F4: Habit Builder
- **User Story:** As a user, I want to track daily healthy habits alongside my sobriety so that I build a recovery lifestyle.
- **Acceptance Criteria:**
  - Pre-loaded habits: Drink water, Exercise, Meditate, Journal, Call a friend, Read, Sleep 8h
  - Add custom habits with name and icon
  - Daily checklist — tap to mark complete
  - Streak tracking per habit (consecutive days)
  - Today view shows all habits with completion status
  - Maximum 12 habits in free version, unlimited in premium
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** M

### F5: Progress Dashboard
- **User Story:** As a user, I want to visualize my progress over time so that I can see how far I've come.
- **Acceptance Criteria:**
  - Money saved: user inputs daily spend → shows cumulative savings (weekly/monthly/total)
  - Habit completion rate: bar chart showing % completion per week (last 4 weeks)
  - Health milestones: pre-loaded timeline ("After 1 week: sleep improves", "After 1 month: liver fat decreases", etc.)
  - All data shown in cards, no complex graphs
- **Priority:** P0
- **Dependencies:** F1, F4
- **Complexity:** M

### F6: Privacy Lock
- **User Story:** As a user, I want my sobriety data to be private so that nobody can see it without my permission.
- **Acceptance Criteria:**
  - App requires Face ID or device passcode on launch
  - No account creation, no email, no sign-up
  - All data stored locally on device
  - Toggle for privacy lock in settings
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** S

### F7: Settings
- **User Story:** As a user, I want to configure the app to my preferences.
- **Acceptance Criteria:**
  - Set/change sobriety start date
  - Toggle privacy lock on/off
  - Daily motivation: on/off
  - Money per day input (for savings calculator)
  - Theme: Light / Dark / System
  - App version display
- **Priority:** P0
- **Dependencies:** F1, F5, F6
- **Complexity:** S

---

## 3. Screen-by-Screen Specification

### Screen: Home
- **Purpose:** Primary view — shows sobriety clock, daily quote, and quick access to habits
- **Layout:** 
  - Header: "Sober for" label
  - Center: Large sobriety clock (days.hours:minutes:seconds)
  - Below clock: Daily quote card (rounded rectangle, light background)
  - Below quote: "Today's Habits" section — horizontal scroll of habit circles (completed = filled, incomplete = outline)
  - Bottom: Tab bar
- **Elements:**
  - Sobriety clock label (text, large, bold)
  - Days/hours/minutes/seconds text fields (monospaced font)
  - Quote text (centered, italic)
  - Author text (small, right-aligned)
  - Habit circles (circular progress indicators, tap to complete)
  - Tab bar (4 items: Home, Habits, Progress, Settings)
- **Interactions:**
  - Tap sobriety clock → shows detailed stats overlay
  - Pull-to-refresh on quote → loads new random quote
  - Tap habit circle → toggles completion, plays haptic feedback
- **Days data:** Computed from start date stored in UserDefaults
- **Navigation:** Root screen, accessed via Home tab

### Screen: Habits
- **Purpose:** View and manage all daily habits
- **Layout:**
  - Header: "Today's Habits" title
  - Content: Vertical list of habit cards
  - Footer: "+" floating action button
- **Elements:**
  - Habit name (text)
  - Habit icon (SF Symbol)
  - Completion checkbox (circular, large tap target)
  - Streak counter (small badge, e.g., "🔥 7 day streak")
  - FAB: "+" button (bottom right, floating)
- **Interactions:**
  - Tap checkbox → toggles completion, plays haptic, updates streak
  - Swipe left on habit → delete option
  - Tap "+" → opens Add Habit screen
  - Long press habit → edit habit
- **Data:** Habits array from Core Data, filtered by today's date
- **Navigation:** Tab bar → Habits tab. "+" → Add Habit modal

### Screen: Add Habit
- **Purpose:** Create a new habit
- **Layout:** Modal sheet
  - Header: "New Habit" title + Cancel/Done buttons
  - Content: Form fields
- **Elements:**
  - Habit name text field (placeholder: "e.g., Drink 8 glasses of water")
  - Icon picker (grid of 20 SF Symbols to choose from)
  - Pre-loaded suggestions section (scrollable chips: "Drink water", "Exercise", "Meditate", etc.)
  - Cancel button, Done button (Done disabled until name entered)
- **Interactions:**
  - Type name → Done button enables
  - Tap suggestion → auto-fills name and icon
  - Tap Done → saves habit, dismisses modal
  - Tap Cancel → discards, dismisses modal
- **Data:** Saves to Core Data habits entity
- **Navigation:** Modal from Habits screen

### Screen: Progress
- **Purpose:** View all progress stats and charts
- **Layout:** Scrollable vertical stack
  - Section 1: Money saved card
  - Section 2: Habit completion chart
  - Section 3: Health milestones timeline
- **Elements:**
  - Money card: Large "$X" total saved, "+$X this week" subtitle
  - Habit chart: Simple bar chart (4 weeks, each bar shows % completion)
  - Health timeline: Vertical milestone list with checkmarks
  - Section headers (text)
- **Interactions:**
  - Scroll to see all sections
  - Tap health milestone → shows detail description
- **Data:** Computed from Core Data habit completion records and UserDefaults settings
- **Navigation:** Tab bar → Progress tab

### Screen: Milestones
- **Purpose:** View milestone timeline
- **Layout:** Vertical timeline
- **Elements:**
  - Milestone cards: date, name, "achieved" badge or "X days to go"
  - Timeline line connecting milestones
  - Add custom milestone button
- **Interactions:**
  - Scroll through timeline
  - Tap "+" → Add Milestone modal
  - Achieved milestones have confetti animation on first view
- **Data:** Pre-loaded milestones + custom milestones from Core Data
- **Navigation:** Navigation link from Progress screen

### Screen: Settings
- **Purpose:** Configure app settings
- **Layout:** Grouped list (iOS Settings style)
- **Elements:**
  - Sobriety start date (date picker row)
  - Privacy lock toggle (switch)
  - Daily motivation toggle (switch)
  - Money per day (number input)
  - Theme picker (segmented control: Light/Dark/System)
  - "Unlock Premium" button (if not purchased)
  - App version text (footer)
- **Interactions:**
  - Date picker → updates sobriety start date → refreshes home screen
  - Toggles → immediate effect
  - Theme picker → immediately changes appearance
- **Data:** UserDefaults for all settings
- **Navigation:** Tab bar → Settings tab

---

## 4. Data Models

### UserSettings
```swift
struct UserSettings {
    var sobrietyStartDate: Date
    var isPrivacyLockEnabled: Bool
    var isDailyMotivationEnabled: Bool
    var moneyPerDay: Double
    var theme: AppTheme // enum: light, dark, system
    var isPremiumUnlocked: Bool
}
```

### Habit
```swift
struct Habit: Identifiable, Codable {
    let id: UUID
    var name: String
    var iconName: String // SF Symbol name
    var createdDate: Date
    var completions: [Date] // Array of completion dates
    var isActive: Bool
    
    var currentStreak: Int {
        // Computed: count consecutive days from today backwards
    }
    
    var isCompletedToday: Bool {
        // Computed: check if today's date is in completions
    }
}
```

### Milestone
```swift
struct Milestone: Identifiable, Codable {
    let id: UUID
    var name: String // e.g., "1 Month Sober"
    var daysRequired: Int // e.g., 30
    var isCustom: Bool
    var achievedDate: Date?
}
```

### Sample Data (Pre-loaded Milestones)
```json
[
  {"name": "24 Hours", "daysRequired": 1},
  {"name": "3 Days", "daysRequired": 3},
  {"name": "1 Week", "daysRequired": 7},
  {"name": "2 Weeks", "daysRequired": 14},
  {"name": "1 Month", "daysRequired": 30},
  {"name": "3 Months", "daysRequired": 90},
  {"name": "6 Months", "daysRequired": 180},
  {"name": "1 Year", "daysRequired": 365},
  {"name": "2 Years", "daysRequired": 730},
  {"name": "5 Years", "daysRequired": 1825},
  {"name": "10 Years", "daysRequired": 3650}
]
```

### Sample Data (Pre-loaded Quotes)
```json
[
  {"text": "One day at a time. That's all you need to think about.", "author": "Unknown"},
  {"text": "Recovery is not a race. You don't have to feel guilty if it takes you longer than you thought it would.", "author": "Unknown"},
  {"text": "The journey of a thousand miles begins with a single step.", "author": "Lao Tzu"},
  {"text": "You are stronger than you think.", "author": "Unknown"},
  {"text": "Every day is a new chance to change your life.", "author": "Unknown"}
  // ... 360+ more quotes bundled
]
```

### Sample Data (Pre-loaded Habits)
```json
[
  {"name": "Drink 8 glasses of water", "iconName": "drop.fill"},
  {"name": "Exercise for 20 minutes", "iconName": "figure.run"},
  {"name": "Meditate for 5 minutes", "iconName": "sparkles"},
  {"name": "Write in journal", "iconName": "book.fill"},
  {"name": "Call or text a friend", "iconName": "message.fill"},
  {"name": "Read for 15 minutes", "iconName": "book.pages.fill"},
  {"name": "Get 8 hours of sleep", "iconName": "moon.fill"},
  {"name": "Take a walk outside", "iconName": "tree.fill"}
]
```

### Data Source
- All pre-loaded content: Bundled JSON files in app bundle
- User data: Core Data (habits, milestones) + UserDefaults (settings)
- No backend, no API, no internet required

---

## 5. Design Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #2D6A4F | Headers, buttons, active states |
| Secondary | #52B788 | Secondary buttons, progress bars |
| Accent | #F4A261 | Celebrations, achievements, CTAs |
| Background | #FAFAF8 | Main background |
| Card Background | #FFFFFF | Cards, modals |
| Text Primary | #1B1B1B | Headings, body text |
| Text Secondary | #6B7280 | Captions, subtitles |
| Success | #40916C | Checkmarks, completed states |
| Error | #EF4444 | Errors, destructive actions |
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
| Subhead | SF Pro Text | 15pt | Regular |
| Footnote | SF Pro Text | 13pt | Regular |
| Caption | SF Pro Text | 12pt | Regular |
| Clock | SF Pro Display | 48pt | Bold (monospaced digits) |

### Spacing
- Base unit: 4pt
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48
- Card padding: 16pt
- Screen edge margin: 16pt
- Section spacing: 24pt

### Corner Radius
- Cards: 16pt
- Buttons: 12pt
- Input fields: 10pt
- Habit circles: 50% (fully circular)

### Shadows
- Card shadow: offset (0, 2), blur 8, opacity 0.08
- Modal shadow: offset (0, 4), blur 16, opacity 0.12
- Button shadow: offset (0, 1), blur 4, opacity 0.1

### Icons (SF Symbols)
- Home: house.fill
- Habits: checkmark.circle.fill
- Progress: chart.bar.fill
- Settings: gearshape.fill
- Plus: plus
- Checkmark: checkmark.circle.fill
- Flame: flame.fill
- Water: drop.fill
- Exercise: figure.run
- Meditate: sparkles
- Journal: book.fill
- Message: message.fill
- Moon: moon.fill
- Tree: tree.fill

---

## 6. App Store Metadata

- **Title:** Sobriety Tracker+
- **Subtitle:** Days Count, You Matter
- **Keywords:** sobriety,tracker,recovery,sober,alcohol free,sobriety counter,sober tracker,day counter,motivation,habit tracker,sober living,addiction recovery
- **Description:** Your beautiful, private sobriety companion. Track every day, hour, and minute of your journey. Celebrate milestones. Build healthy habits. Stay motivated. SOBRIETY CLOCK: A real-time counter showing exactly how long you've been sober. DAILY MOTIVATION: Every day brings a new quote or recovery insight. HABIT BUILDING: Build a daily routine with simple habits. Track your streaks. PROGRESS DASHBOARD: See your journey visualized. Money saved. Health milestones. PRIVACY FIRST: No account needed. Face ID protection. FREE FOREVER CORE: Essential tracking features are free. No ads. No subscriptions.
- **Promotional Text:** Beautiful sobriety tracking with daily motivation and habit building. Free core features, always.
- **What's New (v1.0):** Initial release. Track your sobriety journey with a beautiful, private companion.
- **Screenshots needed:**
  1. Home screen with sobriety clock and daily quote
  2. Habits screen with checklist
  3. Progress dashboard with money saved
  4. Milestone timeline with celebration
  5. Settings screen
- **App Category:** Primary: Health & Fitness, Secondary: Lifestyle
- **Age Rating:** 17+ (alcohol/substance reference)
- **Privacy:** No data collected. All data stored on-device. No tracking.

---

## 7. Build Instructions

### Framework & Dependencies
- SwiftUI (no third-party dependencies)
- SF Symbols for all icons
- Core Data for habit/milestone storage
- UserDefaults for settings
- LocalAuthentication for Face ID

### Minimum Xcode Version
- Xcode 15.0

### Build Order
1. **Project setup:** Create new SwiftUI project, set minimum iOS 16, configure Core Data stack
2. **Data layer:** Create bundled JSON files (quotes, milestones, habit suggestions). Create Core Data models (Habit, Milestone). Create UserDefaults wrapper for settings.
3. **Home screen:** Build sobriety clock view with real-time timer. Add daily quote card. Add habit circles section.
4. **Habits screen:** Build habit list with checkboxes. Add Add Habit modal. Implement streak calculation.
5. **Progress screen:** Build money saved card. Build simple bar chart for habit completion. Build health milestones timeline.
6. **Milestones screen:** Build timeline view. Add celebration animation (confetti using SwiftUI particles or simple animation).
7. **Settings screen:** Build settings form with all controls.
8. **Privacy lock:** Implement LocalAuthentication on app launch.
9. **Polish:** Add haptic feedback, animations, dark mode support, app icon.

### Testing Checklist
- [ ] Sobriety clock updates in real-time
- [ ] Changing start date updates all calculations
- [ ] Habits can be added, completed, and deleted
- [ ] Streak calculation is accurate (including edge cases: timezone changes, missed days)
- [ ] Milestones show correct "days to go" and achieved status
- [ ] Money saved calculation is correct
- [ ] Privacy lock works with Face ID and passcode
- [ ] Dark mode renders correctly on all screens
- [ ] App works in airplane mode (no internet)
- [ ] Data persists across app launches
- [ ] No memory leaks or performance issues on iPhone SE (3rd gen)

### Estimated Build Time
2.5-3 hours

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | "Sober curious" movement sustained growth; seasonal peaks in Jan/Sep. Not a fad. |
| App Gap | 8/10 | Existing apps are dated, ad-heavy, or subscription-locked. Clear quality gap. |
| Build Simplicity | 9/10 | Pure local storage, no backend, no API. CRUD app with timer. Well within 3 hours. |
| Evergreen Potential | 9/10 | Sobriety/recovery is a permanent need. Seasonal spikes provide natural marketing moments. |
| Monetization | 7/10 | Free core + $4.99 one-time unlock is proven for health/wellness apps. |
| **Average** | **8.0/10** | |
