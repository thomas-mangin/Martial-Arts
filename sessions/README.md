# Session History

This folder contains timestamped summaries of each work session with Claude Code.

## Purpose

Session summaries provide:
- **Historical record** of what was accomplished each session
- **At-a-glance review** of progress over time
- **Context for future reference** when you need to remember why decisions were made
- **Pattern tracking** to see what you've been focusing on

## File Naming

Format: `session-YYYY-MM-DD-HHMM.md`

Example: `session-2025-10-30-0145.md` (October 30, 2025 at 1:45 AM)

## Automatic Creation

These files are automatically created when you run `/checkpoint` at the end of each session. You don't need to create them manually.

## Contents

Each session summary includes:
- Session date, time, and duration
- Main focus of the work
- Accomplishments and completions
- Key decisions made
- Challenges encountered
- Conversation highlights
- Files modified
- Next steps identified

## Reviewing History

To review your session history:

```bash
# List all sessions chronologically
ls -lt sessions/

# View a specific session
cat sessions/session-2025-10-30-0145.md

# Search across all sessions for a topic
grep -r "aikido terminology" sessions/

# See most recent session
ls -t sessions/*.md | head -1 | xargs cat
```

## Benefits

- **Resume faster**: Quickly understand what happened last time
- **Track progress**: See how the project evolves over time
- **Identify patterns**: Notice recurring topics or blockers
- **Document journey**: Maintain record of your MA work process
- **Reference decisions**: Find when and why choices were made

---

*This folder is managed automatically by the /checkpoint command*
