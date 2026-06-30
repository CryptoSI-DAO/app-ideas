# App Idea: LEDmask — LED Face Mask Treatment Guide & Timer

*Generated: 2026-06-30*
*Confidence Score: 7.5/10*
*Status: idea_generated | Gap: QUALITY GAP*

---

## Pitch
LEDmask is the definitive companion for at-home LED light therapy face masks. It features treatment protocols for every skin concern (acne, anti-aging, hyperpigmentation, redness), timer-based guided sessions with mask-specific instructions, progress tracking, and a选购 guide for the 30+ LED masks on the market. Think of it as the "Headspace for light therapy" — making LED mask treatments simple, effective, and trackable.

## Target Audience
- Primary: Women 25-50 who own or are shopping for an LED face mask (current market ~$2B growing 15%+ YoY)
- Secondary: Skincare enthusiasts starting light therapy, dermatology patients supplementing treatments
- Demographics: US/UK/AU, $60K+ income, iOS users, active on skincare TikTok/YouTube

## Problem Statement
The LED face mask market is booming (CurrentBody, Dr. Dennis Gross, Omnilux, Therabody TheraFace, EBODY, etc.). Owners receive a mask with a physical remote and minimal instructions. No app exists to: guide users through treatment protocols, track consistency over time, remind them of sessions, or help them choose the right wavelength for their skin concern. The only "LED mask" app on the store is "Shining Mask" (3.2★, 395 reviews) — a brand-specific utility for one obscure Chinese brand with dated UX. There is NO universal LED mask companion app.

## Trend Evidence
- **Exploding Topics #82**: LED Face Mask (+1,800% search growth)
- **Exploding Topics #61**: TheraFace (+3,900%) — direct competitor product category
- **Exploding Topics context**: Clean beauty + at-home beauty device mega-trend
- **Related apps on store**: Nolla Skin (9.1K reviews, acne tracking), Halo: Clear Skin (2.7K reviews), MDacne (18.7K reviews) — all show skincare tracking demand
- **Market data**: LED mask market projected $2.4B by 2027 (Grand View Research)
- **Red Light Therapy Guide** already exists in our catalog (for panels/bulbs) — confirming light therapy demand but NOT covering wearable LED face masks specifically
- **Momentum**: Rising — at-home beauty device market accelerated post-COVID

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Shining Mask | 3.2★ | $0.00 | Single-brand utility for "Shining Mask" brand. 395 reviews. Dated UI. Not a guide. |
| TheraFace (Therabody) | 4.75★ | $0.00 | Brand-locked to Therabody devices. Won't work with any other mask. No skin protocol advice. |
| NuFACE | 4.75★ | $0.00 | Microcurrent only, not LED. Brand-locked. |
| Nolla Skin | 4.9★ | $0.00 | Acne tracking, not LED therapy. No timer/session guidance. |
| Red Light Therapy Guide | N/A | N/A | Existing idea for our catalog — covers panels/bulbs, NOT wearable face masks. Adjacent but different. |

**App Gap**: QUALITY GAP. No universal LED mask companion exists. All existing apps are brand-locked. Users who own masks from CurrentBody, Dr. Dennis Gross, Omnilux, EBODY, or a dozen other quality brands have NO support app at all. The one general app (Shining Mask) has 3.2★ rating — terrible UX = opportunity.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Treatment Timer** — Countdown timer for LED mask sessions. Pre-configured protocols for each wavelength (Blue 415nm for acne, Red 630nm for anti-aging, Near-IR 830nm for deep healing, Green 525nm for pigmentation, Yellow 590nm for redness). Preset 10/15/20-minute sessions per manufacturer guidelines.
2. **Skin Concern Protocols** — 8 pre-built treatment plans based on skin concern: Acne Clearing, Anti-Aging, Brightening, Redness Reduction, Post-Procedure Healing, Maintenance, Wedding Prep, Seasonal Reset. Each includes which wavelength, frequency, duration duration, and complementary skincare tips.
3. **Mask Comparison Guide** — 30+ LED face masks on the market with specs: brand, wavelengths offered, price, coverage area, wired/wireless, FDA-cleared status, wavelength power (mW/cm²). Helps users choose and serves readers who haven't bought yet.
4. **Progress Tracker** — Simple calendar where users log sessions. Track streaks, total sessions, current protocol. Optional photo progress (side-by-side date comparison). No cloud sync needed.
5. **Education Section** — 8 articles explaining LED therapy science, wavelength guide, safety (eye protection), combining with skincare ingredients, who should avoid (pregnancy, photosensitivity meds, etc.).

### Nice-to-Have (v1.1+)
- Before/after photo comparison tool
- Apple Health integration (mindful minutes)
- Weekly/monthly progress reports (charts)
- Community protocol sharing
- Product-specific calibration guides for popular masks
- Skin diary: log breakouts, reactions, complementary products used

## Content & Data
- Treatment protocols: Compiled from manufacturer guidelines (CurrentBody, Dr. Dennis Gross, Omnilux all publish usage guidelines publicly)
- Mask specs: From brand websites, Amazon listings, beauty editor roundups (Allure, Byrdie, Who What Wear — all published 2025-2026 mask buying guides)
- LED science: Peer-reviewed dermatology studies on phototherapy (public access)
- MVP content: 8 protocols + 30 mask profiles + 8 articles (approximately 2 hours to compile)
- Data source: Bundled JSON, no internet required

## Design Direction
- **Style**: Premium, spa-like, scientifically credible. Think: L'Oréal Skin Genesis meets Dark Sky (beautiful data visualization).
- **Color Palette**:
  - Primary: #1A1A2E (deep navy)
  - Red wavelength accent: #E94560 (red therapy)
  - Blue wavelength accent: #4CC9F0 (blue therapy)
  - Amber accent: #F77F00 (warmth)
  - Background: #F8F9FA
  - Card: #FFFFFF
  - Success: #2EC4B6 (teal)
  - Text: #16161A
- **Typography**: SF Pro Rounded for headings (friendly/approachable), SF Pro Text for body. H1: 28pt Bold, H2: 20pt Semibold, Body: 16pt Regular, Caption: 13pt Regular
- **Key Screens**: Home (Start Treatment/Continue Protocol), Protocol List, Timer (countdown), Progress/Calendar, Mask Guide, Learn
- **Navigation**: Tab bar — Treat, Protocols, Masks, Progress, Learn
- **Reference Apps**: Headspace (guided session UX), Dark Sky (data beauty), Timer apps (clean countdown)

## Technical Notes
- **Platform**: iOS (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON + UserDefaults for session history
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
LEDmask — Face Mask Light Therapy

### Subtitle
Guided LED protocols & treatment timer

### Keywords
LED face mask, light therapy, LED therapy, skincare device, face mask timer, currentbody, dr dennis gross, omnilux, anti aging, acne light therapy, red light face

### Category
Primary: Health & Fitness
Secondary: Lifestyle

### Description
Your LED face mask deserves a better app.

LEDmask transforms your LED light therapy treatments from guesswork into guided sessions. Whether you own a CurrentBody, Dr. Dennis Gross, Omnilux, or any other device — LEDmask works with ALL of them.

WHAT'S INSIDE:
• Smart treatment timer with wavelength-specific guidance
• 8 skin concern protocols (acne, anti-aging, brightness, redness & more)
• 30+ LED face mask comparison guide with specs and pricing
• Session streak tracker and progress calendar
• Expert education on LED therapy science and safety

NO MORE GUESSING:
Which color for your skin concern? How long should you go? How often? LEDmask answers all of it with dermatologist-informed protocols tailored to your skin goals.

HOW IT WORKS:
1. Choose your skin concern
2. LEDmask picks the right wavelength and duration
3. Tap Start and relax — the timer guides you
4. Track your sessions and watch your skin transform

No accounts. No subscriptions to start. Just better skin, one session at a time.

Works with every LED face mask brand. Universal companion for light therapy.

### Pricing
- **Model**: Free limited, Premium $2.99 one-time
- **Reasoning**: Free tier = timer + 1 protocol. Premium = all protocols, full mask guide, progress tracking, education.
- **Monetization Path**: Brand partnerships in mask comparison section, skincare product affiliate links.

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | LED Face Mask +1,800%, TheraFace +3,900%, at-home beauty device market $2.4B growing |
| App Gap | 8/10 | One poor-quality brand-locked app exists. No universal companion. Quality gap confirmed. |
| Build Simplicity | 8/10 | Timer + content + calendar tracking. Simple SwiftUI. No camera, no ML. |
| Evergreen Potential | 7/10 | Skincare is permanent. LED therapy specifically growing. But device could evolve away from masks. |
| Monetization | 7/10 | $2.99 feasible. Affiliate to mask brands highly complementary. Market-specific audience willing to pay. |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: LOW — LED therapy has clinical backing (not a fad). Device market growing 15%+ annually.
- **App Store Rejection**: LOW — Standard utility/education app. No medical claims. Add disclaimer: "not medical device."
- **Competition**: MEDIUM — Brands could make better own-apps. But UNIVERSAL angle protects (works with ALL masks). First mover matters.
- **Legal/IP**: LOW — No brand logos or trademarks in listings. Use brand names for reference only (nominative fair use). Add disclaimer.
- **Content Maintenance**: MEDIUM — New masks launch quarterly. Protocol data can be updated via app updates. Low effort (< 1 hour/quarter).
- **Existing Idea Conflict**: Adjacent to "Red Light Therapy Guide" but different — that's for panels/bulbs, this is for wearable face masks. Clear differentiation.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Exploding Topics +1,800%, TheraFace +3,900%, market size $2.4B)
- [x] App Store has only one poor-quality competitor (Shining Mask 3.2★) — universal gap confirmed
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial (treatment protocols, device specs, safety education)
- [x] No obvious legal/copyright issues (trademark fair use for product names)
- [x] Build time estimate ≤ 3 hours (2.5 hours)
- [x] Differentiated from existing "Red Light Therapy Guide" (panels vs. wearable face masks)

---

## Build Instructions for Coding Agent

### Step-by-Step Build Order
1. Create Xcode project — SwiftUI iOS 16.0+, name "LEDmask"
2. Define data models (Protocol, LEDMask, UserSession, Article)
3. Build bundled JSON: protocols.json (8 items), masks.json (30 items), articles.json (8 items)
4. Build Home screen — "Start Treatment" button, current protocol display, streak counter, "continue where you left off"
5. Build Protocols List — Grid of 8 skin concern cards with wavelength color coding
6. Build Timer Screen — Large countdown, wavelength indicator, session info, "Session Complete" state
7. Build Mask Guide — Sortable/filterable list of 30+ masks with spec cards
8. Build Progress/Calendar — Calendar grid showing logged sessions, streak visualization
9. Build Learn Section — Article list with content
10. Add tab bar, polish, dark mode
11. Add StoreKit Pro unlock

### Data Model

```swift
struct TreatmentProtocol: Codable, Identifiable {
    let id: String  // e.g., "acne-clearing"
    let name: String  // e.g., "Acne Clearing"
    let skinConcern: String  // e.g., "Acne & Breakouts"
    let description: String
    let wavelength: Wavelength  // blue, red, green, amber, nearIR, combination
    let durationMinutes: Int  // e.g., 10
    let sessionsPerWeek: Int  // e.g., 3
    let totalWeeks: Int  // e.g., 8
    let complementaryTips: [String]
    let cautions: [String]
}

enum Wavelength: String, Codable {
    case blue = "415nm Blue"
    case red = "630nm Red"
    case green = "525nm Green"
    case amber = "590nm Amber"
    case nearIR = "830nm Near-Infrared"
    case combination = "Multi-wavelength"
}

struct LEDMaskDevice: Codable, Identifiable {
    let id: String  // e.g., "currentbody"
    let brand: String
    let model: String
    let priceUSD: Double
    let wavelengthsOffered: [String]
    let isFDA: Bool
    let wireless: Bool
    let coverage: String  // "Full face" | "Half face" | "Targeted"
    let powerMW: String  // e.g., "30 mW/cm²" or "Unknown"
    let sessionMinutes: Int
    let whereToBuy: String
    let rating: String  // e.g., "4.3★"
}

struct UserSession: Codable, Identifiable {
    let id: UUID
    let protocolId: String
    let date: Date
    let completed: Bool
    let notes: String?
}
```

### Testing Checklist
- [ ] Timer counts down correctly for each protocol duration
- [ ] Session logging works and persists across app launches
- [ ] Streak counter accurate (7-day streak, reset on miss)
- [ ] All 30 masks display with correct specs
- [ ] Protocol cards show correct wavelength color coding
- [ ] No network/airplane mode entirely functional
- [ ] iPhone SE layout does not break (timer must be readable)
