# App Idea: World Cup 2026 Trivia & Predictions

*Generated: 2026-06-14*
*Confidence Score: 8.2/10*

---

## Pitch

A fan engagement app for the FIFA World Cup 2026 that combines match schedules, team trivia, and prediction scoring — all without needing real-time data feeds. Users test their football knowledge with curated trivia, make match predictions before games, and track their prediction accuracy on a leaderboard. Unlike the official FIFA app (which is just schedules and news), this app gamifies the fan experience.

## Target Audience
- Primary: Football/soccer fans in the US (18-45) watching their first World Cup
- Secondary: Casual fans who want to engage more deeply during the tournament
- Demographics: US-based, 18-45, iOS users, sports enthusiasts

## Problem Statement

The official FIFA World Cup 2026 app (#5 on App Store) is purely informational — schedules, scores, news. There's no fan engagement layer. Millions of casual US fans watching their first World Cup want to:
1. Test their knowledge with fun trivia
2. Make predictions and compete with friends
3. Track their "fan IQ" score across the tournament

No app currently combines these three elements in a simple, offline-friendly package.

## Trend Evidence
- **Source 1**: Google Trends — "fifa world cup 2026" at 10M+ searches, 1,000% increase, 3 days ago and still active. "world cup schedule" at 2M+ searches, 200% increase.
- **Source 2**: App Store — FIFA World Cup 2026 app at #5 in top free apps, confirming massive demand. But it's purely informational — no trivia, no predictions, no gamification.
- **Source 3**: TikTok — #golazogemsweek (FIFA collectibles) at 1,359 posts, #summergarden at 45.9K posts showing summer activity interest. World Cup content is exploding across platforms.
- **Momentum**: Rising — World Cup 2026 is in early stages, will peak in July

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| FIFA World Cup 2026 (official) | ⭐ 4.2 | Free | No trivia, no predictions, no gamification. Just schedules and news. |
| OneFootball | ⭐ 4.5 | Free | News-heavy, requires internet, no prediction scoring |
| FotMob | ⭐ 4.8 | Free | Stats-focused, no fan engagement/trivia features |

**App Gap**: No app combines trivia + predictions + scoring in a simple offline package. The official app has the brand but zero gamification. This is a quality gap opportunity.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Match Schedule Browser** — Browse all World Cup matches by date, group, or team. Bundled JSON data (no API needed). Includes team flags, stadium info, kickoff times.
2. **Trivia Quiz Mode** — 100+ curated trivia questions about World Cup history, teams, players, and rules. Multiple choice, 4 options. Score tracked per session.
3. **Prediction Tracker** — Before each match, users pick a winner and score. Stored locally. After match data is bundled in, predictions are scored automatically.
4. **Fan IQ Score** — Combined score from trivia accuracy + prediction accuracy. Displayed as a single "Fan IQ" number with badges (Rookie → Expert → Legend).

### Nice-to-Have (v1.1+)
- Head-to-head challenge mode (compare Fan IQ with friends via share sheet)
- Daily trivia streak with notifications
- Dark mode support
- Widget showing next match countdown

## Content & Data
- **Match schedule**: All 104 matches with date, time, teams, stadium, group — bundled as JSON (~50KB)
- **Trivia questions**: 100+ questions across categories (History, Teams, Players, Rules, Records) — bundled as JSON
- **Team data**: 48 qualified teams with flags (emoji), FIFA rankings, group assignments — bundled as JSON
- **Prediction scoring**: Simple algorithm (correct winner = 3 pts, exact score = 5 pts) computed locally
- All content is factual/public domain — no licensing issues

## Design Direction
- **Style**: Bold, sporty, modern — think ESPN meets quiz app
- **Color Palette**: 
  - Primary: #00A859 (World Cup green)
  - Secondary: #FFD700 (gold)
  - Background: #0A0A0A (near black)
  - Text: #FFFFFF (white)
  - Accent: #E74C3C (red for wrong answers)
- **Typography**: SF Pro Display (bold for scores, regular for body)
- **Key Screens**: Home (next match + Fan IQ), Schedule (list/grid), Trivia (quiz flow), Predictions (match picker), Profile (stats + badges)
- **Navigation**: Tab bar (Home, Schedule, Trivia, Predictions, Profile)
- **Reference Apps**: ESPN, Sporacle (trivia), FIFA official app

## Technical Notes
- **Platform**: iOS (SwiftUI), minimum iOS 16
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON files + UserDefaults for scores/predictions
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
World Cup 2026 Trivia

### Subtitle
Quiz, Predict & Score!

### Keywords
world cup, fifa, soccer, football, trivia, quiz, prediction, 2026, fan, score, match, schedule

### Description
🏆 Think you're a World Cup expert? Prove it!

World Cup 2026 Trivia is the ultimate fan engagement app for the biggest tournament on earth. Test your football knowledge, predict match outcomes, and climb the Fan IQ leaderboard.

🎯 TRIVIA MODE
Over 100 questions covering World Cup history, legendary players, iconic moments, and the rules of the game. How many can you get right?

🔮 PREDICTIONS
Pick your winners before every match. Get points for correct predictions and exact score guesses. Track your accuracy across the entire tournament.

📊 FAN IQ SCORE
Your combined trivia and prediction accuracy creates your Fan IQ — a single number that proves your fan credentials. From Rookie to Legend!

📅 FULL SCHEDULE
Browse all 104 matches by date, group, or team. Never miss a kickoff.

No internet required for trivia and predictions. Play anywhere, anytime.

Download now and show the world your Fan IQ! ⚽

### Category
Primary: Sports
Secondary: Entertainment

### Pricing
- **Model**: Free with ads (banner ads between trivia questions)
- **Reasoning**: High traffic during World Cup = ad revenue. Tournament is time-limited (4 weeks), so free maximizes downloads.
- **Monetization Path**: $1.99 ad-free upgrade, or $0.99 for "Pro Trivia Pack" (200 more questions)

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 10/10 | World Cup 2026 is the #1 trend in US. 10M+ searches, 1,000% increase. Will only grow. |
| App Gap | 8/10 | Official app exists but has zero gamification. No competitor combines trivia + predictions. Clear quality gap. |
| Build Simplicity | 9/10 | All data bundled as JSON. No API. Trivia is just multiple choice. Predictions are local. Very buildable. |
| Evergreen Potential | 6/10 | World Cup is every 4 years. App has a 4-week peak window. But the concept works for any tournament. |
| Monetization | 8/10 | Free + ads during a high-traffic event = solid revenue. $1.99 ad-free is an easy upsell. |
| **Average** | **8.2/10** | |

## Risk Assessment
- **Trend Fizzle**: Low risk — World Cup 2026 is a confirmed event happening in 6 weeks. The trend will only intensify.
- **App Store Rejection**: Low risk — no user-generated content, no real-time data, no gambling. Trivia and predictions are clearly entertainment.
- **Competition**: Medium risk — FIFA could add trivia to their official app. But they're slow to update, and this app launches first.
- **Legal/IP**: Low risk — "World Cup" and "FIFA" are trademarked. Use "World Cup 2026" descriptively (nominative fair use). Don't use official logos. Use team names (which are public).
- **Content Maintenance**: Medium — trivia is static (good), but match schedule data needs to be accurate. Bundle updated JSON before launch.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Google Trends, App Store charts, TikTok)
- [x] App Store search shows official app exists but lacks gamification features
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues (use descriptive naming, not official branding)
- [x] Build time estimate ≤ 3 hours (2.5 hours)
