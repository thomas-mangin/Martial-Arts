# Analyze YouTube Channel

**Usage**: `/analyze-youtube-channel <channel-name>`

**Purpose**: Comprehensive analysis of downloaded YouTube channel transcripts. Identifies themes, teaching style, and generates blog ideas.

**Examples**:
- `/analyze-youtube-channel tony-sargeant`
- `/analyze-youtube-channel heins-approach`
- `/analyze-youtube-channel alexander-gent`

**What It Does**:
- Analyzes all transcripts for the channel
- Identifies major cross-video themes (5-10 themes)
- Documents instructor's unique teaching approach
- Generates 10+ prioritized blog post ideas
- Creates comprehensive channel summary report
- Updates channel registry with findings

**Requirements**:
- Transcripts must be downloaded first (use `/youtube fetch <channel-url>`)
- Channel must have registry entry in `sources/youtube/registry/`

**Output**:
- Channel summary: `sources/youtube/findings/YYYY-MM-DD-<channel>-channel-summary.md`
- Updated registry: `sources/youtube/registry/<channel>.md`

**Time**: 1-2 hours depending on channel size

**When to Use**:
- After downloading all transcripts from a channel
- Before cross-referencing multiple channels
- To identify blog topics from specific instructor

---

## Command Implementation

This command launches the `youtube-channel-analyzer` agent with the specified channel name.
