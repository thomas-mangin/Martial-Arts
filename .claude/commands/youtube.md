# YouTube Command

Download and analyze YouTube video or channel transcripts for blog inspiration.

## Usage

**Fetch and analyze single video:**
`/youtube fetch <video_url>`

**Fetch and analyze entire channel:**
`/youtube fetch <channel_url>`

**Fetch with limit (first N videos):**
`/youtube fetch <channel_url> --limit N`

**Re-analyze existing transcript:**
`/youtube analyze <video_id>`

## Examples

```bash
# Download and analyze single video
/youtube fetch https://www.youtube.com/watch?v=KGFEDrQRWSo

# Download and analyze entire channel
/youtube fetch https://www.youtube.com/@AikidoSangenkai

# Download first 10 videos from channel
/youtube fetch https://www.youtube.com/@AikidoSangenkai --limit 10

# Re-analyze existing transcript
/youtube analyze KGFEDrQRWSo
```

## What It Does

**Fetch mode (single video):**
- Downloads transcript using yt-dlp
- Extracts metadata (title, channel, duration, date)
- Analyzes content for themes and concepts
- Generates 3-5 blog topic ideas
- Creates findings report
- Updates/creates channel registry

**Fetch mode (channel):**
- Lists all videos in channel
- Downloads transcripts for videos not yet fetched
- Analyzes each new video individually
- Generates blog ideas per video
- Creates individual findings reports
- Creates channel summary report with cross-video themes
- Updates/creates channel registry

**Analyze mode:**
- Reads existing transcript and metadata
- Performs deep content analysis
- Extracts additional blog ideas
- Updates findings report

## Files Created

**Fetch mode (single video):**
- `sources/youtube/transcripts/<video_id>.txt`
- `sources/youtube/transcripts/<video_id>.json`
- `sources/youtube/findings/YYYY-MM-DD-<video_id>.md`
- `sources/youtube/registry/<channel-name>.md` (if new)

**Fetch mode (channel):**
- All of the above for each video
- `sources/youtube/findings/YYYY-MM-DD-<channel-name>-channel-summary.md`

**Analyze mode:**
- Updates `sources/youtube/findings/YYYY-MM-DD-<video_id>.md`

## When to Use

- **Fetch (video)**: When discovering individual martial arts videos
- **Fetch (channel)**: When wanting to analyze all content from a specific instructor/channel
- **Fetch --limit**: To sample a channel before doing full analysis
- **Analyze**: To extract additional ideas from previously downloaded videos

## Result

Findings report with blog topic ideas, cross-discipline insights, and discussion prompts.

**Integration**: Ideas can feed into `/discuss` or direct blog writing.

**Note**: Transcripts are for research only. Credit videos if directly inspired.
