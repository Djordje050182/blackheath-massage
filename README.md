# Blackheath Massage Therapy

Marketing site for **Blackheath Massage Therapy** — mobile massage across Blackheath and the upper Blue Mountains, NSW. Therapist: Geoff Turner.

**Live preview:** https://djordje050182.github.io/blackheath-massage/

## What's here

| File | Purpose | Needed for preview? |
|------|---------|---------------------|
| `index.html` | The entire website — HTML, CSS, JS and all imagery baked in as base64. Fully self-contained. | **Yes** |
| `robots.txt` | Allows search + AI crawlers, points to the sitemap. | No (hosting only) |
| `sitemap.xml` | Single-page sitemap for search engines. | No (hosting only) |
| `llms.txt` | Machine-readable summary for LLM / answer-engine grounding. | No (hosting only) |
| `geoff.jpg`, `room.jpg`, `oils.jpg` | Optimised source images, in case we switch to external image refs later. | No |

For a quick shareable preview you only need `index.html`. The rest is for when the site goes to a proper home.

## Hosting via GitHub Pages

1. Repo **Settings > Pages**
2. Source: **Deploy from a branch**, Branch: `main`, Folder: `/ (root)`
3. Save, wait ~60s, refresh the Pages screen for the live URL.

## SEO / canonical setup

All absolute URLs (canonical tag, Open Graph, JSON-LD `@id`s, `sitemap.xml`, `robots.txt`, `llms.txt`) point at the live GitHub Pages origin:

```
https://djordje050182.github.io/blackheath-massage/
```

`.nojekyll` is present so Pages serves every file (including `robots.txt`/`llms.txt`) verbatim.

### If you later move to a custom domain (e.g. `blackheathmassagetherapy.com.au`)

Find-and-replace the origin across `index.html`, `sitemap.xml`, `robots.txt` and `llms.txt`:

```
https://djordje050182.github.io/blackheath-massage  →  https://www.your-domain.com.au
```

…add a `CNAME` file containing the bare domain, point DNS at GitHub Pages, then submit the sitemap in Google Search Console.

## To do before it goes properly live

- Add a `1200x630` `og-image.jpg` at the site root for social link previews. *(A placeholder is generated and committed; swap for a real branded shot when available.)*
- Hero and the 3-image gallery still use stock placeholder photos — swap for real shots when available.
- Add real customer reviews (with `Review` / `aggregateRating` schema) once you have them — do **not** fabricate these; Google penalises fake review markup.
