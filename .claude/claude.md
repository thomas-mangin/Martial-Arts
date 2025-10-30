# Project Context for Claude Code

This file provides context about the project setup and systems in place for AI assistants in future sessions.

---

## Project Purpose

This is a Master's thesis (MA) project focused on writing Aikido blog posts. The system is designed to maintain continuity between Claude Code sessions, allowing work to resume seamlessly.

---

## System Architecture

### Session Continuity System

A complete workflow system has been implemented to maintain context between sessions:

#### Core Documents (Root Directory)

1. **topics.md** - Blog topic management
   - Current topic being worked on
   - Queued topics (priority order)
   - Topic ideas (brainstorming)
   - Completed topics (archive)

2. **session-context.md** - Session state tracking
   - Current Status: What's being worked on now
   - Recent Work: What was accomplished
   - Next Steps: Actionable items for continuation
   - Blockers/Questions: Issues needing resolution
   - Notes: Additional context
   - Updated with timestamp on each checkpoint

3. **decisions.md** - Decision log
   - Chronological record of important decisions
   - Date, decision, and rationale for each entry
   - Helps understand why certain approaches were chosen

4. **blog-template.md** - Blog post template
   - Copy this file for each new blog post
   - Pre-structured sections with guidance
   - Includes metadata fields, content sections, and optional elements

5. **blog-guidelines.md** - Comprehensive writing guide
   - Structure best practices
   - Content category guidelines (Technique, Philosophy, Training, History, Personal Reflection)
   - Writing style and tone recommendations
   - Japanese terminology usage guidelines
   - Quality standards and review process
   - Common pitfalls to avoid

#### Directory Structure

```
/Users/thomas/MA/
├── .claude/
│   ├── commands/
│   │   ├── checkpoint.md       # Save session state
│   │   ├── resume.md           # Load previous session context
│   │   ├── review-aikido.md    # Review blog posts for quality
│   │   ├── discuss.md          # Explore topics through conversation
│   │   ├── extract.md          # Transform discussions to blog drafts
│   │   ├── track-source.md     # Register martial arts bloggers
│   │   └── scan-sources.md     # Monitor bloggers for content
│   └── claude.md               # This file - project context
├── posts/                      # Blog posts directory
├── discussions/                # Discussion notes (informal explorations)
├── sources/                    # Source tracking and monitoring
│   ├── registry/              # Blogger profiles
│   └── findings/              # Content analysis and ideas
├── sessions/                   # Session history (timestamped summaries)
├── topics.md                   # Topic tracking
├── session-context.md          # Session state
├── decisions.md                # Decision log
├── blog-template.md            # Post template
├── blog-guidelines.md          # Writing guidelines
└── help.md                     # User guide
```

**discussions/ Directory:**
- Contains structured notes from informal discussions about Aikido topics
- Created by /discuss command
- Format: `topic-name-YYYY-MM-DD.md`
- Serves as raw material for blog posts
- Can be extracted to blog drafts with /extract command
- Preserves authentic insights and thinking process

**sources/ Directory:**
- Contains tracked martial arts bloggers, YouTube channels, and content analysis
- **registry/**: Blogger and YouTube channel profiles with URLs, disciplines, scan history
- **findings/**: Content analysis reports with blog ideas and response opportunities
- **youtube/transcripts/**: Downloaded YouTube video transcripts
- **youtube/registry/**: YouTube channel/creator profiles
- **youtube/findings/**: YouTube content analysis and blog ideas
- Created by /track-source, /scan-sources, and /youtube-fetch commands
- Enables monitoring community content for inspiration and engagement
- Supports cross-discipline insights (Aikido, Karate, Silat, etc.)

**sessions/ Directory:**
- Contains timestamped session summaries (format: `session-YYYY-MM-DD-HHMM.md`)
- Automatically created by /checkpoint command
- Provides historical record of each work session
- Includes: accomplishments, decisions, conversation highlights, files modified, next steps
- Allows user to review progress over time and search for past topics/decisions

---

## Slash Commands Available

### /checkpoint
**Purpose**: Save current session state before ending work

**What it does:**
1. Checks git status for uncommitted changes
2. Commits all changes to local git (never pushes remotely)
3. Updates session-context.md with current status, recent work, next steps
4. Reviews and updates topics.md
5. Logs any decisions made to decisions.md
6. **Creates timestamped session summary** in sessions/ directory (format: `session-YYYY-MM-DD-HHMM.md`)
   - Includes: session focus, accomplishments, decisions, conversation highlights, files modified, next steps
   - Provides historical record for later review
7. Provides summary of what was saved

**When to use**: End of every work session

**Session History**: Each checkpoint creates a permanent record in sessions/ that can be reviewed later to understand what happened in each session and track progress over time.

### /resume
**Purpose**: Restore context from previous session

**What it does:**
1. Reads and displays session-context.md (status, recent work, next steps, blockers)
2. Shows current topic from topics.md
3. Checks git status for any uncommitted changes
4. Displays recent decisions from decisions.md
5. Asks how to proceed based on context

**When to use**: Start of every work session

### /review-aikido
**Purpose**: Review Aikido blog posts for quality

**What it reviews:**
1. Aikido terminology and spelling (Japanese terms, macrons, romanization)
2. Technical accuracy and fact-checking
3. Writing clarity and accessibility
4. Structure and organization

**Output format:**
- Overall assessment
- Terminology issues
- Technical/factual corrections
- Clarity improvements
- Structural recommendations
- Final recommendation (ready to publish / needs revisions)

**When to use**: After drafting a blog post, before finalizing

### /discuss
**Purpose**: Explore Aikido topics through informal conversation

**What it does:**
1. Engages in conversational dialogue about the chosen topic
2. Asks probing questions to deepen understanding
3. Extracts key insights from the user's responses
4. Records specific examples and stories
5. Identifies decisions and conclusions
6. Creates structured discussion note in discussions/ directory
7. Highlights blog-worthy ideas

**Approach:**
- Conversational and curious (not academic)
- Asks clarifying and deepening questions
- Challenges assumptions gently
- Makes connections between ideas
- Captures authentic voice and phrasing
- Preserves uncertainties and questions

**When to use**: Before writing, to explore ideas informally and develop understanding

**Result**: Discussion note saved as `discussions/[topic-name]-YYYY-MM-DD.md`

### /extract
**Purpose**: Transform discussion notes into blog post drafts

**What it does:**
1. Reads the specified discussion note file
2. Analyzes blog potential (thesis, key points, examples, structure)
3. Assesses if there's sufficient material for a post
4. Creates structured blog post draft in posts/ directory
5. Pulls best insights and examples from discussion
6. Organizes into blog-appropriate structure
7. Identifies gaps that need filling
8. Updates discussion note with extraction status
9. Provides guidance on next steps

**Extraction Quality:**
- Preserves user's authentic voice
- Uses their phrasing where possible
- Structures insights logically
- Includes concrete examples from discussion
- Marks gaps clearly for later development

**When to use**: After discussion is complete and ready to become a blog post

**Result**: Initial blog draft in `posts/[topic-name]-YYYY-MM-DD.md` ready for development and review

### /track-source
**Purpose**: Register martial arts bloggers to monitor for content

**What it does:**
1. Creates blogger profile in sources/registry/
2. Records URL, discipline, focus areas
3. Tracks scan history
4. Maintains source registry index
5. Optional: Fetches initial blog information

**Usage**: `/track-source "[Name]" "[URL]" "[Discipline]"`

**Example**: `/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"`

**When to use**: When discovering a martial arts blogger worth monitoring

**Source profiles include:**
- Blogger name, URL, discipline
- Focus areas and notes
- Scan history and statistics
- Ideas generated from their content
- Connection to user's blog posts

### /scan-sources
**Purpose**: Monitor tracked bloggers for new content and extract blog ideas

**What it does:**
1. Fetches recent posts from tracked blogs
2. Identifies new content since last scan
3. Analyzes posts for key arguments and ideas
4. Generates blog topic ideas (response, alternative perspective, inspired exploration)
5. Creates findings report with actionable ideas
6. Updates source profiles with scan results

**Usage**:
- `/scan-sources` - Scan all tracked sources
- `/scan-sources [name]` - Scan specific source

**Example**: `/scan-sources leo-tamaki`

**When to use**: Weekly or bi-weekly to find new content and inspiration

**Findings report includes:**
- Summary of new posts found
- Key arguments and points from each post
- Blog ideas generated (with type, angle, connection to Aikido)
- Response opportunities
- Discussion prompts for /discuss command
- Recommended actions

**Result**: Findings saved in `sources/findings/YYYY-MM-DD-[source-name].md`

**Integration**: Ideas from findings can feed into /discuss or direct blog writing

### /youtube-fetch
**Purpose**: Download YouTube video transcripts and analyze for blog inspiration

**What it does:**
1. Downloads transcript using yt-dlp (script: scripts/youtube-transcript.py)
2. Extracts video metadata (title, channel, duration, upload date)
3. Converts transcript to readable text format
4. Analyzes content for key themes and martial arts concepts
5. Generates 3-5 blog topic ideas with full details
6. Creates findings report with analysis and recommendations
7. Updates/creates YouTube channel registry profiles

**Usage**: `/youtube-fetch <youtube_url>`

**Example**: `/youtube-fetch https://www.youtube.com/watch?v=KGFEDrQRWSo`

**When to use**: When discovering valuable martial arts video content worth analyzing

**Files created:**
- Transcript: `sources/youtube/transcripts/<video_id>.txt`
- Metadata: `sources/youtube/transcripts/<video_id>.json`
- Findings: `sources/youtube/findings/YYYY-MM-DD-<video_id>-<description>.md`
- Registry: `sources/youtube/registry/<channel-name>.md` (if new)

**Integration**: Ideas from YouTube findings can feed into /discuss or direct blog writing

### /youtube-analyze
**Purpose**: Analyze an already-downloaded YouTube transcript for blog ideas

**What it does:**
1. Reads existing transcript and metadata
2. Performs deep content analysis (themes, concepts, quotes, teaching methods)
3. Extracts cross-discipline insights applicable to Aikido
4. Generates 3-5 detailed blog topic ideas
5. Creates or updates findings report

**Usage**:
- `/youtube-analyze <video_id>`
- `/youtube-analyze <path_to_transcript>`

**Example**: `/youtube-analyze KGFEDrQRWSo`

**When to use**:
- To re-analyze a previously downloaded video
- To extract additional blog ideas from existing transcripts
- After downloading transcript manually

**Result**: Updated findings report in `sources/youtube/findings/`

---

## Git Workflow

- **Local commits only**: Never push to remote unless explicitly requested
- **Commit frequently**: Use /checkpoint to commit work at end of sessions
- **Branch**: Currently on `main` branch
- **Status**: Initial setup files not yet committed (as of 2025-10-30)

---

## Blog Writing Workflow

### Three Approaches:

**Approach A: Discussion-Based (Recommended)**
1. **Start Session**: `/resume` to see where you left off
2. **Explore Topic**: `/discuss [topic-name]` - Have informal conversation
3. **Extract Draft**: `/extract discussions/[file].md` - Create blog draft
4. **Develop Draft**: Expand sections, fill gaps, refine language
5. **Review**: `/review-aikido posts/[filename].md`
6. **Revise**: Based on critical feedback, iterate to MA-level quality
7. **Finalize**: Update topics.md (move to completed)
8. **End Session**: `/checkpoint` to save state and commit

**Approach B: Direct Writing**
1. **Start Session**: `/resume` to see where you left off
2. **Choose Topic**: Review topics.md, select or add new topic
3. **Create Post**: `cp blog-template.md posts/[topic-name]-YYYY-MM-DD.md`
4. **Write Content**: Follow structure in blog-guidelines.md
5. **Review**: `/review-aikido posts/[filename].md`
6. **Revise**: Based on review feedback
7. **Finalize**: Update topics.md (move to completed)
8. **End Session**: `/checkpoint` to save state and commit

**Approach C: Source-Inspired (Blog Content)**
1. **Track Sources**: `/track-source "[Name]" "[URL]" "[Discipline]"` - Register bloggers
2. **Scan Content**: `/scan-sources` - Find new posts and analyze
3. **Review Findings**: Read sources/findings/[report].md for ideas
4. **Explore or Write**:
   - Option A: `/discuss [inspired-topic]` → `/extract` → develop
   - Option B: Write response directly from template
5. **Review**: `/review-aikido posts/[filename].md`
6. **Revise**: Based on critical feedback
7. **Finalize**: Update topics.md, note source connection
8. **End Session**: `/checkpoint` to save state and commit

**Approach D: YouTube-Inspired**
1. **Fetch Content**: `/youtube-fetch <youtube_url>` - Download and analyze video
2. **Review Findings**: Read sources/youtube/findings/[report].md for ideas
3. **Explore or Write**:
   - Option A: `/discuss [inspired-topic]` → `/extract` → develop
   - Option B: Write response directly from template
4. **Review**: `/review-aikido posts/[filename].md`
5. **Revise**: Based on critical feedback
6. **Finalize**: Update topics.md, credit video with link if directly inspired
7. **End Session**: `/checkpoint` to save state and commit

### Content Guidelines Summary:

**Length**: 800-1200 words (sweet spot)

**Structure**:
- Title & metadata
- Introduction (100-200 words)
- Main content (2-4 sections, 500-1500 words)
- Practical takeaways (3-5 points)
- Conclusion (100-150 words)
- Optional: Resources, glossary

**Categories**:
- Technique: Specific waza analysis
- Philosophy: Principles and concepts
- Training: Practice methods and tips
- History: Lineage and development
- Personal Reflection: Journey and insights

**Tone**:
- Knowledgeable but humble
- Accessible but not patronizing
- Personal but not self-centered
- Respectful of tradition but not dogmatic

---

## Important Notes for Future Sessions

### Always Start With:
1. Run `/resume` to load previous context
2. Review session-context.md for next steps
3. Check git status to see any uncommitted work

### During Work:
- Update session-context.md as you progress
- Add topic ideas to topics.md as they come up
- Log important decisions to decisions.md
- Keep blog posts in posts/ directory
- Follow blog-guidelines.md for content quality

### Always End With:
1. Run `/checkpoint` to save state
2. Ensure all changes are committed locally
3. Verify session-context.md reflects current status

### Git Policy:
- Commit locally frequently
- Never push to remote unless explicitly requested by user
- Use descriptive commit messages

### Content Quality:
- Always use `/review-aikido` before finalizing posts
- Verify Japanese terminology (spelling, macrons, romanization)
- Check facts about Aikido history and techniques
- Ensure accessibility for readers new to Aikido

---

## Current Project Status

**Date**: 2025-10-30

**Status**: Initial setup complete - ready to start writing blog content

**What's Done**:
- Session continuity system (checkpoint/resume)
- Document structure (topics, session-context, decisions)
- Blog template and guidelines
- Review system for quality control
- Posts directory created

**What's Next**:
1. Commit initial setup to git
2. Add blog topic ideas to topics.md
3. Choose first topic and start writing
4. Use review system to ensure quality
5. Establish regular checkpoint routine

**No Blockers**: System is ready for content creation

---

## Troubleshooting

### If session-context.md is missing or empty:
- This indicates a fresh start or the checkpoint system wasn't used
- Ask user where they'd like to begin

### If posts are in root directory instead of posts/:
- Move them: `mv *.md posts/` (exclude system files)
- Update topics.md references

### If user mentions previous discussion not saved:
- Each Claude session starts fresh without previous conversation history
- We rely on the files (session-context.md, topics.md, decisions.md) for continuity
- Encourage using /checkpoint to save important context

---

## Key Principles

1. **User owns the content**: Never commit or push without user consent
2. **Context preservation**: Always update tracking files when things change
3. **Quality focus**: Use review system to maintain blog post quality
4. **Simplicity**: Keep the system lightweight and easy to use
5. **Flexibility**: Guidelines are guides, not rigid rules

---

*Last Updated: 2025-10-30*
*This file should be updated when significant changes are made to the project structure or workflow.*
