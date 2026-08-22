# Barefoot Ready — Landing Page Spec (v1.1, shared asset)
*Version 1.0 · Generated 2026-08-22 · One static page, no framework, ~1h build*
*Purpose: App Store marketing URL + SEO capture + top-of-funnel lead magnet. Does NOT give away the paid core.*

---

## 1. Product Decisions

| Decision | Value |
|----------|-------|
| Scope | **Shoe Checklist ONLY is free/interactive.** Program + exercises are teased, not shipped |
| Stack | Single `index.html`, inline CSS + vanilla JS. Zero build step, zero dependencies |
| Hosting | GitHub Pages (new public repo `barefoot-ready-site`) or Cloudflare Pages — free, HTTPS automatic |
| Domain | `barefootready.app` if available (~$10/yr) — else default `*.github.io` is acceptable at launch |
| Analytics | **None** (keeps the "no data collected" story consistent across app + web). Revisit only if traffic justifies privacy-friendly option later |
| Role in listings | iOS App Store "Marketing URL" + Play Store "Website" field both point here |
| Estimated build | ~1 hour |

## 2. Page Structure (single scroll)

1. **Hero** — app name (SF Pro fallback stack: `-apple-system, Roboto, sans-serif`), one-liner *"Your 8-week plan to switch to barefoot shoes safely."*, two store badges (Apple/Google official SVG badges), hero visual = app icon mark (bare footprint on cream)
2. **Free tool: Shoe Checklist** — the 12 items from `checklist.json`, rendered as toggle cards grouped Fit / Build / Test, live "9/12 ready" score bar. State kept in `localStorage` only. Under it: *"The full app turns this into an 8-week plan."* + store badges again
3. **Teaser: the program** — static graphic of the 4 phases (Adapt → Strengthen → Load → Run) with 1-line descriptions. No day-by-day content. "Unlock in the app" CTA
4. **Teaser: exercises** — 3 sample exercise names shown (Short Foot, Toe Splay, Eccentric Calf Raises) + "+15 more in the app". No instructions shown
5. **FAQ** — 4 items: "Do I need special shoes?" / "How long does transition take?" / "Is it safe?" (answer includes red-flag copy + consult-clinician line) / "iOS & Android?"
6. **Footer** — medical disclaimer verbatim from F5, copyright, contact link. No cookie banner needed (no analytics/cookies set)

## 3. Content Source

Copy `checklist.json` from the iOS project `Resources/` into the site repo. Page JS fetches/embeds it (inline the JSON in a `<script type="application/json">` block at build time — keep it a copy, single source of truth remains the iOS project).

## 4. Design Tokens

Same brand palette: moss `#3E7C4F`, sand `#D9B26A`, cream `#FAF7F0`, text `#2B2118`, error `#B91C1C`. Light mode only (web landing page). Max content width 680px, generous whitespace, radius 16px cards. No dark mode in v1 of the page.

## 5. SEO / Metadata (the real reason this page exists)

```html
<title>Barefoot Ready — Safe Barefoot Shoe Transition in 8 Weeks</title>
<meta name="description" content="Free barefoot shoe buying checklist plus a structured
8-week transition program. Strengthen your feet, avoid injury, switch safely. iOS & Android.">
<!-- OG -->
<meta property="og:title" content="Barefoot Ready — 8-Week Barefoot Shoe Transition Coach">
<meta property="og:description" content="Free shoe checklist + full transition program in the app.">
<meta property="og:image" content="[absolute URL to og-image.png 1200×630, cream bg + footprint + wordmark]">
<!-- JSON-LD -->
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"SoftwareApplication",
 "name":"Barefoot Ready","operatingSystem":"iOS, Android",
 "applicationCategory":"HealthApplication","offers":{"@type":"Offer","price":"1.99","priceCurrency":"USD"}}
</script>
```

Target queries (long-tail, winnable vs. affiliate blogs): "barefoot shoe checklist", "what to look for in barefoot shoes", "barefoot shoe transition plan app". Do NOT chase "best barefoot shoes 2026" — unwinnable.

## 6. Acceptance Criteria

- [ ] Single HTML file < 60KB total, loads offline after first visit (tiny inline service worker optional — skip if it complicates)
- [ ] Checklist toggles + score work, persist in localStorage
- [ ] Both store badges link to live listings (placeholder `#` until apps are approved — set `rel="noopener"`, swap URLs at launch)
- [ ] Lighthouse: Performance ≥ 95, Accessibility ≥ 95, SEO ≥ 95
- [ ] No cookies, no external requests except store badge SVGs (self-host them)
- [ ] Disclaimer present in footer + FAQ safety answer

## 7. Build Order

1. HTML skeleton + tokens + hero
2. Checklist component (render from embedded JSON, toggle logic, score bar, localStorage)
3. Teaser sections + FAQ + footer
4. Meta/OG/JSON-LD + og-image.png
5. Lighthouse pass, deploy to GitHub Pages, verify live URL
