# Zebra Striping

## App Specification
- **App Name**: Zebra Striping
- **Bundle ID**: com.lisakim.zebra-striping
- **Platform**: iOS (minimum iOS 15)
- **Orientation**: Portrait
- **Devices**: iPhone SE through iPhone 15 Pro Max

## Feature Breakdown

### Feature 1: Offline Reference Guide
- **User Story**: As a user, I want to access reference information offline so that I can use the app anywhere
- **Acceptance Criteria**: Data loads on first open, searchable offline, no internet required
- **Priority**: P0
- **Dependencies**: Bundled JSON data
- **Complexity**: S

### Feature 2: Search & Filter
- **User Story**: As a user, I want to search for specific terms so that I can find information quickly
- **Acceptance Criteria**: Real-time search results, fuzzy matching, category filters
- **Priority**: P0
- **Dependencies**: Reference data structure
- **Complexity**: M

### Feature 3: Bookmarking
- **User Story**: As a user, I want to bookmark items so that I can save my favorite content
- **Acceptance Criteria**: Add/remove bookmarks, persistent storage, display in favorites tab
- **Priority**: P1
- **Dependencies**: User defaults/local storage
- **Complexity**: S

## Screen-by-Screen Specification

### Screen 1: Home
- **Purpose**: Browse reference content and search
- **Layout**: Navigation bar, search bar, category list, footer
- **Elements**: Search bar, category list, recent items, add button
- **Interactions**: Tap category → go to category screen, tap search → show results
- **Data**: Category names from bundled JSON
- **Navigation**: Home → Category Detail → Item Detail

### Screen 2: Category Detail
- **Purpose**: View items in a category
- **Layout**: Header with category name, item list, tab bar
- **Elements**: Back button, category title, item list, tab bar
- **Interactions**: Tap item → go to item detail, pull to refresh
- **Data**: Items filtered by category from bundled JSON
- **Navigation**: Home → Category Detail → Item Detail

### Screen 3: Item Detail
- **Purpose**: View full item details
- **Layout**: Scrollable content, back button, share button
- **Elements**: Title, content text, share button, related items
- **Interactions**: Tap share → share sheet, tap related → go to item
- **Data**: Full item details from bundled JSON
- **Navigation**: Category Detail → Item Detail

## Data Model
```json
{
  "categories": [
    {"id": "cat1", "name": "Category 1", "icon": "icon_name"},
    {"id": "cat2", "name": "Category 2", "icon": "icon_name"}
  ],
  "items": [
    {"id": "item1", "categoryId": "cat1", "title": "Item Title", "content": "Full content...", "bookmarked": false}
  ]
}
```

## Design Tokens
- **Colors**: Primary #000000, Secondary #666666, Accent #FF6B6B, Background #FFFFFF, Text #000000
- **Typography**: SF Pro Display, H1: 28pt Bold, H2: 22pt SemiBold, Body: 17pt Regular
- **Spacing**: Base 8pt, Padding 16pt, Margin 16pt
- **Corner Radius**: Card 12pt, Button 8pt
- **Icons**: SF Symbols (book, magnifyingglass, star, gear)

## App Store Metadata
- **Title**: Zebra Striping
- **Subtitle**: Reference guide with offline access
- **Keywords**: zebra-striping, reference, guide, offline, zebrastriping
- **Description**: Comprehensive zebra striping reference with offline access. Search, bookmark, and learn anytime.
- **Category**: Reference
- **Age Rating**: 4+
- **Privacy**: No data collection (on-device only)

## Build Instructions
- Xcode 15+, iOS 15+ deployment target
- SwiftUI framework, no third-party dependencies
- Data bundled as JSON in app bundle
- Build order: 1) Data model 2) Home screen 3) Category screen 4) Item detail 5) Search 6) Bookmarks
