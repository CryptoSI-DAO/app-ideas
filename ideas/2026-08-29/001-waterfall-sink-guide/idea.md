# App Idea: Cascade — Waterfall Kitchen Sink Buying Guide

*Generated: 2026-08-29*
*Confidence Score: 7.5/10*

---

## Pitch

A curated buying guide for waterfall kitchen sinks — compares 20+ models by price, material, size, and install type with a simple "which sink for my kitchen" quiz and real user scenarios.

## Target Audience

- **Primary**: Homeowners (30–65) planning a kitchen remodel or sink replacement
- **Secondary**: Renters upgrading their rental kitchen, DIY renovators
- **Demographics**: US/UK/Canada/Australia, homeowners or people renting single-family homes, people with $500–$3000 sink budget

## Problem Statement

Waterfall kitchen sinks are exploding in popularity (740% search growth, #13 on Exploding Topics Aug-2026) — but the App Store has ZERO dedicated buying guides. All top iTunes results are wrong-category pollution: kitchen design apps, plumbing supply catalogs, and kids' games. On Reddit (r/kitchen, 1.3M subscribers in r/DidntKnowIWantedThat), consumers are actively asking "where can I buy a good waterfall sink?" and "is this a gimmick?" — there's real demand for a curated, trustworthy guide. The entire buying decision is served by scattered blog posts and YouTube reviews — no native app exists.

## Trend Evidence

- **Exploding Topics**: "Waterfall Kitchen Sink" ranked #13 on the Aug-2026 list with 740% 5-year search growth
- **iTunes Search API**: Queries for "waterfall kitchen sink," "best waterfall kitchen sink," "kitchen sink buying guide" return ZERO dedicated apps — all top results are wrong-category (kitchen design apps, plumbing fittings, games) = GREEN FIELD gap signal
- **Reddit (DDG proxy)**: Active discussion in r/kitchen ("Looking for a good waterfall sink! Any leads?"), r/DidntKnowIWantedThat (7.6K votes, 215 comments), multiple buying-guide blog posts ranking for the keyword
- **Momentum**: Rising — kitchen remodeling is a durable category; waterfall sinks are a sub-trend with staying power

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Kitchen Design PRO | ⭐ 4.5 | Free | Kitchen design tool, not a sink buyer's guide |
| Flume Water | ⭐ 4.7 | Free | Smart water monitor, wrong product category |
| Ruhe - Kitchen & Bath Fittings | ⭐ 4.7 | Free | Plumbing fittings catalog, not a consumer buying guide |
| Pro-Fit Kitchen Designer | ⭐ 3.0 | Free | Kitchen design app, zero sink comparison |

**App Gap**: ALL top results are wrong-category — kitchen design tools, plumbing supply catalogs, and kids' games. Zero apps exist that help consumers compare, evaluate, or choose a waterfall kitchen sink. The buying-guide layer is entirely served by text-based blog posts and YouTube reviews — no native app exists.

## Core Features (MVP)

### Must-Have (v1.0)

1. **Sink Catalog** — 20–30 curated waterfall kitchen sinks with specs (size, material, bowl count, mounting type, price range, gauge, finish options, noise rating)
2. **"Which Sink for Me" Quiz** — 6-question interactive quiz matching user needs (budget, cabinet size, primary use, style preference, installation type, faucet compatibility) to the best 2–3 sinks
3. **Comparison Mode** — Side-by-side spec comparison of 2–4 selected sinks with key differentiators highlighted
4. **Use Case Guides** — Pre-written recommendations: "Best under $500," "Best for 36-inch cabinet," "Best granite composite," "Best stainless steel," "Best for small kitchens"
5. **Offline-Only** — Fully on-device, no network calls, no data collection

### Nice-to-Have (v1.1+)

- **Price tracker** — monitor Amazon prices (deferred: requires web scraping, breaks offline story)
- **User review summary** — aggregate real buyer feedback per product (deferred: requires ongoing content maintenance)
- **Installation guide videos** — deferred: increases app size significantly

## Content & Data

- **Sink catalog**: 20–30 waterfall kitchen sinks with full spec sheets, curated from public product pages and retailer listings
- **Use case guides**: 8–12 scenario-based recommendations
- **Quiz logic**: Simple rule-based matching algorithm
- **Source**: Public product pages, retailer listings, manufacturer specs
- **MVP content size**: ~150KB of JSON — trivial for an offline app

## Design Direction

- **Style**: Clean, modern, slightly luxurious — think "Wirecutter" meets "Architectural Digest" — product-focused, not cute
- **Color Palette**: Background #F5F5F7, Primary #007AFF (Apple blue), Text #1D1D1F, Secondary #8E8E93, Accent #FF9500
- **Typography**: SF Pro Display (system), headings at 28/22/17, body at 17, caption at 13
- **Key Screens**: Home (use case categories), Sink Detail (full specs + recommendation), Comparison (side-by-side), Quiz (interactive), Settings
- **Navigation**: Tab bar — Home, Catalog, Comparison, Quiz, About
- **Reference Apps**: Wirecutter (editorial authority), This Old House kitchen guides

## Technical Notes

- **Platform**: iOS (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON in app bundle
- **Estimated Build Time**: ~2 hours
- **Complexity**: Low — mostly static content with simple quiz/comparison logic