# Slash Commands Reference

## Quick Command List

**Session Management:**
- `/resume` - Load previous session state
- `/checkpoint` - Save state and commit to git

**Content Creation (Agents):**
- `/discuss [topic]` - Explore topics through conversation
- `/extract [file]` - Transform discussion to blog draft
- `/review-aikido [file]` - Review blog post quality

**Content Discovery (Agents):**
- `/track-source [name] [url] [discipline]` - Register blogger
- `/scan-sources [name]` - Monitor bloggers for new content
- `/youtube-fetch [url]` - Download and analyze YouTube video
- `/youtube-analyze [video_id]` - Re-analyze existing transcript

---

## /resume

**Purpose**: Restore context from previous session

**Usage**: `/resume`

**What it does:**
1. Reads `session-context.md` (status, recent work, next steps, blockers)
2. Shows current topic from `topics.md`
3. Checks git status for uncommitted changes
4. Displays recent decisions from `decisions.md` (last 2-3)
5. Asks how to proceed

**When to use**: Start of every work session

**Output**: Concise session state summary and next steps

---

## /checkpoint

**Purpose**: Save current session state before ending work

**Usage**: `/checkpoint`

**What it does:**
1. Checks git status for uncommitted changes
2. Commits all changes to local git (never pushes remotely)
3. Updates `session-context.md` with current status, recent work, next steps
4. Reviews and updates `topics.md`
5. Logs any decisions made to `decisions.md`
6. Creates timestamped session summary in `sessions/` directory
   - Format: `session-YYYY-MM-DD-HHMM.md`
   - Includes: session focus, accomplishments, decisions, conversation highlights, files modified, next steps
7. Provides summary of what was saved

**When to use**: End of every work session

**Session History**: Each checkpoint creates a permanent record that can be reviewed later to understand what happened in each session.

---

## /discuss

**Purpose**: Explore Aikido topics through informal conversation

**Usage**: `/discuss [topic-name]`

**Examples:**
- `/discuss teaching-relaxation`
- `/discuss biomechanics-of-irimi`
- `/discuss iwama-approach-critique`

**What it does:**
- Agent engages in conversational dialogue about the chosen topic
- Asks probing questions to deepen understanding
- Extracts key insights from your responses
- Records specific examples and stories
- Identifies decisions and conclusions
- Creates structured discussion note in `discussions/` directory
- Highlights blog-worthy ideas

**Approach:**
- Conversational and curious (not academic)
- Asks clarifying and deepening questions
- Challenges assumptions gently
- Makes connections between ideas
- Captures your authentic voice and phrasing
- Preserves uncertainties and questions

**When to use**: Before writing, to explore ideas informally and develop understanding

**Result**: Discussion note saved as `discussions/[topic-name]-YYYY-MM-DD.md`

**Integration**: Can be extracted to blog draft with `/extract` command

---

## /extract

**Purpose**: Transform discussion notes into blog post drafts

**Usage**: `/extract discussions/[filename].md`

**Example**: `/extract discussions/teaching-relaxation-2025-10-30.md`

**What it does:**
- Agent reads the specified discussion note file
- Analyzes blog potential (thesis, key points, examples, structure)
- Assesses if there's sufficient material for a post
- Creates structured blog post draft in `posts/` directory
- Pulls best insights and examples from discussion
- Organizes into blog-appropriate structure
- Identifies gaps that need filling
- Updates discussion note with extraction status
- Provides guidance on next steps

**Extraction Quality:**
- Preserves your authentic voice
- Uses your phrasing where possible
- Structures insights logically
- Includes concrete examples from discussion
- Marks gaps clearly for later development

**When to use**: After discussion is complete and ready to become a blog post

**Result**: Initial blog draft in `posts/[topic-name]-YYYY-MM-DD.md` ready for development and review

---

## /review-aikido

**Purpose**: Review Aikido blog posts for quality before publishing

**Usage**: `/review-aikido posts/[filename].md`

**Example**: `/review-aikido posts/teaching-relaxation-2025-10-30.md`

**What it reviews:**
1. **Aikido terminology** - Japanese terms, macrons, romanization correctness
2. **Technical accuracy** - Facts about techniques, history, principles
3. **Writing clarity** - Accessibility for readers new to Aikido
4. **Structure and organization** - Flow, completeness, logical progression
5. **Authenticity** - Alignment with core values, handling of divisive topics

**Output format:**
- Overall assessment
- Terminology issues (with corrections)
- Technical/factual corrections needed
- Clarity improvements suggested
- Structural recommendations
- Authenticity check (alignment with your values)
- Final recommendation: **ready to publish** or **needs revisions**

**When to use**: After drafting a blog post, before finalizing

**Integration**: Iterate on revisions based on feedback, re-run review until ready

---

## /track-source

**Purpose**: Register martial arts bloggers to monitor for content

**Usage**: `/track-source "[Name]" "[URL]" "[Discipline]"`

**Examples:**
- `/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"`
- `/track-source "Jesse Enkamp" "https://www.karatebyjesse.com" "Karate"`
- `/track-source "Maul Mornie" "https://www.maulmornie.com" "Silat"`

**What it does:**
- Agent creates blogger profile in `sources/registry/`
- Records URL, discipline, focus areas
- Tracks scan history
- Maintains source registry index
- Optional: Fetches initial blog information

**When to use**: When discovering a martial arts blogger worth monitoring

**Source profiles include:**
- Blogger name, URL, discipline
- Focus areas and notes
- Scan history and statistics
- Ideas generated from their content
- Connection to your blog posts

**Result**: Profile saved in `sources/registry/[blogger-slug].md`

---

## /scan-sources

**Purpose**: Monitor tracked bloggers for new content and extract blog ideas

**Usage:**
- `/scan-sources` - Scan all tracked sources
- `/scan-sources [name]` - Scan specific source

**Examples:**
- `/scan-sources` - Scan all tracked bloggers
- `/scan-sources leo-tamaki` - Scan only Leo Tamaki's blog

**What it does:**
- Agent fetches recent posts from tracked blogs
- Identifies new content since last scan
- Analyzes posts for key arguments and ideas
- Generates blog topic ideas:
  - **Response**: Direct response to their argument
  - **Alternative Perspective**: Different viewpoint on same topic
  - **Inspired Exploration**: Their post sparked a related idea
- Creates findings report with actionable ideas
- Updates source profiles with scan results

**When to use**: Weekly or bi-weekly to find new content and inspiration

**Findings report includes:**
- Summary of new posts found
- Key arguments and points from each post
- Blog ideas generated (with type, angle, Aikido connection)
- Response opportunities
- Discussion prompts for `/discuss` command
- Recommended actions

**Result**: Findings saved in `sources/findings/YYYY-MM-DD-[source-name].md`

**Integration**: Ideas from findings can feed into `/discuss` or direct blog writing

---

## /youtube-fetch

**Purpose**: Download YouTube video transcripts and analyze for blog inspiration

**Usage**: `/youtube-fetch <youtube_url>`

**Examples:**
- `/youtube-fetch https://www.youtube.com/watch?v=KGFEDrQRWSo`
- `/youtube-fetch https://youtu.be/abc123XYZ`

**What it does:**
- Agent downloads transcript using yt-dlp (script: `scripts/youtube-transcript.py`)
- Extracts video metadata (title, channel, duration, upload date)
- Converts transcript to readable text format
- Analyzes content for key themes and martial arts concepts
- Generates 3-5 blog topic ideas with full details
- Creates findings report with analysis and recommendations
- Updates/creates YouTube channel registry profiles

**When to use**: When discovering valuable martial arts video content worth analyzing

**Files created:**
- Transcript: `sources/youtube/transcripts/<video_id>.txt`
- Metadata: `sources/youtube/transcripts/<video_id>.json`
- Findings: `sources/youtube/findings/YYYY-MM-DD-<video_id>-<description>.md`
- Registry: `sources/youtube/registry/<channel-name>.md` (if new)

**Important notes:**
- Transcripts are for research and inspiration only
- Never reproduce long excerpts verbatim in blog posts
- If directly inspired by video, mention it with link
- Look for universal principles applicable to Aikido

**Integration**: Ideas from YouTube findings can feed into `/discuss` or direct blog writing

---

## /youtube-analyze

**Purpose**: Analyze an already-downloaded YouTube transcript for blog ideas

**Usage:**
- `/youtube-analyze <video_id>`
- `/youtube-analyze <path_to_transcript>`

**Examples:**
- `/youtube-analyze KGFEDrQRWSo`
- `/youtube-analyze sources/youtube/transcripts/KGFEDrQRWSo.txt`

**What it does:**
- Agent reads existing transcript and metadata
- Performs deep content analysis (themes, concepts, quotes, teaching methods)
- Extracts cross-discipline insights applicable to Aikido
- Generates 3-5 detailed blog topic ideas
- Creates or updates findings report

**When to use:**
- To re-analyze a previously downloaded video
- To extract additional blog ideas from existing transcripts
- After downloading transcript manually

**Result**: Updated findings report in `sources/youtube/findings/`

**Integration**: Ideas can feed into `/discuss` or direct blog writing

---

## Command Comparison

| Command | Type | Speed | Use Case |
|---------|------|-------|----------|
| `/resume` | Lightweight | Fast | Start every session |
| `/checkpoint` | Lightweight | Fast | End every session |
| `/discuss` | Agent | Medium | Explore ideas conversationally |
| `/extract` | Agent | Fast | Discussion → blog draft |
| `/review-aikido` | Agent | Fast | Quality check before publish |
| `/track-source` | Agent | Fast | Register new blogger |
| `/scan-sources` | Agent | Medium-Slow | Find new content weekly |
| `/youtube-fetch` | Agent | Slow | Download & analyze video |
| `/youtube-analyze` | Agent | Fast | Re-analyze existing transcript |

---

*Read this file when you need detailed command documentation. Not loaded by default.*
