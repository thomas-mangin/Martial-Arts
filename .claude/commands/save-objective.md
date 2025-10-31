# Save Current Objective

Save the current work objective and progress to enable crash recovery and seamless resumption after interruptions.

## Usage

`/save-objective`

## What It Does

This command captures the current state of your work in `.claude/state/current-objective.md` to ensure continuity even if Claude crashes or you need to pause unexpectedly.

**The command will:**

1. **Determine Current Instance**
   - Check if multi-instance system is active
   - Identify current instance ID from session context
   - If not using instances, use legacy single-objective mode

2. **Analyze Current Work**
   - Review recent conversation to understand what you're working on
   - Identify the agreed objective and approach
   - Note any requirements or constraints discussed
   - Determine current progress and next steps

3. **Update Current Objective File**
   - **If using instances**:
     - Save to `.claude/state/instances/[instance-id]/current-objective.md`
     - Update heartbeat in session-info.md
     - Update activity log with save timestamp
     - Update registry.md
   - **If not using instances** (backward compatible):
     - Save to `.claude/state/current-objective.md`
   - Include timestamp and status
   - Record:
     - Clear statement of objective
     - Key requirements
     - Approach and reasoning
     - Progress (completed, in progress, remaining)
     - Any blockers or questions
     - Context references (files being modified, related docs)

4. **Confirm Save**
   - Show user what was saved
   - If using instances, show which instance
   - Confirm crash recovery state is preserved

## When to Use

**Automatically** (you don't need to call this manually):
- `/checkpoint` saves state automatically at end of session
- `/resume` loads state automatically at start of session

**Manually** (call this command when):
- Working on complex multi-step task and want to save progress
- About to switch to urgent work and want to preserve current task
- Concerned about losing context due to crash or interruption
- Want explicit confirmation that objective is saved

## Example

```
User: I'm going to work on implementing the authentication system, but I want to make sure this is saved first.
Assistant: /save-objective
[Analyzes conversation and saves current objective]
Objective saved: "Implementing authentication system with JWT tokens"
Progress: Database schema complete, API routes in progress
Next steps: Finish API routes, add frontend integration, write tests
```

## Crash Recovery

If Claude crashes or restarts:
1. Your objective is preserved in instance-specific or legacy state file
2. Next `/resume` will show **CRASH RECOVERY** notice
3. You can immediately continue where you left off
4. No context is lost
5. Multi-instance: Each instance preserves its own state independently

## Implementation Notes

**For Claude Code:**
- Determine if using multi-instance system (check session context)
- Review the last ~10 messages to understand current work
- Identify the main objective from conversation context
- Note any explicit requirements or constraints mentioned
- Determine what's been completed vs. what remains
- Look for any blockers or questions raised
- Write clear, concise summary to state file
- Update timestamp to current time
- Set status appropriately (Active / Paused / Blocked / Complete)
- **If using instances**:
  - Update session-info.md heartbeat
  - Add activity log entry
  - Update registry.md status
  - Save to instance-specific directory
- **If not using instances**:
  - Save to legacy `.claude/state/current-objective.md`

**State File Locations**:
- **Multi-instance**: `.claude/state/instances/[instance-id]/current-objective.md`
- **Legacy**: `.claude/state/current-objective.md`

## Related Commands

- `/resume` - Loads objective state at session start
- `/checkpoint` - Saves objective state at session end
- `/pause-task` - Move current objective to backlog and clear for new work

---

*This command provides explicit crash recovery insurance for complex tasks.*