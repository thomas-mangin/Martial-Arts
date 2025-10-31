# State Tracking & Crash Recovery

This directory contains critical state information that ensures work continuity even if Claude crashes or sessions are interrupted.

## Purpose

**Crash Recovery**: If Claude crashes, restarts, or you need to pause work urgently, this state ensures:
- Your current objective is preserved
- All progress is documented
- Next steps are clear
- Backlog of paused tasks is maintained
- No work is ever lost

## State Files

### current-objective.md
**Purpose**: Track the active task/objective being worked on

**Contains**:
- Clear objective statement
- Key requirements
- Approach and reasoning
- Progress (completed, in progress, remaining)
- Blockers and questions
- Context references (files, docs)

**Updated by**:
- `/save-objective` - Explicit save during work
- `/checkpoint` - Automatic save at session end

**Loaded by**:
- `/resume` - Shows CRASH RECOVERY notice if objective exists
- Manual inspection when needed

### backlog.md
**Purpose**: Track paused/deferred tasks that aren't currently active

**Contains**:
- List of paused tasks with priorities
- Reason for pausing each task
- Progress made before pausing
- Next steps for resumption
- Context files and references

**Updated by**:
- `/pause-task` - Moves current objective to backlog
- `/checkpoint` - Preserves backlog state
- Manual editing if needed

**Loaded by**:
- `/resume` - Shows backlog count
- Manual inspection to review paused work

## Workflows

### Normal Work (No Interruptions)
1. `/resume` - Start session (loads state)
2. Work on task
3. `/save-objective` - (Optional) explicitly save progress
4. `/checkpoint` - End session (saves state automatically)

### Interrupted Work (Urgent Task)
1. Working on Task A
2. `/pause-task "urgent bug"` - Move Task A to backlog
3. Work on urgent bug
4. `/checkpoint` - Save everything
5. Next session: `/resume` - Choose to resume Task A from backlog

### After Crash
1. Claude crashes mid-task
2. Restart Claude Code
3. `/resume` - Shows **CRASH RECOVERY** notice
4. Continue exactly where you left off
5. All context preserved

## Technical Details

**File Format**: Markdown with structured sections
**Location**: `.claude/state/` (in system directory, not user-facing)
**Persistence**: Committed to git via `/checkpoint`
**Visibility**: Shown to user via `/resume` when relevant

## Design Philosophy

**Defensive Programming**:
- Assume crashes will happen
- Preserve state continuously
- Make resumption seamless
- Never lose work

**Minimal Friction**:
- Automatic state saving in `/checkpoint`
- Explicit saves available when needed
- Clear crash recovery notices
- Easy task switching with backlog

**User Trust**:
- Work is never lost
- State is always preserved
- Interruptions are handled gracefully
- Context survives crashes

---

*This system ensures robust continuity and crash recovery for all work in the Aikido Educational Article Series project.*
