# CLAUDE.md — Site Structure & Editing Guide

## Overview

Personal academic website for Maximiliano Moreno-López, built on the **Academic Pages** Jekyll theme and hosted on GitHub Pages. Research focus: climate policy, EU ETS2, distributional impacts, energy transitions.

- Live URL: `https://maximilianomoreno-lopez.github.io`
- Theme base: `academicpages/academicpages.github.io`
- Build: Jekyll (Ruby via `github-pages` gem) + npm (JS minification)

---

## Key Files & Directories

### Site Configuration

**`_config.yml`** — master site settings
- Site title, author info, social links, navigation, analytics
- Defines the four collections: `publications`, `talks`, `teaching`, `portfolio`
- Defines publication categories: `manuscripts`, `working_papers`, `conferences`
- Plugins: jekyll-feed, jekyll-paginate, jekyll-sitemap, jekyll-redirect-from, jemoji

### Content Collections

Each collection lives in its own directory. Every file uses YAML frontmatter.

---

#### `_pages/cv.md` — Curriculum Vitae

Layout: `archive`. Permalink: `/cv/`.
Contains static sections (Education, Experience, Skills, Awards) plus dynamic Jekyll loops that auto-pull entries from `_publications`, `_talks`, and `_teaching`.

```yaml
---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---
```

---

#### `_publications/` — Research Papers

Filename convention: `YYYY-slug.md` (e.g., `2025-ets2-distributional.md`)

Required frontmatter fields:
```yaml
---
title: "Full paper title"
collection: publications
category: working_papers   # manuscripts | working_papers | conferences
permalink: /publication/YYYY-slug
excerpt: 'One-paragraph abstract shown in listings.'
date: YYYY-MM-DD
venue: 'Journal or venue name'
paperurl: 'https://...'    # leave '' if not yet available
citation: 'Author (Year). Title. Venue.'
---
```

Categories map to display groups defined in `_config.yml`:
- `manuscripts` → Journal Articles
- `working_papers` → Working Papers & Work in Progress
- `conferences` → Policy Reports & Conference Papers

---

#### `_teaching/` — Courses & Modules

Filename convention: `YYYY-institution-course.md`

Required frontmatter fields:
```yaml
---
title: "Course Name (Level)"
collection: teaching
type: "Undergraduate course"   # or Graduate course, Workshop, etc.
permalink: /teaching/slug
venue: "Institution, Faculty/Department"
date: YYYY-MM-DD
location: "City, Country"
---
```

`/teaching/` groups courses by the year of `date`, so a course taught in several years gets **one file per year** (e.g. `2025-sciencespo-mathematics.md` and `2026-sciencespo-mathematics.md`, with distinct permalinks). The optional `since: "YYYY"` field still renders a range next to a title but is no longer the preferred way.

---

#### `_talks/` — Presentations & Seminars

Filename convention: `YYYY-slug.md`

Required frontmatter fields:
```yaml
---
title: "Talk title"
collection: talks
type: "Seminar"   # Seminar | Conference | Workshop | Invited Talk
permalink: /talks/YYYY-slug
venue: "Institution or conference name"
date: YYYY-MM-DD
location: "City, Country"
---
```

The `markdown_generator/` directory contains Python scripts that auto-generate talk files from a spreadsheet/TSV — prefer that workflow for bulk additions.

---

#### `_data/resources.yml` — Teaching resources

Student-facing notes and handouts. They live on their own page, `/resources/` (`_pages/resources.html`), which has a nav entry; `/teaching/` only carries a link to it. The list is driven by `_data/resources.yml`:

```yaml
- title: "Resource title"
  course: "Mathematics"        # short label shown above the description
  description: "One sentence shown in the list."
  url: /resources/slug/        # internal permalink, or an external URL / /files/x.pdf
```

The handout itself is a normal page in `_pages/` (e.g. `_pages/resource-derivatives.md`) with a matching `permalink`.

**Practice sheets are generated, not hand-written.** `_pages/resource-derivatives-warmup.html`,
`resource-derivatives-100.html` and `resource-derivatives-second.html` are produced by
`tools/gen_practice.py`, which holds the exercise lists and computes every solution with sympy. `_pages/resource-lagrange-practice.html` comes from `tools/gen_lagrange.py`, where statements and worked solutions are hand-written and every numeric answer is re-derived with sympy before the page is written.
To add or fix an exercise, edit the list in that script and re-run it (`pip install sympy && python tools/gen_practice.py`);
do not edit the generated HTML. Each exercise renders as a card with the solution behind a `<details>` toggle,
typeset by MathJax only when opened (`tex2jax_ignore` keeps it out of the initial pass, since MathJax
mis-measures hidden content). The same reveal script lives in `_includes/practice-reveal.html` for the short practice blocks inside the handouts (`_pages/resource-derivatives.md`, `resource-lagrange.md`): a `div.practice#practice` with `ol.practice-list--long`, one `details.practice-sol` per item, then `{% include practice-reveal.html %}`.

`/resources/` groups entries under a heading per course. The section order is the `course_order` list at the top of `_pages/resources.html` (`"Mathematics,Economics"`); a course with no entries is skipped, and anything whose `course` is not on that list lands under **Other**.

**Maths on content pages:** MathJax 3 is loaded in `_includes/footer/custom.html`, but kramdown turns `$$...$$` into `<script type="math/tex">`, which MathJax 3 no longer reads — the formula silently disappears. Write display maths as a raw HTML block instead:

```html
<div class="math-display">
\[ f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h} \]
</div>
```

Keep inline maths as plain Unicode text (*f′(x)*, *x²*, *∂U/∂x*).

---

#### `_portfolio/` — Projects & Apps

Filename convention: `portfolio-N-slug.md`

Required frontmatter fields:
```yaml
---
title: "Project title"
excerpt: "One-sentence description shown in grid."
collection: portfolio
---
```

Body: describe the project in markdown. Include tech stack, features, and links.

---

#### `_posts/` — Blog

Filename convention: `YYYY-MM-DD-slug.md`

Required frontmatter fields:
```yaml
---
title: 'Post title'
date: YYYY-MM-DD
permalink: /posts/YYYY/MM/slug/
tags:
  - tag1
  - tag2
---
```

---

### Styles

Look: warm charcoal text and headings (nothing blue, he rejected navy), terracotta as the only accent, warm off-white background, warm graphite dark mode, Fraunces (headings) + Inter (everything else). No em dashes, no arrow glyphs in copy.

**Colour tokens** live in `_sass/theme/_default_light.scss` (light) and `_sass/theme/_default_dark.scss` (dark) as CSS custom properties: `--bg`, `--surface`, `--text`, `--heading`, `--muted`, `--border`, `--accent`, `--accent-hover`, `--accent-soft`, `--code-bg`. The theme's own `--global-*` names are mapped onto them in the light file. To change a colour, edit the token; never hardcode a hex in `_custom.scss`. The Sass variables at the top of both theme files must stay identical (both files are imported; the later one wins).

**`_sass/_custom.scss`** is the only stylesheet to edit. It references tokens only, so dark mode needs no overrides there: do not add `html[data-theme="dark"]` blocks or `!important`. Sections in order: base, `.eyebrow` / `.pill` utilities, one 1200px rail, masthead, footer, sidebar, page content, listings, resources, practice sheets, buttons, home, responsive. Fonts load once in `_includes/head/custom.html` (not via `@import` in Sass).

**Home page** is `_pages/home.html` with `layout: home` (`_layouts/home.html`, no theme sidebar). Layout: a sticky profile column on the left (photo, name, four linked affiliations under small-caps labels, two buttons, contact links) and a reading column on the right (lead paragraph, research description with supervisors linked, four most recent publications via Liquid, teaching + resources mini lists, "Beyond research" with the Estrellas del Sur quote last). Update the affiliations list in the aside when a role changes.

Reusable classes: `.eyebrow` (small-caps section label; `h2.teaching-level` is styled the same), `.pill` (outlined tag, used for PDF / Slides / BibTeX links), `.button--solid|ghost` (home CTAs), `.more` (text link that closes a list).

Do not edit vendor sass under `_sass/vendor/` or the theme internals in `_sass/include/`, `_sass/layout/`.

---

## Local Development

```bash
# Install Ruby dependencies
bundle install

# Serve with live reload
bundle exec jekyll serve --livereload

# Or with Docker
docker-compose up
```

JavaScript build (only needed after editing JS files):
```bash
npm install
npm run build:js
```

---

## Common Edits

| Task | File to edit |
|---|---|
| Add a paper | Create `_publications/YYYY-slug.md` |
| Add a talk | Create `_talks/YYYY-slug.md` |
| Add a course | Create `_teaching/YYYY-slug.md` |
| Add a project | Create `_portfolio/portfolio-N-slug.md` |
| Add a teaching resource | Create `_pages/resource-slug.md` + entry in `_data/resources.yml` |
| Update CV sections | Edit `_pages/cv.md` |
| Change nav links | Edit `_config.yml` → `navigation` |
| Change author info | Edit `_config.yml` → `author` block |
| Change site colors/fonts | Edit `_sass/_custom.scss` |
| Add a blog post | Create `_posts/YYYY-MM-DD-slug.md` |

---

## Notes

- All content files use YAML frontmatter delimited by `---`.
- Archive and CV pages auto-populate via Liquid loops — no manual listing needed.
- The `files/` directory holds downloadable assets (PDF CV, papers). Reference them as `/files/filename.pdf`.
- Images for content go in `images/`. Reference as `/images/filename.jpg`.
- The `_data/` directory holds structured data (navigation, author info overrides).
