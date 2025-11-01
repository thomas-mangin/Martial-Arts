# Aikido Educational Article Series - Quick Reference

## Project Purpose
Personal project for writing educational Aikido article series (designed for book publication) with session continuity between Claude Code sessions. MSc-level quality standards applied (author has MSc in Computer Science).

## ⭐ Core Principles

### WHY-First Thinking
**CRITICAL**: When the WHY is clear, all other questions become easier to answer (WHAT, HOW, WHEN, WHERE).

**Always document**: WHY (rationale) → WHAT (decisions) → HOW (approach) → Alternatives → Assumptions

**Purpose**: Enable effective resumption. Conclusions without reasoning are shallow.

### Collaboration Model: Professor-Student Relationship
**CRITICAL**: Read `.claude/docs/collaboration-model.md` for complete relationship model.

**User Role**: Professor/Mentor
- Set direction and focus progress
- Validate thinking quality (not micromanage)
- Course correct when needed
- Provide domain expertise

**Claude Role**: Advanced Student/Expert Changing Domains
- High capability BUT low domain experience
- Propose approaches with reasoning
- Execute deeply once direction clear
- Seek validation proactively
- Make assumptions explicit

**Pattern**: User guides → Claude proposes approach → User validates → Claude executes deeply → User validates results

## 🔄 Interaction Protocol

**CRITICAL**: Read `.claude/docs/workflow-protocol.md` for complete interaction guidelines.

**Key behaviors:**
1. **Session start or work completion** → Present overview of current/paused objectives
2. **When given task** → Clarify and restate, ask for confirmation ONCE
3. **After confirmation** → Save objective, execute completely without further confirmations
4. **State management** → Active objectives in `current-objective.md`, paused in `backlog.md`

## Essential Commands

### Start/End Session
- `/resume` - Load previous session state (run at start of every session)
- `/checkpoint` - Save state and commit to git (run at end of every session)

### Crash Recovery & State Management
- `/save-objective` - Explicitly save current work objective (for crash recovery)
- `/pause-task [reason]` - Move current task to backlog when switching to urgent work

### Multi-Instance Support (Run Multiple Claude Sessions)
- `/instances` - View all active Claude instances and their current work
- `/cleanup-instances` - Archive, delete, or keep stale instances (>24h old)
- `/resume [instance-id]` - Resume specific instance or auto-detect
- `/resume and work on [task]` - Create new instance for specific task

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
- `session-context.md` - Current status, recent work, next steps (shared)
- `topics.md` - Article series progress and queue (shared)
- `decisions.md` - Decision log with rationale (shared)
- `.claude/state/backlog.md` - Paused/deferred tasks (shared)
- `.claude/state/registry.md` - Multi-instance coordination
- `.claude/state/instances/[id]/` - Instance-specific state (isolated per session)

**Content:**
- `articles/` - Article series drafts and finals (organized by series)
- `discussions/` - Informal topic explorations
- `article/` - Article templates and guidelines

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
2. **Always end with `/checkpoint`** - Saves state, commits locally, and pushes to GitHub
3. **Automatic GitHub backup** - Each checkpoint pushes to remote automatically
4. **Use agents for heavy tasks** - They handle details internally
5. **Reference detailed docs** only when needed - See `.claude/docs/`
6. **State is preserved** - Current objective and backlog tracked in `.claude/state/` for crash recovery
7. **Multi-instance ready** - Run multiple Claude sessions without conflicts

## Multi-Instance Usage

**Running concurrent sessions:**
- Each instance gets timestamp-based ID (e.g., `2025-10-31-1945`)
- Instance-specific state isolated in `.claude/state/instances/[id]/`
- Shared files (session-context, topics, backlog) accessible to all
- Use `/instances` to see what other sessions are working on
- Each instance should `/checkpoint` separately when done

**Smart instance detection:**
- `/resume` with no args auto-detects or prompts for instance
- `/resume and work on article` creates new instance automatically
- `/resume 2025-10-31-1945` resumes specific instance explicitly

## Need More Details?

- **Collaboration Model**: Read `.claude/docs/collaboration-model.md` ⭐ **READ FIRST - How we work together**
- **Design Principles**: Read `.claude/docs/design-principles.md` ⭐ **READ SECOND - WHY-first thinking**
- **Interaction Protocol**: Read `.claude/docs/workflow-protocol.md` ⭐ **READ THIRD**
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
