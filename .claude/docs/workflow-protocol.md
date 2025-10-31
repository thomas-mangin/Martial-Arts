# Workflow Protocol

**Purpose**: Ensure consistent, efficient interaction patterns across all Claude Code sessions with clear objective tracking and crash recovery.

---

## Core Principle

This protocol ensures you never lose context, work is clearly understood before execution, and you always know what's active vs. paused.

---

## Session Start Protocol

### When User First Interacts (Session Resume)

**ALWAYS present overview of objectives:**

```
## 📋 Current Objectives Overview

**Active Objective**: [Description from current-objective.md, or "None"]

**Paused Tasks**:
- [Task 1 from backlog.md]
- [Task 2 from backlog.md]
- [Or "None"]

**System Status**: [Brief context from session-context.md]
```

**Then ask**: "What would you like to work on?"

### Where to Read State From

1. **Active Work**: `.claude/state/current-objective.md`
2. **Paused Work**: `.claude/state/backlog.md` (Active Backlog section)
3. **System Context**: `session-context.md` (Current Status)

---

## Task Acceptance Protocol

### When User Gives You a Task

**Step 1: Clarify & Restate**

Parse the user's request and restate it in clear, specific terms:

```
## 🎯 Task Clarification

**What I understand you want me to do:**

[Clear, specific restatement of the task with details]

**[Key details/approach/scope]**

**Is this correct, or would you like me to adjust anything?**
```

**Important**:
- Make the restatement specific and actionable
- Break down complex requests into clear steps
- Clarify any ambiguities
- Ask ONLY ONCE for confirmation

---

**Step 2: Upon Confirmation - Execute Completely**

Once user confirms (says "yes", "go", "correct", etc.):

1. **Save objective immediately** to `.claude/state/current-objective.md`:
   ```markdown
   # Current Objective

   **Last Updated**: [timestamp]
   **Status**: Active

   ## Agreed Objective
   [Clear statement from confirmed task]

   ## Key Requirements
   - [Requirement 1]
   - [Requirement 2]

   ## Approach & Reasoning
   [Brief explanation]

   ## Progress
   **Completed**: []
   **In Progress**: [First task]
   **Remaining**: [List]

   ## Context References
   **Files Being Modified**: [list]
   ```

2. **Execute work to completion**:
   - Use TodoWrite to track progress
   - Work through all steps
   - Handle errors and blockers
   - **Do NOT ask for further confirmations** unless:
     - You encounter a blocker that requires user decision
     - The scope changes significantly
     - You need critical information not available

3. **Upon completion**:
   - Clear the objective from `current-objective.md` (reset to template)
   - Update progress in `session-context.md` if significant
   - Present overview again (see "Work Completion Protocol" below)

---

## Work Completion Protocol

### When Work Is Fully Completed

**ALWAYS present overview again:**

```
✅ **Task Completed**: [Brief description]

**Work Done**:
- [Accomplishment 1]
- [Accomplishment 2]

---

## 📋 Current Objectives Overview

**Active Objective**: None

**Paused Tasks**: [List from backlog.md or "None"]

**Ready for your next task!** What would you like to work on?
```

This helps the user decide what to do next without having to ask.

---

## Pausing Tasks Protocol

### When Switching to Urgent Work

If user asks to switch tasks before current work is complete:

1. **Save current work to backlog**:
   - Move current objective details to `.claude/state/backlog.md`
   - Add paused date, reason, progress made, next steps
   - Clear `current-objective.md` to template

2. **Then proceed with new task** using standard protocol

### Using /pause-task Command

When user explicitly calls `/pause-task [reason]`:
- Document current progress thoroughly
- Move to backlog with reason
- Clear active objective
- Present overview

---

## State File Management

### `.claude/state/current-objective.md`

**Purpose**: Track active work for crash recovery

**When to Update**:
- When task is confirmed (save objective)
- During work (update progress)
- When completed (clear to template)
- When paused (clear to template after moving to backlog)

**Status Values**:
- `Active` - Currently working on
- `Blocked` - Waiting on user/external factor
- `Complete` - Done (temporary, before clearing)

---

### `.claude/state/backlog.md`

**Purpose**: Track paused/deferred tasks

**Sections**:
- **Active Backlog**: Tasks paused but not forgotten
- **Completed Tasks**: Recent completions for reference

**When to Update**:
- Add task when pausing current work
- Remove task when resuming it
- Add to completed section when task finishes from backlog

---

## Crash Recovery

If Claude crashes mid-task:

1. Objective is preserved in `current-objective.md`
2. Next session's `/resume` detects incomplete work
3. Present **CRASH RECOVERY** notice with overview
4. User can choose to continue or switch tasks

---

## Key Principles

1. **Ask Once**: Clarify and confirm once, then execute completely
2. **Save State**: Always save objective before starting work
3. **Present Overview**: At session start and after completing work
4. **No Lost Work**: Pause mechanism ensures nothing is forgotten
5. **Clear Communication**: User always knows what's active vs. paused
6. **Crash Safety**: State files enable seamless recovery

---

## Example Interaction Flow

```
SESSION START:
Claude: [Presents overview from state files]
User: "Add authentication to the API"

CLARIFICATION:
Claude: [Restates task specifically, asks for confirmation]
User: "Yes, go"

EXECUTION:
Claude: [Saves objective, executes completely without further questions]

COMPLETION:
Claude: [Presents completion summary + overview for next task]
```

---

## Related Commands

- `/resume` - Load state at session start (includes presenting overview)
- `/checkpoint` - Save state at session end
- `/save-objective` - Explicitly save current work progress
- `/pause-task [reason]` - Move current work to backlog

---

*This protocol ensures efficient, continuous work with perfect context preservation across sessions.*
