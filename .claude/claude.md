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
│   │   └── review-aikido.md    # Review blog posts for quality
│   └── claude.md               # This file - project context
├── posts/                      # Blog posts directory
├── sessions/                   # Session history (timestamped summaries)
├── topics.md                   # Topic tracking
├── session-context.md          # Session state
├── decisions.md                # Decision log
├── blog-template.md            # Post template
├── blog-guidelines.md          # Writing guidelines
└── help.md                     # User guide
```

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

---

## Git Workflow

- **Local commits only**: Never push to remote unless explicitly requested
- **Commit frequently**: Use /checkpoint to commit work at end of sessions
- **Branch**: Currently on `main` branch
- **Status**: Initial setup files not yet committed (as of 2025-10-30)

---

## Blog Writing Workflow

### Standard Process:

1. **Start Session**: `/resume` to see where you left off
2. **Choose Topic**: Review topics.md, select or add new topic
3. **Create Post**: `cp blog-template.md posts/[topic-name]-YYYY-MM-DD.md`
4. **Write Content**: Follow structure in blog-guidelines.md
5. **Review**: `/review-aikido posts/[filename].md`
6. **Revise**: Based on review feedback
7. **Finalize**: Update topics.md (move to completed)
8. **End Session**: `/checkpoint` to save state and commit

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
