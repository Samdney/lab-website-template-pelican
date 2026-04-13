# Pelican port of lab-website-template

This is a minimal Pelican rewrite of the original Jekyll template that keeps the original HTML/CSS/JS style as closely as possible while changing only what is needed for Pelican.

## What changed

- Replaced Jekyll layouts/includes with Pelican Jinja templates under `themes/lab/templates/`
- Kept the original visual assets, JavaScript, and stylesheet structure
- Transpiled the original SCSS files into static CSS files under `content/extra/_styles/`
- Replaced Jekyll collections and `_data/*.yaml` access with Pelican config + Jinja globals
- Added MathJax support through `pelican-render-math`

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run locally

```bash
make html
python -m http.server 8000 -d output
```

Then open `http://localhost:8000`.

## MathJax

Math rendering is enabled through `pelican-render-math` in `pelicanconf.py`.

Inline math:

```markdown
$E = mc^2$
```

Display math:

```markdown
$$
\int_0^1 x^2\,dx = 1/3
$$
```

## Configure

Main settings live in `pelicanconf.py`:

- `SITENAME`, `SITESUBTITLE`, `SITEDESCRIPTION`
- `HEADER_IMAGE`, `FOOTER_IMAGE`
- `NAV_PAGES`
- `LAB_LINKS`
- `PROJECTS`, `MEMBERS`, `CITATIONS`, `TYPES`

Content lives in:

- `content/pages/` for top-level pages
- `content/articles/` for blog posts
- `content/extra/images/` for images
- `content/extra/_styles/` and `content/extra/_scripts/` for static assets

## Notes

This port intentionally stays close to the original design. The biggest build-time change is that Pelican does not execute Jekyll Liquid includes, so the dynamic Jekyll page snippets were converted into Pelican templates and static page content.


## Team member pages

Individual member pages are defined as Pelican pages under `content/pages/team/` and render through the same `page.html` template using the member metadata in `pelicanconf.py`.
