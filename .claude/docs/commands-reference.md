# Slash Commands Reference

## Quick Command List

**Session Management:**
- `/resume` - Load previous session state (auto-detects or creates instance)
- `/resume [instance-id]` - Resume specific instance
- `/resume and work on [task]` - Create new instance for task
- `/checkpoint` - Save state, commit, and push to GitHub
- `/save-objective` - Explicitly save current work objective
- `/pause-task [reason]` - Move current task to backlog

**Multi-Instance Management:**
- `/instances` - View all active Claude instances
- `/cleanup-instances` - Archive, delete, or keep stale instances

**Content Creation (Agents):**
- `/discuss [topic]` - Explore topics through conversation
- `/extract [file]` - Transform discussion to article draft
- `/review-aikido [file]` - Review article quality

**Content Discovery (Agents):**
- `/track-source [name] [url] [discipline]` - Register blogger
- `/scan-sources [name]` - Monitor bloggers for new content
- `/youtube fetch [url]` - Download and analyze YouTube video/channel
- `/youtube analyze [video_id]` - Re-analyze existing transcript

**System Maintenance (Agent):**
- `/system-maintenance [mode]` - Audit, clean, sync, and optimize project structure

---

## Session Management Commands

### /resume

**Purpose**: Restore context from previous session with multi-instance support

**Usage**:
- `/resume` - Auto-detect active instances or create new
- `/resume [instance-id]` - Resume specific instance (e.g., `/resume 2025-10-31-1953`)
- `/resume and work on [task]` - Create new instance for specific task

**Examples:**
- `/resume` - Smart detection based on state
- `/resume 2025-10-31-1953` - Resume specific instance
- `/resume and work on biomechanics article` - Create new instance

**What it does:**

**Smart Detection** (no args):
1. Checks for active instances (heartbeat <1 hour)
2. If 0 active: Creates new instance automatically
3. If 1 active: Shows instance, asks to continue or create new
4. If 2+ active: Lists all, asks which to resume or create new

**Specific Instance** (instance-id provided):
1. Loads that specific instance's state
2. Reads instance-specific `current-objective.md` for crash recovery
3. Shows active objective if work in progress

**New Instance** (task description provided):
1. Creates new timestamp-based instance
2. Initializes instance directory and files
3. Registers in `.claude/state/registry.md`

**For all modes:**
1. Reads shared state:
   - `session-context.md` (status, recent work, next steps, blockers)
   - `topics.md` (current article and queue)
   - `.claude/state/backlog.md` (paused tasks)
   - `decisions.md` (recent decisions, last 2-3)
2. Checks git status for uncommitted changes
3. Shows other active instances from registry
4. Displays concise summary
5. Asks how to proceed

**When to use**: Start of every work session

**Output**:
- Instance overview (which instance, what others are doing)
- Crash recovery notice if incomplete work detected
- Active objective, paused tasks, system status
- Next steps and how to proceed

**Multi-Instance Notes**:
- Each instance isolated with own current-objective.md
- Shared files (session-context, topics, backlog, decisions) visible to all
- Registry shows what all instances are working on
- Independent crash recovery per instance

---

### /checkpoint

**Purpose**: Save current session state, commit, and backup to GitHub

**Usage**: `/checkpoint`

**What it does (executes autonomously)**:

**Instance State Management**:
1. Updates heartbeat in `.claude/state/instances/[instance-id]/session-info.md`
2. Marks instance status as "Idle" (session ending)
3. Adds activity log entry: "Checkpoint - session end"
4. Updates `.claude/state/registry.md` with final status
5. Instance-specific `current-objective.md` already saved by `/save-objective`

**Git Operations**:
1. Checks git status for uncommitted changes
2. If changes exist:
   - Analyzes changed files to understand what was done
   - Generates descriptive commit message automatically
   - Stages and commits all changes
   - Shows user what was committed
3. If no changes, notes everything already committed

**Automatic GitHub Backup**:
1. Checks if git remote configured
2. If remote exists: `git push origin main`
3. If push succeeds: Confirms to user
4. If push fails: Informs user but completes checkpoint anyway

**Session Documentation**:
1. Analyzes conversation and file changes automatically
2. Creates timestamped session summary in `sessions/`
   - Format: `session-YYYY-MM-DD-HHMM.md`
   - Includes: session focus, accomplishments, decisions, conversation highlights, files modified, next steps
3. Assumes `session-context.md` already current (doesn't ask for updates)
4. Assumes `topics.md` is current
5. Infers and logs any decisions made to `decisions.md` if warranted

**Summary Output**:
- Brief summary of what was checkpointed
- Which instance was saved (if using instances)
- Session summary file created
- Confirmation of GitHub push (if successful)
- Reminder to use `/resume` for next session

**When to use**: End of every work session

**Important Notes**:
- Executes fully autonomously (no questions asked)
- Generates commit messages from changed files analysis
- Multi-instance aware: Each instance checkpoints separately
- Always attempts to push to GitHub for backup
- Efficient: 30-60 seconds total execution time

---

### /save-objective

**Purpose**: Explicitly save current work objective for crash recovery

**Usage**: `/save-objective`

**What it does:**
1. Prompts you to describe current objective if not already saved
2. Captures key requirements, approach, and reasoning
3. Records progress (completed, in progress, remaining)
4. Notes blockers and questions
5. Lists context files and references
6. Saves to `.claude/state/instances/[instance-id]/current-objective.md`
7. Updates instance heartbeat in `session-info.md`

**When to use**:
- When starting significant new work
- After completing major milestones
- Before switching contexts or taking a break
- Periodically during long tasks (defensive programming)

**Why it exists**:
- Crash recovery (if Claude crashes, objective preserved)
- Task continuity (pick up exactly where you left off)
- Progress tracking (clear record of what's done and what remains)
- No work lost even if session interrupted

**Multi-Instance Notes**:
- Each instance has own isolated `current-objective.md`
- Multiple instances can have active objectives simultaneously
- `/resume` detects incomplete work and shows crash recovery notice

---

### /pause-task

**Purpose**: Move current work to backlog when switching to urgent work

**Usage**: `/pause-task [reason]`

**Examples:**
- `/pause-task Need to prioritize article writing`
- `/pause-task Blocked waiting for user input`
- `/pause-task Switching to urgent bug fix`

**What it does:**
1. Documents current progress thoroughly
2. Moves current objective to `.claude/state/backlog.md` with:
   - Paused date and reason
   - Progress made so far
   - Blockers encountered
   - Next steps clearly identified
   - Context files needed to resume
   - Instance tag (which instance paused it)
3. Clears instance-specific `current-objective.md` to template
4. Updates registry
5. Presents overview showing backlog updated
6. Ready for new task

**When to use:**
- Urgent work interrupts current task
- Task blocked waiting for external input
- Switching priorities mid-session
- Need to set aside current work temporarily

**Resuming Paused Tasks**:
- Any instance can resume tasks from shared backlog
- All context preserved for seamless continuation
- No work lost even when priorities change

**Multi-Instance Notes**:
- Paused tasks saved to shared backlog (all instances can see)
- Instance tag identifies which instance paused it
- Crash recovery still works (objective moved to backlog before clearing)

---

## Multi-Instance Commands

### /instances

**Purpose**: View all active Claude instances and their current work

**Usage**: `/instances`

**What it shows:**
1. Reads `.claude/state/registry.md`
2. Lists all instances by status:
   - **Active** (heartbeat <1 hour): Currently working
   - **Idle** (heartbeat 1-24 hours): Session ended, not yet stale
   - **Stale** (heartbeat >24 hours): Consider cleanup
3. For each instance shows:
   - Instance ID (timestamp)
   - Created date/time
   - Last heartbeat
   - Working on (current task/objective)
   - Location (state directory path)
4. Shows statistics:
   - Total instances
   - Active count
   - Idle count
   - Stale count

**When to use:**
- Want to see what other instances are working on
- Deciding whether to resume existing instance or create new
- Checking for stale instances to clean up
- Understanding current multi-instance state

**Output**: Clear overview of all instances with status and activity

---

### /cleanup-instances

**Purpose**: Archive, delete, or keep stale instances (>24h old)

**Usage**: `/cleanup-instances`

**What it does:**
1. Scans `.claude/state/instances/` for all instances
2. Identifies stale instances (no heartbeat >24 hours)
3. If stale instances found:
   - Shows each stale instance with details
   - Asks for each: Archive, Delete, or Keep?
   - **Archive**: Moves to `.claude/state/instances/_archived/`
   - **Delete**: Permanently removes instance directory
   - **Keep**: Updates registry, leaves instance
4. Updates `.claude/state/registry.md`
5. Shows summary of actions taken

**When to use:**
- Weekly or monthly housekeeping
- When you see stale instances in `/instances`
- Before starting new work (clean slate)
- When directory getting cluttered

**Important Notes**:
- No automatic deletion (user decides for each instance)
- Prevents accidental data loss
- Archived instances preserved in `_archived/` for later review
- Only suggests stale instances (>24h), never active/idle ones

---

## Content Creation Commands

### /discuss

**Purpose**: Explore Aikido topics through informal conversation

**Usage**: `/discuss [topic-name]`

**Examples:**
- `/discuss teaching-relaxation`
- `/discuss biomechanics-of-irimi`
- `/discuss iwama-approach-critique`
- `/discuss peace-and-violence`

**What it does:**
- Agent (loaded internally) engages in conversational dialogue
- Asks probing questions to deepen understanding
- Extracts key insights from your responses
- Records specific examples and stories
- Identifies educational frameworks and concepts
- Makes connections between ideas
- Challenges assumptions gently
- Creates structured discussion note in `discussions/`
- Highlights article-worthy ideas

**Agent loads internally** (not in your context):
- `research/core-values.md` - Foundational beliefs
- `research/divisive-topics.md` - Controversial topics framework
- `research/learning-frameworks.md` - Mastery models
- `research/user-profile.md` - Author background

**Approach:**
- Conversational and curious (not academic)
- Captures your authentic voice and phrasing
- Preserves uncertainties and questions
- Identifies both/and possibilities (not forced dichotomies)

**When to use**: Before writing, to explore ideas informally and develop understanding

**Result**: Discussion note saved as `discussions/[topic-name]-YYYY-MM-DD.md`

**Integration**: Use `/extract` to transform discussion into article draft

---

### /extract

**Purpose**: Transform discussion notes into article drafts

**Usage**: `/extract discussions/[filename].md`

**Example**: `/extract discussions/teaching-relaxation-2025-10-30.md`

**What it does:**
- Agent reads the specified discussion note file
- Analyzes educational potential:
  - Identifies core thesis and learning objectives
  - Extracts key concepts and frameworks
  - Finds concrete examples and applications
  - Determines logical structure for progressive learning
- Assesses if there's sufficient material for article
- Creates structured article draft in `articles/[series]/`
- Pulls best insights and examples from discussion
- Organizes for educational depth (not blog engagement)
- Uses your authentic voice and phrasing
- Includes cross-references to related concepts
- Identifies gaps that need filling
- Updates discussion note with extraction status
- Provides guidance on next steps

**When to use**: After discussion is complete and ready to become article

**Result**:
- Initial article draft in `articles/[series]/[topic-name]-YYYY-MM-DD.md`
- Ready for development, expansion, and review
- Clear gaps marked for further work

**Target Output**: 1,500-3,000+ words for comprehensive coverage

---

### /review-aikido

**Purpose**: Review Aikido articles for quality before publishing (critical, not encouraging)

**Usage**: `/review-aikido articles/[filepath].md`

**Examples:**
- `/review-aikido articles/biomechanics/teaching-relaxation-2025-10-30.md`
- `/review-aikido articles/peace-violence/veteran-perspective-2025-10-31.md`

**What it reviews:**

**Agent loads internally** (not in your context):
- `article/article-guidelines.md` - Comprehensive quality standards
- `article/article-series-structure.md` - Series organization
- Earlier articles in same series (for consistency check)

**Review Criteria:**
1. **Aikido terminology** - Japanese terms, macrons, romanization correctness
2. **Technical accuracy** - Facts about techniques, history, principles
3. **Educational depth** - Completeness, comprehensive coverage (not surface-level)
4. **Writing clarity** - Accessibility for target audiences
5. **Structure and organization** - Flow, completeness, logical progression
6. **Series consistency** - Terminology and frameworks compatible with earlier articles
7. **Authenticity** - Alignment with core values, divisive topics handled properly
8. **AI attribution** - "About This Article" section present and correct
9. **Violence context** - Specified when discussing effectiveness
10. **Legal/ethical considerations** - Addressed when applicable

**Output format:**
- Overall assessment (honest, critical)
- Specific issues by category with corrections
- Clarity improvements suggested
- Structural recommendations
- Consistency check with earlier articles
- Final recommendation: **ready to publish** or **needs revisions**

**Approach**:
- Highly critical (MSc-level standards, not casual blog)
- Collaborative (works with you on improvements)
- Specific and actionable feedback
- Honest assessment (doesn't sugar-coat)

**When to use**:
- After drafting an article, before finalizing
- After revisions, to verify improvements
- Iterate until quality standards met

**Integration**: Re-run after revisions until ready to publish

---

## Content Discovery Commands

### /track-source

**Purpose**: Register martial arts bloggers to monitor for content

**Usage**: `/track-source "[Name]" "[URL]" "[Discipline]"`

**Examples:**
- `/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"`
- `/track-source "Jesse Enkamp" "https://www.karatebyjesse.com" "Karate"`
- `/track-source "Maul Mornie" "https://www.maulmornie.com" "Silat"`

**What it does:**
- Agent creates blogger profile in `sources/registry/`
- Records URL, discipline, focus areas
- Tracks scan history and statistics
- Maintains source registry index
- Optional: Fetches initial blog information

**Source profiles include:**
- Blogger name, URL, discipline
- Focus areas and notes
- Scan history (dates, posts found)
- Article ideas generated from their content
- Connection to your articles

**When to use**: When discovering martial arts blogger worth monitoring

**Result**: Profile saved in `sources/registry/[blogger-slug].md`

**Integration**: Use `/scan-sources` to monitor for new content

---

### /scan-sources

**Purpose**: Monitor tracked bloggers for new content and extract article ideas

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
- Generates article topic ideas:
  - **Response**: Direct response to their argument
  - **Alternative Perspective**: Different viewpoint on same topic
  - **Inspired Exploration**: Their post sparked related idea
- Creates findings report with actionable ideas
- Updates source profiles with scan results

**Findings report includes:**
- Summary of new posts found
- Key arguments and points from each post
- Article ideas generated (with type, angle, Aikido connection, series placement)
- Response opportunities
- Discussion prompts for `/discuss` command
- Recommended actions

**When to use**: Weekly or bi-weekly to find new content and inspiration

**Result**: Findings saved in `sources/findings/YYYY-MM-DD-[source-name].md`

**Integration**:
- Use ideas from findings with `/discuss` or direct writing
- Transform their ideas through your framework

---

### /youtube fetch

**Purpose**: Download and analyze YouTube video/channel transcripts for article inspiration

**Usage**: `/youtube fetch <youtube_url>`

**Examples:**
- `/youtube fetch https://www.youtube.com/watch?v=KGFEDrQRWSo` - Single video
- `/youtube fetch https://www.youtube.com/@ChewjiuBJJ` - Entire channel
- `/youtube fetch https://www.youtube.com/@ChewjiuBJJ --limit 10` - First 10 videos from channel

**What it does:**

**For Single Videos:**
- Downloads transcript using yt-dlp (script: `scripts/youtube-transcript.py`)
- Extracts video metadata (title, channel, duration, upload date)
- Converts transcript to readable text format
- Analyzes content for key themes and martial arts concepts
- Generates 3-5 article topic ideas with full details
- Creates findings report with analysis and recommendations
- Updates/creates YouTube channel registry profile

**For Channels:**
- Fetches all videos (or --limit N videos) from channel
- Downloads transcripts for each video
- Creates individual analysis for each
- Identifies channel-wide themes and teaching philosophy
- Cross-references concepts across videos
- Generates comprehensive findings report
- Updates channel registry with complete profile

**Files created:**
- `sources/youtube/transcripts/<video_id>.txt` - Readable transcript
- `sources/youtube/transcripts/<video_id>.json` - Metadata
- `sources/youtube/findings/YYYY-MM-DD-<video_id>.md` - Analysis
- `sources/youtube/registry/<channel-name>.md` - Channel profile

**When to use:**
- Discovering new martial arts video content
- Building research base for cross-validation
- Finding cross-discipline insights
- Identifying universal principles

**Important notes:**
- Transcripts for research and inspiration only
- Never reproduce long excerpts verbatim in articles
- If directly inspired by video, mention it with link
- Look for universal biomechanical principles applicable to Aikido

**Integration**:
- Ideas from findings can feed into `/discuss` or direct article writing
- Use for cross-validation (multiple instructors agreeing strengthens argument)

**Research Base Available**:
- 1,983 transcripts already downloaded
- 5 channels analyzed (Hein, Tony, Alexander, Matthieu, SenshinOne)
- Universal agreements documented
- Productive contrasts identified

---

### /youtube analyze

**Purpose**: Re-analyze existing transcript for additional insights

**Usage**: `/youtube analyze <video_id>`

**Example**: `/youtube analyze KGFEDrQRWSo`

**What it does:**
- Reads existing transcript and metadata from `sources/youtube/transcripts/`
- Performs deep content analysis:
  - Identifies key themes and concepts
  - Extracts martial arts principles
  - Notes teaching approaches and methods
  - Finds cross-discipline insights applicable to Aikido
  - Identifies biomechanical explanations
- Generates 3-5 detailed article topic ideas
- Creates or updates findings report in `sources/youtube/findings/`

**When to use:**
- Extract additional ideas from previously downloaded videos
- Re-analyze with fresh perspective
- Look for concepts relevant to current article series
- Find cross-validation for specific principles

**Result**: Updates `sources/youtube/findings/YYYY-MM-DD-<video_id>.md`

**Integration**: Use findings with `/discuss` or direct article writing

---

## System Maintenance Command

### /system-maintenance

**Purpose**: Maintain project structure, optimize token usage, ensure system health

**Usage**: `/system-maintenance [mode]`

**Modes:**
- `audit` - Health check report (read-only)
- `cleanup` - Archive old sessions, clean TODOs
- `sync` - Update cross-references and INDEX files
- `optimize` - Reduce token bloat
- `full` - Complete maintenance cycle (audit → cleanup → sync → optimize → audit)

**Examples:**
- `/system-maintenance audit` - Check system health
- `/system-maintenance cleanup` - Clean old content
- `/system-maintenance optimize` - Reduce token usage
- `/system-maintenance full` - Complete maintenance run

**What each mode does:**

**Audit mode (read-only):**
- Measures token usage in all key files
- Validates file structure and cross-references
- Checks INDEX completeness
- Detects bloat and stale content
- Generates comprehensive health report with status indicators:
  - 🟢 Green: Within target or <110%
  - 🟡 Yellow: 110-130% (needs attention)
  - 🔴 Red: >130% (must fix)

**Cleanup mode:**
- Archives session summaries >90 days old to `sessions/archive/`
- Removes completed TODOs
- Identifies obsolete files
- Cleans empty directories

**Sync mode:**
- Updates `research/INDEX.md` with all research files
- Ensures agent/command pairs synchronized
- Fixes broken file references
- Updates directory listings in documentation

**Optimize mode:**
- Reduces CLAUDE.md to target size (<500 words)
- Streamlines command files (<200 words each)
- Optimizes session-context.md (<1000 words)
- Moves detailed content to appropriate locations

**Full mode:**
- Runs complete cycle: audit → cleanup → sync → optimize → audit
- Provides before/after comparison
- Shows all improvements made
- Comprehensive report

**When to use:**
- **Monthly**: Run `audit` to check system health
- **Quarterly**: Run `full` for comprehensive maintenance
- **After major changes**: Run `sync` to update cross-references
- **When /resume feels slow**: Run `optimize` to reduce tokens

**Agent loads internally** (complete system context):
- All documentation files
- All agent and command definitions
- All INDEX and tracking files
- Token usage targets and thresholds

**Result**:
- Comprehensive report with health status
- Issues found/fixed
- Token analysis
- Recommendations and next steps
- Before/after comparisons (for write modes)

**Integration**: Maintains the system that maintains the articles - keeps infrastructure lean so you can focus on writing

---

## Command Comparison

| Command | Type | Speed | Use Case |
|---------|------|-------|----------|
| `/resume` | Lightweight | Fast | Start every session (multi-instance aware) |
| `/checkpoint` | Lightweight | Fast | End every session (auto-commit + push) |
| `/save-objective` | Lightweight | Fast | Save work progress for crash recovery |
| `/pause-task` | Lightweight | Fast | Move current work to backlog |
| `/instances` | Lightweight | Fast | View all active instances |
| `/cleanup-instances` | Interactive | Fast | Manage stale instances |
| `/discuss` | Agent | Medium | Explore ideas conversationally |
| `/extract` | Agent | Fast | Discussion → article draft |
| `/review-aikido` | Agent | Medium | Critical quality review before publish |
| `/track-source` | Agent | Fast | Register new blogger |
| `/scan-sources` | Agent | Medium-Slow | Find new content weekly |
| `/youtube fetch` | Agent | Slow | Download & analyze video/channel |
| `/youtube analyze` | Agent | Fast | Re-analyze existing transcript |
| `/system-maintenance` | Agent | Varies | System health & optimization |

---

## Terminology Notes

**Educational Article Series (Not Blog)**:
- This system creates educational articles for progressive learning
- Articles organized into series, building on each other
- Designed for eventual book compilation
- MSc-level quality standards (not casual blog)

**Directory Structure**:
- `articles/` - Article drafts and finals (organized by series)
- `discussions/` - Topic exploration notes
- `article/` - Templates and guidelines
- `posts/` - Legacy directory (pre-transformation from blog to articles)

**Quality Standards**:
- Target length: 1,500-3,000+ words (comprehensive depth)
- Progressive series structure (articles build on each other)
- Multi-audience layering (accessible to beginners, challenging for advanced)
- AI attribution mandatory in all published articles

---

*Read this file when you need detailed command documentation. Not loaded by default.*
