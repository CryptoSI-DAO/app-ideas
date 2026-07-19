# CollaborativeRobotics - Requirements Document

## 1. App Specification
- **App Name**: CollaborativeRobotics
- **Bundle ID**: com.lisakim.collaborativerobotics
- **Target Platform**: iOS (minimum iOS 15.0)
- **Orientation**: Portrait
- **Minimum Device**: iPhone SE (2nd gen) through iPhone 15 Pro Max

## 2. Feature Breakdown

### Core Feature: Knowledge Reference
- **User Story**: As a user, I want to access organized information about Collaborative Robotics so that I can quickly find what I need without internet
- **Acceptance Criteria**: 
  - All content loads instantly from bundled JSON
  - Search returns results in <100ms
  - No network calls required
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

### Secondary Feature: Favorites
- **User Story**: As a user, I want to save favorite topics so I can quickly access them later
- **Acceptance Criteria**:
  - User can tap star icon to favorite
  - Favorites persist across app launches
  - Clear all favorites option
- **Priority**: P1
- **Dependencies**: Core Feature
- **Complexity**: S

### Navigation Feature
- **User Story**: As a user, I want intuitive navigation so I can find content easily
- **Acceptance Criteria**:
  - Tab bar with main sections
  - Back button in navigation bar
  - Smooth transitions between screens
- **Priority**: P0
- **Dependencies**: None
- **Complexity**: S

## 3. Screen-by-Screen Specification

### Screen 1: Home
- **Purpose**: Browse and search topics
- **Layout**: Navigation bar (title, back button), search bar, category list
- **Elements**: 
  - Navigation bar with title
  - Search bar (text field)
  - Category collection view
  - Favorites button (star icon)
- **Interactions**: 
  - Tap search bar → keyboard appears
  - Tap category → navigate to Category Detail
  - Pull down to refresh
- **Data**: Categories from bundled JSON
- **Navigation**: Search → Results, Category → Category Detail

### Screen 2: Category Detail
- **Purpose**: View items in a category
- **Layout**: Navigation bar, scrollable list
- **Elements**:
  - Navigation bar with back button
  - Category title
  - List of items (cards)
- **Interactions**:
  - Tap item → navigate to Item Detail
  - Swipe left → reveal delete (for user-created items)
- **Data**: Items from bundled JSON filtered by category
- **Navigation**: Back → Home, Item → Item Detail

### Screen 3: Item Detail
- **Purpose**: Read detailed information
- **Layout**: Scrollable content view
- **Elements**:
  - Navigation bar with back button
  - Title text
  - Content text
  - Favorite button (star icon)
- **Interactions**:
  - Tap favorite → toggle state
  - Scroll horizontally for image galleries
- **Data**: Item content from bundled JSON
- **Navigation**: Back → Category Detail

## 4. Data Model

```json
{
  "categories": [
    {"id": "basics", "name": "Basics", "icon": "book"},
    {"id": "advanced", "name": "Advanced", "icon": "gear"},
    {"id": "examples", "name": "Examples", "icon": "list.bullet"}
  ],
  "items": [
    {"id": "item-1", "category": "basics", "title": "Introduction", "content": "Detailed explanation...", "favorited": false},
    {"id": "item-2", "category": "basics", "title": "Getting Started", "content": "Step by step guide...", "favorited": false},
    {"id": "item-3", "category": "advanced", "title": "Advanced Techniques", "content": "Expert level content...", "favorited": false}
  ]
}
```

## 5. Design Tokens

- **Colors**:
  - Primary: #e7f900 (neon yellow)
  - Secondary: #00E5FF (neon cyan)
  - Background: #000000 (black)
  - Text: #FFFFFF (white)
  - Success: #10B981 (green)
  - Warning: #F59E0B (amber)
  - Error: #EF4444 (red)

- **Typography**:
  - Font: SF Pro Text, SF Pro Display
  - H1: 28pt, Bold
  - H2: 22pt, Semibold
  - Body: 16pt, Regular
  - Caption: 12pt, Light

- **Spacing**:
  - Base: 8pt
  - Padding: 16pt
  - Margin: 16pt
  - Element spacing: 12pt

- **Corner Radius**:
  - Card: 12pt
  - Button: 8pt
  - Input: 8pt

- **Shadows**:
  - Card: 0px 4px 12px rgba(0,0,0,0.3)
  - Button: 0px 2px 6px rgba(0,0,0,0.2)

- **Icons**: SF Symbols (book, gear, list.bullet, star, magnifyingglass, back)

## 6. App Store Metadata
- **Title**: CollaborativeRobotics
- **Subtitle**: Quick reference guide for Collaborative Robotics
- **Keywords**: collaborative robotics, guide, reference, tutorial, tips
- **Description**: CollaborativeRobotics is your offline companion for Collaborative Robotics. Access comprehensive guides, tips, and references anytime without internet. Perfect for learning, teaching, or quick reference. Features organized content, search functionality, and favorites. No ads, no subscriptions, no internet required.
- **Promotional Text**: New version with improved organization and search
- **What's New**: Initial release - Complete offline reference guide
- **Screenshots**: 
  - Home screen with search and categories
  - Category detail with item list
  - Item detail view with content
- **App Category**: Education, Reference
- **Age Rating**: 4+
- **Privacy**: No data collected, all content on-device

## 7. Build Instructions
- **Framework**: SwiftUI
- **Dependencies**: None (SF Symbols only)
- **Data Source**: Bundled JSON
- **Minimum Xcode**: 14.0
- **Build Order**:
  1. Create data models and sample JSON
  2. Build Home screen with search
  3. Build Category Detail screen
  4. Build Item Detail screen
  5. Add favorites functionality
  6. Add navigation and styling
  7. Test on all device sizes
- **Testing Checklist**:
  - [ ] Content displays correctly on iPhone SE
  - [ ] Content displays correctly on iPhone 15 Pro Max
  - [ ] Search returns correct results
  - [ ] Favorites persist after app restart
  - [ ] No crashes on orientation changes
  - [ ] Performance is smooth (60fps)
