# YouTube Command

Download and analyze YouTube video transcripts for blog inspiration.

## Usage

**Fetch and analyze new video:**
`/youtube fetch <youtube_url>`

**Re-analyze existing transcript:**
`/youtube analyze <video_id>`

## Examples

```bash
# Download and analyze video
/youtube fetch https://www.youtube.com/watch?v=KGFEDrQRWSo

# Re-analyze existing transcript
/youtube analyze KGFEDrQRWSo
```

## What It Does

**Fetch mode:**
- Downloads transcript using yt-dlp
- Extracts metadata (title, channel, duration, date)
- Analyzes content for themes and concepts
- Generates 3-5 blog topic ideas
- Creates findings report
- Updates/creates channel registry

**Analyze mode:**
- Reads existing transcript and metadata
- Performs deep content analysis
- Extracts additional blog ideas
- Updates findings report

## Files Created

**Fetch mode:**
- `sources/youtube/transcripts/<video_id>.txt`
- `sources/youtube/transcripts/<video_id>.json`
- `sources/youtube/findings/YYYY-MM-DD-<video_id>.md`
- `sources/youtube/registry/<channel-name>.md` (if new)

**Analyze mode:**
- Updates `sources/youtube/findings/YYYY-MM-DD-<video_id>.md`

## When to Use

- **Fetch**: When discovering new martial arts video content
- **Analyze**: To extract additional ideas from previously downloaded videos

## Result

Findings report with blog topic ideas, cross-discipline insights, and discussion prompts.

**Integration**: Ideas can feed into `/discuss` or direct blog writing.

**Note**: Transcripts are for research only. Credit videos if directly inspired.
