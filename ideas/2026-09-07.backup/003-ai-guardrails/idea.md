# AI Guardrails App Requirements

## 1. App Specification
- **App Name**: AI Guardrails
- **Bundle ID Suggestion**: com.cryptoai.aiguardrails
- **Target Platform**: iOS (minimum iOS version 16.0)
- **Orientation**: Portrait
- **Minimum Device**: iPhone SE through iPhone 15 Pro Max

## 2. Feature Breakdown
| Feature | User Story | Acceptance Criteria | Priority | Dependencies | Complexity |
|---------|------------|---------------------|----------|--------------|------------|
| AI Principle Library | As an AI developer, I want to reference key AI ethics and safety principles so that I can ensure my projects follow best practices. | - Display list of principles (fairness, transparency, privacy, accountability, etc.) with descriptions.<br>- Allow searching and filtering by category.<br>- Bookmark favorite principles. | P0 | None | L |
| Risk Assessment Tool | As an AI developer, I want to assess my AI project for potential risks so that I can mitigate them early. | - Interactive questionnaire covering data, model, deployment, and impact aspects.<br>- Calculate risk score and show breakdown by category.<br>- Suggest mitigation strategies based on answers. | P0 | None | M |
| Compliance Checklist | As a developer, I want to check compliance with AI regulations (e.g., EU AI Act, NYC Bias Audit Law) so that I can avoid legal issues. | - Select regulation(s) to check against.<br>- Show checklist of requirements with status (met/not met).<br>- Provide guidance on how to meet unmet requirements. | P1 | None | L |
| Incident Response Guide | As an AI practitioner, I want to know how to respond to AI incidents (e.g., bias discovery, privacy breach) so that I can act quickly and responsibly. | - Display step-by-step guide for common incident types.<br>- Include communication templates and escalation paths.<br>- Mark steps as completed during an incident. | P1 | None | L |
| Resource Library | As a learner, I want to access curated resources on AI safety so that I can deepen my knowledge. | - List of articles, papers, videos, and tools with descriptions.<br>- Filter by topic (bias, explainability, robustness) and format.<br>- Mark resources as read/favorite. | P2 | None | L |

## 3. Screen-by-Screen Specification
### Home Screen
- **Purpose**: Navigate to different sections of the app.
- **Layout**:
  - Header: App title.
  - Content: Grid of feature icons and labels (Principles, Risk, Compliance, Incident, Resources).
  - Footer: Tab bar with 5 items (one for each feature).
- **Elements**:
  - Header: Title (Text)
  - Feature Item: Icon (SF Symbols), Label (Text)
  - Tab Bar: 5 items (Principles, Risk, Compliance, Incident, Resources)
- **Interactions**:
  - Tap Feature Item: Navigate to corresponding section.
  - Tap Tab Bar Item: Switch to corresponding section.
- **Data**:
  - Displayed: Static text and icons.
  - Source: Hardcoded in SwiftUI.
- **Navigation**:
  - Get here: Launch app.
  - Go next: To selected section.

### Principles Screen
- **Purpose**: Browse and search AI ethics and safety principles.
- **Layout**:
  - Header: Title, search bar, and back button.
  - Content: List of principles, each showing title, short description, and category icon.
  - Tapping a principle shows full description and related resources.
- **Elements**:
  - Header: Back Button (Button), Title (Text), Search Bar (Text Field)
  - Principle Item: Title (Text), Category Icon (Image), Description (Text)
  - Principle Detail Screen: Full description (Text), Related Resources (list of links), Category Badges.
- **Interactions**:
  - Tap Back Button: Return to Home.
  - Tap Search Bar: Activate search.
  - Type in Search Bar: Filter principle list in real-time.
  - Tap Principle Item: Navigate to detail screen.
  - Tap Bookmark Icon (in detail): Toggle bookmark state.
- **Data**:
  - Displayed: Principle title, description, category, bookmark status.
  - Source: Bundled JSON data for principles, UserDefaults for bookmarks.
- **Navigation**:
  - Get here: From Home (tap Principles or tab bar).
  - Go next: To Principle Detail (tap item), Back to Home.

### Risk Assessment Screen
- **Purpose**: Answer questions to assess AI project risk.
- **Layout**:
  - Header: Title, progress indicator, and back button.
  - Content: Question card with multiple choice options, and navigation buttons (Previous, Next).
  - Show current question number and total.
- **Elements**:
  - Header: Back Button (Button), Title (Text), Progress Indicator (Text like "3/5")
  - Question Card: Question Text (Text), Option Buttons (multiple, each with text and radio circle)
  - Navigation Buttons: Previous (Button), Next (Button) – disabled on first/last question.
  - Result Screen: Risk Score (large text), Risk Level (text and color-coded bar), Breakdown by category (list), Mitigation Suggestions (list).
- **Interactions**:
  - Tap Back Button: Return to Home (if confirmed).
  - Tap Previous/Next Question: Navigate through questionnaire.
  - Tap Option Button: Select answer (only one per question).
  - On last question, tap Next: Show result screen.
  - On result screen, tap Done: Return to Home.
- **Data**:
  - Displayed: Current question, options, progress.
  - Source: Bundled JSON array of questions.
  - Result: Calculated from answers using scoring logic.
- **Navigation**:
  - Get here: From Home (tap Risk Assessment or tab bar).
  - Go next: To Result Screen (after last question), Back to Home.

### Compliance Checklist Screen
- **Purpose**: Check compliance with selected AI regulations.
- **Layout**:
  - Header: Title, regulation selector, and back button.
  - Content: List of requirements, each showing description, status icon, and expandable guidance.
  - Footer: Action button (Export Checklist).
- **Elements**:
  - Header: Back Button (Button), Title (Text), Picker (for regulations)
  - Requirement Item: Description (Text), Status Icon (checkmark/x), Disclosure Indicator (chevron)
  - Expanded View: Guidance Text (Text), Actionable Steps (list)
  - Action Button: Export Checklist (Button)
  - Exported File: PDF or text shared via Share Sheet.
- **Interactions**:
  - Tap Back Button: Return to Home.
  - Change Picker: Reload checklist for selected regulation.
  - Tap Requirement Item: Toggle expansion to show/hide guidance.
  - Tap Export Checklist: Generate and share checklist.
- **Data**:
  - Displayed: Regulation name, requirement descriptions, status (met/not met).
  - Source: Bundled JSON data for regulations and requirements.
  - Status: Determined by user marking as met/not met (stored in UserDefaults).
- **Navigation**:
  - Get here: From Home (tap Compliance or tab bar).
  - Go next: Back to Home.

### Incident Response Guide Screen
- **Purpose**: Access step-by-step guides for AI incidents.
- **Layout**:
  - Header: Title, incident type selector, and back button.
  - Content: List of steps for selected incident type, each with checkbox and description.
  - Footer: Mark All Complete button.
- **Elements**:
  - Header: Back Button (Button), Title (Text), Picker (for incident types: Bias, Privacy Breach, Model Failure, etc.)
  - Step Item: Checkbox, Description (Text)
  - Footer Button: Mark All Complete (Button)
- **Interactions**:
  - Tap Back Button: Return to Home.
  - Change Picker: Reload steps for selected incident type.
  - Tap Step Item: Toggle checkbox.
  - Tap Mark All Complete: Check all steps.
- **Data**:
  - Displayed: Incident type name, step descriptions, completion status.
  - Source: Bundled JSON data for incident types and steps.
  - Completion: Stored in UserDefaults per incident type.
- **Navigation**:
  - Get here: From Home (tap Incident Response or tab bar).
  - Go next: Back to Home.

### Resources Screen
- **Purpose**: Browse and filter AI safety resources.
- **Layout**:
  - Header: Title, search bar, filter buttons, and back button.
  - Content: Grid or list of resources, each showing thumbnail, title, type, and rating.
  - Tapping a resource shows full details and option to open URL.
- **Elements**:
  - Header: Back Button (Button), Title (Text), Search Bar (Text Field), Filter Buttons (by topic, format)
  - Resource Item: Thumbnail (Image), Title (Text), Type (Text), Rating (Stars)
  - Resource Detail Screen: Full description (Text), URL (Button to open in Safari), Read/Favorite toggles.
- **Interactions**:
  - Tap Back Button: Return to Home.
  - Tap Search Bar: Activate search.
  - Type in Search Bar: Filter resource list.
  - Tap Filter Button: Toggle filter active state.
  - Tap Resource Item: Navigate to detail screen.
  - In detail, tap URL Button: Open link in Safari.
  - In detail, toggle Read/Favorite: Update status.
- **Data**:
  - Displayed: Resource title, type, thumbnail, URL, rating, read/favorite status.
  - Source: Bundled JSON data for resources.
- **Navigation**:
  - Get here: From Home (tap Resources or tab bar).
  - Go next: To Resource Detail (tap item), Back to Home.

## 4. Data Model
### Principle (bundled JSON)
```json
[
  {
    "id": "principle_001",
    "title": "Fairness",
    "description": "AI systems should treat all individuals equitably, avoiding bias and discrimination based on protected characteristics.",
    "category": "Ethics",
    "relatedResources": ["resource_001", "resource_002"]
  },
  {
    "id": "principle_002",
    "title": "Transparency",
    "description": "AI systems should be understandable and explainable to users and stakeholders.",
    "category": "Ethics",
    "relatedResources": ["resource_003", "resource_004"]
  }
]
```

### Question (for Risk Assessment, bundled JSON)
```json
[
  {
    "id": "q_001",
    "text": "What type of data does your AI model primarily use?",
    "options": [
      { "text": "Publicly available non-personal data", "score": 0 },
      { "text": "Personal data with consent", "score": 1 },
      { "text": "Sensitive personal data (health, finance, etc.)", "score": 2 },
      { "text": "Data from vulnerable populations", "score": 3 }
    ],
    "category": "Data"
  },
  {
    "id": "q_002",
    "text": "How complex is your AI model?",
    "options": [
      { "text": "Simple rule-based or linear model", "score": 0 },
      { "text": "Standard machine learning (e.g., random forest, SVM)", "score": 1 },
      { "text": "Deep learning neural network", "score": 2 },
      { "text": "Large language model or foundation model", "score": 3 }
    ],
    "category": "Model"
  }
]
```

### Regulation (bundled JSON)
```json
[
  {
    "id": "regulation_001",
    "name": "EU AI Act",
    "description": "Proposed regulation by the European Union on artificial intelligence.",
    "requirements": [
      { "id": "req_001", "text": "Prohibit AI systems that manipulate human behavior to circumvent user free will.", "category": "Unacceptable Risk" },
      { "id": "req_002", "text": "Conduct conformity assessment for high-risk AI systems before market placement.", "category": "High Risk" }
    ]
  }
]
```

### Incident Type (bundled JSON)
```json
[
  {
    "id": "incident_001",
    "name": "Bias Discovery",
    "description": "Identification of unfair bias in AI model outputs affecting a protected group.",
    "steps": [
      { "description": "Pause deployment of the affected model immediately.", "order": 1 },
      { "description": "Notify relevant stakeholders (legal, ethics board, product lead).", "order": 2 },
      { "description": "Conduct root cause analysis to identify source of bias (data, features, etc.).", "order": 3 }
    ]
  }
]
```

### Resource (bundled JSON)
```json
[
  {
    "id": "resource_001",
    "title": "Fairness and Machine Learning: Limitations and Opportunities",
    "type": "Article",
    "url": "https://example.com/fairness-ml",
    "read": false,
    "favorite": false
  }
]
```

### User Preferences (stored in UserDefaults)
```json
{
  "bookmarkedPrinciples": ["principle_001"],
  "complianceStatus": {
    "regulation_001": {
      "req_001": true,
      "req_002": false
    }
  },
  "completedIncidentSteps": {
    "incident_001": [1, 2] // step numbers completed
  },
  "resourceStatus": {
    "resource_001": { "read": true, "favorite": false }
  }
}
```

## 5. Design Tokens
- **Colors**:
  - Primary: #2563EB (blue)
  - Secondary: #10B981 (emerald)
  - Accent: #F59E0B (amber)
  - Background: #F8FAFC (slate-50)
  - Text: #1E293B (slate-800)
  - Success: #10B981
  - Warning: #F59E0B
  - Error: #EF4444 (red-500)
- **Typography**:
  - Font Family: SF Pro Display
  - H1: 34pt, weight Bold
  - H2: 24pt, weight SemiBold
  - Body: 17pt, weight Regular
  - Caption: 12pt, weight Regular
- **Spacing**:
  - Base unit: 8pt
  - Padding/Margin: 8, 16, 24, 32, 48
- **Corner Radius**:
  - Card: 12pt
  - Button: 8pt
  - Input: 8pt
- **Shadows**:
  - Card: offset x=0, y=2, blur=8, opacity=0.1
  - Button: offset x=0, y=1, blur=3, opacity=0.2
- **Icons**: SF Symbols
  - Principles: scale.3d
  - Risk: exclamationmark.triangle.fill
  - Compliance: checkmark.seal.fill
  - Incident: exclamationmark.oclock.fill
  - Future: arrow.triangle.2.circlepath.doc.fill
  - Bookmark: bookmark.fill
  - Checkmark: checkmark.circle.fill
  - Export: square.and.arrow.up

## 6. App Store Metadata
- **Title**: AI Guardrails (12 chars)
- **Subtitle**: AI Ethics & Safety Guide (27 chars)
- **Keywords**: AI, ethics, safety, guardrails, principles, risk assessment, compliance, bias, fairness, transparency (96 chars)
- **Description**: 
  AI Guardrails is your pocket guide to building responsible AI systems. Reference key AI ethics and safety principles, assess your project's risks with an interactive questionnaire, check compliance with emerging regulations, and learn how to respond to AI incidents. Whether you're a developer, product manager, or policy maker, this app helps you navigate the complex landscape of AI safety with practical tools and curated resources. All content is available offline – no internet connection required.
- **Promotional Text**: Build AI responsibly with principles, risk tools, and compliance guides.
- **What's New**: Initial release with principle library, risk assessment, compliance checklists, incident guides, and resource library.
- **Screenshots Needed**: 
  1. Home screen with feature grid
  2. Principles screen showing list and search
  3. Risk Assessment screen showing question and progress
  4. Compliance Checklist screen showing requirements and export
  5. Incident Response Guide screen showing steps
  6. Resources screen showing list and detail
- **App Category**: Productivity (primary), Reference (secondary)
- **Age Rating**: 4+
- **Privacy**: No data collected (all data bundled or stored in UserDefaults preferences, no networking, no personal data shared)

## 7. Build Instructions
- **Framework**: SwiftUI
- **Dependencies**: None (Swift standard library + SF Symbols)
- **Data**: Bundled JSON files in app bundle for all static content; UserDefaults for user preferences and bookmarks.
- **Minimum Xcode Version**: 15.0
- **Build Order**:
  1. Create data model structs for principles, questions, regulations, incidents, resources, and user preferences.
  2. Create bundled JSON files and load them at startup.
  3. Build Home screen with navigation to sections.
  4. Build Principles screen with list, search, and detail view.
  5. Build Risk Assessment screen with questionnaire logic and result calculation.
  6. Build Compliance Checklist screen with regulation selector and requirement list.
  7. Build Incident Response Guide screen with incident type selector and step list.
  8. Build Resources screen with list, search, filter, and detail view.
  9. Implement navigation between screens.
  10. Add App Store metadata and icons.
  11. Test in simulator on various iPhone sizes.
- **Testing Checklist**:
  - [ ] Home screen loads and shows feature grid.
  - [ ] Principles list loads and search filters correctly.
  - [ ] Principle detail shows full description and bookmark toggle.
  - [ ] Risk Assessment questionnaire presents questions and calculates score.
  - [ ] Result screen shows risk level and breakdown.
  - [ ] Compliance Checklist allows selecting regulation and marking requirements met/not met.
  - [ ] Incident Response Guide allows selecting incident type and toggling step completion.
  - [ ] Resources list loads and search/filter works.
  - [ ] Resource detail shows URL and read/favorite toggles.
  - [ ] All content is accessible offline (disable network and verify).
  - [ ] App respects portrait orientation only.
  - [ ] No network requests are made.
  - [ ] App builds and runs on iPhone SE (2nd gen) and iPhone 15 Pro Max simulators.

## 8. Multi-Platform Companion Specs (Android)
When building for Android, generate a separate `requirements-android.md` file with the following adaptations:
- **applicationId**: com.cryptoai.aiguardrails (matches iOS bundle ID)
- **Stack**: Kotlin 2.x + Jetpack Compose + Material 3, minSdk 26 / targetSdk 35
- **Shared content JSONs**: copied byte-for-byte into `assets/`; never edit locally — report content issues instead.
- **Platform-mapping table**:
  - iOS UserDefaults → Android SharedPreferences
  - iOS SF Symbols → Android Material Icons (principles: scale, risk: warning, compliance: shield_check, incident: error, future: refresh)
  - iOS SF Pro Rounded → Android system Roboto font
  - iOS drop shadows → Android tonal elevation 2dp
  - iOS bundled JSON → Android via `assets.open()` and parsing
- **Extra Android acceptance criteria**:
  - Process-death persistence: user preferences (bookmarks, compliance status, etc.) survive force-stop and relaunch.
  - Predictive-back pop order: works correctly with Compose navigation.
  - Usable at 200% font scale: layouts adapt to large text sizes.
  - Zero `<uses-permission>` entries: manifest declares no permissions for offline privacy claim.
- **Play Store metadata**:
  - Title: AI Guardrails (30 chars)
  - Short displays: AI ethics & safety guide (80 chars)
  - Description: Reuse iOS description if ≤4000 chars (it is).
  - Data Safety form: "No data collected" matches permission-free manifest.
  - Content rating: Everyone expected.
  - Screenshots: same as iOS, minimum 2.
- **Estimated build time**: ~+0.5h vs iOS build (Compose overhead).

## 9. PWA Decision Rule
Not applicable for paid utility app. Instead, specify a static landing page (~1h, free hosting) with:
- **Purpose**: Free interactive top-of-funnel tool ONLY (e.g., "AI Ethics Quiz" – helps users identify their knowledge gaps).
- **Core product locked behind store links**.
- **Landing page doubles as App Store "marketing URL" field value**.
- **Tech stack**: Next.js 15 (App Router, TS, Tailwind, `output:'export'`), Vercel free.
- **Sequenced AFTER the iOS and Android apps ship** (store badges need live URLs).

**Agent guardrails**: 
- Author all entries explicitly; no placeholders.
- Localization-ready strings from day 1.
- No brand names in UI or store body copy.
- Total estimated build time ≤ 3 hours (iOS: ~2.5h, Android: ~3.0h).