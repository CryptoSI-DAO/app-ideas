# App Idea: Broadway Season Guide 2026 — Tony Awards Edition

*Generated: 2026-06-08*
*Confidence Score: 7.4/10*

---

## Pitch
A gorgeous, comprehensive guide to the 2025-2026 Broadway season — every Tony-nominated show, synopses, cast lists, song highlights, theater locations, and winner predictions all in one app. Perfect for theater fans, Tony Awards watchers, and tourists planning a NYC Broadway trip.

## Target Audience
- Primary: Broadway and musical theater fans following the Tony Awards
- Secondary: NYC tourists looking to see a Tony-nominated show
- Demographics: US, 22-55, skews female, iOS users, arts/culture enthusiasts, higher income

## Problem Statement
The 2026 Tony Awards are driving massive search interest (100K+ searches, 700% spike) with multiple shows trending simultaneously (Schmigadoon on Broadway, The Lost Boys, Death of a Salesman revival). Yet there's no single app that aggregates the full Broadway season — synopses, Tony nominations, cast, theater info, and predictions. Fans are forced to juggle Playbill.com (terrible mobile), Wikipedia, and individual show websites.

## Trend Evidence
- **Source 1**: Google Trends — "tony awards" at 100K+ searches, 700% increase, active 14 hours
- **Source 2**: Google Trends — Related terms all trending: "schmigadoon broadway" (10K+, 1000%), "death of a salesman" (20K+, 900%), "the lost boys musical" (20K+, 900%)
- **Source 3**: TikTok — #broadway consistently trending; #tonyawards hashtag growing; theater TikTok is a massive community
- **Momentum**: Rising — Tony Awards telecast drives peak interest; sustained interest from trending shows

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Playbill | ⭐3.4 | Free | Cluttered UI, ticket sales focus, no show guide |
| Broadway News | ⭐3.7 | Free | News only, no show database or Tony coverage |
| TodayTix | ⭐4.8 | Free | Ticket purchasing app, no show guide content |
| Shubert Broadway | ⭐N/A | Free | Only covers Shubert theaters, not full season |

**App Gap**: No app exists that combines the full Broadway season guide with Tony Awards coverage in a beautiful, browsable format. Playbill and TodayTix are ticket apps. Broadway News is just news articles. A curated, visual, offline Broadway guide is a clear white space.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Show Catalog** — All 30+ shows currently on Broadway with synopsis, cast, theater, runtime, and content rating
2. **Tony Awards Section** — All nominees by category (Best Musical, Best Play, Best Actor/Actress, etc.) with show cross-references
3. **Theater Directory** — Every Broadway theater with address, subway directions, seat count, and current show
4. **Winner's Circle** — Tony Award winners (to be updated post-ceremony)
5. **My Shows Tracker** — Mark shows you've seen, want to see, and get notified when near a theater
6. **Tony Night Countdown** — Countdown to the Tony Awards ceremony with schedule

### Nice-to-Have (v1.1+)
- Song highlight Spotify links per show
- "If you liked X, try Y" recommendation engine
- Ticket price ranges and TodayTix integration link
- Historical Tony Awards data (past 5 years winners)
- AR theater marquee viewer

## Content & Data
- **Shows**: 30-35 Broadway shows with synopsis (2-3 sentences), creative team, cast highlights, theater name, runtime, content rating
- **Tony Categories**: All 2026 Tony Award categories with nominees and show references
- **Theaters**: ~41 Broadway theaters with address, subway station, seat map thumbnail
- **Winners**: Tony Award winners (updated post-June 2026 ceremony)
- **Source**: Playbill.com, Tony Awards official site, Broadway League, public theater listings
- **Content Volume**: ~150 data items, all bundled as JSON

## Design Direction
- **Style**: Elegant, luxurious — think Broadway marquee meets premium magazine
- **Color Palette**:
  - Primary: #C9A96E (gold — Tony Awards)
  - Secondary: #1A1A1A (near-black — theater curtains)
  - Accent: #8B0000 (deep red — Broadway)
  - Background: #FAFAFA (warm white)
  - Text: #1A1A1A (dark)
- **Typography**: Georgia or New York (serif for elegance — theater marquees), SF Pro Text (body — mobile readability)
- **Key Screens**: Home (Tony countdown + featured), Show List, Show Detail, Tony Nominees by Category, Theater Map/Gallery, My Shows
- **Navigation**: Tab bar (Explore, Shows, Tony Awards, Theaters, My Shows)
- **Reference Apps**: Goodreads (collection UX), Resy (elegant directory), Halide (premium dark UI)

## Technical Notes
- **Platform**: iOS 16+ (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON files in app bundle
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
Broadway 2026 Tony Guide

### Subtitle
Shows, Nominees & Theater Guide

### Keywords
broadway, tony awards, tony awards 2026, broadway shows, musical theater, theater nyc, tony nominees, broadway guide, off broadway, theater tickets, schmigadoon broadway

### Description
Your complete guide to the 2025-2026 Broadway season and the 2026 Tony Awards.

🎭 ALL BROADWAY SHOWS — Browse every show currently running on Broadway. Read synopses, see cast highlights, find theaters, and check runtimes.

🏆 TONY AWARDS COVERAGE — Full nominee list by category. See which shows are nominated, track winners, and get expert predictions.

📍 THEATER DIRECTORY — Every Broadway theater with address, subway directions, and what's playing now.

❤️ MY SHOWS — Track what you've seen and what you want to see. Personalize your Broadway experience.

⏱️ TONY NIGHT COUNTDOWN — Never miss the ceremony. Get the full broadcast schedule.

From "Schmigadoon!" to "Death of a Salesman" to "The Lost Boys" — if it's on Broadway this season, it's in this app.

Perfect for theater fans, Tony night parties, and your next NYC trip.

### Category
Primary: Entertainment
Secondary: Reference

### Pricing
- **Model**: Free
- **Reasoning**: Maximize downloads during Tony Awards season. Builds audience for annual updates.
- **Monetization Path**: Annual "Broadway Season Guide" update each year ($0.99 per season). Partner with TodayTix for ticket affiliate revenue.

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | 100K+ searches for Tony Awards at 700%, multiple related Broadway terms trending simultaneously |
| App Gap | 9/10 | Zero comprehensive Broadway season guide apps — only ticket apps and news |
| Build Simplicity | 8/10 | Bundled JSON, clean card-based UI, ~2.5 hours |
| Evergreen Potential | 8/10 | Annual Broadway season creates recurring update cycle; Tony Awards every June |
| Monetization | 6/10 | Free for Tony season; annual updates can be paid. Affiliate ticket revenue potential. |
| **Average** | **7.4/10** | |

## Risk Assessment
- **Trend Fizzle**: LOW — Tony Awards is an annual event; Broadway is a permanent NYC institution
- **App Store Rejection**: LOW — purely informational content
- **Competition**: MEDIUM — Playbill could improve their app, but currently terrible on mobile
- **Legal/IP**: LOW — show synopses and theater info are factual/public data
- **Content Maintenance**: MEDIUM — Major update each Broadway season (September), Tony Awards update (June)

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Google Trends for tony awards + multiple related Broadway terms, TikTok theater community)
- [x] App Store search shows 0 comprehensive Broadway season guide apps
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual theater/show data, non-controversial
- [x] No obvious legal/copyright issues (factual show data)
- [x] Build time estimate ≤ 3 hours (2.5 hours)
