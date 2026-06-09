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

## To do before it goes properly live

- The canonical tag, `sitemap.xml`, `robots.txt` and the JSON-LD all currently point at `https://www.blackheathmassagetherapy.com.au/`. Fine for a preview, but these must match the real final domain before submitting to Google.
- Add a `1200x630` `og-image.jpg` at the site root for social link previews.
- Hero and the 3-image gallery still use stock placeholder photos — swap for real shots when available.
