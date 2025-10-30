# Aikido Blog MA Thesis - Quick Reference

## Project Purpose
Master's thesis project for writing Aikido blog posts with session continuity between Claude Code sessions.

## Essential Commands

### Start/End Session
- `/resume` - Load previous session state (run at start of every session)
- `/checkpoint` - Save state and commit to git (run at end of every session)

### Content Creation Agents
- `/discuss [topic]` - Explore topics through conversation → saves to discussions/
- `/extract [file]` - Transform discussion into blog draft → saves to posts/
- `/review-aikido [file]` - Review blog post quality before publishing

### Content Discovery Agents
- `/track-source [name] [url] [discipline]` - Register martial arts bloggers
- `/scan-sources [name]` - Monitor bloggers for new content and ideas
- `/youtube fetch [url]` - Download and analyze YouTube transcripts
- `/youtube analyze [video_id]` - Re-analyze existing transcripts

### System Maintenance
- `/system-maintenance [mode]` - Audit, clean, sync, and optimize project structure
  - Modes: `audit`, `cleanup`, `sync`, `optimize`, `full`
  - Keeps system lean without using your context

## Core Files (Root Directory)

**Session Management:**
- `session-context.md` - Current status, recent work, next steps
- `topics.md` - Blog topic queue and ideas
- `decisions.md` - Decision log with rationale

**Content:**
- `posts/` - Blog post drafts and finals
- `discussions/` - Informal topic explorations
- `blog/blog-template.md` - Copy this for new posts

**Reference (read when needed):**
- `research/` - Core values, divisive topics, learning frameworks, biomechanics
- `sources/` - Tracked bloggers, YouTube channels, findings
- `syllabus/` - Technical Aikido reference

## Typical Workflows

**Approach A: Discussion-Based (Recommended)**
1. `/resume` → `/discuss [topic]` → `/extract` → develop → `/review-aikido` → `/checkpoint`

**Approach B: Direct Writing**
1. `/resume` → copy template → write → `/review-aikido` → `/checkpoint`

**Approach C: Source-Inspired**
1. `/track-source` → `/scan-sources` → `/discuss [inspired-topic]` → `/extract` → develop → `/review-aikido` → `/checkpoint`

**Approach D: YouTube-Inspired**
1. `/youtube fetch [url]` → review findings → `/discuss` → `/extract` → develop → `/review-aikido` → `/checkpoint`

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
