# App Idea: Wonders — Interactive Architecture Guide to the World's Most Amazing Buildings

*Generated: 2026-06-05*
*Confidence Score: 7.4/10*

---

## Pitch

A visually stunning, fully offline iOS guide to the world's most amazing buildings — from the Sagrada Familia (trending today at 10K+ searches) to the Sydney Opera House, Guggenheim Bilbao, and 30+ more architectural masterpieces. Each building gets an interactive card with construction timeline, architectural style breakdown, fun facts, visiting info, and a "build it in LEGO" connection. Perfect for architecture enthusiasts, travelers, and curious minds who look at buildings and wonder "how did they build THAT?"

## Target Audience
- Primary: Architecture enthusiasts, travelers, and design-minded people aged 25-55
- Secondary: Students of architecture, LEGO fans interested in architecture sets, tourists planning trips
- Demographics: US/UK/Global, iOS-leaning, skews educated and affluent, interests in travel, design, art, photography

## Problem Statement
Architecture content is scattered across Wikipedia, travel blogs, and Instagram accounts. There's no single, beautiful, offline-first app dedicated to the world's architectural wonders. When something like "Lego Sagrans Familia" trends (5K+ searches today), people want to learn more about the actual building — its history, design, when it'll be finished — but there's no beautiful app that satisfies that curiosity. Pinterest and Wikipedia are the current "apps" for this, and neither is designed for the task.

## Trend Evidence
- **Source 1**: Google Trends — "sagrada familia" at 10K+ searches (+300%), "lego sagrada familia" at 5K+ searches (+100%) in Shopping category today. Architecture/travel interest is spiking.
- **Source 2**: Cultural trend — LEGO Architecture sets are one of LEGO's fastest-selling product lines. The intersection of architecture + LEGO + travel content is a growing niche on Instagram and YouTube.
- **Source 3**: App Store Gap — Searching "architecture guide" or "world wonders" returns travel apps (TripAdvisor, Lonely Planet) or generic photo apps. No dedicated architecture wonder guide exists.
- **Momentum**: Sustained — architecture tourism is post-COVID boom. Travel content is at all-time highs on social media.

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| TripAdvisor | ⭐ 4.5 | Free | Generic travel, no architecture focus, requires internet |
| LEGO Builder | ⭐ 4.4 | Free | LEGO-only, no real architecture education |
| Wikipedia | ⭐ 3.8 | Free | Text-heavy, no visual experience, requires internet |
| ArchDaily | ⭐ 3.5 | Free | News-focused, professional audience, not tourist-friendly |

**App Gap**: No app combines beautiful architecture photography, educational content, visiting information, and LEGO/creative connections in one offline package.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Building Cards** — 30+ architectural wonders, each with: hero illustration (SF Symbols + shape-based art), name, location, year started/completed, architectural style, and 3 fun facts.
2. **Construction Timeline** — Visual timeline showing when each building was started, key construction milestones, and completion date (or "still under construction" for Sagrada Familia).
3. **Architecture Style Guide** — 10 architectural styles (Gothic, Modernist, Brutalist, Art Deco, etc.) with descriptions, key features, and which buildings exemplify each style.
4. **Visiting Info** — City, country, best time to visit, estimated visit duration, and one "pro tip" per building.
5. **Favorites & Bucket List** — Mark buildings as "Visited" or "Want to Visit" with a personal bucket list view.

### Nice-to-Have (v1.1+)
- AR view: "See this building in your room" using ARKit
- Map view showing all buildings on a world map
- LEGO set info for buildings that have LEGO versions
- "Architecture style quiz" — which style are you?
- Widget showing "Building of the Day"

## Content & Data
- **Buildings**: 30 architectural wonders spanning 6 continents and 2,000+ years of construction
- **Styles**: 10 architectural styles with descriptions
- **Data per building**: Name, location, coordinates, years, architect, style, 3 fun facts, visiting info, bucket list flag
- **Sources**: Public domain architectural records, UNESCO World Heritage data, original writing
- **Images**: No photos needed — use SF Symbols + SwiftUI shapes for a stylized, illustrated look (faster to build, unique aesthetic)
- **Content effort**: ~6-8 hours to research and write

## Design Direction
- **Style**: Clean, architectural, gallery-like — think Apple Design Awards meets Frank Lloyd Wright
- **Color Palette**:
  - Primary: #1C2541 (deep navy)
  - Secondary: #3A506B (slate blue)
  - Accent: #5BC0BE (teal/turquoise)
  - Background: #F0F4F8 (light gray-blue)
  - Text: #1C2541
  - Card BG: #FFFFFF
  - Gold accent: #D4AF37 (for "wonder" badge)
- **Typography**: SF Pro Display (headings — bold weight), SF Pro Text (body), monospaced for dates/dimensions
- **Key Screens**: Home (Featured Building), All Buildings (grid), Building Detail, Styles, Bucket List, Settings
- **Navigation**: Tab bar (Explore, Styles, Bucket List) + detail push navigation
- **Reference Apps**: Apple Maps (card design), Museum apps (gallery layout), Dark Sky (information density)

## Technical Notes
- **Platform**: iOS 17+ (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None
- **Data Storage**: Bundled JSON files (buildings, styles)
- **Estimated Build Time**: ~2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
Wonders — Architecture Guide

### Subtitle
30+ buildings that defy belief

### Keywords
architecture,building,wonders,sagrada familia,travel,design,world heritage,lego architecture,tourist,guide,landmark,famous buildings

### Description
🏛️ Discover the world's most extraordinary buildings.

From the 130-year construction of the Sagrada Familia to the gravity-defying Marina Bay Sands, Wonders is your beautifully designed guide to the buildings that make you stop and stare.

EXPLORE 30+ ARCHITECTURAL WONDERS
• Sagrada Familia, Sydney Opera House, Guggenheim Bilbao, and 27+ more
• Each building with construction timeline, style breakdown, and fun facts
• Stylized illustrations (no internet needed!)

LEARN ARCHITECTURAL STYLES
• Gothic, Modernist, Brutalist, Art Deco, and 6+ more
• Clear explanations with visual examples
• Which style is your favorite?

TRACK YOUR TRAVELS
• Mark buildings as "Visited" or "Want to Visit"
• Personal bucket list
• Perfect for architecture-curious travelers

BUILT FOR THE CURIOUS MIND
• Works 100% offline — perfect for airplane mode
• No ads, no tracking, no accounts
• Beautiful typography and design on every screen

### Category
Primary: Travel
Secondary: Education

### Pricing
- **Model**: Paid, $2.99
- **Reasoning**: Niche educational/travel content commands $2.99-$4.99. Comparable to Lonely Planet guides (which are $5-10). Value proposition is high for the target audience.
- **Monetization Path**: Expand with more buildings (Wonders Volume 2), city-specific packs, or AR features as premium upgrades.

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 6/10 | Sagrada Familia and Lego architecture are trending today, but this is more of a sustained niche interest than a viral moment. LEGO Architecture is a growing product line. |
| App Gap | 9/10 | No dedicated architecture wonder guide app exists. Travel apps are too general. LEGO apps are too product-specific. |
| Build Simplicity | 8/10 | Pure content app. Visual design is the main challenge — using SF Symbols + SwiftUI shapes for illustrations instead of photos. No backend needed. |
| Evergreen Potential | 9/10 | Architecture is timeless. These buildings have been wonders for decades and will continue for centuries. Travel planning is a perennial use case. |
| Monetization | 6/10 | $2.99 is reasonable but niche audience limits volume. Series potential (city packs, more buildings) is the real play. |
| **Average** | **7.4/10** | |

## Risk Assessment
- **Trend Fizzle**: Low risk — architecture and travel are evergreen interests. Sagrada Familia will be under construction for another 10+ years, maintaining relevance.
- **App Store Rejection**: Low risk — educational/travel content, no copyright issues with original writing.
- **Competition**: Low risk — the space is empty. If travel apps add architecture features, it validates the concept.
- **Legal/IP**: Low risk — building facts are public domain. No photos needed (using stylized illustrations).
- **Content Maintenance**: Very low — buildings don't change much. Update when Sagrada Familia completes (estimated 2028-2030).

## Validation Checklist
- [x] At least 3 sources confirm the opportunity (Google Trends today, LEGO Architecture growth, App Store gap)
- [x] App Store search shows 0 dedicated architecture wonder guide apps
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours (2.5 hours)
