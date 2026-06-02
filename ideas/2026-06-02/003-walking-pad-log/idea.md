# App Idea: WalkDesk — Under-Desk Walk Tracker

*Generated: 2026-06-02*
*Confidence Score: 7.6/10*

---

## Pitch
WalkDesk is a walking tracker purpose-built for under-desk treadmill (walking pad) users. It logs dedicated walking-pad sessions, tracks steps-per-day, estimates calories burned, and builds weekly/monthly habit streaks — all without GPS (because you're literally walking in place). The UI is designed for the small glances you take at your phone propped up next to the treadmill. Clean, bold numbers, session timer, distance calculated from step count × user-configured stride length. No clutter, no features you don't need while walking.

## Target Audience
- Primary: Remote workers (ages 25–50) who own or are considering an under-desk walking pad to combat sedentary work
- Secondary: WFH wellness enthusiasts, desk job workers with back pain, and hybrid workers making the commute-to-desk transition
- Demographics: US, 25–50, higher income (walking pads cost $200–$600), tech-forward, health-motivated

## Problem Statement
Walking pads (under-desk treadmills) are one of the fastest-growing fitness products of 2024–2026 (7,500%+ search growth on Exploding Topics). Thousands of people buy them daily. But the tracking experience is terrible — people use generic step counters (designed for outdoor walks), Or they use running apps (designed for GPS running on trails). No app exists specifically for the unique experience of walking 2–4 mph in place at your desk while reading Slack. WalkDesk fills this gap with: no GPS needed, session-based logging (not route-based), big easy-to-read numbers, and estimates tuned for flat treadmill surfaces.

## Trend Evidence
- **Source 1 (Exploding Topics)**: "Walking Pad" ranked #33 at 7,500% search growth (June 2026)
- **Source 2 (YouTube/TikTok)**: #desksetup and #walkingtreadmill have hundreds of millions of views; influencers regularly feature standalone apps for tracking
- **Source 3 (App Store Gap)**: Searching "walking pad tracker" returns 10 results — but all are generic GPS-based outdoor walking apps (StepsApp, MapMyWalk, Walkmeter). None are designed for under-desk use. The closest dedicated app is missing.
- **Momentum**: Rising — the walking pad trend correlates directly with the work-from-home movement, which is sustained structurally

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| StepsApp Pedometer | ⭐4.8 (279K ratings) | Free | GPS outdoor-focused; no walking pad specialization; no session timer |
| MapMyWalk | ⭐4.4 (471K ratings) | Free | GPS-based routes; completely wrong paradigm for desk walking |
| Walkmeter Walking & Hiking GPS | ⭐4.7 (13K ratings) | Free | GPS-based; designed for hikers |
| Weight Loss Walking by Slimkit | ⭐4.4 (14K ratings) | Generic | Generic outdoor walking; no desk/walking pad awareness |

**App Gap**: Every existing walking app assumes you're moving geographically. None offer: session-timer mode, step-count-based distance (no GPS), display designed for desk-side phone mounting, or walking-pad-specific metrics like "time at 2.5 mph." This is a quality gap — the market exists but is served by wrong-shaped tools.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Session Timer** — Big start/stop/pause button. Timer counts up while walking. Sessions auto-save when stopped. Displays session time, estimated distance (steps × stride length), and estimated calories. Designed for fat-finger accuracy at desk distance.
2. **Step Counter** — Pedometer using CoreMotion (CMPedometer) to count phone-in-pocket steps. Users see live step count or can manually enter step count from treadmill display.
3. **Stride Length Calibration** — Settings screen where users enter their stride length (with a 30-second calibration walk option). Default: 0.762m (30 inches) for men, 0.67m (26 inches) for women. Customizable per user.
4. **Session History** — List of past walking pad sessions with date, duration, distance, calories. Weekly view (mon-sun) showing total weekly distance and time.
5. **Daily/Weekly Goals** — User-configurable goals: step target per day, distance target per week, or active minutes per day. Progress shown as simple ring/circle indicator on home screen.

### Nice-to-Have (v1.1+)
- HealthKit integration (write steps and active minutes)
- Complications/widget for Apple Watch
- Export session data as CSV
- "Desk stretch reminder" after N minutes of walking
- Integration with walking pad APIs (some Bluetooth-enabled treadmills expose data)
- Monthly challenges ("Walk 50 km this month")

## Content & Data
- No external content needed — the app is a pure utility tracker
- Calorie estimation formula: `MET × weight(kg) × time(hrs)`, where MET for walking at 2.5 mph ≈ 2.8, 3.0 mph ≈ 3.3, 3.5 mph ≈ 3.8
- Calibration tips for stride length measurement (bundled help text)
- Sample data: 7 days of session history pre-loaded for first-time app preview
- Weight entry in Settings for calorie calculation (default: 70 kg / 154 lbs)

## Design Direction
- **Style**: Ultra-clean, bold numbers, glanceable. While walking at a desk, you shouldn't need to squint or read paragraphs. Think big digital clock meets fitness tracker.
- **Color Palette**:
  - Primary: #1B4D3E (deep green — calm, walking, nature)
  - Secondary: #2E86AB (ocean blue — steady, reliable)
  - Accent: #F39C12 (amber — energy, goals)
  - Background: #F8FFFB (near-white with green tint)
  - Card Background: #FFFFFF
  - Text Primary: #0D1B16
  - Timer Display Color: #1B4D3E (same as primary)
  - Text Secondary: #6B7280
  - Progress Ring: Gradient from #2E86AB to #1B4D3E

- **Typography**: SF Mono for timer/numeric displays (monospace keeps numbers from jumping). SF Pro Display for labels. Timer text: 72pt bold SF Mono.
- **Key Screens**: Home (live session + timer + today's progress), History (session list + weekly summary), Goals (set targets), Settings (weight, stride length, units)
- **Navigation**: Tab bar (Now / History / Goals / Settings)
- **Reference Apps**: Gymaholic (timer UX), Streaks (simple goal screen), Apple Fitness rings (progress indicator idea)

## Technical Notes
- **Platform**: iOS 16.0+ (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: CoreMotion (CMPedometer for step counting). HealthKit optional for v1.1.
- **Data Storage**: AppStorage/SwiftData for session persistence. Estimated schema: Session { id, date, duration, steps, distance, calories }
- **Estimated Build Time**: 2.5–3 hours
- **Complexity**: Low-Medium (CoreMotion integration adds a small layer, but the data model is simple)

## App Store Listing

### Title
WalkDesk — Walking Pad Tracker

### Subtitle
Under-desk treadmill step & time log

### Keywords
walking pad,under desk treadmill,step counter,walk tracker,desk exercise,work from home fitness,sedentary,steps,pedometer,office walking

### Description
Tracker built for the treadmill under your desk.

WalkDesk is made for people who walk while they work. No GPS routes. No outdoor maps. Just clean, big-number tracking for your under-desp treadmill sessions.

SESSION TIMER
Big, bold timer. Start. Stop. Walk. Everything updates in real time: elapsed time, estimated distance, estimated calories burned.

STEP COUNTER
Uses your iPhone's motion sensors to count steps while the phone is in your pocket. Or enter steps manually from your treadmill's display.

SET YOUR STRIDE
One-time calibration sets your personal stride length for accurate distance. Or use smart defaults based on height/gender.

WEEKLY GOALS
Set daily step targets or weekly distance goals. Beautiful progress rings show how close you are.

SESSION HISTORY
Every walk is saved. Review sessions, see weekly totals, spot trends. Simple list or calendar view.

WHY NOT JUST USE A REGULAR WALKING APP?
Because walking at your desk is different. Apps like MapMyWalk track outdoor routes — they don't know you're walking 2.8 mph in place between Zoom calls. WalkDesk is purpose-built: no GPS required, big numbers designed for a phone propped next to your treadmill, and metrics that make sense when you go nowhere (but still move your body).

Requirements: iPhone (uses Motion sensors). Works with any walking pad or manual treadmill.

### Category
Primary: Health & Fitness
Secondary: Lifestyle

### Pricing
- **Model**: Free with Pro unlock at $2.99
- **Reasoning**: Walking pad market is growing but not huge yet. Free maximizes downloads. Pro unlock (weekly analytics, unlimited sessions, HealthKit export) captures revenue from power users.
- **Monetization Path**: Add subscription tier ($4.99/mo) for treadmill-specific workout plans ("30-minute desk walk routines"), sync across devices, and Apple Watch companion.

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 9/10 | 7,500% search growth; structurally tied to WFH which isn't going away |
| App Gap | 8/10 | No dedicated walking-pad app exists; all competitors are repurposed GPS runners |
| Build Simplicity | 7/10 | CoreMotion adds complexity; data model is simple; 2.5–3 hours estimated |
| Evergreen Potential | 7/10 | Tied to walking pad adoption which may peak, but "desk fitness" as a category is growing |
| Monetization | 7/10 | Freemium limits revenue per user but expands reach. Niche audience = lower total ceiling but higher conversion |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: Medium. Walking pad sales could slow as novelty fades. However, once someone owns a walking pad, they need ongoing tracking — installed base persists even if new sales decline.
- **App Store Rejection**: None. Standard utility app.
- **Competition**: Medium. Apple could add "indoor treadmill" as a workout type in Fitness+. But Apple's fitness apps are generic, not niche-focused. A dedicated app always outperforms generic for a specific use case.
- **Legal/IP**: None. Pure utility. No third-party content.
- **Content Maintenance**: Minimal. No external content. Bug fixes and feature additions only.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics 7,500%, YouTube/TikTok views, WFH correlation)
- [x] App Store search shows zero apps purpose-built for walking pads
- [x] MVP can be built without backend/API dependencies (CoreMotion is on-device)
- [x] No content to maintain
- [x] No legal concerns
- [x] Build time estimate ≤ 3 hours
