# App Idea: CreatineTracker

*Generated: 2026-06-02*
*Confidence Score: 8.2/10*

---

## Pitch
CreatineTracker is a dead-simple supplement tracking app built specifically for creatine users. It has a daily check-in timer, a streak counter, hydration reminders, and a science-backed dosing guide — all in under 3 MB with zero internet required. Perfect for the biohacking-adjacent fitness crowd who tracks every gram of protein but still forgets their creatine dose half the time.

## Target Audience
- Primary: Gym-goers and fitness enthusiasts (ages 18–35) who take creatine supplements, especially creatine gummies (the fastest-growing creatine format on TikTok)
- Secondary: Biohackers, nootropic users, and anyone already tracking supplements with spreadsheets or notes apps
- Demographics: US, 18–45, predominantly male but growing female segment, health-conscious

## Problem Statement
Creatine is the most researched sports supplement in history, yet nobody has built a good dedicated tracker. The App Store has only four tiny apps for creatine, and they all have 0–2 ratings and reviews. Users are drowning in generic supplement trackers or just setting random reminders they ignore. The "creatine gummies" TikTok trend is exploding, and gummy users specifically need tracking because doses are easy to double-count (they taste like candy). Nobody serves this niche well.

## Trend Evidence
- **Source 1 (Exploding Topics)**: Creatine Gummies tagged as a trending topic (June 2026) — steady growth in search volume
- **Source 2 (TikTok/Twitter)**: #creatinegummies has 100M+ views on TikTok; routines showing "my daily supplements" format drive massive engagement
- **Source 3 (App Store Gap)**: Only 4 results for "creine tracker" — all with 0–2 ratings, none with a modern UI or gummy-specific features. The best existing app (Kreas at $0.00 with 0 ratings) has zero traction.
- **Momentum**: Rising — creatine searches grow 5–10% YoY, gummy format is the fastest-growing subcategory

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Kreas - Creatine Tracker | ⭐0 (0 ratings) | Free | No reviews = no validation |
| CreaTrack: Creatine + Strength | ⭐4.5 (2 ratings) | Free | 2 ratings means dead product |
| iCreatine - Daily Tracker | ⭐5 (1 rating) | Free | 1 rating |
| Creatime | ⭐1 (1 rating) | Free | 1 star |

**App Gap**: The App Store has zero established creatine tracker apps. This is a true green-field — not even a mediocre incumbent to beat. Every existing app is effectively abandoned.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Daily Dose Logger** — One-tap "I took my creatine" button that logs the dose with timestamp. Supports custom dose amounts (3g, 5g, 10g gummy equivalents) and dosage form: powder, capsule, gummy.
2. **Streak Tracker** — Calendar view showing consecutive days of supplementation. Displays current streak, longest streak, and total doses taken. Streaks reset after a missed day.
3. **Hydration Reminder** — Push notification reminders to drink water after logging a creatine dose (creatine requires adequate hydration). Configurable reminder delay (0/15/30 min).
4. **Supplement Reference Guide** — Bundled content page explaining: what creatine is, how it works, dosing protocols (load vs. maintenance), different creatine forms (monohydrate, HCl, ethyl ester, gummy), and hydration tips. Written in-app, no internet needed.
5. **Streak History** — Simple list view of past doses with date, time, dose amount, and notes (optional text field).

### Nice-to-Have (v1.1+)
- iCloud sync so streaks survive app reinstall
- Widget showing current streak on home screen
- Apple Health integration (write water intake data)
- Weekly/monthly summary charts
- Multiple supplement support (not just creatine)

## Content & Data
- Supplement reference guide: ~2000 words of curated creatine knowledge (mechanisms, dosing protocols, form comparisons, safety profile, hydration)
- Bundle as JSON in app bundle for the reference content
- Sample data for preview mode: 14 days of pre-populated streak history so the app looks alive when first opened
- No user content — all data is private and local
- Estimated content preparation time: 1 hour of research + writing

## Design Direction
- **Style**: Clean, modern minimalism — card-based with generous white space. Think Streaks app meets Waterllama.
- **Color Palette**:
  - Primary: #FF6B6B (coral red — energetic, supplement-red, not medical)
  - Secondary: #4ECDC4 (mint — clean, hydrating)
  - Accent: #FFE66D (yellow — energy, caution notes)
  - Background: #FFFFFF (clean white)
  - Card Background: #F7F8FA
  - Text Primary: #1A1A2E
  - Text Secondary: #6B7280
- **Typography**: SF Rounded for headings, SF Pro Text for body. Large day counts (e.g., "DAY 12") as the hero visual element.
- **Key Screens**: Home (today's status + big tap button), Calendar/Streak view, Reference guide, Settings (configure dose amount, reminder timing)
- **Navigation**: Tab bar (Today / History / Guide / Settings)
- **Reference Apps**: Streaks (habit tracker UX), Waterllama (water tracking + widget), Ladder (fitness app simplicity)

## Technical Technical Notes
- **Platform**: iOS 16.0+ (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP. Optional Apple HealthKit (write water) in v1.1.
- **Data Storage**: AppStorage / UserSettings for streak persistence. No CoreData needed.
- **Estimated Build Time**: 2–2.5 hours (very small data model, no networking)
- **Complexity**: Low

## App Store Listing

### Title
CreatineTracker

### Subtitle
Daily creatine dose & streak tracker

### Keywords
creatine,creatine tracker,creatine gummies,supplement tracker,gym,fitness,biohacking,protein,hydration,streak tracker

### Description
The simplest way to stay consistent with your creatine.

Creatine is the most proven sports supplement in the world — but only if you take it every day. CreatineTracker makes that effortless.

🎯 ONE-TAP LOGGING
Tap the big button. Done. Your dose is logged with the time and date. Supports powder, capsules, and gummies (yes, we have gummy-specific dosing).

🔥 STREAK TRACKING
Build an unbreakable habit. See your current streak, longest streak, and total days on creatine — all in a beautiful calendar view.

💧 HYDRATION REMINDERS
Creatine works best with proper hydration. Get a gentle reminder after each dose to drink water.

📖 SCIENCE-BACKED REFERENCE
Everything you need to know about creatine — types, dosing, loading phases, safety — all offline and beautifully presented.

✨ WHO IS THIS FOR?
– Gym goers who track every gram but forget their creatine
– Creatine gummy users (it's easy to lose count!)
– Anyone who wants a simple, beautiful habit tracker for one specific supplement

No accounts. No subscriptions. No internet required. Just you and your gains.

### Category
Primary: Health & Fitness
Secondary: Lifestyle

### Pricing
- **Model**: Paid (Free) with optional tip
- **Reasoning**: Single-purpose utility apps convert well as paid downloads at $0.99–$1.99, but free maximizes reach for a habit tracker. Offer free with optional in-app "tip jar" ($0.99–$4.99). This feels generous and builds goodwill.
- **Monetization Path**: If the app gains traction, add a Pro unlock ($2.99 one-time) for Apple Health sync, widgets, multi-supplement support, and advanced analytics.

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | "Creatine gummies" is trending on TikTok; creatine searches grow 5–10% YoY — sustained growth, not a spike |
| App Gap | 9/10 | Zero established competitors; 4 apps all with 0–2 ratings — true green field |
| Build Simplicity | 9/10 | Probably the simplest app in today's batch: one main screen, one data model, no networking |
| Evergreen Potential | 8/10 | Creatine is one of the few supplements with decades of research. Not a fad — it's permanent. |
| Monetization | 7/10 | Small niche limits total revenue, but the targeted audience has high conversion potential for fitness supplements. Pro upgrade path exists. |
| **Average** | **8.2/10** | |

## Risk Assessment
- **Trend Fizzle**: Low. Creatine isn't a trend — it's a staple supplement used by millions for 30+ years. The gummy format may cycle in and out, but overall creatine use is stable.
- **App Store Rejection**: None. No claims about medical benefits — purely a tracking/logging app.
- **Competition**: Medium risk. Fitness apps could add creatine tracking as a feature, but nobody's prioritizing it. Speed to market matters.
- **Legal/IP**: None. "Creatine" is a generic chemical compound. No trademark issues.
- **Content Maintenance**: Minimal. The reference guide is evergreen. No frequent updates needed beyond bug fixes.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (TikTok views, Exploding Topics, search volume)
- [x] App Store search shows 0 relevant apps with any meaningful traction
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 2.5 hours (well under 3-hour limit)
