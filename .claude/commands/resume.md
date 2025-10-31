# Resume Previous Session

You are helping the user resume work by loading saved context and managing multi-instance coordination.

## Arguments

- No arguments: Smart detection of instance to resume or create new
- `[instance-id]`: Explicitly resume specific instance (e.g., `2025-10-31-1945`)
- `[task description]`: Create new instance for specific task (e.g., "and work on article writing")

## Steps to Execute

### 1. Show Workflow Reminder

Display brief reminder:
```
📋 WORKFLOW REMINDER

Your Aikido Educational Article Series System:
• /resume (now) - Start session, see where you left off
• Work - Write articles, add topics, make progress
• /checkpoint - End session, save & commit everything

Quick Commands:
• /discuss [topic] - Explore ideas through conversation
• /extract [file] - Transform discussion to article draft
• /review-aikido [file] - Review article quality before publishing
• /instances - See all active instances

📖 Need help? See .claude/CLAUDE.md or .claude/docs/ for details
────────────────────────────────────────────
```

### 2. Detect or Determine Instance ID

**Apply smart detection logic:**

1. **If explicit instance ID provided** (matches `YYYY-MM-DD-HHMM` format):
   - Use that instance
   - Load from `.claude/state/instances/[instance-id]/`
   - If doesn't exist, error: "Instance not found. Run `/instances` to see active instances."

2. **If task description provided** (any other text):
   - Create new instance with current timestamp
   - Instance ID: `date +%Y-%m-%d-%H%M` format
   - Create instance directory
   - Initialize session-info.md

3. **If no arguments** (smart detection):
   - Check git status for uncommitted changes in `.claude/state/instances/*/`
   - Count active instances (heartbeat <1 hour)

   **If 0 active instances**:
   - Create new instance automatically

   **If 1 active instance**:
   - Show: "Found 1 active instance: [instance-id] working on [task]"
   - Ask: "Continue this instance or start new? (c/n)"
   - If continue: use existing
   - If new: create new timestamp-based instance

   **If 2+ active instances**:
   - Show all active instances with summary
   - Ask: "Which instance to resume? (Enter instance-id or 'new')"
   - Use selected instance or create new

### 3. Initialize/Update Instance

**If new instance:**
- Create directory: `.claude/state/instances/[instance-id]/`
- Copy template to `session-info.md` with current timestamp
- Create blank `current-objective.md` from template
- Register in registry.md

**If existing instance:**
- Update heartbeat in session-info.md
- Mark status as "Active"
- Update registry.md

### 4. Show Instance Overview

Display which instance you are and what others are doing:

```
🔷 YOUR INSTANCE: 2025-10-31-1945
   Created: 30 minutes ago
   Working on: Multi-instance architecture implementation

📊 OTHER ACTIVE INSTANCES:
   • 2025-10-31-1430 (5h ago) - YouTube analysis - Guillaume Erard

Run `/instances` for full details
────────────────────────────────────────────
```

### 5. Check for Crash Recovery State

- Read `.claude/state/instances/[instance-id]/current-objective.md`
- If contains real objective (not template):
  - Display **CRASH RECOVERY** notice
  - Show progress, blockers, next steps
  - This ensures continuity after crashes

### 6. Check Shared Backlog

- Read `.claude/state/backlog.md`
- If backlog has tasks:
  - Show count: "You have [N] paused tasks in backlog"
  - List brief summary of each

### 7. Load Session Context (Shared)

- Read `session-context.md`
- Display summary:
  - Current Status
  - Recent Work
  - Next Steps
  - Blockers/Questions
  - Notes

### 8. Review Current Topic (Shared)

- Read `topics.md`
- Show current topic
- Show next topics in queue

### 9. Check Git Status

- Run `git status` to show uncommitted changes
- Identifies work-in-progress

### 10. Recent Decisions (Shared)

- Read last 2-3 entries from `decisions.md`
- Show for context

### 11. Ask How to Proceed

Based on context:
- If crash recovery state exists: "Continue with [task]?"
- If new instance: "What would you like to work on?"
- If continuing instance: "Continue with [task] or switch to something else?"

## Important Notes

- **Instance isolation**: Each instance has own current-objective.md
- **Shared context**: session-context.md, topics.md, backlog.md, decisions.md are shared
- **Registry**: Always update registry.md on instance start
- **Heartbeat**: Update session-info.md with current timestamp
- **Smart detection**: Make it easy - infer intent from arguments and state
- Present information clearly and concisely
- Goal is quick context loading and getting back to work

## Examples

```bash
/resume                                    # Smart detect or create new
/resume 2025-10-31-1945                   # Resume specific instance
/resume and work on biomechanics article  # Create new instance for task
```
