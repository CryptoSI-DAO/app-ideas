# App Idea: SunGuard — Sunscreen Guide & SPF Coach

> **Pitch**: A smart sunscreen companion: SPF education, skin-type assessment, reapplication reminders, and UV-index-based protection coaching — all in one beautiful app.

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | Birch Juice Sunscreen #45 on Exploding Topics (+2,100%); LED Face Mask +1,800%; UV awareness rising year-over-year |
| App Gap | 8/10 | Competition split: UV weather apps (SunSafe 10K rev) OR timer-only apps (REAPPLY 33 rev). NO app combines education + timer + coaching. |
| Build Simplicity | 8/10 | Bundled JSON for SPF/skin education. Local notifications for reapp. No backend needed. |
| Evergreen Potential | 8/10 | Skin cancer awareness is structural. SPF use is daily recurring behavior. Summer peaks but year-round need. |
| Monetization | 8/10 | Free core (timer + UV education) + $1.99 Pro (skin profile, product finder, family accounts) |
| **Average** | **7.8/10** | |

## The Opportunity

Sunscreen apps exist but are fragmented:
- **UV Index weather apps** (SunSafe, UV Index Widget) — Tell you UV level but don't coach sunscreen application
- **Simple timers** (REAPPLY, Squak) — Just a notification timer, no education
- **Tanning apps** (Beam Tanning) — Focused on tanning, opposite goal

No iOS app combines ALL of the following:
1. SPF education (what SPF means, chemical vs mineral, PA ratings)
2. Skin type assessment (Fitzpatrick scale quiz)
3. Personalized reapplication schedule based on UV index + skin type
4. Product finder by category (face, body, water-resistant, kids)
5. Family profiles (different skin types, different SPF needs)

## App Store Gap Analysis

| App | Reviews | Rating | Type | Gap |
|-----|---------|--------|------|-----|
| SunSafe: UV Index & Tanning | 10,254 | 4.77 | Weather app | No sunscreen coaching, just UV display |
| UV Index Widget - Worldwide | 14,258 | 4.76 | Weather app | Same — UV only |
| REAPPLY: Sunscreen Timekeeper | 33 | 3.42 | Timer only | No education, poor rating |
| Squak Sunscreen Reminders | 13 | 4.92 | Timer only | Tiny, feature-sparse |
| SPF - Tan Timer & UV Tracker | 4,755 | 4.57 | Tanning-focused | Wrong goal (tan vs protect) |
| Sunface - UV-Selfie | 271 | 4.32 | Camera/filter | No education or timer |

**The gap**: A comprehensive sunscreen coach that's educational + actionable + personalized.

## Social Context
- Skin cancer awareness growing post-pandemic
- "Slap of sunscreen" selfie culture on social media
- Dermatologists increasingly recommend daily SPF
- Birch Juice Sunscreen trending shows consumers actively seeking better sun protection

## Competitor Weaknesses
1. **UV Weather apps** — Don't connect UV to action (apply/reeapply sunscreen)
2. **Timer apps** — No personalevery user gets same 2-hour reminder regardless of skin type or UV)
3. **All existing apps** — No skin type quiz, no family mode, no SPF education layer

## Requirements Summary

- **Name**: SunGuard
- **Bundle ID**: com.cryptosi.sunguard
- **Platform**: iOS 16+
- **Core Flow**: Skin type quiz → Get personalized SPF recommendation → Set reapplication timer → Track protection streaks
- **Data**: Bundled JSON (skin types, SPF guide, product categories). Local notifications.
- **Build Time**: ~2 hours
- **Price**: Free (timer + UV education) + $1.99 Pro unlock (skin profiles, streaks, product finder)
- **Category**: Health & Fitness > Medical

## Risks
- No live UV data (would need API — rejected). Workaround: Use bundled UV zone info by region, or let users input local UV index manually
- Regulatory: Avoid medical claims ("protects against skin cancer" → use "dermatologist recommended daily SPF")
- Seasonality in Northern Hemisphere (mitigate with indoor/UV-through-windows messaging)
