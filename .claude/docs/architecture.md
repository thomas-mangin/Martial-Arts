# System Architecture

## Directory Structure

```
/Users/thomas/MA/
├── .claude/
│   ├── OVERVIEW.md             # Quick reference (loaded in context)
│   ├── agents/                 # Agent implementations
│   ├── commands/               # Lightweight slash commands
│   └── docs/                   # Detailed documentation (read on-demand)
├── blog/
│   ├── blog-template.md
│   ├── blog-guidelines.md
│   ├── blog-engagement-techniques.md
│   └── blog-series-structure.md
├── research/
│   ├── INDEX.md                # Quick reference to research files
│   ├── core-values.md
│   ├── divisive-topics.md
│   ├── learning-journey.md
│   ├── biomechanical-principles.md
│   └── [other research files]
├── sources/
│   ├── registry/               # Blogger profiles
│   ├── findings/               # Content analysis
│   └── youtube/
│       ├── transcripts/
│       ├── registry/
│       └── findings/
├── posts/                      # Blog post drafts and finals
├── discussions/                # Topic exploration notes
├── sessions/                   # Session history
├── syllabus/                   # Technical Aikido reference
├── topics.md                   # Blog topic queue
├── session-context.md          # Current session state
├── decisions.md                # Decision log
└── PROJECT-STATUS.md           # High-level overview

```

## Core Documents

### Session State Files (Always Updated)

**session-context.md** - The single source of truth for current state
- Current Status: What's being worked on now
- Recent Work: What was accomplished
- Next Steps: Actionable items for continuation
- Blockers/Questions: Issues needing resolution
- Notes: Additional context
- Updated with timestamp on each checkpoint

**topics.md** - Blog topic management
- Current topic being worked on
- Queued topics (priority order)
- Topic ideas (brainstorming)
- Completed topics (archive)

**decisions.md** - Decision log
- Chronological record of important decisions
- Date, decision, and rationale for each entry
- Helps understand why certain approaches were chosen

### Reference Files (Read On-Demand)

**Research Files** - Philosophical grounding
- Read `research/INDEX.md` for quick reference
- Load specific files only when needed for authenticity checks

**Blog Guidelines** - Writing standards
- Read `blog/blog-guidelines.md` when writing
- Read `blog/blog-template.md` when starting new post

**Source Tracking** - Content discovery
- Agents handle reading source files internally
- User only sees findings reports

**Information Routing** - Where to store new information
- Read `.claude/docs/information-routing.md` when unsure where to store user-provided information
- Defines decision tree for routing knowledge to correct files
- Prevents file bloat and maintains clean architecture

## Agent System

Agents are autonomous workers that handle complex multi-step tasks. They read necessary files internally and return only final results.

**Why Agents?**
- Reduce context window usage (don't load instructions upfront)
- Handle file I/O internally (read research files on-demand)
- Complex logic encapsulated (multi-step workflows)
- Cleaner user experience (just results, not process)

**Available Agents:**
- `discuss-agent` - Topic exploration
- `extract-agent` - Discussion to blog draft
- `review-agent` - Blog post quality review
- `scan-sources-agent` - Monitor bloggers
- `track-source-agent` - Register bloggers
- `youtube-fetch-agent` - Download and analyze videos
- `youtube-analyze-agent` - Re-analyze transcripts

## Session Continuity Model

**Problem**: Claude Code sessions are stateless - each session starts fresh

**Solution**: Persist state in files, not memory

**How it Works:**
1. `/resume` at start - Loads session-context.md, topics.md, decisions.md
2. Work on tasks - Update state files as you progress
3. `/checkpoint` at end - Commits all changes, updates state files, creates session summary

**Benefits:**
- Seamless handoff between sessions
- Complete session history in sessions/ directory
- Git history provides audit trail
- Minimal context loading (only current state, not history)

## Git Workflow

- **Local commits only** - Never push unless requested
- **Commit frequently** - Every checkpoint commits work
- **Branch**: Currently on `main`
- **Descriptive messages** - Each commit explains what changed

## Token Optimization Strategy

**Before (Heavy):**
- Load all command documentation (~10k words)
- Load full system architecture (~3k words)
- Load workflow examples (~2k words)
- **Total: ~56k tokens on /resume**

**After (Lean):**
- Load OVERVIEW.md only (~500 words = ~2k tokens)
- Load session state files (~500 words = ~2k tokens)
- Agents read detailed docs internally as needed
- **Total: ~8-10k tokens on /resume**

**Token Savings: 80-85%**

---

*Read this file only when you need to understand the system architecture. Not loaded by default.*
