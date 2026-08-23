# App Idea: GlowPlan — IPL Hair Tracker

*Generated: 2026-08-23*
*Confidence Score: 7.6/10*

---

## Pitch
At-home IPL/laser hair removal devices are a 450%-growth hardware category, and every serious user follows a strict 12-week session schedule with skin-tone-dependent intensity levels. Yet the App Store only offers device-locked companion apps (Braun, Philips Lumea, Silk'n — rated 1.42★) and salon booking platforms. GlowPlan is the brand-neutral treatment companion: set up your plan per body zone, log sessions with intensity and photos-free progress notes, follow the Fitzpatrick skin-tone chart for safe settings, and get a maintenance-phase schedule after week 12. Works whether you own Ulike, Braun, Philips, Nira, Silk'n, or a no-name Amazon device.

## Target Audience
- Primary: Women 22–45 using at-home IPL devices, mid-way through a 12-week initial phase, juggling schedules across body zones
- Secondary: Buyers deciding between devices (comparison table); waxing/shaving converts planning their transition
- Demographics: Beauty-tech spenders, US/UK/EU, high iOS share, motivated by routine adherence

## Problem Statement
IPL results depend entirely on consistency: weekly sessions for 12 weeks, then touch-ups — per body zone, with intensity matched to skin tone. Users currently track this with phone Notes, paper calendars, or the manufacturer's app — which locks to one brand, nags with marketing, and in Silk'n's case holds a 1.42-star rating. Switching devices or owning two brands means two apps. Nobody serves the neutral, private, offline tracking job.

## Trend Evidence
- **Source 1**: Exploding Topics — Laser Hair Removal Device +450% search growth; device category expanding annually (Ulike, Braun, Philips, Amiro all shipping new models)
- **Source 2**: Device makers ship trackers themselves (Ulike web tracker, Braun/Lumea/Avanor apps) — evidence the tracking job is real enough to build software for
- **Source 3**: Beauty blogs publish "IPL hair removal schedule: weekly plan" explainers (MITHLUX, Belis Laser) — content demand for scheduling knowledge with no good tool answer
- **Momentum**: Rising — steady category growth rather than spike

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Braun IPL app | ⭐ 4.62 (1,243) | Free | Braun devices only; marketing push notifications |
| Philips Lumea IPL | ⭐ 4.76 (1,006) | Free | Philips devices only |
| Silk'n Hair Removal | ⭐ 1.42 (43) | Free | Quality gap exemplar — poorly rated companion |
| Avanor IPL | unrated (new) | Free | Single-brand |
| Booksy / Fresha / LaserAway | ⭐ ~4.8 | Free | Salon booking — different job (professional treatments) |
| Aesthetic Diary | 0 ratings | Free | Generic medspa treatment log; no IPL protocol intelligence |

**App Gap**: Fragmented. Companions exist but each is device-locked; salon platforms serve clinics. A neutral cross-brand tracker with protocol intelligence (skin-tone chart, zone schedules, maintenance phase) does not exist. Silk'n's 1.42★ shows even brand apps leave users stranded.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Zone-Based Plan Setup** — pick body zones (face, underarms, arms, legs, bikini, back/chest), get a per-zone weekly schedule aligned to the standard 12-week protocol with rest-day spacing
2. **Session Logging** — one-tap log per zone: date, intensity level used, minutes, skin reaction note; streak and adherence stats
3. **Skin-Tone Safe Settings Chart** — Fitzpatrick scale I–VI guide mapping tone → recommended starting intensity and cautions (with verbatim patch-test disclaimer)
4. **Maintenance Scheduler** — after week 12, auto-transitions zones to monthly touch-up cadence with due indicators
5. **Device Comparison Table** — static reference of major device classes (diode vs IPL, energy ranges, cap sizes) to help choosers — no affiliate links

### Nice-to-Have (v1.1+)
- Local reminders for due sessions — deferred: notification permission + timezone edge cases cost build time; v1.0 uses a "due today" home badge instead
- Progress journal with optional encrypted photos — deferred: privacy/review complexity
- Multiple profiles — deferred: single-user assumption for v1.0

## Content & Data
- Protocol templates (initial weeks 1–12 weekly; maintenance monthly), Fitzpatrick chart (6 tones × guidance/cautions), zone catalog (~8 zones with session-time hints), device class comparison (~10 rows), FAQ (~15 entries)
- Source: manufacturer published manuals (protocol norms), dermatology public guidance — curated, no medical claims
- MVP: all static JSON (~75 min authoring). Future: protocol updates rare

## Design Direction
- **Style**: Clean clinical-calm — spa-like serenity, generous rounding, soft gradients, progress-forward
- **Color Palette**: Porcelain background `#F7F5F2`, Soft lilac primary `#B9A7D9`, Deep plum text `#33283E`, Mint success `#8FCBB0`, Coral warning `#E8998D`, Slate divider `#DCD7D0`
- **Typography**: SF Pro Rounded headers (friendly-clinical), SF Pro body
- **Key Screens**: Home (today's due zones + streak), Plan Setup, Zone Detail (log history), Skin-Tone Chart, Devices, Settings
- **Navigation**: Tab bar (Today, Plan, Chart, More) + stack pushes
- **Reference Apps**: Contrast Therapy Protocol (session-tracking pattern), EyeGym (daily practice loop)

## Technical Notes
- **Platform**: iOS (SwiftUI), iOS 16+
- **Backend**: None — fully on-device
- **APIs**: None; NO local notifications in v1.0 (zero-permission install)
- **Data Storage**: SwiftData/UserDefaults for logs; bundled JSON for protocol/chart/device data
- **Estimated Build Time**: 2.5 hours
- **Complexity**: Medium-Low (date math per zone is the trickiest part)

**First-launch disclaimer (verbatim requirement)**: "GlowPlan is a personal scheduling and logging tool. It is not a medical device and does not provide medical advice. Always follow your device manufacturer's instructions for intensity, session length, and contraindications. Perform a patch test before first use and consult a dermatologist if you are unsure, pregnant, or taking photosensitizing medication."

## App Store Listing

### Title
GlowPlan — IPL Hair Tracker

### Subtitle
Sessions, schedule & skin tone

### Keywords
ipl,laser hair removal,home laser,beauty schedule,treatment log,smooth skin,epilation,device tracker

*(98 chars)*

### Description
Stop guessing when your next IPL session is due. GlowPlan is the brand-neutral tracker for at-home laser and IPL hair removal — built for YOUR routine, whatever device you own.

WORKS WITH ANY DEVICE
Ulike, Braun, Philips Lumea, Silk'n, Amiro, or an unbranded Amazon find — GlowPlan isn't tied to one manufacturer. No marketing pings, no upsells. Just your plan.

YOUR 12-WEEK PLAN, HANDLED
Set up body zones once — underarms, legs, bikini, face, and more — and get a clear weekly schedule based on standard IPL protocols. See what's due today, what you completed, and your adherence streak at a glance.

LOG IN ONE TAP
Record intensity level, session time, and a quick reaction note per zone. Over weeks, watch your consistency build — the single biggest factor in IPL results.

SKIN-TONE SMART
A built-in Fitzpatrick scale chart maps your skin tone to sensible starting intensities and key cautions, so safer settings are always one glance away.

MAINTENANCE, AUTOMATED
After the initial phase, zones shift smoothly to a monthly touch-up cadence with clear due indicators — so results don't quietly slip.

PRIVATE BY DESIGN
• 100% offline, zero permissions requested
• No accounts, no tracking, no data collected
• Includes a static device-class comparison for anyone still choosing

Note: GlowPlan is a scheduling and logging tool — not medical advice. Always follow your device manufacturer's instructions and perform a patch test first.

Your smoothest 12 weeks start here.

### Category
Primary: Health & Fitness
Secondary: Lifestyle

### Pricing
- **Model**: Paid $2.99
- **Reasoning**: Buyer owns a $200–500 device; $2.99 organization tool is an easy add-on purchase; utility used weekly for months justifies paid over ads
- **Monetization Path**: One-time paid now; v1.1 reminder pack or couple-profile IAP possible

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | +450% growth; steady hardware-driven demand, not explosive |
| App Gap | 8/10 | Only device-locked companions (one at 1.42★); neutral tracker unclaimed |
| Build Simplicity | 8/10 | Standard tracker patterns; per-zone date logic adds care |
| Evergreen Potential | 8/10 | Hair removal demand permanent; devices keep selling |
| Monetization | 7/10 | Motivated buyer, weekly-use utility, $2.99 sticks |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: Very Low — tied to hardware adoption curve, not a hashtag
- **App Store Rejection**: Low — wellness utility with disclaimers; avoids medical claims; Review Note 1.4.1 (medical) risk minimized by "not a medical device" language
- **Competition**: Medium — Braun/Philips could open their apps to all devices (unlikely near-term); another indie could ship first — speed matters
- **Legal/IP**: Low — no brand logos; device names in comparison table are nominative fair use; keep descriptions factual
- **Content Maintenance**: Low — protocol norms stable; annual device-table refresh

## Validation Checklist
- [x] At least 3 sources confirm rising trend (ET growth, maker-built trackers, blog demand)
- [x] App Store search shows no brand-neutral tracker; nearest comps locked or 1.42★
- [x] MVP can be built without backend/API dependencies (zero permissions)
- [x] Content factual with verbatim disclaimers (health-adjacent gate passed)
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours (2.5h)
