# Requirements Document: MicroHabit

*Generated: 2026-06-11*
*Version: 1.0*

---

## 1. App Specification

- **App Name:** MicroHabit - Tiny Habits
- **Bundle ID:** com.lisakim.microhabit
- **Target Platform:** iOS 16.0+
- **Orientation:** Portrait only
- **Minimum Device:** iPhone SE (3rd gen) through iPhone 15 Pro Max

---

## 2. Feature Breakdown

### F1: Tiny Habit Creator
- **User Story:** As a user, I want to create tiny habits with absurdly small commitments so that I can't fail.
- **Acceptance Criteria:**
  - Add habit with: name (e.g., "Do 2 pushups"), anchor (e.g., "After I brush my teeth"), frequency
  - Pre-loaded suggestions: 50+ tiny habits across 6 categories
  - Icon selection (20 SF Symbols)
  - Free tier: 5 habits. Premium: unlimited.
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** S

### F2: Today View
- **User Story:** As a user, I want to see and complete my habits for today with minimal friction.
- **Acceptance Criteria:**
  - List of today's habits with large checkboxes
  - One tap to complete → celebration animation (confetti)
  - Completed habits shown with strikethrough and green checkmark
  - Streak counter per habit (flame icon)
  - Empty state: encouraging message + "Add your first tiny habit"
- **Priority:** P0
- **Dependencies:** F1
- **Complexity:** S

### F3: Streak Tracking
- **User Story:** As a user, I want to see my streaks grow so that I feel motivated to maintain them.
- **Acceptance Criteria:**
  - Current streak displayed per habit (consecutive days completed)
  - Longest streak recorded
  - Visual flame icon that grows/brightens with streak length
  - Streak breaks clearly indicated (no punishment, just reset)
- **Priority:** P0
- **Dependencies:** F2
- **Complexity:** S

### F4: Tiny Habits Guide
- **User Story:** As a new user, I want to learn about the tiny habits method so I can use it effectively.
- **Acceptance Criteria:**
  - 12 bundled articles on tiny habits methodology
  - Topics: what are tiny habits, why they work, choosing anchors, troubleshooting, habit stacking
  - Clean reading view
  - Progress indicator (articles read)
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** S

### F5: Weekly Review
- **User Story:** As a user, I want to see my weekly completion rates so I can identify patterns.
- **Acceptance Criteria:**
  - Bar chart showing completion % per habit for last 7 days
  - Overall weekly completion rate
  - Simple, clean visualization (no complex analytics)
- **Priority:** P0
- **Dependencies:** F2
- **Complexity:** S

### F6: Habit Suggestions
- **User Story:** As a new user, I want inspiration for tiny habits to start with.
- **Acceptance Criteria:**
  - 50+ pre-loaded tiny habit suggestions
  - Categories: Health, Mindfulness, Learning, Productivity, Relationships, Creativity
  - Each suggestion shows: name, anchor example, category
  - Tap to add directly to habits
- **Priority:** P0
- **Dependencies:** None
- **Complexity:** S

---

## 3. Screen-by-Screen Specification

### Screen: Today
- **Purpose:** Primary view — see and complete today's habits
- **Layout:**
  - Header: "Today" + date + streak summary ("3 habits on fire 🔥")
  - Content: Vertical list of habit rows
  - Empty state: illustration + "Start small. Add your first tiny habit."
  - FAB: "+" button
  - Bottom: Tab bar
- **Elements:**
  - Habit row: checkbox (large, circular), habit name, anchor text (small, gray), streak badge (🔥 + number)
  - Completed state: green checkmark, strikethrough text, subtle celebration
  - FAB: "+" floating action button (bottom right)
  - Tab bar (3 items: Today, Guide, Review)
- **Interactions:**
  - Tap checkbox → completes habit, plays haptic + confetti animation, updates streak
  - Swipe left → delete/edit options
  - Tap "+" → Add Habit modal
  - Pull to refresh
- **Data:** Habits from Core Data, filtered by today's frequency setting
- **Navigation:** Root screen, Today tab

### Screen: Add Habit
- **Purpose:** Create a new tiny habit
- **Layout:** Modal sheet
  - Header: "New Tiny Habit" + Cancel/Done
  - Content: Form + suggestions
- **Elements:**
  - Habit name text field (placeholder: "e.g., Do 2 pushups")
  - Anchor text field (placeholder: "e.g., After I brush my teeth")
  - Icon picker (grid of 20 SF Symbols)
  - Frequency picker (segmented: Daily, Weekdays, Custom)
  - Suggestions section: scrollable chips of pre-loaded habits
  - Cancel/Done buttons
- **Interactions:**
  - Type name → Done enables
  - Tap suggestion → auto-fills all fields
  - Tap Done → saves, dismisses, returns to Today
- **Data:** Saves to Core Data
- **Navigation:** Modal from Today screen

### Screen: Habit Detail
- **Purpose:** View detailed stats for a single habit
- **Layout:** Detail view
- **Elements:**
  - Habit name (large)
  - Current streak (large flame + number)
  - Longest streak
  - Completion calendar (last 30 days, heat map style)
  - Created date
  - Edit/Delete buttons
- **Interactions:**
  - Tap edit → opens Edit Habit modal
  - Tap delete → confirmation alert
- **Data:** Core Data habit entity
- **Navigation:** Tap habit row → push to detail

### Screen: Guide
- **Purpose:** Read about tiny habits methodology
- **Layout:**
  - Header: "Tiny Habits Guide"
  - Content: List of article cards
- **Elements:**
  - Article card: title, short description, read indicator
  - Progress bar at top (X of 12 read)
- **Interactions:**
  - Tap article → opens reading view
  - Mark as read on scroll to bottom
- **Data:** Bundled JSON articles
- **Navigation:** Tab bar → Guide tab

### Screen: Article Reader
- **Purpose:** Read a care guide article
- **Layout:** Scrollable text view
- **Elements:**
  - Article title (large)
  - Article body (formatted text)
  - "Mark as Read" button (bottom)
  - Back button
- **Interactions:**
  - Scroll to read
  - Tap "Mark as Read" → updates progress
- **Data:** Bundled JSON
- **Navigation:** Push from Guide

### Screen: Review
- **Purpose:** View weekly completion stats
- **Layout:**
  - Header: "This Week"
  - Content: Bar chart + summary
- **Elements:**
  - Bar chart: one bar per habit, height = completion % (last 7 days)
  - Overall completion rate (large number)
  - Encouraging message based on performance
  - Week navigation (previous/next arrows)
- **Interactions:**
  - Swipe or tap arrows to change week
  - Tap bar → shows habit detail
- **Data:** Computed from Core Data completion records
- **Navigation:** Tab bar → Review tab

---

## 4. Data Models

### Habit
```swift
struct Habit: Identifiable, Codable {
    let id: UUID
    var name: String // e.g., "Do 2 pushups"
    var anchor: String // e.g., "After I brush my teeth"
    var iconName: String // SF Symbol name
    var frequency: HabitFrequency // enum: daily, weekdays, custom
    var createdDate: Date
    var completions: [Date] // Array of completion dates
    var isActive: Bool
    
    var currentStreak: Int {
        // Count consecutive days from today backwards where completion exists
        var streak = 0
        var date = Calendar.current.startOfDay(for: Date())
        while completions.contains(where: { Calendar.current.isDate($0, inSameDayAs: date) }) {
            streak += 1
            date = Calendar.current.date(byAdding: .day, value: -1, to: date) ?? date
        }
        return streak
    }
    
    var longestStreak: Int {
        // Calculate longest consecutive run in completions array
    }
    
    var isCompletedToday: Bool {
        completions.contains { Calendar.current.isDate($0, inSameDayAs: Date()) }
    }
    
    var weeklyCompletionRate: Int {
        // Percentage of last 7 days completed
    }
}

enum HabitFrequency: String, Codable, CaseIterable {
    case daily = "Daily"
    case weekdays = "Weekdays"
}
```

### Article
```swift
struct Article: Identifiable, Codable {
    let id: String
    let title: String
    let description: String
    let content: String
    let order: Int
}
```

### Sample Data (Habit Suggestions - first 10 of 50+)
```json
[
  {"name": "Do 2 pushups", "anchor": "After I brush my teeth", "iconName": "figure.strengthtraining.functional", "category": "Health"},
  {"name": "Read one page", "anchor": "After I sit on the couch", "iconName": "book.fill", "category": "Learning"},
  {"name": "Write one sentence", "anchor": "After I open my laptop", "iconName": "pencil", "category": "Productivity"},
  {"name": "Do 5 deep breaths", "anchor": "After I sit at my desk", "iconName": "wind", "category": "Mindfulness"},
  {"name": "Drink one glass of water", "anchor": "After I use the bathroom", "iconName": "drop.fill", "category": "Health"},
  {"name": "Put on workout clothes", "anchor": "After I take off my work clothes", "iconName": "tshirt.fill", "category": "Health"},
  {"name": "Write one thing I'm grateful for", "anchor": "After I get into bed", "iconName": "heart.fill", "category": "Mindfulness"},
  {"name": "Floss one tooth", "anchor": "After I brush my teeth", "iconName": "mouth.fill", "category": "Health"},
  {"name": "Send one text to a friend", "anchor": "After I check my phone", "iconName": "message.fill", "category": "Relationships"},
  {"name": "Sketch for 2 minutes", "anchor": "After I eat lunch", "iconName": "paintbrush.fill", "category": "Creativity"}
]
```

### Sample Data (Articles - 12 total)
```json
[
  {"id": "what-are-tiny-habits", "title": "What Are Tiny Habits?", "description": "The science behind starting small", "order": 1},
  {"id": "why-tiny-works", "title": "Why Tiny Habits Work", "description": "The psychology of small wins", "order": 2},
  {"id": "choosing-anchors", "title": "Choosing Your Anchors", "description": "How to attach habits to existing routines", "order": 3},
  {"id": "celebration", "title": "The Power of Celebration", "description": "Why celebrating tiny wins rewires your brain", "order": 4},
  {"id": "troubleshooting", "title": "When Habits Don't Stick", "description": "Common pitfalls and how to fix them", "order": 5},
  {"id": "habit-stacking", "title": "Habit Stacking", "description": "Building chains of tiny habits", "order": 6},
  {"id": "scaling-up", "title": "Scaling Up", "description": "When and how to make habits bigger", "order": 7},
  {"id": "environment-design", "title": "Design Your Environment", "description": "Make good habits easy and obvious", "order": 8},
  {"id": "tracking", "title": "The Role of Tracking", "description": "Why tracking matters (and why it doesn't)", "order": 9},
  {"id": "identity", "title": "Identity-Based Habits", "description": "Becoming the person you want to be", "order": 10},
  {"id": "patience", "title": "Patience & Persistence", "description": "Why habits take longer than you think", "order": 11},
  {"id": "next-steps", "title": "Your Next Steps", "description": "Where to go from here", "order": 12}
]
```

### Data Source
- Habit suggestions: Bundled JSON
- Articles: Bundled JSON
- User habits: Core Data
- No backend, no API, no internet required

---

## 5. Design Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #6C63FF | Headers, buttons, active states |
| Secondary | #E8E7FF | Backgrounds, tags, subtle elements |
| Accent | #FF6B6B | Streaks, celebrations, alerts |
| Background | #FFFFFF | Main background |
| Card Background | #F8F8FF | Cards, list rows |
| Text Primary | #2D2D2D | Headings, body text |
| Text Secondary | #8E8E93 | Captions, subtitles |
| Success | #4CAF50 | Completed habits, checkmarks |
| Flame Start | #FF6B6B | Streak flame (low) |
| Flame End | #FFD93D | Streak flame (high) |
| Divider | #E5E7EB | Separators |

### Typography
| Style | Font | Size | Weight |
|-------|------|------|--------|
| Large Title | SF Pro Display | 34pt | Bold |
| Title 1 | SF Pro Display | 28pt | Bold |
| Title 2 | SF Pro Display | 22pt | Semibold |
| Headline | SF Pro Text | 17pt | Semibold |
| Body | SF Pro Text | 17pt | Regular |
| Callout | SF Pro Text | 16pt | Regular |
| Caption | SF Pro Text | 12pt | Regular |

### Spacing
- Base unit: 4pt
- Scale: 4, 8, 12, 16, 20, 24, 32
- Card padding: 16pt
- Screen edge margin: 16pt
- Habit row vertical padding: 16pt

### Corner Radius
- Cards: 16pt
- Buttons: 12pt
- Checkboxes: 50% (circular)
- Tags: 8pt

### Icons (SF Symbols)
- Today: house.fill
- Guide: book.fill
- Review: chart.bar.fill
- Plus: plus.circle.fill
- Checkmark: checkmark.circle.fill
- Flame: flame.fill
- Book: book.fill
- Pencil: pencil
- Heart: heart.fill
- Drop: drop.fill
- Wind: wind
- Message: message.fill
- Paintbrush: paintbrush.fill
- Tshirt: tshirt.fill
- Mouth: mouth.fill

---

## 6. App Store Metadata

- **Title:** MicroHabit - Tiny Habits
- **Subtitle:** Small Steps, Big Changes
- **Keywords:** habit tracker,tiny habits,micro habits,productivity,streak tracker,self improvement,daily habits,routine tracker,atomic habits,behavior change
- **Description:** Build habits that actually stick. Start absurdly small. MicroHabit is based on the proven "Tiny Habits" method from Stanford researcher BJ Fogg. Make your habits so small you can't say no. DEAD SIMPLE: No complex setup. Just add habits and check them off. STREAK TRACKING: Watch your streaks grow. TINY HABITS GUIDE: Learn the science of habit formation. 50+ HABIT IDEAS: Browse tiny habit suggestions. FREE TO START: Track up to 5 habits free, forever.
- **Promotional Text:** Based on the proven Tiny Habits method. Start absurdly small. Build habits that stick.
- **What's New (v1.0):** Initial release. Start small. Stay consistent. Transform your life.
- **Screenshots needed:**
  1. Today screen with habit list and checkboxes
  2. Celebration animation on habit completion
  3. Add Habit screen with suggestions
  4. Weekly Review chart
  5. Guide article list
- **App Category:** Primary: Productivity, Secondary: Health & Fitness
- **Age Rating:** 4+
- **Privacy:** No data collected. All data stored on-device. No tracking.

---

## 7. Build Instructions

### Framework & Dependencies
- SwiftUI (no third-party dependencies)
- SF Symbols for all icons
- Core Data for habit storage
- UserDefaults for settings

### Minimum Xcode Version
- Xcode 15.0

### Build Order
1. **Project setup:** Create SwiftUI project, iOS 16 minimum, Core Data stack
2. **Data layer:** Create bundled JSON (habit suggestions, articles). Create Core Data model (Habit with completions).
3. **Today screen:** Build habit list with checkboxes. Implement completion toggle with haptic + animation.
4. **Add Habit:** Build modal form with suggestions. Implement habit creation.
5. **Streak tracking:** Implement streak calculation logic. Build flame icon visualization.
6. **Guide:** Build article list and reading view.
7. **Review:** Build simple bar chart for weekly completion.
8. **Polish:** Add confetti animation (SwiftUI particles or Lottie alternative), empty states, app icon.

### Testing Checklist
- [ ] Habits can be added, completed, and deleted
- [ ] Streak calculation is accurate (consecutive days)
- [ ] Longest streak is tracked correctly
- [ ] Completion toggle works with haptic feedback
- [ ] Weekly completion rate is calculated correctly
- [ ] Free tier limits at 5 habits
- [ ] Articles display correctly
- [ ] App works in airplane mode
- [ ] Data persists across launches
- [ ] No crashes on iPhone SE (3rd gen)
- [ ] Confetti animation plays on completion

### Estimated Build Time
2-2.5 hours
