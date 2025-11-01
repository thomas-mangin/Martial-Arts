# Workflow Protocol

**Purpose**: Ensure consistent, efficient interaction patterns across all Claude Code sessions with clear objective tracking and crash recovery.

**Last Updated**: 2025-11-01

---

## WHY-First Thinking (CRITICAL)

**Primary Principle**: When the WHY is clear, all other questions (WHAT, HOW, WHEN) become easier to answer.

**Every significant decision, analysis, or work product must document**:
1. **WHY** - Rationale, purpose, reasoning (MOST IMPORTANT)
2. **WHAT** - Decisions, conclusions, outputs
3. **HOW** - Approach, methodology, implementation
4. **Alternatives considered** - What was rejected and why
5. **Assumptions & context** - What underlies decisions

**See**: `.claude/docs/design-principles.md` for complete WHY-first thinking framework and examples.

**Purpose**: Conclusions without reasoning are shallow and difficult to resume. Future Claude instances need rationale, not just outputs.

---

## Core Principle

This protocol ensures you never lose context, work is clearly understood before execution, and you always know what's active vs. paused.

---

## Multi-Instance Support

The system supports running multiple concurrent Claude Code sessions without conflicts.

### File Scope: Shared vs Instance-Specific

**Shared Files** (accessible to all instances):
- `session-context.md` - Project-wide status, recent work, next steps
- `topics.md` - Article series progress and queue
- `decisions.md` - Decision log with rationale
- `.claude/state/backlog.md` - Paused/deferred tasks from all instances
- `.claude/state/registry.md` - Master index of all instances

**Instance-Specific Files** (isolated per session):
- `.claude/state/instances/[instance-id]/current-objective.md` - Active work for this instance
- `.claude/state/instances/[instance-id]/session-info.md` - Instance metadata and heartbeat

**Instance ID Format**: Timestamp-based `YYYY-MM-DD-HHMM` (e.g., `2025-10-31-1953`)

### How /resume Handles Instances

**Smart detection logic**:
1. `/resume` with no args → Auto-detect active instances or create new
2. `/resume [instance-id]` → Resume specific instance explicitly
3. `/resume and work on [task]` → Create new instance for that task

**When multiple instances exist**:
- Checks for uncommitted changes in instance directories
- Shows active instances and prompts user to select
- Each instance maintains independent current-objective.md

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

**Note**: The `/resume` command handles instance detection and loads appropriate state automatically.

1. **Active Work**: `.claude/state/instances/[instance-id]/current-objective.md` (instance-specific)
2. **Paused Work**: `.claude/state/backlog.md` (shared - Active Backlog section)
3. **System Context**: `session-context.md` (shared - Current Status)
4. **Other Instances**: `.claude/state/registry.md` (shows what other sessions are working on)

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

1. **Save objective immediately** to `.claude/state/instances/[instance-id]/current-objective.md`:
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

   **Note**: Use `/save-objective` command which automatically saves to the current instance's directory.

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

### `.claude/state/instances/[instance-id]/current-objective.md`

**Purpose**: Track active work for crash recovery (instance-specific)

**Location**: Each instance has its own isolated current-objective.md

**When to Update**:
- When task is confirmed (save objective via `/save-objective` command)
- During work (update progress)
- When completed (clear to template)
- When paused (clear to template after moving to backlog)

**Status Values**:
- `Active` - Currently working on
- `Blocked` - Waiting on user/external factor
- `Complete` - Done (temporary, before clearing)

**Multi-Instance Context**: Multiple instances can each have active objectives simultaneously without conflicts

---

### `.claude/state/backlog.md`

**Purpose**: Track paused/deferred tasks (shared across all instances)

**Location**: Shared file - all instances can see and access the backlog

**Sections**:
- **Active Backlog**: Tasks paused but not forgotten
- **Completed Tasks**: Recent completions for reference

**When to Update**:
- Add task when pausing current work (via `/pause-task` command)
- Remove task when resuming it
- Add to completed section when task finishes from backlog

**Multi-Instance Context**: Tasks from any instance can be paused to backlog and resumed by any instance

---

## Crash Recovery

If Claude crashes mid-task:

1. Objective is preserved in `.claude/state/instances/[instance-id]/current-objective.md`
2. Next session's `/resume` detects incomplete work in instance
3. Present **CRASH RECOVERY** notice with overview
4. User can choose to continue or switch tasks

**Multi-Instance Context**: Each instance has independent crash recovery. If one instance crashes, others are unaffected. User can `/resume [instance-id]` to recover specific crashed instance.

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

**Session Management**:
- `/resume` - Load state at session start (auto-detects or creates instance, presents overview)
- `/resume [instance-id]` - Resume specific instance explicitly
- `/resume and work on [task]` - Create new instance for specific task
- `/checkpoint` - Save state at session end (instance-specific)
- `/save-objective` - Explicitly save current work progress (to current instance)
- `/pause-task [reason]` - Move current work to backlog (shared)

**Multi-Instance Management**:
- `/instances` - View all active Claude instances and their current work
- `/cleanup-instances` - Archive, delete, or keep stale instances (>24h old)

---

*This protocol ensures efficient, continuous work with perfect context preservation across sessions.*
