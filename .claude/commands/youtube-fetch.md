# YouTube Fetch Command

You are helping the user download and analyze YouTube video transcripts for blog inspiration.

## Command Format

`/youtube-fetch <youtube_url>`

**Example**: `/youtube-fetch https://www.youtube.com/watch?v=KGFEDrQRWSo`

## Steps to Execute

1. **Download Transcript**
   - Run the youtube-transcript.py script with the provided URL
   - Script location: `scripts/youtube-transcript.py`
   - Command: `python scripts/youtube-transcript.py "<url>"`
   - This will create:
     - Transcript text file: `sources/youtube/transcripts/<video_id>.txt`
     - Metadata JSON: `sources/youtube/transcripts/<video_id>.json`
     - Raw SRT file: `sources/youtube/transcripts/<video_id>.en.srt`

2. **Read Metadata**
   - Read the JSON metadata file
   - Extract: video title, channel, upload date, duration

3. **Analyze Transcript Content**
   - Read the transcript text file
   - Identify key themes and topics discussed
   - Extract martial arts concepts, techniques, philosophy
   - Note teaching approaches and demonstrations
   - Identify cross-discipline insights (if applicable)

4. **Generate Blog Ideas**
   - Based on transcript analysis, generate 3-5 blog topic ideas
   - For each idea, include:
     - **Title**: Compelling blog post title
     - **Type**: Response / Alternative Perspective / Inspired Exploration / Extension
     - **Angle**: The specific approach or argument
     - **Connection**: How it relates to Aikido specifically
     - **Target Audiences**: 3-5 audience profiles who would benefit
     - **Key Points**: 3-4 main points to explore
     - **Hook Potential**: What makes this interesting/engaging

5. **Create Findings Report**
   - Save analysis and blog ideas to: `sources/youtube/findings/<date>-<video_id>.md`
   - Include:
     - Video metadata (title, channel, URL, date)
     - Content summary (what was discussed)
     - Key arguments/demonstrations
     - Blog ideas generated
     - Discussion prompts for /discuss command
     - Recommended next actions

6. **Update Registry** (if this is a new channel)
   - Check if channel exists in `sources/youtube/registry/`
   - If new, create profile: `sources/youtube/registry/<channel-slug>.md`
   - Include: channel name, focus, discipline(s), videos tracked

7. **Display Summary**
   - Show video title and channel
   - Display number of blog ideas generated
   - Highlight most promising ideas
   - Suggest next steps (discuss, write directly, add to topics.md)

## Important Notes

- **Copyright Awareness**: Transcripts are for research and inspiration only. Never reproduce long excerpts verbatim in blog posts.
- **Fair Use**: Using transcripts to generate original ideas and insights is legitimate fair use.
- **Attribution**: If directly inspired by a video, mention it in blog post with link.
- **Cross-Discipline Value**: YouTube martial arts content often crosses disciplines - look for universal principles applicable to Aikido.
- **Quality Filter**: Not all videos will generate good blog ideas - be selective and honest in assessment.

## Integration with Workflow

This command integrates with existing workflows:

- **Approach A**: `/youtube-fetch` → `/discuss [topic]` → `/extract` → develop
- **Approach B**: `/youtube-fetch` → write directly from findings
- **Approach C**: `/youtube-fetch` → add ideas to topics.md for later

## Error Handling

If transcript download fails:
- Video may not have subtitles/captions available
- Try suggesting the user enable subtitles on the video first
- Offer alternative: user could manually transcribe key sections
