# Resume Previous Session

You are helping the user resume work from their previous session by loading saved context.

## Steps to Execute

1. **Show Workflow Reminder**
   - Display a brief, friendly reminder of how to use the system
   - Format it clearly and concisely
   - Include the essential workflow steps:
     ```
     📋 WORKFLOW REMINDER

     Your Aikido Blog System:
     • /resume (now) - Start session, see where you left off
     • Work - Write posts, add topics, make progress
     • /checkpoint - End session, save & commit everything

     Quick Commands:
     • /discuss [topic] - Explore ideas through conversation
     • /extract [file] - Transform discussion to blog draft
     • /review-aikido [file] - Review post quality before publishing
     • /scan-sources - Monitor bloggers for new content

     📖 Need help? See OVERVIEW.md or .claude/docs/ for details
     ────────────────────────────────────────────
     ```

2. **Check for Crash Recovery State**
   - Read `.claude/state/current-objective.md` if it exists
   - If it contains a real objective (not template):
     - Display a **CRASH RECOVERY** notice showing the saved objective
     - Show progress, blockers, and next steps from state file
     - This ensures continuity even after crashes or interruptions
   - Read `.claude/state/backlog.md` if it exists
   - If backlog has active tasks:
     - Show count of paused/backlog tasks
     - Note: "You have [N] paused tasks in backlog"
   - This state tracking ensures no work is ever lost

3. **Load Session Context**
   - Read `session-context.md`
   - Display a clear summary of:
     - Current Status: What they were working on
     - Recent Work: What was accomplished
     - Next Steps: What to do next
     - Blockers/Questions: Any issues or decisions needed
     - Notes: Any other relevant context

4. **Review Current Topic**
   - Read `topics.md`
   - Show the current topic they're working on
   - Show the next topics in queue

5. **Check Git Status**
   - Run `git status` to show if there are any uncommitted changes
   - This helps identify if any work-in-progress exists

6. **Recent Decisions**
   - Read the last 2-3 entries from `decisions.md`
   - Show recent decisions for context

7. **Ask How to Proceed**
   - Based on the session context, ask the user:
     - "Would you like to continue with [current task from next steps]?"
     - "Or would you like to work on something else?"
   - Be ready to help with whatever they choose

## Important Notes
- Present information clearly and concisely
- The goal is to quickly get them back into the flow of work
- Be proactive in suggesting next actions based on the context
- If session-context.md doesn't exist or is empty, let them know this is a fresh start
