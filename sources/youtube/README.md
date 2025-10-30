# YouTube Content Tracking System

This directory contains tools and data for tracking YouTube martial arts content and extracting blog inspiration.

---

## Purpose

Track YouTube channels and videos that provide valuable martial arts instruction, philosophy, and insights. Extract transcripts, analyze content, and generate blog topic ideas inspired by cross-discipline martial arts teaching.

---

## Directory Structure

```
sources/youtube/
├── README.md                    # This file
├── transcripts/                 # Downloaded video transcripts
│   ├── <video_id>.txt          # Readable transcript
│   ├── <video_id>.json         # Video metadata
│   └── <video_id>.en.srt       # Raw SRT subtitle file
├── registry/                    # YouTube channel/creator profiles
│   ├── jesse-enkamp.md
│   ├── maul-morie.md
│   └── ...
└── findings/                    # Content analysis and blog ideas
    ├── 2025-10-30-<video_id>-<description>.md
    └── ...
```

---

## Workflow

### 1. Download and Analyze Video

Use the `/youtube-fetch` slash command or run the script directly:

```bash
python scripts/youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

**This will:**
- Download video transcript (auto-generated or manual subtitles)
- Extract metadata (title, channel, duration, upload date)
- Save readable transcript to `transcripts/<video_id>.txt`
- Save metadata to `transcripts/<video_id>.json`

### 2. Analyze Content

Use the `/youtube-analyze` slash command to:
- Read and analyze transcript
- Identify key themes, concepts, and teachings
- Extract cross-discipline insights applicable to Aikido
- Generate 3-5 detailed blog topic ideas
- Create findings report with actionable recommendations

### 3. Track Channels/Creators

Create profiles in `registry/` for valuable channels:
- Channel name and URL
- Primary discipline(s)
- Content focus and style
- Videos analyzed
- Why the source is valuable
- Target audiences served

### 4. Generate Blog Ideas

Findings reports include:
- Video content summary
- Key themes and concepts
- Notable quotes (paraphrased)
- Cross-discipline insights for Aikido
- 3-5 blog topic ideas with full details
- Discussion prompts for `/discuss` command
- Recommended next steps

---

## Technical Requirements

- **yt-dlp** must be installed (`brew install yt-dlp` or `pip install yt-dlp`)
- Python 3.x for running transcript download script
- Internet connection for downloading transcripts

---

## Usage Notes

### Copyright and Fair Use

- ✓ **Allowed**: Using transcripts for research and idea generation
- ✓ **Allowed**: Paraphrasing concepts and generating original blog posts
- ✓ **Allowed**: Brief quotes with attribution
- ✗ **Not Allowed**: Reproducing long transcript excerpts verbatim in blog posts
- **Best Practice**: Credit video and channel with link if directly inspired

### Transcript Availability

Not all videos have transcripts:
- Auto-generated subtitles (most common)
- Manual subtitles (highest quality)
- No subtitles (script will fail)

If no transcript is available, consider:
- Manually transcribing key sections
- Requesting creator enable subtitles
- Finding similar content elsewhere

### Quality Filtering

Not every video warrants analysis:
- ✓ Master-level instruction with clear principles
- ✓ Cross-discipline insights applicable to Aikido
- ✓ Deep exploration of martial concepts
- ✓ Cultural and philosophical context
- ✗ Basic technique demonstrations without depth
- ✗ Entertainment-focused content without pedagogical value
- ✗ Content too discipline-specific to apply to Aikido

---

## Tracked Sources

### Jesse Enkamp (Karate Nerd)
- **Channel**: [@KARATEbyJesse](https://www.youtube.com/@KARATEbyJesse)
- **Focus**: Cross-discipline martial arts, master interviews, karate tradition
- **Value**: High-quality master interviews with universal principles
- **Videos Analyzed**: 1 (Maul Morié Silat interview)

### Maul Morié (Silat Expert)
- **Appears On**: Various channels as guest instructor
- **Focus**: Silat, practical self-defense, realistic combat principles
- **Value**: High-level teaching with clear principles applicable across arts
- **Videos Analyzed**: 1 (Jesse Enkamp interview)

*(Add more sources as you discover valuable content)*

---

## Integration with Blog Workflow

YouTube findings integrate seamlessly with existing blog workflows:

**Approach A: Discussion-Based**
1. `/youtube-fetch <url>` - Download and analyze
2. `/discuss [topic]` - Explore idea from findings
3. `/extract` - Transform discussion to blog draft
4. Develop, review, finalize

**Approach B: Direct Writing**
1. `/youtube-fetch <url>` - Download and analyze
2. Review findings report for blog ideas
3. Use blog template to write directly
4. Review, revise, finalize

---

## Example: Analyzing the Maul Morié Video

```bash
# 1. Download transcript
python scripts/youtube-transcript.py "https://www.youtube.com/watch?v=KGFEDrQRWSo"

# Files created:
# - sources/youtube/transcripts/KGFEDrQRWSo.txt
# - sources/youtube/transcripts/KGFEDrQRWSo.json
# - sources/youtube/transcripts/KGFEDrQRWSo.en.srt

# 2. Analyze content (via slash command or manually)
# Creates: sources/youtube/findings/2025-10-30-KGFEDrQRWSo-maul-morie-silat.md

# 3. Review findings
# 5 blog ideas generated:
# - "Drill Makes Skill: Why Your Aikido Kata Isn't Supposed to Be Your Technique"
# - "The Aikido Paradox: How Being Non-Destructive Can Make You More Martial"
# - "Reading Before Reacting: How Aikido's Sensitivity Training Mirrors Elite Combat Skills"
# - "Why Aikido Training Feels Unrealistic (And Why That's Actually the Point)"
# - "The Water Village Principle: How Cultural Context Shapes Martial Techniques"

# 4. Write blog post
# Choose idea, use /discuss or write directly, review with /review-aikido
```

---

## Tips for Effective Analysis

1. **Focus on Principles**: Extract universal principles, not technique minutiae
2. **Find Contrasts**: Differences between arts often reveal insights about both
3. **Look for Extensions**: Similar concepts explored from different angles
4. **Note Teaching Methods**: How masters explain concepts can inspire your writing
5. **Consider Audiences**: Which blog audiences would benefit from these insights?
6. **Maintain Originality**: Use video as inspiration, not source material to copy

---

## Maintenance

- Periodically review registry profiles for outdated information
- Update channel URLs if changed
- Note videos that are removed or made private
- Track which blog posts were inspired by which videos
- Consider re-analyzing older transcripts for fresh perspectives

---

*System Created*: 2025-10-30
*Purpose*: Expand blog inspiration sources beyond written content to include video instruction
*Integration*: Works alongside blog source tracking (/track-source, /scan-sources)
