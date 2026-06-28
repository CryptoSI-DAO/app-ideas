# 🚨 App Idea: EyeGym — Daily Vision Training

*Generated: 2026-06-28*
*Confidence Score: 7.8/10 → Extended Research Score: 8.1/10*
*Status: 🚨 HIGH PRIORITY — BUILD RECOMMENDED*

**Extended Research:** See [extended-research/eyegym-vision-training.md](../extended-research/eyegym-vision-training.md) for full competitive analysis, revenue model, risk assessment, and phased build plan.

---

## Pitch
EyeGym is a beautifully-designed iOS app that guides desk workers and heavy screen users through 3–5 minute daily vision training routines. It combines clinically-inspired eye exercises (20-20-20 rule, focus shifting, palming, convergence training) with gentle animations and streak tracking — all bundled on-device, no internet required. No competitor uses modern wellness-app UX; existing apps look dated and clinical.

## Target Audience
- Primary: Remote workers, developers, designers spending 8+ hours daily on screens
- Secondary: Students, gamers, anyone experiencing digital eye strain
- Demographics: 22–45, US/UK/CA/AU, tech-savvy, health-conscious, already uses wellness apps

## Problem Statement
Digital eye strain affects 65% of US adults (American Optometric Association), yet the App Store options are either clinical-looking vision therapy apps with < 300 reviews, or generic screen-time trackers. No one has built a *beautiful*, daily-habit eye training app positioned as wellness tool rather than medical device. Users want a Headspace-for-their-eyes.

## Trend Evidence
- **Exploding Topics**: Blue light filter discussion trending across Tech Times, HubermanLab subreddit, PCMag. Eye strain awareness growing as screen time increases.
- **Reddit signals**: r/HubermanLab discussing blue light filters (1 month ago), r/techsupport threads on eye strain remedies — high engagement
- **Search signal**: "Eye strain relief" app on App Store dominated by 1-review apps; "Vision Training" only 299 reviews for top result
- **Momentum**: Sustained/rising — screen time only increases yearly

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Vision Training & Eye Exercise | ⭐4.54 (299 reviews) | Free | Dated UI, medical aesthetic, no streak/habit system |
| Vision Workout: Eye Training | ⭐4.70 (1,124 reviews) | Free | Functional but ugly, no onboarding, no daily reminders |
| Lazy Eye & Amblyopia Exercise | ⭐4.33 (21 reviews) | Free | Medical-only focus, terrible ratings |

**App Gap**: Quality gap. Existing apps are functional but look like they're from 2018. No one uses modern SwiftUI animations, haptics, wellness-app positioning, or streak tracking for eye health. Green field for a beautiful daily-habit app.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Daily Routine** — 3 guided exercises per session with looping Lottie-style UI animations showing eye movement direction
2. **Exercise Library** — 12 exercises in 4 categories (Focus, Relaxation, Mobility, Coordination), each with illustration + text instructions
3. **Streak Tracker** — Consecutive days completing daily routine, with weekly/monthly calendar view
4. **Smart Reminder** — 1 notification daily at user's chosen time, with "Done" action from notification
5. **20-20-20 Mode** — Optional 20-minute timer that reminds: every 20 min, look 20 feet away for 20 seconds

### Nice-to-Have (v1.1+)
- Screen time integration (ScreenTime API) to auto-suggest breaks
- Session duration analytics
- Dark mode exercise illustrations
- Apple Watch companion for haptic reminders

## Content & Data
- 12 eye exercises with: name, duration (30-90s), description, animation direction data, category
- Routine templates: "Morning Wake-up" (3 min), "Afternoon Reset" (2 min), "Evening Wind-down" (4 min)
- All content bundled as JSON in app bundle

## Design Direction
- **Style**: Clean wellness-app aesthetic (like Headspace meets Apple Fitness)
- **Color Palette**: 
  - Primary: #2D5BFF (calming blue)
  - Background: #F8FAFC (soft off-white)
  - Accent: #10B981 (success green for streaks)
  - Text: #1E293B (dark slate)
  - Card: #FFFFFF with subtle shadow
- **Typography**: SF Pro Display (headings), SF Pro Text (body)
- **Spacing**: 8/12/16/24/32pt scale
- **Corner radius**: Cards 16pt, Buttons 12pt
- **Shadows**: 0,2,8,0.08 for cards; 0,4,16,0.12 for floating elements
- **Icons**: SF Symbols — eye, eye.fill, flame, calendar, clock, checkmark.circle.fill
- **Key Screens**: Home (today's routine + streak), Exercise Detail (animation + timer), Library (all exercises), Settings (reminder time)
- **Navigation**: Tab bar (Today, Library, Progress)

## Technical Notes
- **Platform**: iOS 16+ (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON + UserDefaults for streak persistence
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low

## App Store Listing

### Title
EyeGym — Daily Vision Training

### Subtitle
Strengthen Your Eyes Daily

### Keywords
eye exercise,vision training,eye strain,screen fatigue,digital eye strain,eye health,20 20 20,blue light,computer vision,desk worker,eye workout,vision therapy,eye care,screen break,eye relaxation

### Description
Your eyes need a workout too.

EyeGym is the beautifully simple daily vision training app for anyone who stares at screens all day. Just 3–5 minutes of guided exercises can reduce eye strain, improve focus flexibility, and keep your eyes feeling fresh.

**HOW IT WORKS:**
• Complete your daily routine — 3 guided exercises with smooth animations
• Follow along as each exercise shows you exactly where to move your eyes
• Build streaks and track your consistency over time
• Enable 20-20-20 mode for passive reminders throughout the day

**12 EXERCISES ACROSS 4 CATEGORIES:**
🎯 Focus Training — near-far focusing, convergence drills
🧘 Relaxation — palming, blink exercises, warm-up routines
👁 Mobility — circular movements, directional tracking
🔄 Coordination — cross-eye training, depth perception

**NO INTERNET. NO ADS. NO SUBSCRIPTIONS.**
Everything works offline. Your streak data stays on your device. No account needed. One purchase, lifetime access.

Whether you're a developer, designer, student, or anyone whose work lives on a screen — give your eyes the daily care they deserve.

### Category
Primary: Health & Fitness
Secondary: Medical

### Pricing
- **Model**: Paid $3.99 one-time
- **Reasoning**: Utility wellness app with real, actionable content. $3.99 is an easy impulse buy for daily-use health tools.
- **Monetization Path**: Future: eye exercise packs as $0.99 IAP bundles; Apple Watch companion as separate free app

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | Evergreen concern (eye strain) with growing awareness, not a spike |
| App Gap | 8/10 | Top competitors have < 1,200 reviews and dated UIs; major quality gap |
| Build Simplicity | 9/10 | Bundled JSON, timer + animations, no backend, trivial persistence |
| Evergreen Potential | 8/10 | Screen time only increases; eye care never goes out of style |
| Monetization | 7/10 | Paid model works for wellness utilities; $3.99 = low friction |
| **Average** | **7.8/10** | |

## Risk Assessment
- **Trend Fizzle**: LOW — digital eye strain is a permanent, growing issue, not a fad
- **App Store Rejection**: LOW — not making medical claims; clearly labeled as wellness/exercise
- **Competition**: MEDIUM — big players (Calm, Headspace) could add eye content, but they haven't yet
- **Legal/IP**: LOW — exercises are public-domain techniques; animations are original
- **Content Maintenance**: LOW — eye exercises don't change; only content updates would be new exercise packs

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Tech Times, HubermanLab, PCMag all covering blue light/eye strain)
- [x] App Store search shows ≤ 3 relevant apps OR top apps have < 1,200 reviews
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours
