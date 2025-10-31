# System Architecture

## Overview

This is an educational article series writing system with multi-instance support, designed for progressive learning and eventual book compilation. MSc-level quality standards applied.

**Purpose**: Write comprehensive Aikido educational articles that build on each other systematically, leveraging extensive research from YouTube transcripts, personal experience, and martial arts knowledge.

---

## Directory Structure

```
/Users/thomas/MA/
├── .claude/
│   ├── CLAUDE.md               # Quick reference (loaded in context)
│   ├── agents/                 # Agent implementations
│   ├── commands/               # Lightweight slash commands
│   ├── docs/                   # Detailed documentation (read on-demand)
│   └── state/                  # Session state management
│       ├── registry.md         # Multi-instance coordination
│       ├── backlog.md          # Paused tasks (shared)
│       └── instances/          # Instance-specific state
│           ├── [instance-id]/
│           │   ├── current-objective.md
│           │   └── session-info.md
│           └── _archived/      # User-archived instances
├── article/
│   ├── article-template.md
│   ├── article-guidelines.md
│   ├── article-series-structure.md
│   └── article-voice-guide.md
├── articles/                   # Article drafts and finals (organized by series)
├── discussions/                # Topic exploration notes
├── posts/                      # Legacy directory (pre-transformation)
├── research/
│   ├── INDEX.md                # Quick reference to research files
│   ├── user-profile.md         # Author background and expertise
│   ├── audience-profiles.md    # Target reader profiles
│   ├── core-values.md          # Foundational beliefs
│   ├── divisive-topics.md      # Controversial topics framework
│   ├── learning-frameworks.md  # Mastery progression models
│   ├── biomechanics/           # Organized biomechanics principles
│   └── [other research files]
├── sources/
│   ├── registry/               # Blogger profiles
│   ├── findings/               # Content analysis
│   └── youtube/
│       ├── transcripts/        # 1,983 transcript files
│       ├── registry/           # Channel profiles
│       └── findings/           # Video analysis and article ideas
├── sessions/                   # Session history
├── syllabus/                   # Technical Aikido reference
├── topics.md                   # Article series progress and queue
├── session-context.md          # Current session state (shared)
└── decisions.md                # Decision log (shared)
```

---

## Multi-Instance Architecture

**Purpose**: Run multiple concurrent Claude Code sessions without conflicts

### File Scope

**Shared Files** (accessible to all instances):
- `session-context.md` - Project-wide status, recent work, next steps
- `topics.md` - Article series progress and queue
- `decisions.md` - Decision log with rationale
- `.claude/state/backlog.md` - Paused/deferred tasks from all instances
- `.claude/state/registry.md` - Master index of all instances

**Instance-Specific Files** (isolated per session):
- `.claude/state/instances/[instance-id]/current-objective.md` - Active work for this instance
- `.claude/state/instances/[instance-id]/session-info.md` - Instance metadata and heartbeat

### Instance Management

**Instance ID Format**: Timestamp-based `YYYY-MM-DD-HHMM` (e.g., `2025-10-31-1953`)

**Lifecycle**:
- Created by `/resume` when starting new work
- Updated by `/save-objective` during work
- Marked "Idle" by `/checkpoint` at session end
- Cleaned up by `/cleanup-instances` when stale (>24h)

**Coordination**:
- Registry tracks all instances with status and heartbeat
- Each instance sees what others are working on
- Independent crash recovery per instance
- No conflicts between concurrent sessions

---

## Core Documents

### Session State Files (Shared - Always Updated)

**session-context.md** - Single source of truth for project-wide state
- Current Status: Overall system phase and readiness
- Recent Work: What was accomplished recently
- Next Steps: Actionable items for continuation
- Blockers/Questions: Issues needing resolution
- Notes: Additional context
- Updated with timestamp on each checkpoint

**topics.md** - Article series management
- Current article being worked on
- Article series queue (priority order)
- Potential article series (from research)
- Completed articles (archive)
- Audience coverage tracking

**decisions.md** - Decision log with rationale
- Foundational Values: Core beliefs about martial arts
- Writing Style: Voice, honesty, frameworks
- Content Strategy: Multi-audience, progressive series, educational depth
- Content Quality: Review standards, self-consistency
- System Architecture: Technical organization
- Session Management: Git and workflow decisions

**`.claude/state/backlog.md`** - Paused task management (shared)
- Active Backlog: Tasks paused but not forgotten
- Completed Tasks: Recent completions for reference
- Tasks from any instance can be paused and resumed

### Reference Files (Read On-Demand)

**Research Files** - Philosophical and technical grounding
- Read `research/INDEX.md` for quick reference
- Load specific files only when needed for authenticity checks
- `user-profile.md` - Author background (veteran, shodan, biomechanics focus)
- `audience-profiles.md` - Complete target reader definitions
- `core-values.md` - Biomechanics over mysticism, peace through understanding cost
- `divisive-topics.md` - Violence context framework, legal/ethical context
- `learning-frameworks.md` - Knowing vs embodied understanding
- `biomechanics/` - 32 principles across 7 categories

**Article Guidelines** - Writing standards
- Read `article/article-guidelines.md` when writing
- Read `article/article-template.md` when starting new article
- Read `article/article-series-structure.md` for series organization
- Read `article/article-voice-guide.md` for tone and perspective

**Source Tracking** - Content discovery and validation
- Agents handle reading source files internally
- User only sees findings reports
- 1,983 YouTube transcripts for cross-validation
- 60+ article ideas documented

---

## Agent System

Agents are autonomous workers that handle complex multi-step tasks. They read necessary files internally and return only final results.

**Why Agents?**
- Reduce context window usage (don't load instructions upfront)
- Handle file I/O internally (read research files on-demand)
- Complex logic encapsulated (multi-step workflows)
- Cleaner user experience (just results, not process)

**Available Agents:**
- `discuss` - Topic exploration through conversation
- `extract` - Discussion to article draft transformation
- `review-aikido` - Article quality review (educational depth, consistency, completeness)
- `track-source` - Register martial arts bloggers
- `scan-sources` - Monitor bloggers for new content
- `youtube fetch` - Download and analyze video transcripts
- `youtube analyze` - Re-analyze existing transcripts
- `system-maintenance` - Audit, clean, sync, and optimize project structure

---

## Session Continuity Model

**Problem**: Claude Code sessions are stateless - each session starts fresh

**Solution**: Persist state in files, not memory

**How it Works:**

1. **`/resume`** at start
   - Loads shared state (session-context.md, topics.md, backlog.md)
   - Detects or creates instance
   - Shows crash recovery if instance has incomplete work
   - Presents overview of current and paused objectives

2. **Work on tasks**
   - Update instance-specific current-objective.md as you progress
   - Update shared session-context.md as major milestones reached
   - Add ideas to topics.md as they emerge
   - Log important decisions to decisions.md

3. **`/checkpoint`** at end
   - Commits all changes to git
   - Pushes to GitHub automatically
   - Updates instance heartbeat and marks "Idle"
   - Creates session summary in sessions/
   - Updates registry

**Benefits:**
- Seamless handoff between sessions
- Complete session history in sessions/ directory
- Git history provides audit trail
- Minimal context loading (only current state, not history)
- Multi-instance support enables parallel workflows
- Crash recovery per instance

---

## State Management & Crash Recovery

### Current Objective Tracking

**Instance-Specific**: `.claude/state/instances/[instance-id]/current-objective.md`

**Purpose**: Track active work for crash recovery

**Contains**:
- Agreed objective and requirements
- Approach and reasoning
- Progress (completed, in progress, remaining)
- Blockers and questions
- Context files and references

**Updated**:
- When task confirmed (via `/save-objective`)
- During work (progress updates)
- When completed (cleared to template)
- When paused (moved to backlog, then cleared)

### Backlog Management

**Shared**: `.claude/state/backlog.md`

**Purpose**: Track paused/deferred tasks from all instances

**Workflow**:
- `/pause-task [reason]` - Move current work to backlog
- Task preserved with progress, context, next steps
- Any instance can resume backlog tasks
- Completed backlog tasks archived

### Crash Recovery

If Claude crashes mid-task:
1. Objective preserved in instance's current-objective.md
2. Next session's `/resume` detects incomplete work
3. Presents CRASH RECOVERY notice with overview
4. User can continue or switch tasks
5. Each instance has independent recovery

---

## Git Workflow

- **Local commits** - Every checkpoint commits work
- **Automatic push** - Pushes to GitHub after each checkpoint
- **Branch**: Currently on `main`
- **Descriptive messages** - Each commit explains what changed
- **Never force push** - Safety first

---

## Token Optimization Strategy

**Goal**: Minimize context loading to enable longer conversations and complex workflows

**Before (Heavy):**
- Load all command documentation (~10k words)
- Load full system architecture (~3k words)
- Load workflow examples (~2k words)
- **Total: ~56k tokens on /resume**

**After (Lean):**
- Load CLAUDE.md only (~500 words = ~2k tokens)
- Load session state files (~500 words = ~2k tokens)
- Agents read detailed docs internally as needed
- **Total: ~8-10k tokens on /resume**

**Token Savings: 80-85%**

**Maintenance**: `/system-maintenance` agent monitors and optimizes token usage

**Targets** (measured by system-maintenance agent):
- /resume load: <10,000 tokens target
- 🟢 Green: Within target or <110%
- 🟡 Yellow: 110-130% (needs attention)
- 🔴 Red: >130% (must fix)

---

## System Transformation History

**Original**: Blog writing system with standalone posts
**Current**: Educational article series system designed for book publication

**Key Changes**:
- `blog/` → `article/` (templates and guidelines)
- `posts/` → `articles/` (organized by series)
- Standalone posts → Progressive series (articles build on each other)
- Blog-style (800-1200 words) → Educational depth (1,500-3,000+ words)
- Engagement focus → Comprehensive learning focus
- Casual tone → MSc-level quality standards

**Legacy**: `posts/` directory remains for historical content

---

*Read this file only when you need to understand the system architecture. Not loaded by default.*
