# Aikido Educational Article Series - Quick Reference

## Project Purpose
Master's thesis project for writing educational Aikido article series (designed for book publication) with session continuity between Claude Code sessions.

## Essential Commands

### Start/End Session
- `/resume` - Load previous session state (run at start of every session)
- `/checkpoint` - Save state and commit to git (run at end of every session)

### Content Creation Agents
- `/discuss [topic]` - Explore topics through conversation → saves to discussions/
- `/extract [file]` - Transform discussion into article draft → saves to articles/
- `/review-aikido [file]` - Review article quality (educational depth, consistency, completeness)

### Content Discovery Agents
- `/track-source [name] [url] [discipline]` - Register martial arts bloggers
- `/scan-sources [name]` - Monitor bloggers for new content and ideas
- `/youtube fetch [url]` - Download and analyze video/channel transcripts
  - Supports single videos or entire channels
  - Use `--limit N` to fetch first N videos from channel
- `/youtube analyze [video_id]` - Re-analyze existing transcripts

### System Maintenance
- `/system-maintenance [mode]` - Audit, clean, sync, and optimize project structure
  - Modes: `audit`, `cleanup`, `sync`, `optimize`, `full`
  - Keeps system lean without using your context

## Core Files (Root Directory)

**Session Management:**
- `session-context.md` - Current status, recent work, next steps
- `topics.md` - Article series progress and queue
- `decisions.md` - Decision log with rationale

**Content:**
- `articles/` - Article series drafts and finals (organized by series)
- `discussions/` - Informal topic explorations
- `blog/` - Article templates and guidelines (legacy name)

**Reference (read when needed):**
- `research/` - Core values, divisive topics, learning frameworks, biomechanics
- `sources/` - Tracked bloggers, YouTube channels, findings
- `syllabus/` - Technical Aikido reference

## Typical Workflows

**Approach A: Discussion-Based (Recommended)**
1. `/resume` → `/discuss [topic]` → `/extract` → develop article → `/review-aikido` → revise → `/checkpoint`

**Approach B: Direct Writing**
1. `/resume` → copy template → write article → `/review-aikido` → revise → `/checkpoint`

**Approach C: Source-Inspired**
1. `/track-source` → `/scan-sources` → `/discuss [inspired-topic]` → `/extract` → develop article → `/review-aikido` → `/checkpoint`

**Approach D: YouTube-Inspired**
1. `/youtube fetch [url]` → review findings → `/discuss` → `/extract` → develop article → `/review-aikido` → `/checkpoint`

**Note**: Articles should be written in series order. Review for consistency with earlier articles in same series.

## Key Principles

1. **Always start with `/resume`** - Loads where you left off
2. **Always end with `/checkpoint`** - Saves state and commits locally
3. **Never push to remote** unless explicitly requested
4. **Use agents for heavy tasks** - They handle details internally
5. **Reference detailed docs** only when needed - See `.claude/docs/`

## Need More Details?

- **Architecture**: Read `.claude/docs/architecture.md`
- **Workflows**: Read `.claude/docs/workflows.md`
- **Commands**: Read `.claude/docs/commands-reference.md`
- **Research Files**: Read `research/INDEX.md`
- **Troubleshooting**: Read `.claude/docs/troubleshooting.md`

## Current Status

Check `session-context.md` for:
- What you were working on
- What was accomplished
- What to do next
- Any blockers or questions

---

*This overview is designed to minimize token usage. Read detailed documentation only when needed.*
