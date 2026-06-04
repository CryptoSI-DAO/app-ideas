# App Idea: Screwworm Watch — Outbreak Guide & Safety Checklist

*Generated: 2026-06-04*
*Confidence Score: 7.6/10*

---

## Pitch

A consumer-facing guide to the New World Screwworm outbreak — what it is, how to recognize it, protect your pets, and stay informed as the parasite spreads northward toward the US border. Factual, non-sensationalist, with CDC/USDA-sourced information in plain English. People are searching "screwworm" + "what to know" — this app answers that need offline.

## Target Audience
- Primary: Pet owners and parents in southern US states (TX, FL, AZ, NM, CA)
- Secondary: Hikers, campers, and rural residents in outbreak-adjacent areas
- Demographics: 25-55, iOS-leaning, US-based, safety-conscious

## Problem Statement

The New World Screwworm — a flesh-eating parasitic fly — is spreading northward through Mexico toward the US border. CDC and USDA have issued health advisories. ABC News, ScienceAlert, and mainstream media are covering it. But there's NO consumer iOS app that explains:
- What screwworm actually is (most people have never heard of it)
- How to recognize infestation signs in pets
- What to do if you spot it
- Current outbreak map and status

The only app (Screwworm Tracker) is a field-reporting tool for ranchers and vets — not a consumer education app.

## Trend Evidence
- **Google Trends**: "screwworm" — 10K+ searches, 200% increase, started 5 hours ago (active breakout)
- **Mainstream Media**: ABC News coverage (April 2026), CDC situation summary updated June 2026, ScienceAlert "flesh-eating parasite spreading toward US"
- **CDC/USDA**: Official health advisories, situation summaries, and consumer-facing quick facts pages all published in 2026 — confirming this is a current, ongoing concern
- **Google Autocomplete**: "screwworm what to know" — direct informational intent

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Screwworm Tracker (field reporting) | N/A | Free | For ranchers/vets only — not consumer education. Reporting tool, not guide. |

**App Gap**: Zero consumer education apps exist. The only app is a niche veterinary field tool. Massive gap for a "what is screwworm + how to protect your family" reference app.

## Core Features (MVP)

### Must-Have (v1.0)
1. **What Is Screwworm?** — Plain-English explainer with lifecycle diagrams, sourced from CDC. What it does, how it spreads, why it matters now.
2. **Outbreak Status Dashboard** — Static map showing current outbreak zone (Mexico/Central America) and US border proximity. Text summary of latest USDA status update.
3. **Pet Safety Checklist** — 10-point checklist: inspect wounds, keep pets indoors at dawn/dusk, contact vet if you see maggots, etc. Based on USDA guidelines.
4. **Recognition Guide** — Visual guide to identifying screzzorm infestation: what to look for in wounds, symptoms in pets and livestock. Text descriptions with illustrated diagrams (SF Symbols + custom illustrations).
5. **What To Do** — Step-by-step action plan if you suspect infestation: isolate animal, call vet, report to USDA APIS. Emergency contact numbers.

### Nice-to-Have (v1.1+)
- Push notifications for USDA updates (requires backend — deferred)
- Offline mode for rural/outdoor use
- Multilingual support (Spanish for border communities)
- Printable PDF checklist for vet offices

## Content & Data
- CDC New World Screwworm situation summary (cdc.gov)
- USDA APHIS current status page
- MSD Manual consumer version (medical reference)
- ABC News / ScienceAlert articles for plain-language writing
- All content is factual, public-domain government information

## Design Direction
- **Style**: Clean, authoritative, medical-reference feel — not sensationalist
- **Color Palette**: Primary #1A5276 (deep trust blue), Secondary #27AE60 (safety green), Accent #E74C3C (alert red for warnings), Background #F8F9FA, Text #2C3E50
- **Typography**: SF Pro Display for headers, SF Pro Text for body. H1: 28pt Bold, H2: 22pt Semibold, Body: 16ptRegular, Caption: 14pt
- **Key Screens**: Home (status + quick nav), What Is Screwworm, Outbreak Map, Pet Safety Checklist, Recognition Guide, What To Do
- **Navigation**: Tab bar with 4 tabs: Overview, Protect, Identify, Act
- **Reference Apps**: CDC apps, WebMD (clean medical reference UX)

## Technical Notes
- **Platform**: iOS (SwiftUI), minimum iOS 16
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: Bundled JSON with structured content sections
- **Estimated Build Time**: ~2.5 hours
- **Complexity**: Low

## App Store Listing

### Title
Screwworm Safety Guide

### Subtitle
Outbreak info, pet safety & checklist

### Keywords
screwworm,parasite,pet safety,outbreak,CDC,USDA,health guide,infestation,animal health,new world screwworm

### Description
**Stay informed about the New World Screwworm outbreak — in plain English.**

Screwworm Watch gives you factual, CDC-sourced information about the parasitic fly spreading toward the US border. No panic. No fluff. Just what you need to know.

**WHAT'S INSIDE:**
→ What is screwworm? Clear explanation with lifecycle overview
→ Current outbreak status — where it is now and how close to the US
→ Pet safety checklist — 10 steps to protect your animals
→ Recognition guide — what infestation looks like and symptoms to watch
→ Action plan — exact steps to take if you suspect screwworm
→ Emergency contacts and reporting information

**SOURCED FROM:** CDC, USDA APHIS, and verified medical references. Content reviewed for accuracy.

**BUILT FOR:** Pet owners, parents, hikers, and rural residents in southern US states who want factual, actionable information — without having to search through government websites.

All content works offline. No account needed. No data collected.

### Category
Primary: Health & Fitness
Secondary: Reference

### Pricing
- **Model**: Free
- **Reasoning**: Public health information should be free. Drives maximum adoption for a trend-dependent app.
- **Monetization Path**: Future paid version with real-time USDA feed integration, or partner with pet health brands for sponsored content (clearly labeled)

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | 200% spike, 10K+ searches. CDC/USDA actively updating. Mainstream media coverage growing. |
| App Gap | 9/10 | Zero consumer education apps. Only 1 niche field-reporting tool. Complete green field. |
| Build Simplicity | 9/10 | Pure content app. No backend, no APIs, no real-time data. Structured JSON + static UI. ~2.5 hours. |
| Evergreen Potential | 5/10 | Outbreak-dependent. Will decline once USDA declares containment. BUT screwworm is a recurring threat — content stays relevant for future outbreaks. |
| Monetization | 6/10 | Free model for max reach. Future: USDA feed integration (paid), pet health brand sponsorships, or pivot to general "parasite/pest alert" platform. |
| **Average** | **7.6/10** | |

## Risk Assessment
- **Trend Fizzle**: Medium-High. If USDA contains the outbreak quickly, interest drops. Mitigation: Position as general "parasite alert" reference; content has shelf life for future outbreaks.
- **App Store Rejection**: Low risk. Health/educational content with no medical claims. Include disclaimers: "For informational purposes only. Consult a veterinarian for medical advice."
- **Competition**: Low short-term risk. No competitors. If trend continues, news apps may add screwworm coverage, but dedicated guide app is differentiated.
- **Legal/IP**: Very low risk. All content sourced from public-domain government (CDC/USDA) and rewritten in plain English. No proprietary data.
- **Content Moderate**: Content is disease/parasite-related. Ensure tone is factual, not gross-out or sensationalist. App Store may flag if imagery is graphic — use diagrams/illustrations instead of photos.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Google Trends, CDC, ABC News)
- [x] App Store search shows 0 consumer education apps for this topic
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial (government-sourced)
- [x] No obvious legal/copyright issues (public domain government info)
- [x] Build time estimate ≤ 3 hours

---

# Requirements Document — Screwworm Safety Guide

## 1. App Specification
- **App Name**: Screwworm Safety Guide (30 chars exactly)
- **Bundle ID**: com.cryptosi.screwwormwatch
- **Target Platform**: iOS 16.0+
- **Orientation**: Portrait only
- **Minimum Device**: iPhone SE (3rd gen) through iPhone 16 Pro Max

## 2. Feature Breakdown

### Feature 1: What Is Screwworm? (Overview)
- **User Story**: As a concerned pet owner, I want to understand what screwworm is and why it's in the news, so I can assess the risk to my family and pets.
- **Acceptance Criteria**: User can read a 3-paragraph plain-English overview, see lifecycle stages described in 4 bullet points, and access a "Learn More" link to CDC source.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

### Feature 2: Outbreak Status
- **User Story**: As someone living near the southern US border, I want to know how close the outbreak is to my area, so I can take appropriate precautions.
- **Acceptance Criteria**: Static map image showing outbreak zone, text summary of current status with date of last update, proximity warning for US states.
- **Priority**: P0
- **Dependencies**: None (static content in MVP)
- **Complexity**: S

### Feature 3: Pet Safety Checklist
- **User Story**: As a pet owner, I want a clear checklist of steps to protect my animals, so I don't have to search through government websites.
- **Acceptance Criteria**: 10-item checklist with checkbox UI. Each item has a title + 1-sentence explanation. Progress saved locally.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

### Feature 4: Recognition Guide
- **User Story**: As a worried pet owner, I want to know what screwworm infestation looks like, so I can catch it early and get help.
- **Acceptance Criteria**: 5 warning signs listed with descriptions. Illustrated using SF Symbols + custom SwiftUI illustrations (no photos). "When to call a vet" callout section.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: M

### Feature 5: What To Do (Action Plan)
- **User Story**: As someone who suspects they've found screwworm, I want step-by-step instructions, so I can act quickly and correctly.
- **Acceptance Criteria**: Numbered 1-5 action steps. Emergency contact numbers (USDA APIS hotline, local vet finder via tel: link). "Report to USDA" button that opens mailto: with pre-filled report template.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

### Feature 6: Disclaimer & Sources
- **User Story**: As a reader, I want to know where this information comes from, so I can trust it.
- **Acceptance Criteria**: Footer on every screen: "Sources: CDC, USDA APIS. For informational purposes only. Not medical advice." Dedicated Sources screen with links.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

## 3. Screen-by-Screen Specification

### Screen 1: Home (Overview Tab)
- **Purpose**: Quick status overview + navigation to all sections
- **Layout**: Navigation view, scrollable
- **Elements**:
  - Header: App icon + "Screwworm Safety Guide" title
  - Status card: Red/orange/green indicator + "Outbreak Status: Active — Mexico/Central America" + last updated date
  - "What is Screwworm?" preview card (2 lines + "Read More" button)
  - Quick-action grid (2x2): "Pet Safety Checklist" | "Recognition Guide" | "Outbreak Map" | "What To Do"
  - Footer: Sources disclaimer
- **Interactions**: Tap card → navigate to detail screen
- **Data**: Static content from bundled JSON
- **Navigation**: Tab bar item 0

### Screen 2: What Is Screwworm? (Detail)
- **Purpose**: Full educational content
- **Layout**: Scroll view with sections
- **Elements**:
  - H1: "What is Screwworm?"
  - 3-paragraph overview text
  - Section: "The Lifecycle" — 4-stage numbered list with SF Symbols (egg → larva → pupa → fly)
  - Section: "Why Now?" — current outbreak context
  - Section: "Who's at Risk?" — pets, livestock, wildlife, rarely humans
  - "Sources: CDC" link
- **Interactions**: Scroll, tap source link → open Safari
- **Data**: Static bundled content
- **Navigation**: Push from Home

### Screen 3: Outbreak Map (Protect Tab)
- **Purpose**: Visual status of outbreak proximity
- **Layout**: Full-screen map illustration + text
- **Elements**:
  - H1: "Outbreak Status"
  - Custom SwiftUI Map illustration (simplified North America with highlighted zones)
  - Status text: "Active outbreak: Mexico, Central America" + "No confirmed US cases as of [date]"
  - Proximity warning box (orange): "Cases detected within 200 miles of Texas border"
  - USDA status summary paragraph
  - Last updated date stamp
- **Interactions**: None (static content)
- **Data**: Static bundled content
- **Navigation**: Tab bar item 1

### Screen 4: Pet Safety Checklist (Protect Tab → Checklist)
- **Purpose**: Interactive checklist
- **Layout**: List with checkboxes
- **Elements**:
  - H1: "Protect Your Pets"
  - 10 checklist items, each with:
    - Checkbox (toggle)
    - Title (bold)
    - 1-sentence description
  - Progress indicator: "X of 10 completed"
  - "When to Call Your Vet" callout at bottom
- **Interactions**: Tap checkbox → toggle, progress updates
- **Data**: Local state (UserDefaults)
- **Navigation**: Tab bar item 1 → push

### Screen 5: Recognition Guide (Identify Tab)
- **Purpose**: Help users identify potential infestation
- **Layout**: Scrollable list
- **Elements**:
  - H1: "What to Look For"
  - Warning banner: "If you suspect screwworm, contact a vet immediately"
  - 5 symptom cards, each with:
    - SF Symbol icon (exclamationmark.triangle.fill)
    - Symptom name
    - Description
  - "Commonly Affected Animals" section
  - "Not Sure?" section with "Find a Vet" button
- **Interactions**: Tap "Find a Vet" → open tel: link
- **Data**: Static bundled content
- **Navigation**: Tab bar item 2

### Screen 6: What To Do (Act Tab)
- **Purpose**: Emergency action plan
- **Layout**: Numbered steps + contacts
- **Elements**:
  - H1: "If You Suspect Screwworm"
  - 5 numbered action steps (large, tappable)
  - Emergency contacts card: USDA APIS Hotline, State Vet Association
  - "Report It" button → opens mailto: with pre-filled subject
  - Important disclaimer: "Do not attempt to remove larvae yourself"
- **Interactions**: Tap phone number → call, tap Report → mailto:
- **Data**: Static content
- **Navigation**: Tab bar item 3

### Screen 7: Sources & Disclaimer
- **Purpose**: Credibility and legal protection
- **Layout**: Simple scroll view
- **Elements**:
  - "Sources" list: CDC, USDA APHIS, MSD Manual
  - Full medical disclaimer
  - "Last content review: [date]"
  - App version
- **Interactions**: Tap source → open Safari
- **Data**: Static
- **Navigation**: Settings gear on tab bar or footer link

## 4. Data Model

```json
{
  "metadata": {
    "version": "1.0.0",
    "contentDate": "2026-06-04",
    "lastUpdated": "2026-06-04"
  },
  "outbreakStatus": {
    "level": "active",
    "headline": "Active outbreak in Mexico and Central America",
    "usProximity": "Cases detected within 200 miles of Texas border",
    "usCases": false,
    "lastUpdated": "2026-06-02",
    "source": "USDA APHIS"
  },
  "overview": {
    "title": "What is Screwworm?",
    "paragraphs": [
      "New World Screwworm (NWS) is a parasitic fly species whose larvae feed on the living tissue of warm-blooded animals. The female fly lay eggs on open wounds, and the hatching larvae burrow into flesh, causing a condition called myiasis.",
      "The fly was eradicated from the United States in the 1960s-70s using the Sterile Insect Technique. However, NWS remains endemic in parts of South America and the Caribbean. In 2025-2026, a major outbreak has spread through Mexico and Central America, approaching the US border.",
      "While primarily affecting livestock and wildlife, NWS can also infest pets and, rarely, humans. Early detection and veterinary treatment are critical. The USDA and CDC are actively monitoring the situation."
    ],
    "lifecycle": [
      {"stage": "Egg", "description": "Laid on open wounds or mucous membranes. Hatch within 24 hours.", "symbol": "circle.fill"},
      {"stage": "Larva", "description": "Buries into living tissue and feeds for 5-7 days. This causes damage.", "symbol": "worm.fill"},
      {"stage": "Pupa", "description": "Drops to ground and pupates for 7-10 days.", "symbol": "oval.fill"},
      {"stage": "Adult Fly", "description": "Emerges and mates. Female can lay 400-500 eggs in her lifetime.", "symbol": "ant.fill"}
    ]
  },
  "checklist": {
    "title": "Pet Safety Checklist",
    "items": [
      {"id": 1, "title": "Inspect pets daily", "description": "Check for wounds, especially around ears, nose, navel, and any breaks in skin."},
      {"id": 2, "title": "Keep pets indoors at dawn and dusk", "description": "Screwflies are most active during cooler parts of the day."},
      {"id": 3, "title": "Treat all wounds promptly", "description": "Clean and dress any cuts or scrapes. Apply vet-recommended wound spray."},
      {"id": 4, "title": "Use vet-approved insect repellent", "description": "Ask your vet about screwworm-effective repellents for your area."},
      {"id": 5, "title": "Keep livestock areas clean", "description": "Remove manure and debris that attract flies."},
      {"id": 6, "title": "Be extra cautious during branding/castration", "description": "These procedures create entry points. Use approved wound treatments."},
      {"id": 7, "title": "Isolate any animal with suspicious wounds", "description": "Separate from herd/flock until a vet can examine."},
      {"id": 8, "title": "Save suspicious larvae if safe to do so", "description": "Place in a sealed container for vet identification. Do not handle bare-handed."},
      {"id": 9, "title": "Know your emergency vet's number", "description": "Have it saved in your phone. Don't wait if you suspect infestation."},
      {"id": 10, "title": "Report suspected cases", "description": "Contact your state veterinarian or USDA APHIS immediately."}
    ]
  },
  "recognition": {
    "symptoms": [
      {"name": "Worsening wound", "description": "A wound that appears to get worse instead of healing, with unusual swelling or discharge."},
      {"name": "Visible larvae", "description": "Small, worm-like maggots burrowing into tissue. Unlike common flies, these attack living flesh."},
      {"name": "Bloody discharge", "description": "Serosanguineous (blood-tinged) oozing from a wound, especially with a foul smell."},
      {"name": "Behavioral changes", "description": "Animal becomes restless, loses appetite, or isolates from group. Signs of pain."},
      {"name": "Burrow holes", "description": "Small holes in or around a wound where larvae have tunneled into tissue."}
    ]
  },
  "actionPlan": {
    "steps": [
      "Don't panic. Stay calm and isolate the animal from others.",
      "Do NOT attempt to remove larvae yourself — improper removal worsens damage.",
      "Call your veterinarian immediately. Describe symptoms and mention screwworm concern.",
      "If confirmed, your vet will contact the state veterinarian. You may need to preserve larvae for identification.",
      "Report to USDA APHIS: 1-866-536-7593 or via email." 
    ],
    "emergencyContacts": [
      {"name": "USDA APHIS Emergency Hotline", "phone": "18665367593"},
      {"name": "CDC New World Screwworm Info", "url": "https://www.cdc.gov/new-world-screwworm/"}
    ]
  }
}
```

## 5. Design Tokens
- **Colors**: Primary #1A5276, Secondary #27AE60, Accent/Warning #E74C3C, Background #F8F9FA, Card Background #FFFFFF, Text Primary #2C3E50, Text Secondary #7F8C8D, Divider #E0E0E0
- **Typography**: SF Pro Display (headers), SF Pro Text (body). H1: 28pt/Bold, H2: 22pt/Semibold, H3: 18pt/Medium, Body: 16pt/Regular, Caption: 14pt/Regular, Small: 12pt/Regular
- **Spacing**: Base unit 4pt. Padding: 16pt (screen), 12pt (cards). Margins: 8pt (tight), 16pt (standard), 24pt (section)
- **Corner Radius**: Cards 12pt, Buttons 8pt, Checkboxes 4pt
- **Shadows**: Card shadow: offset (0, 2), blur 8pt, opacity 0.1. No shadow on inner elements.
- **Icons**: SF Symbols throughout. Status: exclamationmark.triangle.fill. Checklist: checkmark.circle.fill. Map: map.fill. Phone: phone.fill. Link: arrow.up.right.square

## 6. Build Instructions
- **Framework**: SwiftUI
- **No third-party dependencies**
- **Data**: Bundled JSON in app bundle
- **Minimum Xcode**: Xcode 15
- **Build Order**:
  1. Create new iOS project (SwiftUI, iOS 16+)
  2. Add data.json to bundle root
  3. Create Content model struct + JSON decoder
  4. Build TabView with 4 tabs
  5. Build Home screen (status card + quick nav)
  6. Build What Is Screwworm detail screen
  7. Build Outbreak Map screen (static illustration)
  8. Build Pet Safety Checklist (with UserDefaults persistence)
  9. Build Recognition Guide
  10. Build What To Do / Action Plan
  11. Add Sources & Disclaimer
  12. Test in simulator: iPhone SE (3rd gen), iPhone 15 Pro Max

## 7. Testing Checklist
- [ ] All 4 tabs render correctly
- [ ] Checklist state persists across app launches
- [ ] Phone number links trigger phone call prompt
- [ ] Mailto link opens mail app with pre-filled subject
- [ ] Source links open Safari to correct URLs
- [ ] No content truncation on iPhone SE (small screen)
- [ ] Dark mode works (test system toggle)
- [ ] No network calls required for any feature
- [ ] Build succeeds with no warnings
