# App Idea: BlueRay — Evening Wind-Down Coach

*Generated: 2026-06-28*
*Confidence Score: 7.6/10*

---

## Pitch
BlueRay is an iOS app that helps you build a healthier evening screen routine — not by filtering your screen (iOS doesn't allow that), but by coaching you through a personalized wind-down ritual. It combines screen-time awareness, sleep hygiene education, and gentle prompts to put your phone down at the right time. Think of it as a "sleep coach" that focuses on the 60 minutes before bed.

## Target Audience
- Primary: People who scroll in bed and know they shouldn't
- Secondary: Biohackers, Huberman Lab listeners, anyone optimizing sleep
- Demographics: 22–40, US/UK/CA, already interested in wellness, uses phone in bed

## Problem Statement
iOS restricts third-party blue-light filter apps, and the built-in Night Shift is passive. People KNOW they shouldn't scroll before bed but lack a structured, beautiful system to break the habit. Existing screen-time apps (BePresent, 55K reviews) focus on general usage limits — none specifically target the pre-sleep wind-down window with coaching, education, and ritual-building.

## Trend Evidence
- **Exploding Topics**: Blue light filter discussion trending; eye strain and sleep disruption awareness growing
- **Reddit**: r/HubermanLab discussing blue light (1 month ago, high engagement), r/sleep threads on phone use before bed
- **Media**: Tech Times, PCMag, Forbes all publishing blue light / sleep articles in 2025-2026
- **App Store signal**: "Blue Light Filter" app has 3.3 stars (127 reviews) — users want this but existing solutions are poor
- **Momentum**: Sustained — sleep optimization is a permanent wellness trend

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| BePresent: Screen Time Control | ⭐4.84 (55,730 reviews) | Free | General screen-time, not sleep-specific |
| Blue Light Filter | ⭐3.35 (127 reviews) | Free | Poor ratings, iOS restrictions limit functionality |
| Luma Sleep – Night Screen | ⭐4.16 (25 reviews) | Free | Tiny, basic, no coaching element |
| one sec | ⭐4.83 (23,053 reviews) | Free | Friction tool, not a wind-down coach |

**App Gap**: No app combines sleep hygiene education + wind-down ritual + screen-time awareness into a beautiful pre-sleep coaching experience. BePresent is too general; one sec is too punitive; blue light apps are technically limited.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Wind-Down Timer** — User sets target "phone down" time; app counts down from 60 min before with gentle coaching prompts
2. **Sleep Hygiene Cards** — 20 evidence-based tips (Huberman-inspired, cited) delivered as swipeable cards during wind-down
3. **Evening Ritual Builder** — User builds a 3-step pre-sleep routine (e.g., "Dim lights → Read 10 min → Meditate 5 min") with checklist
4. **Screen Time Snapshot** — Shows today's total screen time + bedtime pick-up count (via ScreenTime API)
5. **Wind-Down Streak** — Tracks consecutive nights user completed their ritual before target time

### Nice-to-Have (v1.1+)
- Shortcuts integration to auto-dim HomeKit lights at wind-down start
- Apple Watch wind-down companion
- Sleep quality self-reporting (1-5 scale) correlated with screen habits
- Widget showing "X minutes until wind-down"

## Content & Data
- 20 sleep hygiene tips with: title, 2-3 sentence explanation, source citation
- 15 pre-built ritual activities (dim lights, read, meditate, journal, stretch, etc.)
- Default wind-down duration: 60 minutes (configurable 30-120)
- All content bundled as JSON

## Design Direction
- **Style**: Dark, calming, night-mode-first design (like Dark Noise meets Apple Sleep)
- **Color Palette**:
  - Primary: #8B5CF6 (soft purple)
  - Background: #0F0A1A (deep night)
  - Accent: #F59E0B (warm amber — sunset tones)
  - Text: #E2E8F0 (soft white)
  - Card: #1E1B2E (dark surface)
- **Typography**: SF Pro Display (headings), SF Pro Text (body)
- **Spacing**: 8/12/16/24/32pt scale
- **Corner radius**: Cards 20pt, Buttons 14pt
- **Shadows**: Minimal — dark mode uses elevation via color, not shadow
- **Icons**: SF Symbols — moon.stars, bed.double, clock, lightbulb, checkmark.circle, sparkles
- **Key Screens**: Home (wind-down countdown + tonight's ritual), Tips (swipeable cards), Ritual Builder, Progress (streaks + screen time trends)
- **Navigation**: Tab bar (Tonight, Tips, Rituals, Progress)

## Technical Notes
- **Platform**: iOS 16+ (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: FamilyControls/ScreenTime API for screen-time data (optional, degrades gracefully)
- **Data Storage**: Bundled JSON + UserDefaults for streaks and ritual config
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low

## App Store Listing

### Title
BlueRay — Evening Wind-Down Coach

### Subtitle
Build a Better Pre-Sleep Routine

### Keywords
sleep coach,wind down,bedtime routine,screen time,sleep hygiene,phone addiction,evening routine,sleep better,digital wellness,blue light,sleep tracker,bedtime reminder,phone free,night routine,sleep optimization

### Description
Your phone is stealing your sleep. BlueRay helps you take it back.

BlueRay is your personal evening wind-down coach. Instead of willpower, you get a structured ritual that gently guides you away from your screen and into restful sleep.

**HOW IT WORKS:**
• Set your target "phone down" time each night
• BlueRay counts down with calming coaching prompts
• Complete your personalized wind-down ritual
• Build streaks and watch your sleep habits transform

**BUILD YOUR EVENING RITUAL:**
Choose from 15 activities to create your perfect pre-sleep sequence:
💡 Dim the lights  📖 Read  🧘 Meditate  📝 Journal  
🧴 Skincare  🤸 Stretch  🎵 Listen to music  ☕ Herbal tea

**20 SLEEP HYGIENCE INSIGHTS:**
Swipe through evidence-based tips from sleep science — learn why your evening habits matter and how small changes compound.

**TRACK YOUR PROGRESS:**
• Wind-down streak counter
• Daily screen time snapshot
• Bedtime pick-up count
• Weekly consistency score

No filtering. No blocking. No punishment. Just a beautiful system that makes putting your phone down feel natural.

Sleep better starting tonight.

### Category
Primary: Health & Fitness
Secondary: Lifestyle

### Pricing
- **Model**: Freemium — free (3 rituals, basic tips) / Premium $4.99 one-time (unlimited rituals, all tips, trends)
- **Reasoning**: Sleep apps thrive on freemium; free tier hooks users, premium unlocks full value
- **Monetization Path**: Premium unlock; future: sleep sounds pack, Apple Watch app

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | Sleep optimization is a sustained mega-trend; Huberman effect continues |
| App Gap | 8/10 | No app owns "wind-down coach" positioning; existing apps are too general or punitive |
| Build Simplicity | 9/10 | Bundled JSON, timer, UserDefaults; ScreenTime API is optional |
| Evergreen Potential | 8/10 | Sleep is forever; phone-in-bed habit isn't going away |
| Monetization | 6/10 | Freemium requires more users to convert; but $4.99 premium is solid |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: LOW — sleep optimization is a permanent wellness pillar
- **App Store Rejection**: LOW — no medical claims; uses ScreenTime API properly
- **Competition**: MEDIUM — Calm/BetterSleep could add wind-down features, but they're meditation-first
- **Legal/IP**: LOW — sleep tips are public-domain science; no Huberman branding used
- **Content Maintenance**: LOW — sleep science is stable; tips don't expire

## Validation Checklist
- [x] At least 3 sources confirm rising trend (HubermanLab, Tech Times, PCMag all covering sleep/screen)
- [x] App Store search shows no app owns "wind-down coach" positioning
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours
