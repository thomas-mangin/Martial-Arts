# YouTube-Fetch Command - Download and Analyze YouTube Transcripts

Launches the youtube-fetch agent to download video transcripts and analyze for blog inspiration.

## Usage

`/youtube-fetch <youtube_url>`

**Example:**
- `/youtube-fetch https://www.youtube.com/watch?v=KGFEDrQRWSo`

## What It Does

The youtube-fetch agent will:
1. Download transcript using youtube-transcript.py script
2. Extract video metadata (title, channel, duration, date)
3. Analyze content for key themes and martial arts concepts
4. Identify cross-discipline insights applicable to Aikido
5. Generate 3-5 detailed blog topic ideas
6. Create findings report with actionable recommendations
7. Update or create YouTube channel registry profile

## Result

Files created:
- Transcript: `sources/youtube/transcripts/<video_id>.txt`
- Metadata: `sources/youtube/transcripts/<video_id>.json`
- Findings: `sources/youtube/findings/YYYY-MM-DD-<video_id>-<description>.md`

## When to Use

When discovering valuable martial arts video content worth analyzing for blog inspiration. Part of YouTube-inspired workflow:

`/youtube-fetch` → review findings → `/discuss [topic]` → `/extract` → develop → `/review-aikido`

## Note

Transcripts are for research and inspiration only. Always transform concepts into original ideas and credit the source if directly inspired.
