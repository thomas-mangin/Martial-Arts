# Track-Source Command - Register Martial Arts Content Creators

Launches the track-source agent to register martial arts bloggers or YouTube channels for monitoring.

## Usage

`/track-source "[Name]" "[URL]" "[Discipline]"`

**Examples:**
- `/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"`
- `/track-source https://www.youtube.com/@Tony_Sargeant`

## What It Does

The track-source agent will:
1. Detect content type (blog or YouTube channel)
2. Fetch initial information from the source
3. Create profile in `sources/registry/` or `sources/youtube/registry/`
4. Record URL, discipline, focus areas
5. Set up tracking structure for scanning/analysis

## Result

**For Blogs**: Profile saved in `sources/registry/[name].md`
- Ready to scan with `/scan-sources [name]`

**For YouTube**: Profile saved in `sources/youtube/registry/[name].md`
- Ready to analyze videos with `/youtube-fetch <video_url>`

## When to Use

When discovering a martial arts blogger or YouTube channel worth monitoring for inspiration, response opportunities, and cross-discipline insights.

## Note

The agent will fetch initial context automatically. For blogs, use `/scan-sources` for ongoing monitoring. For YouTube channels, use `/youtube-fetch` to analyze specific videos.
