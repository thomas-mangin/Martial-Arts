# Pause Current Task

Move the current task to backlog when you need to switch to something else, ensuring no work is lost.

## Usage

`/pause-task [reason]`

**Arguments:**
- `reason` (optional) - Brief explanation of why pausing (e.g., "urgent bug", "blocked", "waiting for clarification")

## What It Does

This command moves your current work objective to the backlog, preserving all context and progress, so you can start fresh on a new task without losing anything.

**The command will:**

1. **Capture Current State**
   - Read `.claude/state/current-objective.md`
   - Extract all progress, requirements, and context
   - Determine what's completed vs. remaining

2. **Add to Backlog**
   - Append task to `.claude/state/backlog.md`
   - Include:
     - Task name (from objective)
     - Priority (infer from context or ask user)
     - Pause date and reason
     - Objective and requirements
     - Progress made so far
     - Next steps for when resuming
     - Context files and references
   - Keep backlog organized (active tasks at top)

3. **Clear Current Objective**
   - Reset `.claude/state/current-objective.md` to template
   - Makes way for new task to be tracked
   - Old task is safely preserved in backlog

4. **Confirm Transition**
   - Show user what was moved to backlog
   - Confirm ready for new task
   - Show current backlog count

## When to Use

**Use this command when:**
- Urgent work interrupts your current task
- You're blocked and need to work on something else while waiting
- You want to switch focus but preserve current work state
- User asks to "put this on hold" or "work on something else first"

**Don't use when:**
- Simply taking a break (current objective stays active)
- Completing current task (just finish it normally)
- Ending session (use `/checkpoint` instead)

## Example

```
User: Let's pause this authentication work for now. There's an urgent bug in the payment system.
Assistant: /pause-task urgent bug
[Moves authentication work to backlog]
✓ Task paused: "Implementing authentication system with JWT tokens"
✓ Added to backlog with "urgent bug" reason
✓ Progress preserved: Database schema complete, API routes 60% done
✓ Next steps saved: Finish API routes, add frontend integration, write tests

Current backlog: 1 task
Ready to start on payment system bug!
```

## Resuming Paused Tasks

To return to a paused task:
1. Check backlog: Look at `.claude/state/backlog.md`
2. Tell Claude: "Let's resume the authentication task from backlog"
3. Claude will move it from backlog back to current objective
4. Continue where you left off

## Implementation Notes

**For Claude Code:**
- Read current-objective.md to get full task context
- Create well-structured backlog entry with all details
- Include timestamp and reason for pause
- Assign priority (High/Medium/Low) based on context or ask user
- Preserve all progress information
- Add clear "Next steps" for easy resumption
- Clear current-objective.md (reset to template)
- Keep backlog organized (most recent/highest priority first)
- Show friendly confirmation with task summary

**State Files**:
- Source: `.claude/state/current-objective.md`
- Destination: `.claude/state/backlog.md`

## Related Commands

- `/save-objective` - Save current work without pausing
- `/resume` - Shows backlog count at session start
- `/checkpoint` - Preserves backlog at session end

---

*This command ensures seamless task switching without losing any work context.*