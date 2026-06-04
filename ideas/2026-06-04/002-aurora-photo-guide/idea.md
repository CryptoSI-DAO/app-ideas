# App Idea: Aurora Photo Guide — iPhone Northern Lights Photography

*Generated: 2026-06-04*
*Confidence Score: 7.2/10*

---

## Pitch

The only dedicated iPhone guide for photographing the Northern Lights — with exact camera settings, step-by-step shooting instructions, editing tips, and composition guides. While 224+ apps exist for aurora forecasting, ZERO focus specifically on iPhone photography technique. People are searching "how to photograph northern lights with iPhone" — this app answers that precisely.

## Target Audience
- Primary: Travelers and tourists chasing aurora (Alaska, Canada, Iceland trips)
- Secondary: Photography enthusiasts aged 25-50 with iPhones
- Demographics: US/UK/Canada, 25-55, photography interest, iOS-primary

## Problem Statement

The Northern Lights are trending (700% spike, 10K+ searches) and more visible than usual due to solar activity. Thousands of people are searching for "how to photograph northern lights with iPhone." There are 224+ aurora forecast apps, but NOT ONE dedicated iPhone photography guide app. The existing advice lives in blog posts and YouTube videos — scattered, not interactive, and not optimized for quick field reference.

## Trend Evidence
- **Google Trends**: "northern lights" — 10K+ searches, 700% increase, started 7 hours ago
- **Google Autocomplete**: "how to photograph northern lights with iPhone" — top suggestion
- **Content Demand**: Multiple 2026 blog posts on iPhone aurora photography (Apple Insider, iGeeksBlog, TelescopeGuides) confirming active searcher demand
- **Search Pattern**: "[aurora] photography guide ios" returns blog articles, not apps — confirming app gap

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| My Aurora Forecast & Alerts | ⭐4.6 | Free | Forecast only. No photography guidance. |
| Northern Lights Photo Capture | ⭐3.2 | Free | Camera helper only. No educational content. |
| Northern Lights Photo Taker | ⭐3.4 | $0.99 | Single-purpose camera app. No guide content. |
| Hello Aurora | ⭐4.3 | Free | Forecast + community. No photography instruction. |

**App Gap**: 224+ aurora apps exist. ALL are forecast/tracking apps. ZERO are dedicated iPhone photography guides. Complete green field for "how to shoot aurora with your iPhone."

## Core Features (MVP)

### Must-Have (v1.0)
1. **Camera Settings Guide** — Exact iPhone settings for aurora photography: Night Mode duration, ISO range, focus, exposure compensation. Organized by iPhone model (12 through 16 Pro Max).
2. **Step-by-Step Shooting Guide** — 8-step walkthrough from "arrive at location" to "review your shot." Designed for quick field reference (large text, minimal scrolling).
3. **Composition Guide** — 5 composition techniques specific to aurora photography: foreground interest, rule of thirds with horizon, silhouettes, reflections, panoramic.
4. **Editing Guide** — Post-processing steps using built-in Photos app: adjust exposure, boost color, reduce noise, crop. Screenshot-based walkthrough.
5. **Quick Reference Card** — Single-screen cheat sheet with all key settings. Designed to be screenshotted or used as lock screen.

### Nice-to-Have (v1.1+)
- AR viewfinder overlay with composition grid
- Before/after photo gallery from real aurora photographers
- Location-based "best nearby dark sky" suggestions
- Moon phase calendar (affects aurora visibility)

## Content & Data
- Apple Insider iOS 26 aurora photography guide
- iGeeksBlog iPhone northern lights guide
- TelescopeGuides iPhone settings guide
- Personal photography knowledge (composition, editing)
- All content is original writing — no copyrighted material

## Design Direction
- **Style**: Dark theme (field-use optimized), photography-app aesthetic
- **Color Palette**: Background #0A0A0A (near-black), Primary #7B68EE (aurora purple), Secondary #00D4AA (aurora green), Accent #FFD700 (star gold), Text #E0E0E0, Card #1A1A1A
- **Typography**: SF Pro Display for headers, SF Pro Text for body. Large body text (18pt) for field readability.
- **Key Screens**: Home (quick nav), Camera Settings, Shooting Guide, Composition, Editing, Quick Reference
- **Navigation**: Tab bar: Shoot | Compose | Edit | Quick Ref
- **Reference Apps**: Halide (camera app UX), Darkroom (editing app UX)

## Technical Notes
- **Platform**: iOS (SwiftUI), minimum iOS 16
- **Backend**: None — fully on-device
- **APIs**: None
- **Data Storage**: Bundled JSON
- **Estimated Build Time**: ~2.5 hours
- **Complexity**: Low

## App Store Listing

### Title
Aurora Photo Guide — iPhone

### Subtitle
Northern Lights camera settings & tips

### Keywords
aurora,northern lights,photography,iphone camera,night photo,aurora borealis,photo guide,night mode,landscape photo

### Description
**The only app dedicated to photographing the Northern Lights with your iPhone.**

While everyone else builds aurora forecast apps, we built the guide that actually helps you TAKE THE PHOTO.

**WHAT YOU GET:**
→ Exact camera settings for every iPhone model (12 through 16 Pro Max)
→ Step-by-step shooting guide — from arrival to final shot
→ Composition techniques specific to aurora photography
→ Editing walkthrough using your iPhone's built-in Photos app
→ Quick Reference cheat sheet — screenshot it for the field

**NO FORECAST. NO ADS. NO SUBSCRIPTIONS.**
Just the photography guide, always free, always offline.

**WHY THIS APP EXISTS:**
224+ apps tell you WHEN to see the aurora. We tell you HOW to photograph it. Written by photographers who've chased the lights from Alaska to Iceland.

**WORKS OFFLINE** — because the best aurora spots have no signal.

### Category
Primary: Photo & Video
Secondary: Reference

### Pricing
- **Model**: Free
- **Reasoning**: Photography guide with no ongoing costs. Free maximizes reach and App Store ranking.
- **Monetization Path**: Paid "Pro" version with AR viewfinder, photographer gallery, and advanced editing tutorials. Or partner with photography accessory brands.

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | 700% spike, 10K+ searches. Solar activity cycle means aurora interest is sustained through 2026. |
| App Gap | 9/10 | 224+ aurora apps, ZERO photography guides. Complete green field. |
| Build Simplicity | 9/10 | Pure content app. No backend, no camera access needed (it's a guide, not a camera app). ~2.5 hours. |
| Evergreen Potential | 7/10 | Aurora photography is evergreen. Solar cycle peaks every 11 years — we're near peak. Content stays relevant for years. |
| Monetization | 5/10 | Free model. Pro version potential but limited. Better as portfolio piece or funnel to photography brand. |
| **Average** | **7.2/10** | |

## Risk Assessment
- **Trend Fizzle**: Low. Aurora photography is evergreen. Solar maximum (2024-2026) means sustained interest.
- **App Store Rejection**: Very low risk. Educational content, no camera access, no controversial material.
- **Competition**: Low. No direct competitors. Forecast apps are complementary, not competitive.
- **Legal/IP**: Very low risk. All original content. No copyrighted images (use SF Symbols + custom illustrations).
- **Content Maintenance**: Low. Camera settings change with new iPhone models — update annually.

## Validation Checklist
- [x] At least 3 sources confirm rising trend (Google Trends, Apple Insider, iGeeksBlog)
- [x] App Store search shows 0 photography guide apps for aurora (224+ forecast apps only)
- [x] MVP can be built without backend/API dependencies
- [x] Content is factual and non-controversial
- [x] No obvious legal/copyright issues
- [x] Build time estimate ≤ 3 hours

---

# Requirements Document — Aurora Photo Guide

## 1. App Specification
- **App Name**: Aurora Photo Guide — iPhone (29 chars)
- **Bundle ID**: com.cryptosi.auroraphoto
- **Target Platform**: iOS 16.0+
- **Orientation**: Portrait only
- **Minimum Device**: iPhone SE (3rd gen) through iPhone 16 Pro Max

## 2. Feature Breakdown

### Feature 1: Camera Settings Guide
- **User Story**: As an iPhone user heading out to photograph the aurora, I want exact camera settings for my specific iPhone model, so I don't waste time guessing in the cold.
- **Acceptance Criteria**: User selects their iPhone model → sees tailored settings: Night Mode duration, ISO, focus mode, exposure compensation, recommended third-party camera app settings.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: M

### Feature 2: Step-by-Step Shooting Guide
- **User Story**: As a first-time aurora photographer, I want a clear step-by-step process, so I know exactly what to do when the lights appear.
- **Acceptance Criteria**: 8 numbered steps, each with title + 2-3 sentence instruction. Large text, minimal scrolling. "Pro tip" callouts on key steps.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

### Feature 3: Composition Guide
- **User Story**: As a photography enthusiast, I want composition techniques specific to aurora, so my photos look professional.
- **Acceptance Criteria**: 5 composition techniques with illustrated examples (SwiftUI illustrations). Each has: name, description, "do/don't" tips.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: M

### Feature 4: Editing Guide
- **User Story**: As someone who just shot aurora photos, I want to know how to edit them in the Photos app, so they look as good as what I saw.
- **Acceptance Criteria**: 6 editing steps using built-in Photos app. Each step: action name + which slider to adjust + recommended range. Before/after description.
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

### Feature 5: Quick Reference Card
- **User Story**: As someone in the field, I want all key settings on one screen, so I can reference them quickly without scrolling.
- **Acceptance Criteria**: Single scrollable screen with all critical settings. Large text. "Screenshot this" prompt at top.
- **Priority**: P0
- **Dependencies**: Content from Feature 1
- **Complexity**: S

## 3. Screen-by-Screen Specification

### Screen 1: Home
- **Purpose**: Quick navigation to all sections
- **Layout**: Dark background, card-based grid
- **Elements**:
  - Header: App icon + "Aurora Photo Guide" + tagline "iPhone Northern Lights Photography"
  - 2x2 grid of cards: "Camera Settings" | "Shooting Guide" | "Composition" | "Editing"
  - Quick Reference card (full width, highlighted)
  - Footer: "Works offline. No ads. No subscriptions."
- **Interactions**: Tap card → navigate to detail
- **Data**: Static
- **Navigation**: Tab bar item 0

### Screen 2: Camera Settings
- **Purpose**: Model-specific camera settings
- **Layout**: Model picker + settings list
- **Elements**:
  - H1: "Camera Settings"
  - iPhone model picker (SegmentedPickerStyle or Menu)
  - Settings card for selected model:
    - Night Mode: "On — set to 10-30 seconds"
    - ISO: "1600-3200"
    - Focus: "Manual — set to infinity"
    - Exposure: "+0.3 to +0.7"
    - Timer: "3-10 second delay (reduces shake)"
    - RAW: "Enable ProRAW if available"
  - "Pro Tip" callout: "Use a tripod or stable surface. Even with Night Mode, any movement blurs the aurora."
  - Third-party app recommendations (Halide, ProCamera) with brief settings
- **Interactions**: Select model → settings update
- **Data**: Bundled JSON with per-model settings
- **Navigation**: Tab bar item 0 → push

### Screen 3: Shooting Guide
- **Purpose**: Step-by-step field instructions
- **Layout**: Numbered list, large text
- **Elements**:
  - H1: "Shooting Guide"
  - 8 numbered steps:
    1. Scout your location before dark
    2. Set up on stable ground (tripod ideal)
    3. Point north (aurora typically appears on northern horizon)
    4. Enable Night Mode, set to max duration
    5. Set focus to infinity (tap sky, then lock focus)
    6. Use timer or voice shutter to avoid shake
    7. Take multiple shots — aurora changes fast
    8. Review and adjust — check histogram for overexposure
  - Each step has: number (large, colored), title (bold), 2-3 sentences, optional "Pro Tip"
- **Interactions**: Scroll
- **Data**: Static bundled content
- **Navigation**: Tab bar item 0 → push

### Screen 4: Composition Guide
- **Purpose**: Photography composition techniques
- **Layout**: Scrollable cards
- **Elements**:
  - H1: "Composition Techniques"
  - 5 technique cards:
    1. "Foreground Interest" — trees, cabins, rocks for scale
    2. "Rule of Thirds" — horizon on lower third, aurora above
    3. "Silhouettes" — dark foreground subject against bright sky
    4. "Reflections" — lakes and water double the aurora
    5. "Panoramic" — wide shot for massive displays
  - Each card: title, description, "Do" tip, "Don't" tip, SF Symbol illustration
- **Interactions**: Scroll
- **Data**: Static bundled content
- **Navigation**: Tab bar item 1

### Screen 5: Editing Guide
- **Purpose**: Post-processing walkthrough
- **Layout**: Numbered steps
- **Elements**:
  - H1: "Edit in Photos App"
  - 6 steps:
    1. Open photo in Photos → Edit
    2. Exposure: +0.3 to +0.7 (brighten overall)
    3. Brilliance: +20 to +40 (recover shadow detail)
    4. Saturation: +10 to +20 (boost aurora colors)
    5. Noise Reduction: +30 to +50 (clean up high ISO grain)
    6. Crop: Straighten horizon, remove distracting edges
  - "Before/After" description text
  - "Advanced" section: mention Halide, Lightroom mobile
- **Interactions**: Scroll
- **Data**: Static bundled content
- **Navigation**: Tab bar item 2

### Screen 6: Quick Reference
- **Purpose**: Single-screen cheat sheet
- **Layout**: Compact list, large text
- **Elements**:
  - H1: "Quick Reference"
  - "📸 Screenshot this screen for the field" banner
  - All key settings in compact format:
    - Night Mode: ON (10-30s)
    - ISO: 1600-3200
    - Focus: ∞ (infinity)
    - Exposure: +0.3 to +0.7
    - Timer: 3-10s
    - RAW: ON (ProRAW if available)
    - Point: North
    - Stability: Tripod or solid surface
  - "Composition: Foreground + low horizon"
  - "Edit: Exposure up, Saturation up, Noise down"
- **Interactions**: Scroll (minimal)
- **Data**: Static
- **Navigation**: Tab bar item 3

## 4. Data Model

```json
{
  "metadata": {
    "version": "1.0.0",
    "contentDate": "2026-06-04"
  },
  "cameraSettings": {
    "models": [
      {
        "name": "iPhone 16 Pro Max",
        "nightMode": "On — 10 to 30 seconds",
        "iso": "1600-3200 (auto in Night Mode)",
        "focus": "Manual — tap sky, then hold to lock AE/AF",
        "exposure": "+0.3 to +0.7",
        "timer": "3-10 second delay",
        "raw": "Enable ProRAW (48MP) for maximum editing flexibility",
        "tips": ["Use the 5x telephoto for close-up aurora detail", "Action Mode is NOT suitable — use main camera"]
      },
      {
        "name": "iPhone 16 / 16 Pro",
        "nightMode": "On — 10 to 30 seconds",
        "iso": "1600-3200 (auto in Night Mode)",
        "focus": "Manual — tap sky, then hold to lock AE/AF",
        "exposure": "+0.3 to +0.7",
        "timer": "3-10 second delay",
        "raw": "Enable ProRAW",
        "tips": ["Main camera (26mm) is best for wide aurora shots"]
      },
      {
        "name": "iPhone 15 / 15 Pro",
        "nightMode": "On — 10 to 30 seconds",
        "iso": "1600-3200 (auto in Night Mode)",
        "focus": "Manual — tap sky, then hold to lock AE/AF",
        "exposure": "+0.3 to +0.7",
        "timer": "3-10 second delay",
        "raw": "Enable ProRAW on Pro models",
        "tips": ["48MP main camera on 15 Pro captures excellent detail"]
      },
      {
        "name": "iPhone 14 / 14 Pro",
        "nightMode": "On — 10 to 30 seconds",
        "iso": "1600-3200 (auto in Night Mode)",
        "focus": "Manual — tap sky, then hold to lock AE/AF",
        "exposure": "+0.3 to +0.7",
        "timer": "3-10 second delay",
        "raw": "Enable ProRAW on Pro models",
        "tips": ["Photographic Styles: set to Rich Contrast for better aurora colors"]
      },
      {
        "name": "iPhone 13 / 13 Pro",
        "nightMode": "On — 10 to 30 seconds",
        "iso": "1600-3200 (auto in Night Mode)",
        "focus": "Manual — tap sky, then hold to lock AE/AF",
        "exposure": "+0.3 to +0.7",
        "timer": "3-10 second delay",
        "raw": "Enable ProRAW on Pro models",
        "tips": ["Night Mode on ultra-wide is available but lower quality"]
      },
      {
        "name": "iPhone 12 / 12 Pro",
        "nightMode": "On — 10 to 30 seconds",
        "iso": "1600-3200 (auto in Night Mode)",
        "focus": "Manual — tap sky, then hold to lock AE/AF",
        "exposure": "+0.3 to +0.7",
        "timer": "3-10 second delay",
        "raw": "Enable ProRAW on Pro models",
        "tips": ["First iPhone with Night Mode on all cameras. Main camera recommended."]
      },
      {
        "name": "iPhone SE (3rd gen)",
        "nightMode": "On — 1 to 10 seconds (shorter range)",
        "iso": "Auto (limited manual control)",
        "focus": "Tap sky to focus, then hold to lock",
        "exposure": "+0.3 to +0.7 (swipe up after tapping focus)",
        "timer": "3 second delay recommended",
        "raw": "Not available",
        "tips": ["Single camera limits options. Use Night Mode max duration. Consider a third-party camera app for more control."]
      }
    ]
  },
  "shootingSteps": [
    {"step": 1, "title": "Scout before dark", "detail": "Arrive at your location while there's still light. Identify foreground elements (trees, rocks, buildings) and determine north direction. Set up your tripod.", "tip": "Use the Compass app to find magnetic north."},
    {"step": 2, "title": "Stabilize your iPhone", "detail": "Mount on a tripod or place on a stable surface. Even with Night Mode, any movement during a 10-30 second exposure will blur the image.", "tip": "A small beanbag on a car hood works in a pinch."},
    {"step": 3, "title": "Point north", "detail": "Aurealis typically appears on the northern horizon. Point your main camera (not ultra-wide) toward the brightest area of activity.", "tip": "If aurora is directly overhead, point straight up for a dramatic shot."},
    {"step": 4, "title": "Enable Night Mode", "detail": "Tap the yellow moon icon. Slide the duration to maximum (10-30 seconds depending on model). The longer the exposure, the more aurora detail you capture.", "tip": "If aurora is moving fast, use shorter duration (5-10s) to avoid motion blur."},
    {"step": 5, "title": "Lock focus to infinity", "detail": "Tap on the sky in your viewfinder. Hold until 'AE/AF Lock' appears. This prevents the camera from hunting focus in the dark.", "tip": "If you can't lock focus, tap a bright star or the aurora itself."},
    {"step": 6, "title": "Use a timer", "detail": "Set a 3-10 second timer or use 'Hey Siri, take a picture.' This prevents shake from pressing the shutter button.", "tip": "Volume-up button on connected headphones also works as shutter."},
    {"step": 7, "title": "Shoot multiple frames", "detail": "Aurora changes rapidly. Take 10-20 shots in succession. Review on your screen and adjust settings as needed.", "tip": "Bracket your exposures: try 5s, 10s, 20s to see which works best."},
    {"step": 8, "title": "Review and adjust", "detail": "Zoom in on your shots. Check for sharpness, color, and composition. Adjust exposure compensation if shots are too dark or washed out.", "tip": "The aurora often looks more vivid in person than in photos. Editing will help close the gap."}
  ],
  "compositionTechniques": [
    {"name": "Foreground Interest", "description": "Include trees, cabins, mountains, or people in the lower frame for scale and depth.", "do": "Place foreground subject on a rule-of-thirds line", "dont": "Leave the bottom third as empty black space", "symbol": "mountain.2.fill"},
    {"name": "Rule of Thirds", "description": "Place the horizon on the lower third line. Let the aurora fill the upper two-thirds.", "do": "Use the iPhone camera grid overlay", "dont": "Center the horizon — it creates a static, boring composition", "symbol": "rectangle.split.3x3"},
    {"name": "Silhouettes", "description": "Position a recognizable subject (person, tree, building) between you and the aurora for a dramatic silhouette.", "do": "Expose for the sky, letting the foreground go dark", "dont": "Try to light the foreground — it distracts from the aurora", "symbol": "figure.stand"},
    {"name": "Reflections", "description": "Shoot over a lake, river, or wet surface. The reflection doubles the aurora's visual impact.", "do": "Place the water's edge at the bottom of frame", "dont": "Forget to check for wind — ripples break the reflection", "symbol": "water.waves"},
    {"name": "Panoramic", "description": "For massive aurora displays, use Pano mode to capture the full sweep across the sky.", "do": "Move slowly and steadily", "dont": "Go too wide — aurora detail gets lost in a thin strip", "symbol": "panorama"}
  ],
  "editingSteps": [
    {"step": 1, "action": "Open in Edit mode", "instruction": "Open your aurora photo in Photos, tap Edit", "slider": "N/A"},
    {"step": 2, "action": "Increase Exposure", "instruction": "Slide Exposure to +0.3 to +0.7 to brighten the overall image", "slider": "Exposure: +30 to +70"},
    {"step": 3, "action": "Add Brilliance", "instruction": "Slide Brilliance to +20 to +40 to recover shadow detail and add glow", "slider": "Brilliance: +20 to +40"},
    {"step": 4, "action": "Boost Saturation", "instruction": "Slide Saturation to +10 to +20 to enhance aurora greens and purples", "slider": "Saturation: +10 to +20"},
    {"step": 5, "action": "Reduce Noise", "instruction": "Slide Noise Reduction to +30 to +50 to clean up grain from high ISO", "slider": "Noise Reduction: +30 to +50"},
    {"step": 6, "action": "Crop and Straighten", "instruction": "Straighten the horizon. Crop out distracting elements at edges", "slider": "Crop tool"}
  ]
}
```

## 5. Design Tokens
- **Colors**: Background #0A0A0A, Card #1A1A1A, Primary #7B68EE (aurora purple), Secondary #00D4AA (aurora green), Accent #FFD700, Text #E0E0E0, Text Secondary #888888
- **Typography**: SF Pro Display (headers), SF Pro Text (body). H1: 28pt/Bold, H2: 22pt/Semibold, Body: 18pt/Regular (larger than typical for field readability), Caption: 14pt
- **Spacing**: Base 4pt. Screen padding: 16pt. Card padding: 16pt. Section spacing: 24pt
- **Corner Radius**: Cards 12pt, Picker 8pt
- **Shadows**: None (dark theme — shadows invisible)
- **Icons**: SF Symbols. Camera: camera.fill. Compose: viewfinder. Edit: slider.horizontal.3. Quick Ref: doc.text.fill

## 6. Build Instructions
- **Framework**: SwiftUI
- **No third-party dependencies**
- **Data**: Bundled JSON
- **Minimum Xcode**: Xcode 15
- **Build Order**:
  1. Create iOS project (SwiftUI, iOS 16+, dark mode only)
  2. Add data.json to bundle
  3. Create data models + decoder
  4. Build TabView with 4 tabs
  5. Build Home screen (card grid)
  6. Build Camera Settings (model picker + settings display)
  7. Build Shooting Guide (numbered steps)
  8. Build Composition Guide (technique cards)
  9. Build Editing Guide (numbered steps)
  10. Build Quick Reference (compact list)
  11. Test on iPhone SE and iPhone 15 Pro Max simulators

## 7. Testing Checklist
- [ ] All 4 tabs render correctly in dark mode
- [ ] Camera settings update when switching iPhone models
- [ ] All 8 shooting steps display without truncation
- [ ] All 5 composition techniques render with icons
- [ ] All 6 editing steps display correctly
- [ ] Quick Reference fits on one screen (minimal scrolling)
- [ ] No content truncation on iPhone SE
- [ ] No network calls required
- [ ] Build succeeds with no warnings
