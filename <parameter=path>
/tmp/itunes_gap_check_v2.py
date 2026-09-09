import urllib.request
import urllib.parse
import json
import time
import sys
import re

def search_itunes(term, limit=10):
    """Search iTunes Store for apps matching the term"""
    url = f"https://itunes.apple.com/search?term={urllib.parse.quote(term)}&entity=software&limit={limit}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data.get('results', [])
    except Exception as e:
        print(f"Error searching iTunes for '{term}': {e}")
        return []

def get_expected_categories(term):
    """Determine what categories would be relevant for a search term"""
    term_lower = term.lower()
    
    # Mapping of keywords to relevant categories
    category_mapping = {
        # Tech/Development
        'open source': ['Utilities', 'Productivity', 'Developer Tools', 'Business', 'Education'],
        'osint': ['Utilities', 'Productivity', 'Reference', 'News', 'Business'],
        'intelligence': ['Utilities', 'Productivity', 'Reference', 'Business', 'Finance'],
        'ai': ['Utilities', 'Productivity', 'Education', 'Business', 'Lifestyle'],
        'generator': ['Utilities', 'Productivity', 'Photo & Video', 'Music', 'Lifestyle'],
        'guide': ['Reference', 'Education', 'Lifestyle', 'Books', 'Productivity'],
        'tracker': ['Health & Fitness', 'Utilities', 'Productivity', 'Lifestyle'],
        'scanner': ['Utilities', 'Productivity', 'Business', 'Lifestyle'],
        'detector': ['Utilities', 'Productivity', 'Security', 'Lifestyle'],
        'checker': ['Utilities', 'Productivity', 'Lifestyle', 'Business'],
        '],
        'planner': ['Productivity', 'Lifestyle', 'Business', 'Education'],
        'manager': ['Productivity', 'Business', 'Utilities', 'Lifestyle'],
        'organizer': ['Productivity', 'Lifestyle', 'Business'],
        'app': ['Utilities', 'Productivity', 'Business', 'Lifestyle'],
        'tool': ['Utilities', 'Productivity', 'Business', 'Lifestyle'],
        
        # Specific topics from our list
        'hair glossing': ['Lifestyle', 'Health & Fitness', 'Beauty', 'Food & Drink'],
        'lash clusters': ['Lifestyle', 'Health & Fitness', 'Beauty'],
        'penpot': ['Productivity', 'Business', 'Utilities', 'Developer Tools'],
        'vanceai': ['Photo & Video', 'Utilities', 'Productivity', 'Lifestyle'],
        'long-haired dachshund': ['Lifestyle', 'Education', 'Reference', 'Books'],
        'dupr': ['Sports', 'Health & Fitness', 'Lifestyle', 'Utilities'],
        'tuta email': ['Productivity', 'Business', 'Utilities', 'Communication'],
        'cherry bag charm': ['Lifestyle', 'Shopping', 'Food & Drink'],
        'workflow automation': ['Productivity', 'Business', 'Utilities', 'Developer Tools'],
        'coffee soap': ['Lifestyle', 'Food & Drink', 'Health & Fitness'],
        'yuzu peel': ['Food & Drink', 'Lifestyle', 'Health & Fitness', 'Cooking'],
        'note gpt': ['Productivity', 'Education', 'Utilities', 'Lifestyle', 'Books'],
        'ai for teachers': ['Education', 'Productivity', 'Utilities', 'Business'],
        'pistachio perfume': ['Lifestyle', 'Health & Fitness', 'Shopping'],
        'enterprise resource planning': ['Business', 'Productivity', 'Utilities'],
        'carsized': ['Lifestyle', 'Utilities', 'Productivity', 'Automotive'],
        'padel shoes': ['Lifestyle', 'Health & Fitness', 'Sports'],
        'ai music generator': ['Music', 'Utilities', 'Productivity', 'Lifestyle', 'Entertainment'],
        'sleep bonnet': ['Lifestyle', 'Health & Fitness', 'Medical', 'Beauty']
    }
    
    # Check for exact matches first
    if term_lower in category_mapping:
        return category_mapping[term_lower]
    
    # Check for partial matches
    for key, categories in category_mapping.items():
        if key in term_lower:
            return categories
    
    # Default categories for general terms
    return ['Utilities', 'Productivity', 'Lifestyle', 'Reference', 'Education', 'Business']

def categorize_app_relevance(app_name, primary_genre, genres, description, expected_categories):
    """Determine if an app is relevant to our search based on expected categories"""
    name_lower = app_name.lower()
    desc_lower = description.lower()
    genres_list = [g.strip() for g in genres] if isinstance(genres, list) else []
    if primary_genre and primary_genre not in genres_list:
        genres_list = [primary_genre] + genres_list
    
    # Check if app name or description strongly indicates relevance
    # Look for the core concept in name or description
    term_words = re.findall(r'\b\w+\b', term.lower())
    
    # Special handling for specific known apps we want to detect as relevant
    relevant_indicators = {
        'open source intelligence': ['osint', 'open source', 'intelligence'],
        'osint': ['osint', 'open source', 'intelligence'],
        'hair glossing': ['hair', 'gloss', 'shine', 'treatment'],
        'lash clusters': ['lash', 'cluster', 'extension', 'eye'],
        'penpot': ['penpot', 'design', 'collaboration', 'prototyping'],
        'vanceai': ['vance', 'ai', 'photo', 'image', 'enhance'],
        'long-haired dachshund': ['dachshund', 'dog', 'pet', 'breed'],
        'dupr': ['dupr', 'pickleball', 'rating', 'score'],
        'tuta email': ['tuta', 'email', 'encrypted', 'privacy'],
        'cherry bag charm': ['cherry', 'bag', 'charm', 'accessory', 'charm'],
        'workflow automation': ['workflow', 'automation', 'process', 'streamline'],
        'coffee soap': ['coffee', 'soap', 'scrub', 'brew'],
        'yuzu peel': ['yuzu', 'peel', 'citrus', 'fruit', 'flavor'],
        'note gpt': ['note', 'gpt', 'ai', 'study', 'learning'],
        'ai for teachers': ['ai', 'teacher', 'education', 'classroom', 'student'],
        'pistachio perfume': ['pistachio', 'perfume', 'fragrance', 'scent'],
        'enterprise resource planning': ['erp', 'enterprise', 'resource', 'planning', 'business'],
        'carsized': ['car', 'size', 'dimension', 'vehicle', 'compare'],
        'padel shoes': ['padel', 'shoe', 'footwear', 'sport', 'court'],
        'ai music generator': ['ai', 'music', 'generator', 'create', 'song'],
        'sleep bonnet': ['sleep', 'bonnet', 'hair', 'night', 'protect']
    }
    
    # Check if this is a known relevant app type
    if term_lower in relevant_indicators:
        indicators = relevant_indicators[term_lower]
        for indicator in indicators:
            if indicator in name_lower or indicator in desc_lower:
                return "RELEVANT"
    
    # Check if any expected category matches the app's genres
    for expected in expected_categories:
        if expected in genres_list:
            return "RELEVANT"
    
    # Check if term words appear in name or description
    matches = 0
    for word in term_words:
        if len(word) > 3 and (word in name_lower or word in desc_lower):
            matches += 1
    
    if matches >= 2:  # At least 2 significant word matches
        return "RELEVANT"
    
    # Check for obvious pollution categories that are never relevant for utility apps
    pollution_categories = [
        'Game', 'Games', 'Entertainment', 'Music', 'Photo & Video',
        'Social Networking', 'Dating', 'Sports'
    ]
    
    for pollution in pollution_categories:
        if pollution in genres_list:
            return "POLLUTION"
    
    # Default to potentially relevant if we can't definitively say it's pollution
    return "POTENTIALLY_RELEVANT"

def is_green_field(term):
    """Check if a term represents a green field opportunity"""
    print(f"\nChecking '{term}' for green field opportunity...")
    
    # Get expected categories for this term
    expected_categories = get_expected_categories(term)
    print(f"  Expected relevant categories: {', '.join(expected_categories[:5])}")
    
    # Search for the term
    results = search_itunes(term, limit=10)
    
    if not results:
        print(f"  No results found for '{term}' - POTENTIAL GREEN FIELD")
        return True, "NO_RESULTS"
    
    # Check top 5 results
    top_5 = results[:5]
    pollution_count = 0
    relevant_count = 0
    potentially_relevant_count = 0
    
    print(f"  Top 5 results for '{term}':")
    for i, app in enumerate(top_5, 1):
        name = app.get('trackName', 'Unknown')
        primary_genre = app.get('primaryGenreName', '')
        genres = app.get('genres', [])
        description = app.get('description', '')
        
        # Make genres a list if it isn't already
        if isinstance(genres, str):
            genres_list = [g.strip() for g in genres.split(',')] if genres else []
        else:
            genres_list = [str(g).strip() for g in genres] if genres else []
        
        # Ensure primary genre is in the list
        if primary_genre and primary_genre not in genres_list:
            genres_list = [primary_genre] + genres_list
        
        relevance = categorize_app_relevance(name, primary_genre, genres_list, description, expected_categories)
        
        print(f"    {i}. {name}")
        print(f"       Primary Genre: {primary_genre}")
        if genres_list:
            print(f"       All Genres: {', '.join(genres_list[:5])}")
        print(f"       Relevance: {relevance}")
        
        if relevance == "POLLUTION":
            pollution_count += 1
        elif relevance == "RELEVANT":
            relevant_count += 1
        else:  # POTENTIALLY_RELEVANT
            potentially_relevant_count += 1
        print()
    
    # Determine if it's a green field
    # Green field: ALL top 5 results are from completely different categories (pollution)
    # Not green field: Any of the top 5 results are relevant or potentially relevant
    if relevant_count == 0 and potentially_relevant_count == 0 and pollution_count == 5:
        print(f"  RESULT: ALL top 5 results are from different categories - GREEN FIELD CONFIRMED")
        return True, "GREEN_FIELD"
    elif relevant_count > 0:
        print(f"  RESULT: {relevant_count}/5 top results are relevant - NOT A GREEN FIELD (quality gap possible)")
        return False, "RELEVANT_APPS_EXIST"
    elif potentially_relevant_count > 0:
        print(f"  RESULT: {potentially_relevant_count}/5 top results are potentially relevant - NOT A CLEAR GREEN FIELD")
        return False, "POTENTIALLY_RELEVANT_APPS"
    else:
        print(f"  RESULT: Unclear mixture - needs manual review")
        return False, "UNCLEAR"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python itunes_gap_check_v2.py <search_term>")
        sys.exit(1)
    
    term = sys.argv[1]
    is_green, reason = is_green_field(term)
    
    if is_green:
        print(f"\n✅ '{term}' appears to be a green field opportunity!")
    else:
        print(f"\n❌ '{term}' is not a green field opportunity: {reason}")