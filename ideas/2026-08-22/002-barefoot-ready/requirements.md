# Barefoot Ready — Requirements Document
*Version 1.0 · Generated 2026-08-22 · Handoff-ready for coding agent*
*Idea source: ideas/2026-08-22/002-barefoot-ready · Extended research: GO verdict*

---

## 1. App Specification

| Field | Value |
|-------|-------|
| App name | Barefoot Ready |
| Bundle ID | `com.cryptosi.barefootready` |
| Platform | iOS 17.0+, SwiftUI, no storyboards |
| Orientation | Portrait only |
| Devices | iPhone SE (3rd gen) → iPhone 16 Pro Max |
| Backend | **NONE** — fully on-device, offline-first |
| Dependencies | Zero third-party packages. Foundation + SwiftUI + SF Symbols only |
| Persistence | `UserDefaults` (progress state), bundled JSON (content) |
| Xcode | Xcode 15.4+ / Swift 5.10 |
| Estimated build | ~2.5 hours |

---

## 2. Feature Breakdown

### F1. 8-Week Transition Program — P0, M
**User story**: As a first-time barefoot shoe buyer, I want a day-by-day plan so that I adapt without injury.
**Acceptance criteria**:
- [ ] 56 day-cards across 4 phases render from bundled JSON (Adapt wk1–2, Strengthen wk3–4, Load wk5–6, Run wk7–8)
- [ ] Tapping a day's check circle marks complete, plays haptic, updates progress ring immediately
- [ ] Completion state persists across relaunch (UserDefaults)
- [ ] Progress ring shows week N/8 and % of current week done
- [ ] Days are completable out of order but ring math counts only current week
**Dependencies**: D1 ProgramDay JSON. **Complexity**: M

### F2. Foot Exercise Library — P0, S
**User story**: As a user, I want clear instructions for foot-strengthening exercises so I know exactly what to do.
**Acceptance criteria**:
- [ ] 18 exercises listed, filterable by phase chip row (All / Adapt / Strengthen / Load / Run)
- [ ] Detail view shows steps, reps badge, target area, caution callout where present
- [ ] "Mark done" from detail returns to previous screen and reflects state
- [ ] Works fully offline
**Dependencies**: D2 Exercise JSON. **Complexity**: S

### F3. Shoe Selection Checklist — P0, S
**User story**: As a shopper, I want a buying checklist so I don't buy a fake barefoot shoe.
**Acceptance criteria**:
- [ ] 12 toggle items grouped Fit / Build / Test, live score footer ("9/12 ready")
- [ ] Toggle state persists; reset button clears all with confirmation alert
- [ ] Each item expands/collapses its explainer text
**Dependencies**: D3 ChecklistItem JSON. **Complexity**: S

### F4. Program Overview — P0, S
**User story**: As a user, I want to see all phases at a glance so I understand the journey.
**Acceptance criteria**: [ ] 4 phase sections with week rows showing completion %; tap any week jumps to it in Today context.
**Dependencies**: F1 state. **Complexity**: S

### F5. About + Medical Disclaimer — P0, XS
**User story**: As a user, I want safety context so I use the app responsibly.
**Acceptance criteria**: [ ] About tab shows disclaimer verbatim: *"Barefoot Ready provides general fitness education, not medical advice. Stop any activity that causes sharp or localized pain and consult a qualified clinician."* Shown also on first launch as a dismissable sheet (persisted acknowledgement flag).
**Dependencies**: none. **Complexity**: XS

### F6. Soreness Journal — P1 (v1.1)
Simple daily soreness log 0–5 with red-flag guidance copy. Deferred.
### F7. HealthKit Reminders — P1 (v1.1). Deferred.
### F8. Brand/Affiliate Directory — P2 (v1.2, disclosed affiliate links). Deferred.

---

## 3. Screen-by-Screen Specification

Tab bar, 4 tabs: **Program** (`figure.walk`), **Exercises** (`figure.strengthtraining.functional`), **Checklist** (`checklist`), **About** (`info.circle`). All tabs always visible.

### S1. Today (tab 1 root)
- **Purpose**: show current position and what to do now
- **Layout**: header block → progress ring → today card → upcoming days list
- **Elements**: (1) Title "Week 3 of 8 · Strengthen" (SF Pro Rounded 30 bold); (2) progress ring 96pt, track `#E5E0D5`, fill `#3E7C4F`, center label "%"; (3) DayCard for current day: white bg radius 16, day number chip, target-minutes label "45 min in barefoots", 2 linked exercise rows with `chevron.right`; (4) check-off circles 28pt, empty `#D9D4C8`, filled `#3E7C4F` + `checkmark`; (5) next-3-days compact rows
- **Interactions**: tap circle → complete + haptic `UIImpactFeedbackGenerator(style:.medium)`; tap DayCard/exercise row → push Exercise Detail; horizontal swipe between day cards
- **Data**: program JSON + UserDefaults completion set
- **Navigation**: root of tab 1; pushes S3

### S2. Program Overview (push from "See full plan" button under ring)
- **Purpose**: whole-journey map
- **Layout**: vertical scroll, 4 phase sections
- **Elements**: phase header chips (phase name + weeks range, bg tinted by phase color: Adapt `#3E7C4F`, Strengthen `#D9B26A`, Load `#C97B3D`, Run `#B91C1C` at 15% opacity); week rows w/ mini progress bar + "62%" caption; info footnote about pacing
- **Interactions**: tap week row → dismiss back to Today focused on that week
- **Navigation**: push/pop from S1

### S3. Exercise Detail (push from anywhere exercises are linked)
- **Purpose**: teach one exercise
- **Layout**: hero icon block → steps → reps → caution → CTA
- **Elements**: hero block 120pt bg `#F0EBDD` with SF Symbol (`figure.yoga`/`figure.barre` etc., 48pt `#3E7C4F`); numbered step rows (SF Pro body 16, line spacing 4); reps badge (capsule, bg `#D9B26A` 20%, text `#2B2118` semibold 14); caution callout when `caution != nil`: bg `#D97706` 12%, left border 3pt `#D97706`, icon `exclamationmark.triangle.fill`; "Mark done" button full-width 52pt, radius 12, bg `#3E7C4F`, label `.white` semibold
- **Interactions**: Mark done → haptic success, button becomes "Done ✓" disabled state, pop after 400ms
- **Data**: single Exercise item

### S4. Exercises (tab 2 root)
- **Elements**: search field (`.searchable`); phase filter chip row (All/Adapt/Strengthen/Load/Run, selected = solid `#3E7C4F` + white text, unselected = `#FAF7F0` bg + `#2B2118` border 1pt); list of exercise cards (icon 36pt, name semibold 17, target-area caption 13 `#6B5D4F`)
- **Interactions**: tap card → S3; chips filter instantly
- **Data**: Exercise array

### S5. Shoe Checklist (tab 3 root)
- **Layout**: nav title, grouped sections, score footer pinned bottom
- **Elements**: 3 section headers (Fit / Build / Test); 12 toggle rows — leading custom checkbox 24pt radius 6, label semibold 16, chevron expand affordance; expanded explainer text body 14 `#6B5D4F`; footer bar: "9/12 ready" bold 20 + Reset text-button `#B91C1C`
- **Interactions**: toggle row → score animates; reset → `confirmationDialog("Reset checklist?", "All checks will be cleared.")` → confirm clears
- **Data**: ChecklistItem array + persisted dict

### S6. About (tab 4 root)
- **Elements**: app icon mark, version label, disclaimer paragraph (verbatim from F5), "Sources & method" disclosure group listing public physio/community guidance basis, contact link
- **Interactions**: static content only

---

## 4. Data Model

All content bundled at `Resources/*.json`, decoded with `Codable`.

```jsonc
// program.json — 56 entries, one per day
// ProgramDay
{"week":1,"day":1,"phase":"Adapt","targetMinutes":30,
 "exerciseIds":["toe-splay","short-foot"],
 "note":"Wear barefoot shoes around the house only"}
{"week":4,"day":3,"phase":"Strengthen","targetMinutes":60,
 "exerciseIds":["short-foot","single-leg-balance","calf-raises-eccentric"],
 "note":"Add 10 min if zero soreness yesterday"}
{"week":8,"day":6,"phase":"Run","targetMinutes":90,
 "exerciseIds":["ankle-mobility","calf-raises-eccentric"],
 "note":"Final long walk-run: alternate 5 min run / 3 min walk"}

// exercises.json — 18 entries
// Exercise
{"id":"short-foot","name":"Short Foot",
 "steps":["Sit with foot flat on floor","Draw ball of foot toward heel without curling toes","Hold 5s, release fully"],
 "reps":"10 × 5s","area":"Arch","phases":["Adapt","Strengthen"],
 "symbol":"figure.mind.and.body",
 "caution":null}
{"id":"calf-raises-eccentric","name":"Eccentric Calf Raises",
 "steps":["Stand on step edge, heels off","Rise on both feet","Lower slowly on one foot over 3s"],
 "reps":"3 × 10 each leg","area":"Calves / Achilles","phases":["Load","Run"],
 "symbol":"figure.strengthtraining.functional",
 "caution":"Mild ache is normal; sharp pain means stop"}
{"id":"toe-splay","name":"Toe Splay",
 "steps":["Sit, feet flat","Spread toes apart as far as possible","Hold 10s, relax"],
 "reps":"10 × 10s","area":"Toes / Forefoot","phases":["Adapt","Strengthen","Load","Run"],
 "symbol":"hand.point.up.left.fill",
 "caution":null}

// checklist.json — 12 entries
// ChecklistItem
{"id":"toe-box","group":"Fit","label":"Toe box lets toes splay fully","detail":"No pinching at widest part; wiggle test"}
{"id":"stack-height","group":"Build","label":"Stack height under ~10mm","detail":"Thin sole = better ground feel; measure at heel"}
{"id":"flex-point","group":"Test","label":"Shoe bends at the ball, not the arch","detail":"Hold toe and heel, flex — it must crease where your foot creases"}

// ProgressState — UserDefaults key "barefoot.progress.v1"
{"completedDays":[1,2,3],"checklist":{"toe-box":true,"stack":true},
 "disclaimerAccepted":true}
```

Relationships: `ProgramDay.exerciseIds[] → Exercise.id` (resolve via dictionary lookup, never crash on missing id — skip silently + debug log).

---

## 5. Design Tokens

```
Colors            Light                Dark
primaryMoss       #3E7C4F              #5EA371
accentSand        #D9B26A              #E3C385
backgroundCream   #FAF7F0              #1C1915
cardWhite         #FFFFFF              #26221C
textPrimary       #2B2118              #F0EBDD
textSecondary     #6B5D4F              #A89A87
success           #3E7C4F              #5EA371
warning           #D97706              #F09A3E
error             #B91C1C              #E05252
ringTrack         #E5E0D5              #332E27
divider           #EDE8DC              #332E27
Phase tints: Adapt=#3E7C4F, Strengthen=#D9B26A, Load=#C97B3D, Run=#B91C1C (all at 15% opacity backgrounds, full-strength text)

Typography   SF Pro Rounded: title 30/bold, section 20/semibold
             SF Pro: body 16/regular, caption 13/regular, stat 34/bold rounded
Spacing      base 4 · scale 4/8/12/16/24/32 · screen margin 16
Radius       card 16 · button 12 · chip capsule · checkbox 6
Shadow       cards only: y=2 blur=8 black 8% opacity (light) / none (dark)
Icons        SF Symbols throughout; tab icons listed §3
```

---

## 6. App Store Metadata

| Field | Value |
|-------|-------|
| Title (14/30) | Barefoot Ready |
| Subtitle (29/30) | Safe barefoot shoe transition |
| Keywords (100 max) | `barefoot shoes,minimalist shoes,barefoot running,foot strength,toe box,zero drop,transition,foot health,wide toe box,foot exercise,strong feet` (135 — TRIM TO: `barefoot shoes,minimalist shoes,barefoot running,foot strength,toe box,zero drop,transition,foot health,wide toe box,strong feet` = 100 ✓ count before submit) |
| Category | Primary Health & Fitness / Secondary Lifestyle |
| Price | Paid $1.99, Tier 1 |
| Age rating | 4+ |

**Promotional text (170 max)**:
> Your feet need a transition plan. 8 weeks, 18 foot exercises, one smart shoe checklist — switch to barefoot shoes without the injuries. (139)

**Description**: use the draft in `idea.md` §App Store Listing verbatim (~1,150 chars, within limit).

**What's New (v1.0)**: "Initial release — 8-week program, 18-exercise library, and shoe-buying checklist."

**Screenshots required (6.9")**: S1 Today w/ ring at 43%, S3 Exercise Detail, S5 Checklist mid-score, S2 Overview, plus 2 lifestyle-framed variants of S1/S5. No device frames beyond Apple's native tool.

**Privacy**: **No data collected. No tracking. No analytics.** Privacy manifest: `NSPrivacyCollectedDataTypes` empty, `NSPrivacyTracking false`. Info.plist needs NO permission strings (no HealthKit/network in v1.0).

---

## 7. Build Instructions

**Build order**:
1. Xcode project scaffold, tokens file (`Theme.swift` with all §5 values incl. dark variants), Codable models + JSON decode tests
2. Content JSON authoring: 56 ProgramDays (write all 56 — do not generate placeholders), 18 Exercises, 12 ChecklistItems
3. Today screen: ring, DayCard, completion state + UserDefaults persistence
4. Exercise library list → detail; wire linked exercises from DayCards
5. Overview screen + week jump-back
6. Checklist screen with live score + reset dialog
7. About + first-launch disclaimer sheet (ack flag persisted)
8. Polish: haptics, empty states, app icon (bare footprint on cream), launch screen plain cream
9. Smoke test per checklist below

**Testing checklist (simulator)**:
- [ ] Kill + relaunch → completions persist
- [ ] Ring % correct on day 7→8 boundary and week rollover
- [ ] All 18 exercises open; filters work; no crash on missing symbol names (fallback `figure.walk`)
- [ ] Checklist score matches toggles; reset works
- [ ] iPhone SE 3rd gen: no clipping at smallest width; Dynamic Type up to XXL doesn't break layout
- [ ] Dark mode: legible everywhere (use dark tokens above)
- [ ] Offline: airplane mode, full functionality
- [ ] Disclaimer sheet appears once, ack persists

**Agent notes**: No networking code anywhere. No third-party SPM. Keep all strings localizable from day 1 (`String(localized:)`) even though only EN ships in v1.0. Do not reference brand names (Vivobarefoot, Xero) inside app UI/content — keywords metadata only.
