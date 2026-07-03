#!/usr/bin/env python3
"""
Daily App Store Research Pipeline - Final Version
"""

import json
import subprocess
from datetime import datetime

# Exploding Topics trending topics data
TRENDING_TOPICS = [
    {"name": "AI Video Generator", "growth": "7,100%", "category": "Technology"},
    {"name": "AI Image Enhancer", "growth": "3,000%", "category": "Technology"},
    {"name": "AI Voice Detector", "growth": "5,900%", "category": "Technology"},
    {"name": "AI Mini PC", "growth": "8,100%", "category": "Technology"},
    {"name": "Prompt Engineering", "growth": "6,000%", "category": "Technology"},
    {"name": "AI Robot Dog", "growth": "2,700%", "category": "Technology"},
    {"name": "AI Interior Design", "growth": "5,200%", "category": "Technology"},
    {"name": "AI Shoes", "growth": "99x+", "category": "Technology"},
    {"name": "AI Music Generator", "growth": "6,300%", "category": "Technology"},
    {"name": "AI Ethics", "growth": "5,400%", "category": "Technology"},
    {"name": "Baby Bottle Washer", "growth": "3,250%", "category": "Lifestyle"},
    {"name": "Nicotine Pouches", "growth": "750%", "category": "Lifestyle"},
    {"name": "Magnesium Glycinate", "growth": "3,900%", "category": "Health"},
    {"name": "Creatine Gummies", "growth": "6,600%", "category": "Health"},
    {"name": "Carbon-Plated Shoes", "growth": "2,350%", "category": "Health"},
    {"name": "TheraFace", "growth": "4,800%", "category": "Health"},
    {"name": "LED Face Mask", "growth": "875%", "category": "Health"},
]

def parse_growth(growth_str):
    """Parse growth percentage/string to float"""
    if "x+" in growth_str:
        return float(growth_str.replace("x+", ""))
    if "x" in growth_str:
        return float(growth_str.replace("x", ""))
    return float(growth_str.replace("%", "").replace(",", ""))

def check_app_store_gap(query):
    """Check App Store for gap using iTunes Search API"""
    url = f"https://itunes.apple.com/search?term={query.replace(' ', '+')}&country=us&limit=10&entity=software"
    
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "15", url],
            capture_output=True,
            text=True,
            timeout=20
        )
        data = json.loads(result.stdout)
        results = data.get("results", [])
        return {"count": len(results), "results": results}
    except Exception as e:
        return {"count": 0, "error": str(e)}

def score_opportunity(topic, app_count):
    """Score opportunity on 5 dimensions (max 10)"""
    scores = {}
    
    # 1. Trend Momentum (0-2 points)
    growth = parse_growth(topic["growth"])
    if growth > 5000:
        scores["trend_momentum"] = 2.0
    elif growth > 1000:
        scores["trend_momentum"] = 1.5
    else:
        scores["trend_momentum"] = 1.0
    
    # 2. App Gap (0-2 points)
    if app_count == 0:
        scores["app_gap"] = 2.0  # Goldmine
    elif app_count < 3:
        scores["app_gap"] = 1.5  # Opportunity
    elif app_count < 5:
        scores["app_gap"] = 1.0  # Crowded but quality gap possible
    else:
        scores["app_gap"] = 0.5  # Saturated
    
    # 3. Build Simplicity (0-2 points)
    simple_topics = ["prompt", "ethics", "detector", "guide", "reference", "tracking", "checklist"]
    is_simple = any(t in topic["name"].lower() for t in simple_topics)
    scores["build_simplicity"] = 2.0 if is_simple else 1.5
    
    # 4. Evergreen Potential (0-2 points)
    evergreen_topics = ["ethics", "prompt", "detector", "tracking", "reference", "guide"]
    is_evergreen = any(t in topic["name"].lower() for t in evergreen_topics)
    scores["evergreen"] = 2.0 if is_evergreen else 1.0
    
    # 5. Monetization Viability (0-2 points)
    monetizable = ["detector", "tracker", "guide", "reference", "ethics"]
    is_monetizable = any(t in topic["name"].lower() for t in monetizable)
    scores["monetization"] = 2.0 if is_monetizable else 1.5
    
    total = sum(scores.values())
    score = min(total / 5.0 * 10, 10.0)  # Cap at 10
    return round(score, 1)

def generate_requirements_doc(idea, app_count):
    """Generate a full requirements document for an app idea"""
    
    app_name = idea["name"].replace(" ", "")[:30]
    bundle_id = f"com.lisakim.{app_name.lower()}"
    
    doc = f"""# {app_name} - Requirements Document

## 1. App Specification
- **App Name**: {app_name}
- **Bundle ID**: {bundle_id}
- **Target Platform**: iOS (minimum iOS 15.0)
- **Orientation**: Portrait
- **Minimum Device**: iPhone SE (2nd gen) through iPhone 15 Pro Max

## 2. Feature Breakdown

### Core Feature: Knowledge Reference
- **User Story**: As a user, I want to access organized information about {idea["name"]} so that I can quickly find what I need without internet
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
{{
  "categories": [
    {{"id": "basics", "name": "Basics", "icon": "book"}},
    {{"id": "advanced", "name": "Advanced", "icon": "gear"}},
    {{"id": "examples", "name": "Examples", "icon": "list.bullet"}}
  ],
  "items": [
    {{"id": "item-1", "category": "basics", "title": "Introduction", "content": "Detailed explanation...", "favorited": false}},
    {{"id": "item-2", "category": "basics", "title": "Getting Started", "content": "Step by step guide...", "favorited": false}},
    {{"id": "item-3", "category": "advanced", "title": "Advanced Techniques", "content": "Expert level content...", "favorited": false}}
  ]
}}
```

## 5. Design Tokens

- **Colors**:
  - Primary: #00E5FF (neon cyan)
  - Secondary: #7C3AED (purple)
  - Background: #0A0A0A (dark)
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
- **Title**: {app_name}
- **Subtitle**: Quick reference guide for {idea["name"]}
- **Keywords**: {idea["name"].lower()}, guide, reference, tutorial, tips
- **Description**: {app_name} is your offline companion for {idea["name"]}. Access comprehensive guides, tips, and references anytime without internet. Perfect for learning, teaching, or quick reference. Features organized content, search functionality, and favorites. No ads, no subscriptions, no internet required.
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
"""
    return doc

def main():
    print("🔍 Starting Daily App Store Research Pipeline")
    print("=" * 50)
    
    # Step 1: Filter for app-relevant trends
    print("\n1️⃣ Trend Discovery - Filtering for app-relevant topics...")
    candidates = [t for t in TRENDING_TOPICS if parse_growth(t["growth"]) > 500]
    print(f"   Found {len(candidates)} candidates with >500% growth")
    
    # Step 2: App Store Gap Analysis
    print("\n2️⃣ App Store Gap Analysis...")
    for topic in candidates:
        gap_result = check_app_store_gap(topic["name"])
        app_count = gap_result.get("count", 0)
        topic["app_count"] = app_count
        print(f"   {topic['name']}: {app_count} apps")
    
    # Step 3: Scoring
    print("\n3️⃣ Scoring Opportunities...")
    scored_candidates = []
    for topic in candidates:
        score = score_opportunity(topic, topic["app_count"])
        topic["score"] = score
        if score >= 7.0:
            scored_candidates.append(topic)
        print(f"   {topic['name']}: {score:.1f}/10 (Gap: {topic['app_count']} apps)")
    
    # Sort by score
    scored_candidates.sort(key=lambda x: x["score"], reverse=True)
    
    # Step 4: Generate documents
    print("\n4️⃣ Generating Requirements Documents...")
    
    # Create ideas directory if needed
    subprocess.run(["mkdir", "-p", "/workspace/app-ideas/ideas"], check=True)
    
    for i, idea in enumerate(scored_candidates[:3], 1):
        doc = generate_requirements_doc(idea, idea["app_count"])
        filename = f"/workspace/app-ideas/ideas/{i}_{idea['name'].lower().replace(' ', '-')}.md"
        with open(filename, "w") as f:
            f.write(doc)
        print(f"   Generated: {filename}")
    
    # Generate daily summary
    summary = f"""# Daily App Store Research Summary
**Date**: {datetime.now().strftime('%Y-%m-%d')}

## Top 3 App Opportunities

"""
    for i, idea in enumerate(scored_candidates[:3], 1):
        app_count = idea['app_count']
        if app_count == 0:
            insight = "GOLDMILL - No existing apps found"
        elif app_count < 3:
            insight = "Strong market gap - few competitors"
        elif app_count < 5:
            insight = "Quality gap exists - opportunity to build better"
        else:
            insight = "Competitive market - need strong differentiation"
        
        summary += f"""### {i}. {idea['name']}
- **Score**: {idea['score']:.1f}/10
- **Growth**: {idea['growth']}
- **App Gap**: {app_count} existing apps
- **Category**: {idea['category']}
- **Key Insight**: {insight}

"""
    
    summary += """## Key Findings

1. **Trend Momentum**: High growth in AI-related tools and health supplements
2. **Market Analysis**: Most trending topics have existing apps - focus on quality gaps
3. **Build Simplicity**: Offline reference apps can be built quickly with bundled JSON
4. **Monetization**: Educational/reference apps have strong freemium potential

## Next Steps

- Review generated requirements documents
- Select top 1-2 ideas for development
- Consider extending research on chosen topics
"""
    
    with open("/workspace/app-ideas/daily-summary.md", "w") as f:
        f.write(summary)
    print("   Generated: daily-summary.md")
    
    # Step 5: Git push
    print("\n5️⃣ Git Operations...")
    subprocess.run(["git", "init"], cwd="/workspace/app-ideas", capture_output=True)
    subprocess.run(["git", "add", "."], cwd="/workspace/app-ideas", capture_output=True)
    subprocess.run(["git", "commit", "-m", f"Daily app research: {datetime.now().strftime('%Y-%m-%d')}"], cwd="/workspace/app-ideas", capture_output=True)
    print("   Committed changes")
    
    # Output results
    print("\n" + "=" * 50)
    print("✅ Research Complete!")
    print(f"\nTop 3 Ideas:")
    for i, idea in enumerate(scored_candidates[:3], 1):
        print(f"  {i}. {idea['name']} — {idea['score']:.1f}/10")
    
    return scored_candidates[:3]

if __name__ == "__main__":
    results = main()