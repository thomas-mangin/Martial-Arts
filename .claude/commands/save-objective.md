# Save Current Objective

Save the current work objective and progress to enable crash recovery and seamless resumption after interruptions.

## Usage

`/save-objective`

## What It Does

This command captures the current state of your work in `.claude/state/current-objective.md` to ensure continuity even if Claude crashes or you need to pause unexpectedly.

**The command will:**

1. **Analyze Current Work**
   - Review recent conversation to understand what you're working on
   - Identify the agreed objective and approach
   - Note any requirements or constraints discussed
   - Determine current progress and next steps

2. **Update Current Objective File**
   - Save to `.claude/state/current-objective.md`
   - Include timestamp and status
   - Record:
     - Clear statement of objective
     - Key requirements
     - Approach and reasoning
     - Progress (completed, in progress, remaining)
     - Any blockers or questions
     - Context references (files being modified, related docs)

3. **Confirm Save**
   - Show user what was saved
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
1. Your objective is preserved in `.claude/state/current-objective.md`
2. Next `/resume` will show **CRASH RECOVERY** notice
3. You can immediately continue where you left off
4. No context is lost

## Implementation Notes

**For Claude Code:**
- Review the last ~10 messages to understand current work
- Identify the main objective from conversation context
- Note any explicit requirements or constraints mentioned
- Determine what's been completed vs. what remains
- Look for any blockers or questions raised
- Write clear, concise summary to state file
- Update timestamp to current time
- Set status appropriately (Active / Paused / Blocked / Complete)

**State File Location**: `.claude/state/current-objective.md`

## Related Commands

- `/resume` - Loads objective state at session start
- `/checkpoint` - Saves objective state at session end
- `/pause-task` - Move current objective to backlog and clear for new work

---

*This command provides explicit crash recovery insurance for complex tasks.*