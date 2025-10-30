# YouTube-Analyze Command - Re-Analyze Existing Transcripts

Launches the youtube-analyze agent to analyze already-downloaded transcripts for blog ideas.

## Usage

- `/youtube-analyze <video_id>`
- `/youtube-analyze <path_to_transcript>`

**Examples:**
- `/youtube-analyze KGFEDrQRWSo`
- `/youtube-analyze sources/youtube/transcripts/KGFEDrQRWSo.txt`

## What It Does

The youtube-analyze agent will:
1. Read existing transcript and metadata files
2. Perform deep content analysis (themes, concepts, teaching methods)
3. Extract cross-discipline insights applicable to Aikido
4. Generate 3-5 detailed blog topic ideas
5. Create or update findings report

## Result

Findings saved or updated in `sources/youtube/findings/YYYY-MM-DD-<video_id>-<description>.md`

Includes:
- Content summary and key themes
- Notable concepts (paraphrased)
- Cross-discipline insights for Aikido
- 3-5 blog ideas with full details
- Discussion prompts and next steps

## When to Use

- To re-analyze a previously downloaded video with fresh perspective
- To extract additional blog ideas from existing transcripts
- After downloading transcript manually

Part of YouTube workflow:

Download once with `/youtube-fetch`, then `/youtube-analyze` as needed for fresh angles.

## Note

Multiple analyses of the same video can yield different blog ideas. Each analysis adds to findings with timestamp.
