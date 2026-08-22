# Barefoot Ready — Landing Page Spec (v1.1, shared asset)
*Version 1.1 · Generated 2026-08-22 · Next.js · ~2h build*
*Purpose: App Store marketing URL + SEO base for content marketing + top-of-funnel lead magnet. Does NOT give away the paid core.*

---

## 1. Product Decisions

| Decision | Value |
|----------|-------|
| Scope | **Shoe Checklist ONLY is free/interactive.** Program + exercises are teased, not shipped |
| Stack | Next.js 15 (App Router) · TypeScript · Tailwind CSS v4 · fully static (`output: 'export'`) |
| Hosting | **Vercel free tier** (auto HTTPS, preview deploys per commit). Static export also portable to GitHub Pages/Cloudflare Pages if ever needed |
| Domain | `barefootready.app` if available (~$10/yr) — else default `*.vercel.app` acceptable at launch |
| Analytics | **None** (keeps "no data collected" story consistent across app + web). Revisit only if traffic justifies privacy-friendly option later |
| Content-marketing path | Repo structured so `/blog` (MDX) can be added post-launch without refactor — that's how we eventually outrank affiliate blogs on long-tail terms |
| Role in listings | iOS App Store "Marketing URL" + Play Store "Website" field both point here |
| Estimated build | ~2 hours |

## 2. Project Structure

```
barefoot-ready-site/
├── app/
│   ├── layout.tsx          # root layout + Metadata API (title, description, OG)
│   ├── page.tsx            # the landing page (all sections §3)
│   ├── globals.css         # Tailwind entry + brand tokens as CSS vars
│   └── opengraph-image.png # 1200×630 static (simpler than OG runtime gen)
├── components/
│   ├── Hero.tsx
│   ├── ShoeChecklist.tsx   # interactive lead magnet (client component)
│   ├── ProgramTeaser.tsx
│   ├── ExerciseTeaser.tsx
│   ├── FAQ.tsx
│   └── Footer.tsx
├── data/checklist.json     # copy of iOS Resources/checklist.json (single source of truth stays iOS)
└── public/                 # store badges SVG (self-hosted), favicon, og image
```

No Supabase, no API routes, no server state. Everything renders at build time. The only client component is `ShoeChecklist` (interactivity).

## 3. Page Sections (single scroll)

1. **Hero** — app name, one-liner *"Your 8-week plan to switch to barefoot shoes safely."*, two store badges (Apple/Google official SVGs), icon mark (bare footprint on cream)
2. **Free tool: Shoe Checklist** — 12 items from `data/checklist.json`, toggle cards grouped Fit / Build / Test, live "9/12 ready" score bar, state in `localStorage`. Under it: *"The full app turns this into an 8-week plan."* + store badges again
3. **Teaser: the program** — static graphic, 4 phases (Adapt → Strengthen → Load → Run), 1-line each. No day-by-day content. "Unlock in the app" CTA
4. **Teaser: exercises** — 3 names shown (Short Foot, Toe Splay, Eccentric Calf Raises) + "+15 more in the app". No instructions
5. **FAQ** — 4 items: "Do I need special shoes?" / "How long does transition take?" / "Is it safe?" (includes red-flag copy + consult-clinician line) / "iOS & Android?"
6. **Footer** — medical disclaimer verbatim from F5, copyright, contact. No cookie banner (no cookies set)

## 4. Design Tokens

Same palette: moss `#3E7C4F`, sand `#D9B26A`, cream `#FAF7F0`, text `#2B2118`, error `#B91C1C`, defined once as CSS vars consumed by Tailwind. Light mode only. Max content width 680px, radius 16px cards, generous whitespace. Font: system stack (`-apple-system, Roboto, sans-serif`).

## 5. SEO / Metadata

Use Next Metadata API in `layout.tsx` (build-time rendered into `<head>`):

```ts
export const metadata: Metadata = {
  title: "Barefoot Ready — Safe Barefoot Shoe Transition in 8 Weeks",
  description: "Free barefoot shoe buying checklist plus a structured 8-week transition program. Strengthen your feet, avoid injury, switch safely. iOS & Android.",
  openGraph: { title: "...", description: "...", images: ["/opengraph-image.png"] },
}
```

Plus JSON-LD in `page.tsx`:
```json
{"@context":"https://schema.org","@type":"SoftwareApplication",
 "name":"Barefoot Ready","operatingSystem":"iOS, Android",
 "applicationCategory":"HealthApplication","offers":{"@type":"Offer","price":"1.99","priceCurrency":"USD"}}
```

Target queries (long-tail, winnable): "barefoot shoe checklist", "what to look for in barefoot shoes", "barefoot shoe transition plan app". Do NOT chase "best barefoot shoes 2026" — unwinnable vs. established affiliate blogs for now; that's future blog-post territory.

## 6. Acceptance Criteria

- [ ] `next build` succeeds with `output: 'export'`; deploys to Vercel free tier
- [ ] Checklist toggles + score work, persist in localStorage
- [ ] Both store badges link to live listings (placeholder `#` until approved, swap URLs at launch)
- [ ] Lighthouse (mobile): Performance ≥ 95, Accessibility ≥ 95, SEO ≥ 95; first-load JS ≤ 100KB
- [ ] Zero external requests (badges/fonts self-hosted); system font stack only
- [ ] Disclaimer present in footer + FAQ safety answer
- [ ] `/blog` route stub NOT shipped yet — repo structure just must not preclude it

## 7. Build Order

1. Scaffold `create-next-app@latest` (TS + Tailwind + App Router), set `output: 'export'`, tokens as CSS vars
2. Copy `checklist.json` from iOS project into `data/`
3. Layout + metadata + hero
4. `ShoeChecklist.tsx` (client component: render, toggle, score bar, localStorage)
5. Teaser sections + FAQ + footer
6. OG image + store badge assets + JSON-LD
7. Lighthouse pass → deploy Vercel → verify live URL + meta tags in view-source
