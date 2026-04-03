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

**`_sass/_custom.scss`** — primary custom stylesheet

- Typography: Inter (body), Source Serif 4 (headings)
- Accent color: teal `#0d9488`
- Text colors: `#111827` (primary), `#374151` (secondary), `#6b7280` (muted)
- Do not edit vendor sass files under `_sass/vendor/`

Other sass files:
- `_sass/_syntax.scss` — code block syntax highlighting
- `_sass/_themes.scss` — light/dark theme variables
- `_sass/include/`, `_sass/layout/`, `_sass/theme/` — theme internals (avoid editing)

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
