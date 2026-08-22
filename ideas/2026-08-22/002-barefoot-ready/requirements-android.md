# Barefoot Ready — Android Requirements Document
*Version 1.0 · Generated 2026-08-22 · Handoff-ready for coding agent*
*Companion to `requirements.md` (iOS). Content JSONs are SHARED — copy verbatim.*

---

## 1. App Specification

| Field | Value |
|-------|-------|
| App name | Barefoot Ready |
| applicationId | `com.cryptosi.barefootready` (matches iOS bundle ID) |
| Platform | Android 8.0+ (minSdk 26), targetSdk 35 |
| Language/UI | Kotlin 2.0+ · Jetpack Compose · Material 3 |
| Orientation | Portrait locked (`android:screenOrientation="portrait"` on all activities) |
| Devices | Phones; must render correctly 320dp–430dp width. No tablet layouts in v1.0 |
| Backend | **NONE** — fully offline |
| Dependencies | androidx + Compose BOM only. Zero third-party libraries. No network stack |
| Persistence | `SharedPreferences` (`barefoot.progress.v1`) — sufficient for this state size; skip DataStore |
| Content | Same three JSON files as iOS, copied into `app/src/main/assets/` unchanged |
| Estimated build | ~3 hours |

---

## 2. Feature Breakdown

Feature set is **identical to iOS §2** (F1–F5 P0, F6–F9 deferred — F9 landing page is a shared web asset, spec in `landing-page-spec.md`, built after both apps ship). Same user stories, same priorities, same acceptance criteria. Platform implementation mapping:

| Concern | iOS | Android |
|---------|-----|---------|
| Progress persistence | UserDefaults | SharedPreferences (JSON string) |
| Bundled content | Bundle JSON | `assets/*.json`, read via `assets.open()` |
| Completion haptic | UIImpactFeedbackGenerator | `LocalHapticFeedback.current.performHapticFeedback(LongPress)` on check; `view.performHapticFeedback(KEYBOARD_TAP)` acceptable alternative |
| Icons | SF Symbols | Material Symbols Outlined (mapping in §3) |
| Rounded display font | SF Pro Rounded | Default Roboto, bold weights (no custom font in v1.0) |
| Progress ring | SwiftUI Circle trim | Custom `Canvas` drawArc — stroke 10dp, round caps |

Acceptance criteria carry over unchanged, plus these Android-specific ones:
- [ ] Back gesture/button navigates correctly from every pushed screen (predictive back enabled)
- [ ] Process death: complete a day → force-stop from recents → relaunch → state intact
- [ ] System font scale 200%: all screens remain usable, no clipped text
- [ ] Airplane mode: full functionality

---

## 3. Screen-by-Screen Specification

Same six screens, same layout/elements/interactions/data/navigation as **iOS §3**, with these Android adaptations:

**Navigation**: `NavHost` inside single-activity `ComponentActivity`. Bottom navigation bar with 4 destinations (Program, Exercises, Checklist, About). Push = navigate with args; Exercise Detail pops on "Mark done".

**Icon mapping (SF Symbol → Material Symbol)**:

| Purpose | SF Symbol | Material Symbol |
|---------|-----------|-----------------|
| Tab: Program | figure.walk | `DirectionsWalk` |
| Tab: Exercises | figure.strengthtraining.functional | `FitnessCenter` |
| Tab: Checklist | checklist | `Checklist` |
| Tab: About | info.circle | `Info` |
| Caution callout | exclamationmark.triangle.fill | `WarningAmber` |
| Row chevron | chevron.right | `ChevronRight` |
| Exercise hero fallback | figure.walk | `AccessibilityNew` |

Exercise `symbol` field values in JSON are SF Symbol names — Android maps by exercise `id` via a local table; unknown ids fall back to `AccessibilityNew`. Do NOT modify shared JSON.

**Screen-specific deltas**:
- **S1 Today**: progress ring drawn with Canvas arc (background track color `ringTrack`, sweep = week completion fraction). DayCard = `ElevatedCard` radius 16dp, elevation 1dp (tonal — do not use heavy shadows). Check circles: 28dp `IconToggleButton`.
- **S3 Exercise Detail**: caution callout = Row with 12% alpha `#D97706` background + 3dp leading border strip. Mark done button: `Button` height 52dp, corner 12dp, colors from tokens; success state disables and swaps label to "Done ✓".
- **S4 Exercises**: filter chips = Material3 `FilterChip` row (horizontal scroll). Search = top-app-bar search or `SearchBar` M3 component.
- **S5 Checklist**: expandable rows via `animateContentSize()`; reset uses `AlertDialog` titled "Reset checklist?", message "All checks will be cleared.", confirm/cancel.
- **S6 About**: disclaimer paragraph verbatim from F5. First-launch disclaimer = `AlertDialog` shown once when `disclaimerAccepted == false`; acknowledging persists flag.

---

## 4. Data Model

**Identical to iOS §4.** Single source of truth: the JSON files already shipped in the iOS project. Android agent copies them byte-for-byte into `assets/`. Same Codable→data-class structs:

```kotlin
data class ProgramDay(val week:Int, val day:Int, val phase:String,
    val targetMinutes:Int, val exerciseIds:List<String>, val note:String?)
data class Exercise(val id:String, val name:String, val steps:List<String>,
    val reps:String, val area:String, val phases:List<String>,
    val symbol:String?, val caution:String?)
data class ChecklistItem(val id:String, val group:String,
    val label:String, val detail:String)
```

Decode with `kotlinx.serialization` (first-party, include plugin) or `org.json` — agent's choice; kotlinx recommended. Missing `exerciseIds` lookups: skip silently + Log.d, never crash.

ProgressState shape mirrors iOS exactly: `{"completedDays":[...],"checklist":{...},"disclaimerAccepted":true}` stored as JSON string under SharedPreferences key `barefoot.progress.v1`.

---

## 5. Design Tokens

Hex values **identical to iOS §5** (light and dark palettes, phase tints, spacing 4/8/12/16/24/32, radii 16/12/capsule/6). Implementation:

- Light/Dark via `isSystemInDarkTheme()`, hard-coded Color values from token table (no dynamic color/Material You — brand consistency wins)
- Typography: Roboto — title 30sp/bold, section 20sp/sp600, body 16sp, caption 13sp, stat 34sp/bold (all sp, respecting font scale)
- Elevation: cards 1dp tonal elevation only; no drop shadows (Material convention)
- Shapes: card 16dp, button 12dp, chip full capsule, checkbox 6dp
- Status bar matches background cream/dark background per theme (edge-to-edge enabled)

---

## 6. Google Play Metadata

| Field | Value |
|-------|-------|
| Title (30 max) | Barefoot Ready (14) |
| Short description (80 max) | `Your 8-week plan to switch to barefoot shoes safely. Exercises + shoe checklist.` (81 → trim to `Your 8-week plan to switch to barefoot shoes safely. Exercises & shoe checklist.` = 80 ✓ verify before submit) |
| Full description (4000 max) | Reuse iOS description verbatim (~1,150 chars) |
| Category | Health & Fitness |
| Tags | Health & Fitness; Fitness |
| Price | Paid, $1.99 (US tier; let Play auto-convert other markets) |
| Content rating | Questionnaire: no violence/user-generated content/accounts → expect **Everyone** |
| Data safety form | **No data collected, no data shared.** No encryption section triggers. Matches reality — no permissions requested |
| Permissions | NONE in manifest. No INTERNET permission — makes offline claim auditable |
| Screenshots | Min 2 phone screenshots: S1 Today (mid-progress ring), S5 Checklist. Recommended 4: + S3 detail, S2 overview |
| Release | Production track, manual review expected 1–7 days |

---

## 7. Build Instructions

**Project setup**: Empty Activity (Compose) template, AGP 8.5+, Kotlin 2.x, Compose BOM latest stable. `android.enableJetifier` not needed. Version catalog fine.

**Build order**:
1. Scaffold, Theme.kt with all §5 tokens (incl. dark), data classes + asset JSON decoding
2. Copy the 3 JSON files from iOS repo path `ideas/2026-08-22/002-barefoot-ready/` reference (or ask orchestrator for the iOS project's Resources folder) into `assets/`
3. Today screen: Canvas ring, DayCard, check toggles + SharedPreferences persistence
4. Exercises list (chips + search) → detail screen; wire linked exercises
5. Program Overview + week jump-back
6. Checklist with live score + reset dialog
7. About + one-time disclaimer dialog
8. Polish: haptics, predictive back handling, edge-to-edge status bar, launcher icon (bare footprint on cream — adaptive icon, foreground/background layers)
9. Smoke test per checklist below

**Testing checklist (emulator)**:
- [ ] Complete day → force-stop → relaunch: persisted
- [ ] Ring % correct at day 7→8 boundary and week rollover
- [ ] All 18 exercises open; chip filters correct; unknown symbol falls back gracefully
- [ ] Checklist score live-updates; reset dialog works
- [ ] 200% font scale: no clipped/unreadable text
- [ ] Dark mode legible everywhere
- [ ] Predictive back: correct pop order, disclaimer dialog not dismissable-by-back without ack (use cancelable=false until acknowledged)
- [ ] APK/AAB installs clean on API 26 emulator AND current API emulator
- [ ] Manifest has zero `<uses-permission>` entries

**Agent notes**: No third-party dependencies beyond androidx/google-first-party. All UI strings go in `strings.xml` (localization-ready even though EN-only v1.0). Never edit the shared JSON content files — if content looks wrong, report back, don't fix locally. No brand names (Vivobarefoot/Xero) anywhere in UI or store listing body copy.
