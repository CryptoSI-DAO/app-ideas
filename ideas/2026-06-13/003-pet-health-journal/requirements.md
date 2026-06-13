# App Idea: Pet Health Journal

*Generated: 2026-06-13*
*Confidence Score: 6.8/10*

---

## Pitch
A simple, visual health journal for pet owners to track vet visits, medications, weight, vaccinations, and daily symptoms — keeping all pet health data in one place instead of scattered across paper records and vet receipts. With pet ownership at record highs and pet health spending projected to exceed $40B in the US this year, owners need (and will pay for) tools that help them manage their pet's wellbeing.

## Target Audience
- Primary: Dog and cat owners (56% of US households own a pet)
- Secondary: Multi-pet households, new pet owners, pet parents of senior/sick animals
- Demographics: US-based, 25-55, skews female (60/40), iPhone users

## Problem Statement
Pet owners manage health data across: vet paper records, text threads with partners, photos of pill bottles, calendar reminders for medications, and memory. When the vet asks "when did you start that medication?" — nobody knows. Existing pet apps focus on pet sitting (Rover), social (DogLog), or pure vet finding — not health tracking. The health journal niche is underserved on iOS.

## Trend Evidence
- **Source 1**: Exploding Topics shows "cat toothpaste" (+688%) — exploding interest in proactive pet dental/health care. Signals owners are getting more serious about pet health management.
- **Source 2**: Pet industry spending has grown 7% YoY for 5 consecutive years. "Pet parents" now outnumber "pet owners" in surveys — people view pets as family members, demanding healthcare-grade tracking.
- **Source 3**: App Store search for "pet health tracker" returns ~50 results, but most are vets booking apps, social networks, or dog walk trackers. True health journal apps have <1,000 reviews and look dated.
- **Momentum**: Sustained rise — pet ownership grew during COVID and hasn't declined. The "pet as family" trend continues.

## Competitor Analysis

| App Name | Rating | Price | Weakness |
|----------|--------|-------|----------|
| Pet Care Tracker | ⭐ 3.2 | Free with ads | Cluttered UI, limited tracking categories, ads for pet health app is aggressive |
| PetDesk | ⭐ 4.3 | Free | Primarily vet appointment booking, not health journal |
| 11Pets | ⭐ 3.8 | Freemium | Feature-heavy but overwhelming UI, subscription for core features |
| DogLog | ⭐ 4.0 | Free | Social-focused, not health-focused |

**App Gap**: No clean, simple, health-first pet journal exists. Pet owners desperately need a place to log symptoms, meds, weight trends, and vet notes without social features or booking integrations. The best existing app (11Pets) is feature-bloated and confusing.

## Core Features (MVP)

### Must-Have (v1.0)
1. **Pet Profiles** — Create profiles for multiple pets with photo, name, breed, birth date, weight, microchip ID, and vet contact. Support dogs, cats, birds, rabbits, and "other".
2. **Health Log** — Daily entries tracking: symptoms (dropdown from 30+ common issues), mood (great/good/okay/poor), activity level, appetite, and notes. Quick-add buttons for common activities (walk, fed, meds given, vomited, etc.).
3. **Medications & Reminders** — Log current medications with name, dosage, frequency, and start/end dates. Push notification reminders at scheduled times.
4. **Weight Tracker** — Log weight over time with a simple line chart showing trend. Flag significant changes (>10% in 30 days).
5. **Vet Visit Log** — Record vet visits with date, reason, diagnosis, treatments, and cost. Attach notes. Running total of annual vet spend.

### Nice-to-Have (v1.1+)
- **Vaccination Records** — Track all vaccines with due dates and reminders
- **Photo Timeline** — Daily photo log to document visible symptoms or recovery
- **Export Vet Report** — Generate PDF summary to email to vet before appointments
- **Multi-Pet Dashboard** — Overview of all pets' health status on home screen
- **Apple Health Sync** — Pet walks sync to owner's Health app as "Walking"

## Content & Data
- **Symptom Library**: 40+ common pet symptoms organized by body system (digestive, respiratory, skin, behavioral, musculoskeletal, etc.)
- **Medication Database**: 60+ common pet medications with standard dosages (for display only — includes vet consultation disclaimer)
- **Breed Reference**: Top 50 dog breeds and 30 cat breeds with standard weight ranges
- **All data is user-entered with smart defaults. No external API.**

## Design Direction
- **Style**: Warm, friendly, life.app aesthetic. Round cards, soft colors, pet photo-heavy. Think of it as a baby tracker app but for pets.
- **Color Palette**:
  - Primary: #FF6B6B (Warm Coral)
  - Secondary: #4ECDC4 (Teal)
  - Accent: #FFE66D (Sunny Yellow)
  - Background: #FFF9F5 (Warm white)
  - Card: #FFFFFF
  - Text Primary: #2D3436
  - Text Secondary: #636E72
  - Shadows: 0px 2px 6px rgba(255, 107, 107, 0.10)
- **Typography**: SF Pro Rounded (friendly feel). H1: 28pt Bold. H2: 22pt Semibold. Body: 16pt Regular. Pet names: 20pt Bold Rounded.
- **Key Screens**: Home Dashboard (pet cards), Pet Profile, Daily Log Entry, Health History, Medications, Weight Chart, Vet Visits, Settings
- **Navigation**: Tab bar (Home, Log, Meds, History, Settings) with pet selector at top
- **Reference Apps**: Baby Tracker (NCB), WaterMinder (simplicity), Daylio (mood tracking)

## Technical Notes
- **Platform**: iOS (SwiftUI), minimum iOS 17
- **Backend**: None — fully on-device
- **APIs**: None for MVP
- **Data Storage**: SwiftData / Core Data, all local
- **Notifications**: UNUserCenter for medication reminders
- **Estimated Build Time**: 2.5-3 hours
- **Complexity**: Medium (multiple data entities and relationships)

## App Store Listing

### Title
PetLog — Health Journal

### Subtitle
Track vet visits, meds & weight

### Keywords
pet,dog,cat,health,vet,medical,vaccine,weight,medication,symptom,veterinary,journal,tracker,pet care,animal,bird,rabbit,puppy,kitten,log,record

### Description
Keep your pet's health history in your pocket — not in a shoebox of vet receipts.

PetLog is a simple, beautiful health journal for dogs, cats, and other pets. Track daily symptoms, medications, weight, vet visits, and vaccinations — all in one place.

WHY PETLOG?
• Beautiful pet profiles with photos & key info
• Quick daily health log — mood, appetite, activity, symptoms in under 30 seconds
• Medication reminders — never miss a dose again
• Weight tracking with trend charts
• Vet visit history with costs — know exactly what you're spending
• 100% private — your pet's data stays on your device
• Works for dogs, cats, birds, rabbits, and more

WHEN TO USE PETLOG:
✓ Your pet is on daily medication
✓ Managing a chronic condition
✓ Tracking weight for vet recommendations
✓ Preparing for vet visits with complete history
✓ Managing multiple pets
✓ You're a new pet parent who wants to stay organized

Pet health shouldn't be complicated. PetLog gives you peace of mind — and gives your vet better information. When your vet asks "how long has that been happening?" you'll finally have an answer.

Free to download and use. No account required.

### Category
Primary: Health & Fitness
Secondary: Lifestyle

### Pricing
- **Model**: Free with one-time unlock ($3.99 for unlimited pets, currently limited to 2 pets in free version)
- **Reasoning**: Free download attracts pet parents. Multi-pet households (30%+ of pet owners) will pay to unlock. $3.99 is reasonable for health management tool. One-time purchase aligns with user expectations for utility apps.
- **Monetization Path**: PDF vet report export ($0.99), insurance documentation mode

## Scoring Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trend Momentum | 7/10 | Pet ownership is secular trend. Health spending growing. "Pet as family" continues. |
| App Gap | 7/10 | Pet apps exist but health journal niche is underserved. 11Pets is closest but bloated. Clean opportunity. |
| Build Simplicity | 7/10 | Multiple data entities, relationships, charts. More complex than other ideas but still achievable in 3 hours. |
| Evergreen Potential | 8/10 | People will always have pets. Pet health is permanent need. |
| Monetization | 6/10 | Pet owners spend willingly on pets. $3.99 unlock is reasonable. Smaller market than productivity/finance. |
| **Average** | **7.0/10** | |

## Risk Assessment
- **Trend Fizzle**: Very low — pet ownership is deeply embedded in American culture
- **App Store Rejection**: Low — health app but for animals, no HIPAA concerns. Include medical disclaimer.
- **Competition**: Low-Medium — existing apps aren't focused on health journaling specifically
- **Legal/IP**: Low — include clear "not veterinary advice" disclaimer throughout app
- **Content Maintenance**: Low — symptom/medication libraries are stable over time

## Validation Checklist
- [x] At least 3 sources confirm trend (Exploding Topics pet care, pet industry spending growth, App Store gap)
- [x] App Store shows weak competition in health journal niche specifically
- [x] MVP can be built without backend/API dependencies
- [x] Non-controversial content with appropriate disclaimers
- [x] No legal/copyright issues
- [x] Build time estimate ≤ 3 hours
