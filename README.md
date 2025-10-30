# Aikido Blog Writing System

A comprehensive workflow system for writing, reviewing, and managing Aikido blog posts as part of an MA thesis project.

## Overview

This project provides a complete session continuity system designed to maintain context between work sessions, ensuring consistent progress on MA-level Aikido blog content. The system uses Claude Code with custom slash commands to manage the writing workflow, maintain quality standards, and track progress over time.

## Features

- **Session Continuity**: Seamless resumption of work between sessions with `/resume` and `/checkpoint` commands
- **Critical Review System**: MA-level quality standards with collaborative, iterative improvement
- **Historical Tracking**: Timestamped session summaries for progress review
- **Blog Templates**: Structured templates and comprehensive writing guidelines
- **Decision Logging**: Track important choices and their rationale
- **Topic Management**: Pipeline for blog ideas from brainstorming to completion

## Quick Start

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed and configured
- Git initialized in this directory

### Starting Your First Session

1. **Open Claude Code** in this directory
2. **Type `/resume`** to see the workflow reminder and current context
3. **Review help.md** for complete documentation

### Essential Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/resume` | Load previous session context | Start of every session |
| `/checkpoint` | Save state and commit changes | End of every session |
| `/review-aikido [file]` | Review blog post quality | After drafting a post |

## Project Structure

```
/Users/thomas/MA/
├── .claude/
│   ├── commands/          # Slash command definitions
│   └── claude.md          # AI assistant documentation
├── posts/                 # Your blog posts go here
├── sessions/              # Timestamped session summaries
├── blog-template.md       # Template for new posts
├── blog-guidelines.md     # Comprehensive writing guide
├── help.md               # Complete user documentation
├── topics.md             # Topic tracking and planning
├── session-context.md    # Current session state
└── decisions.md          # Decision log with rationale
```

## Workflow

### Starting a Session
```
/resume
```
- See where you left off
- Review next steps
- Check current topic

### During Work
```bash
# Create a new blog post
cp blog-template.md posts/my-topic-2025-10-30.md

# Edit and write...

# Review when ready
/review-aikido posts/my-topic-2025-10-30.md

# Revise based on feedback
# Re-review until excellent
```

### Ending a Session
```
/checkpoint
```
- Commits changes to git (local only)
- Updates session context
- Creates timestamped session summary
- Saves complete state

## Documentation

- **[help.md](help.md)** - Complete user guide with examples and workflows
- **[blog-guidelines.md](blog-guidelines.md)** - Writing standards and structure guide
- **[.claude/claude.md](.claude/claude.md)** - System documentation for AI assistants
- **[sessions/README.md](sessions/README.md)** - Guide to session history

## Quality Standards

This system enforces **MA-level quality standards**:

- Rigorous, critical feedback (not just praise)
- Iterative collaborative improvement
- Precision in terminology and facts
- Depth of analysis and insight
- Clear, engaging writing

The `/review-aikido` command provides comprehensive feedback on:
- Aikido terminology and spelling
- Technical accuracy and fact-checking
- Writing clarity and depth
- Structure and organization

## Session History

Every `/checkpoint` creates a timestamped summary in `sessions/` directory:
- What was accomplished
- Key decisions made
- Conversation highlights
- Files modified
- Next steps

Review any past session to understand the project's evolution.

## Git Workflow

- **Local commits only**: Changes are committed locally, never pushed automatically
- **You control publishing**: Decide when/if to push to a remote repository
- **Clean history**: Each checkpoint creates a meaningful commit

## Getting Help

1. **Read [help.md](help.md)** - Comprehensive guide to the system
2. **Read [blog-guidelines.md](blog-guidelines.md)** - Writing guidance and standards
3. **Ask Claude** - Just ask questions in Claude Code
4. **Review sessions/** - See what you've accomplished previously

## File Types

### Files You Edit Regularly
- `topics.md` - Track blog topics and ideas
- `session-context.md` - Current status and notes
- `posts/*.md` - Your blog posts
- `decisions.md` - Important decisions

### Reference Files (Don't Edit)
- `blog-template.md` - Copy this for new posts
- `blog-guidelines.md` - Writing reference
- `help.md` - User guide

### System Files (Auto-Generated)
- `sessions/*.md` - Session summaries (created by /checkpoint)
- `.claude/*` - System documentation

## Philosophy

This system is designed around three principles:

1. **Excellence over completion** - MA-level quality through rigorous review
2. **Continuity over memory** - Files maintain context, not conversation history
3. **Collaboration over automation** - Work together iteratively, don't just accept first drafts

## Next Steps

After your first `/resume`:

1. Add blog topic ideas to `topics.md`
2. Choose your first topic
3. Copy `blog-template.md` to `posts/[topic]-[date].md`
4. Write following `blog-guidelines.md`
5. Review with `/review-aikido`
6. Revise and improve
7. `/checkpoint` when done

## Support

For issues or questions:
- Refer to [help.md](help.md) for detailed guidance
- Check [blog-guidelines.md](blog-guidelines.md) for writing questions
- Review past sessions in `sessions/` for context
- Ask Claude Code directly for assistance

## License

This is a personal MA thesis project. Content and system are for educational purposes.

---

**Ready to start?** Type `/resume` in Claude Code to begin your first session!
