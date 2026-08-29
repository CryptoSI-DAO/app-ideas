# App Idea: PassKey Companion — Passwordless Consumer Guide

*Generated: 2026-08-27*
*Confidence Score: 8.0/10*

---

## Pitch

A plain-English guide to going passwordless — explains passkeys, face/fingerprint unlock, and recovery in everyday language, with a step-by-step migration checklist that walks consumers through replacing every account without ever seeing a password.

## Target Audience

- **Primary**: Everyday consumers (30–60) who want to stop managing passwords but don't know where to start
- **Secondary**: Tech-curious seniors and non-native English speakers who got overwhelmed by password managers
- **Demographics**: US/UK/Canada/Australia, smartphone users, people with 20+ online accounts

## Problem Statement

Password managers (LastPass, 1Password, Keeper) are everywhere — but millions of consumers still don't use one, or use one poorly. The App Store is saturated with *tools* (password generators, authenticator apps) but has ZERO plain-English *guides* that walk a consumer through the actual migration process. Google Trends shows "passwordless" at 1,750% growth — the demand is real, the educational supply is zero.

## Trend Evidence

- **Exploding Topics**: "Passwordless" ranked #97 on the Aug-2026 list with 1,750% 5-year search growth
- **Google Trends RSS**: Consistent searches around "passwordless authentication" and "how to go passwordless" across the past 30 days — sustained, not fad
- **Apple/Google push**: Apple's Passkey launch (WWDC 2022) and Google's Passwordless Day are driving ecosystem-level adoption; every major platform now supports passkeys
- **Momentum**: Rising — the infrastructure exists; the consumer education layer does not

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Keeper Password Manager | ⭐ 4.9 | Free (IAP) | Tool, not guide — assumes you already understand passwordless |
| Duo Mobile | ⭐ 4.9 | Free | Enterprise 2FA — consumer-unfriendly, no education layer |
| Authenticator App | ⭐ 4.6 | Free | Code generator only — no migration walkthrough |
| Password Manager - Safe Lock | ⭐ 4.5 | Free | Generic password tool, zero passkey education |

**App Gap**: ALL top results are *tools* for people who already know what they're doing. Zero consumer-friendly educational guides that walk through the actual migration process account-by-account. The "passwordless" trend is exploding but the App Store has nothing to teach consumers how to participate.

## Core Features (MVP)

### Must-Have (v1.0)

1. **Passwordless 101 Primer** — A 5-screen walkthrough explaining what passkeys are, how face/fingerprint unlock works, and why it's safer than passwords — written in plain English with no jargon
2. **Account Migration Checklist** — A searchable list of 50+ major online services (banking, email, social, shopping, utilities) with toggle-complete checkboxes and per-service instructions on how to enable passkeys/2FA
3. **Recovery Guide** — What to do if you lose your phone or switch devices — how passkey recovery works across Apple/Google accounts, plus a printable emergency card template
4. **Passkey Compatibility Lookup** — A searchable database showing which services support passkeys (built from public documentation, updated via bundled JSON)
5. **Offline-Only** — No network calls, no data collection, fully on-device

### Nice-to-Have (v1.1+)

- **Personal migration timeline tracker** — progress bar across account categories
- **QR code scanner for enabling 2FA at point-of-sale** (deferred: requires camera permission, complicates privacy story)
- **Video tutorial library** — deferred: increases app size significantly

## Content & Data

- **Passkey compatibility database**: 50+ services with passkey support status, instructions per service, last-updated date (bundled JSON, refreshed quarterly)
- **Migration checklist**: Category-based (Banking, Email, Social, Shopping, Utilities, Health, Travel, Government) with 5–10 services per category
- **Recovery templates**: Printable emergency card, device-switch checklist, account recovery contact list
- **Source**: Public documentation from Apple, Google, FIDO Alliance, and each service's support pages
- **MVP content size**: ~200KB of JSON — trivial for an offline app

## Design Direction

- **Style**: Clean, trustworthy, modern — think "Apple Support" meets "Notion" — not cute, not gamified
- **Color Palette**: Background #F5F5F7, Primary #007AFF (Apple blue), Text #1D1D1F, Success #34C759, Warning #FF9500
- **Typography**: SF Pro Display (system), headings at 28/22/17, body at 17, caption at 13
- **Key Screens**: Home (primer + quick start), Checklist (category grid), Service Detail (per-service instructions), Recovery (emergency templates), Settings (no data, no ads)
- **Navigation**: Tab bar — Home, Checklist, Recovery, About
- **Reference Apps**: Apple's "Security" support pages, Google's "Passwordless" hub

## Technical Notes

- **Platform**: iOS (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON in app bundle
- **Estimated Build Time**: ~2 hours
- **Complexity**: Low — mostly static content with checklist state persistence

## App Store Listing

### Title
PassKey Companion (20 chars)

### Subtitle
Go passwordless in a day (27 chars)

### Keywords
passwordless, passkey, password, security, 2fa, authentication, account, migration, guide, checklist, privacy, safe, login, face id, touch id, fingerprint, authenticator, recovery, digital security, online safety

### Description
Tired of managing dozens of passwords? The passwordless revolution is here — but most people don't know how to actually switch. PassKey Companion is the plain-English guide that walks you through going passwordless, step by step.

Inside you'll find:
• A 5-minute primer explaining passkeys, Face ID, and fingerprint unlock in everyday language
• A 50+ service migration checklist — banking, email, social, shopping — with per-account instructions
• What happens if you lose your phone (recovery guide + printable emergency card)
• A searchable directory showing which services support passkeys right now

No passwords to remember. No technical jargon. No data collected — everything runs on your device.

Perfect for: people switching from password managers, seniors wanting simpler security, and anyone who's ever been locked out of an account.

### Category
Primary: Reference
Secondary: Productivity

### Pricing
- **Model**: Paid $2.99 upfront
- **Reasoning**: One-and-done purchase matches the "set it and forget it" security positioning; no subscription pressure, no ads
- **Monetization Path**: v1.1+ quarterly JSON updates ($0.99 IAP or free update for existing buyers); v2.0 could add a free companion web tool

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | 1,750% growth, strong but not #1-charting |
| App Gap | 9/10 | Zero consumer education guides; all top apps are enterprise/developer tools |
| Build Simplicity | 9/10 | Static content + checklist = ~2h build, no backend |
| Evergreen Potential | 8/10 | Passwordless is a decade-scale infrastructure shift; content stays relevant |
| Monetization | 7/10 | $2.99 upfront, thin margins but low effort; quarterly update path |
| **Average** | **8.0** | |

## Risk Assessment

- **Trend Fizzle**: LOW — passwordless is a fundamental security infrastructure shift, not a fad
- **App Store Rejection**: LOW — educational/reference content, no claims of security guarantees
- **Competition**: MEDIUM — a big publisher (Apple, Google, Nist) could release a similar guide for free
- **Legal/IP**: LOW — public information, no trademarked terms used in copy
- **Content Maintenance**: MEDIUM — passkey compatibility changes quarterly; plan for v1.1 update cycle
- **Content Accuracy**: IMPORTANT — must verify all service instructions before shipping; inaccurate security guidance is a liability

## Validation Checklist

- [x] At least 3 sources confirm rising trend (Exploding Topics, Google Trends, Apple ecosystem push)
- [x] App Store search shows zero consumer education guides (all top apps are tools)
- [x] MVP can be built without backend/API dependencies (fully offline)
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours (~2h estimated)