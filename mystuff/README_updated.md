# Lab Website Template (Pelican Edition)

A Python **Pelican** version of the Greene Lab website template, adapted to preserve the original visual style while adding a cleaner static-site workflow, improved page organization, **paper pages**, **dark/light mode**, and support for academic/lab-focused content.

This template is intended for research groups, academic labs, collaborative projects, and personal academic websites that need a polished and customizable static website with a structure for:

- research
- publications
- projects
- team pages
- news and outreach
- contact pages
- article-style posts
- paper-style pages with table of contents

---

## Highlights

### Familiar lab website structure
The template keeps the familiar structure of the original lab website while using a Pelican-based content workflow.

### Dark and light mode
The site supports a dark/light theme toggle across standard pages, article pages, and paper pages.

### Paper pages
A dedicated paper-page layout supports HTML imported from external paper-generation workflows, such as LaTeXML/ar5iv-style output, including a left-side table of contents and metadata sidebar.

### Academic icons
The template includes **academic and scholarly icons** in addition to the usual site/social icons. This makes it easier to link to lab resources such as:

- ORCID
- Google Scholar
- PDF / manuscript links
- websites
- code repositories
- outreach and media resources

### Mobile responsiveness
The template has been updated to behave well on different screen sizes. Navigation, content sections, grids, cards, and paper layouts are designed to adapt cleanly on smaller screens.

### Pelican-native content structure
Pages, articles, and section overviews work within Pelican’s content system, so the site is easy to manage with Markdown and templates rather than a custom backend.

---

## Screenshots

### Homepage

Light mode:

![Homepage light mode](screenshots/screenshot-index-light.png)

Dark mode:

![Homepage dark mode](screenshots/screenshot-index-dark.png)

---

### Paper pages

The template includes a dedicated paper-page layout for article-like academic pages with metadata, a table of contents, and a reading-focused layout.

Light mode:

![Paper page light mode](screenshots/screenshot-paper-light.png)

Dark mode:

![Paper page dark mode](screenshots/screenshot-paper-dark.png)

---

### Example post page

Standard article/post pages support math, metadata, and previous/next navigation.

![Example post page](screenshots/screenshot-examplepost-dark.png)

---

### News pages

The template supports section overview pages such as **News**, with section text, search/filter UI, and article cards.

News overview header:

![News page header](screenshots/screenshot-news1-dark.png)

News listing:

![News page listing](screenshots/screenshot-news2-dark.png)

---

### Publications pages

Publication overview pages can display highlighted publications and structured citation cards.

Publications overview:

![Publications overview](screenshots/screenshot-publications1-dark.png)

Publication list cards:

![Publication list cards](screenshots/screenshot-publications2-dark.png)

---

### Projects page

Projects can be displayed as featured cards and sectioned listings.

![Projects page](screenshots/screenshot-projects-dark.png)

---

### Research page

A dedicated research landing page is also supported.

![Research page](screenshots/screenshot-research-dark.png)

---

### Contact page

Contact pages support CTA buttons and card-based layouts.

![Contact page](screenshots/screenshot-contact-dark.png)

---

### Lab / team pages

The template supports lab overview pages, team listings, and nested subpages.

Lab overview:

![Lab overview](screenshots/screenshot-lab1-dark.png)

Team section inside lab pages:

![Lab team section](screenshots/screenshot-lab2team-dark.png)

Standalone team page:

![Standalone team page](screenshots/screenshot-team-dark.png)

---

## Mobile responsiveness

The template is designed to be responsive across desktop and smaller screens.

Key responsive behaviors include:

- navigation that adapts to smaller widths
- grid layouts that collapse cleanly
- card-based sections that reflow on narrow screens
- paper layouts whose side content can move below or above the main content when needed
- readable typography and spacing across viewport sizes

When customizing templates, it is recommended to preserve the responsive CSS blocks and media queries already used by the theme.

---

## Academic icons and metadata

This Pelican template extends the lab-site concept with stronger support for academic metadata and scholarly links.

Examples include:

- ORCID links in headers and footers
- publication and paper resource icons
- PDF / manuscript / website / code links in citation cards
- support for social metadata for pages and articles
- paper-page metadata blocks for bibliographic context

These features are intended to make the site more useful as an academic project or lab homepage.

---

## Paper pages

One major addition in this version is the support for **paper-style pages**.

These are useful when you want a page that behaves less like a normal website page and more like an online paper or manuscript page.

Typical features include:

- title and author block
- metadata/info sidebar
- table of contents
- math support
- dark/light mode compatibility
- HTML imported from LaTeXML/ar5iv-style paper output
- integration into the main website navigation

This allows you to host papers or manuscript-style documents directly inside the website without breaking the overall site design.

---

## `paperhtml.py`

This repository also includes a helper script called **`paperhtml.py`** for importing paper HTML into the website workflow.

### What it does

The script:

- reads a chosen HTML file from a source directory
- extracts the content inside `<body>...</body>`
- writes a generated Markdown file into a target directory
- prepends Pelican metadata such as title, slug, category, and icon
- copies the remaining directory contents to the target directory
- skips the original HTML file itself

The script therefore helps convert existing HTML paper output into a form that is easier to integrate into the Pelican website content structure.

### Typical usage

```bash
python paperhtml.py /path/to/target
python paperhtml.py /path/to/target /path/to/source
python paperhtml.py /path/to/target /path/to/source --html-file index.html
```

### Generated output

The script writes a Markdown file whose filename is derived from the HTML `<title>`, normalizes it into a slug-friendly name, and inserts metadata like:

- `title`
- `slug`
- `category: paper`
- `icon`

It is especially useful if your paper workflow already generates HTML and you want to bring that into the Pelican site without manually copying `<body>` content each time.

### When to use it

Use `paperhtml.py` when:

- you have an existing exported HTML paper page
- you want to reuse the paper content inside the Pelican site
- you want to preserve assets from the source directory
- you want to avoid manually rewriting imported HTML into Markdown page files

---

## Content organization

A typical content structure may look like this:

```text
content/
  pages/
    contact.md
    research.md
    publications.md
    projects.md
    news.md
    outreach.md
    lab/
      index.md
      team.md
  articles/
    ...
  images/
  _styles/
  _scripts/
```

This structure keeps site pages, article content, and section-specific subpages organized while still working naturally with Pelican.

---

## Running the site

Typical local workflow:

```bash
make clean
make html
make serve
```

Then open the local preview in your browser.

---

## Customization

Common customization points include:

- `pelicanconf.py` for site-wide settings
- `themes/lab/templates/` for layout templates
- `content/pages/` for section pages
- `content/articles/` for post-style content
- `content/_styles/` for CSS
- `content/_scripts/` for JavaScript

---

## Recommended use cases

This template works particularly well for:

- research labs
- academic groups
- scientific software projects
- collaborative writing projects
- teaching and outreach sites
- personal academic websites

---

## Notes

- The theme intentionally stays close to the Greene Lab visual language while adapting it for Pelican.
- Paper pages are a custom extension and are especially useful for academic publishing workflows.
- The screenshots above show both standard site pages and paper-specific pages to illustrate the range of supported layouts.
