# App Idea: Persepolis Companion — The Definitive Graphic Novel Guide

*Generated: 2026-06-05*
*Confidence Score: 7.6/10*

---

## Pitch

A beautifully crafted, fully offline companion app for Marjane Satrapi's masterpiece "Persepolis" — the autobiographical graphic novel about growing up during the Iranian Revolution. The app provides chapter-by-chapter summaries, character profiles, historical context, thematic analysis, and a visual timeline of the Iranian Revolution. With Persepolis trending at 100K+ searches today (1,000% increase) due to renewed cultural interest, this app serves readers, students, and book clubs who want to go deeper into one of the most important graphic novels of the 21st century.

## Target Audience
- Primary: Readers aged 18-40 who are reading or have read Persepolis (book clubs, college students, graphic novel enthusiasts)
- Secondary: Educators teaching Middle Eastern history, graphic novel studies, or memoir writing
- Demographics: US/UK/Canada, college-educated, iOS-leaning, interests in literature, history, social justice

## Problem Statement
Persepolis is one of the most assigned books in US colleges and is experiencing a massive resurgence in popularity. But readers — especially those unfamiliar with Iranian history — struggle with the historical context. There's no dedicated, well-designed app that provides chapter summaries, character guides, and historical context in one place. Existing resources are scattered across SparkNotes, Wikipedia, and random blog posts. A dedicated companion app fills this gap.

## Trend Evidence
- **Source 1**: Google Trends — "marjane satrapi" at 100K+ searches today (+1,000%), "persepolis" and "persepolis book" as related trending queries. This is a breakout-level spike.
- **Source 2**: Cultural momentum — Persepolis has been banned/challenged in multiple US school districts in 2024-2025, generating significant media coverage and driving curiosity-driven reads (the "Streisand Effect").
- **Source 3**: App Store Gap — Searching "persepolis" or "graphic novel guide" returns zero relevant apps. The educational/literary companion app space is underserved.
- **Momentum**: Rising — driven by book bans, cultural conversations about censorship, and the graphic novel's 20th anniversary.

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| SparkNotes (general) | ⭐ 4.2 | Free | Covers Persepolis but generic, ad-heavy, no visual elements, no character maps |
| LitCharts | ⭐ 4.0 | Subscription | Text-heavy, no interactive features, no historical timeline |
| Goodreads | ⭐ 4.5 | Free | Social features only, no chapter content or analysis |

**App Gap**: No dedicated Persepolis companion app exists. General study guides are text-heavy and ad-laden. An app with visual character maps, interactive timelines, and curated historical context would be unique.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Chapter Guide** — All 20 chapters with 2-3 sentence summaries, key quotes, and discussion questions. Organized in a clean list with progress tracking.
2. **Character Profiles** — 15+ character cards with name, relationship map, key quotes, and role in the story. Visual character relationship diagram.
3. **Historical Timeline** — Interactive timeline of the Iranian Revolution (1978-1984) with key events, photos (public domain), and connections to the story's events.
4. **Themes Explorer** — 8 major themes (Identity, Revolution, Feminism, Exile, Family, War, Freedom, Coming of Age) with explanations and chapter references.
5. **Reading Tracker** — Mark chapters as read, track reading progress, set reading goals.

### Nice-to-Have (v1.1+)
- Audio narration of key quotes
- Book club discussion mode (share questions, track group progress)
- "Iran Today" section with modern context
- Marjane Satrapi biography and other works
- Dark mode with sepia-toned theme (matching the book's black-and-white art style)

## Content & Data
- **Chapter summaries**: 20 chapters, ~200 words each
- **Character profiles**: 15 characters with relationships
- **Historical timeline**: 30+ events with dates and descriptions
- **Themes**: 8 themes with 300-word essays each
- **Discussion questions**: 3 per chapter (60 total)
- **Sources**: Public domain historical content, original analysis, SparkNotes-equivalent summaries (original writing, not copied)
- **Content effort**: ~10-12 hours of research and writing

## Design Direction
- **Style**: Minimalist, literary, black-and-white with red accent (matching the graphic novel's aesthetic)
- **Color Palette**:
  - Primary: #1A1A1A (near black)
  - Secondary: #FFFFFF (white)
  - Accent: #E63946 (red — matching Persepolis cover)
  - Background: #FAFAFA (off-white)
  - Text: #1A1A1A
  - Card BG: #FFFFFF
  - Muted: #999999
- **Typography**: New York (Apple's serif font for literary feel), SF Pro Text for UI elements
- **Key Screens**: Home (Reading Progress), Chapter List, Chapter Detail, Characters, Timeline, Themes, Settings
- **Navigation**: Tab bar (Read, Characters, Timeline, Themes) + detail push navigation
- **Reference Apps**: Apple Books (reading experience), Streaks (progress tracking), Timeline apps

## Technical Notes
- **Platform**: iOS 17+ (SwiftUI)
- **Backend**: None — fully on-device
- **APIs**: None
- **Data Storage**: Bundled JSON files (chapters, characters, timeline events, themes)
- **Estimated Build Time**: ~2.5 hours
- **Complexity**: Low-Medium

## App Store Listing

### Title
Persepolis Companion — Graphic Novel Guide

### Subtitle
Chapter guide, characters & history

### Keywords
persepolis,marjane satrapi,graphic novel,book guide,iranian revolution,chapter summary,character guide,book club,literature,memoir

### Description
📖 The definitive companion app for Marjane Satrapi's masterpiece.

Persepolis Companion helps you understand, appreciate, and discuss one of the most important graphic novels of our time. Whether you're reading it for the first time, teaching it in a classroom, or leading a book club discussion, this app has everything you need.

CHAPTER GUIDE
• All 20 chapters with summaries, key quotes, and discussion questions
• Track your reading progress
• Beautiful, distraction-free reading companion

CHARACTER PROFILES
• 15+ characters with detailed profiles
• Relationship map showing how characters connect
• Key quotes for each character

HISTORICAL TIMELINE
• Interactive timeline of the Iranian Revolution (1978-1984)
• 30+ key events with context
• See how real history connects to Marjane's story

THEMES EXPLORER
• 8 major themes explored in depth: Identity, Revolution, Feminism, Exile, Family, War, Freedom, Coming of Age
• Chapter references for each theme
• Perfect for essays and book club discussions

No internet required. No ads. No tracking. Just the book and its world.

### Category
Primary: Books
Secondary: Education

### Pricing
- **Model**: Paid, $2.99
- **Reasoning**: Educational/literary apps command higher price points. Students and educators expect to pay for quality study aids. Comparable to SparkNotes+ or LitCharts subscription but one-time.
- **Monetization Path**: Future companion apps for other graphic novels (Maus, Fun Home, etc.) as a series

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 8/10 | 100K+ searches today, 1,000% spike. Book bans driving sustained interest. But the spike may be short-lived (1-2 weeks). |
| App Gap | 9/10 | Zero dedicated Persepolis apps exist. General study guides are poor quality. |
| Build Simplicity | 8/10 | Pure content app. No backend, no API. SwiftUI with bundled JSON. Timeline view is the most complex element. |
| Evergreen Potential | 6/10 | Persepolis is a perennial bestseller and college assignment, so baseline demand is evergreen. But the trending spike will fade. Long-tail rather than viral. |
| Monetization | 7/10 | $2.99 paid app is reasonable for educational content. Series potential (other graphic novel companions). |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: Medium risk — the 100K+ search spike will fade within 1-2 weeks. However, Persepolis has permanent baseline demand from schools and book clubs.
- **App Store Rejection**: Low risk — educational content, no copyright issues (original summaries and analysis, not reproducing the book).
- **Competition**: Low risk — nobody is building dedicated literary companion apps for specific books. If anything, a competitor would validate the concept.
- **Legal/IP**: Low risk — original analysis and summaries are fair use. Not reproducing any content from the book.
- **Content Maintenance**: Low — content is complete at launch. No updates needed unless adding new features.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Google Trends 100K+ spike, book ban news cycle, App Store gap)
- [x] App Store search shows 0 relevant dedicated apps
- [x] MVP can be built without backend/API dependencies
- [x] Content is original analysis/summary (fair use)
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours (2.5 hours)
