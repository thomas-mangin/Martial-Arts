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

     Quick Guide:
     1. Check "Next Steps" below for what to do
     2. Copy blog-template.md for new posts → posts/
     3. Follow blog-guidelines.md for structure
     4. Use /review-aikido [file] before finalizing

     📖 Need help? Read help.md for complete guide
     ────────────────────────────────────────────
     ```

2. **Load Session Context**
   - Read `session-context.md`
   - Display a clear summary of:
     - Current Status: What they were working on
     - Recent Work: What was accomplished
     - Next Steps: What to do next
     - Blockers/Questions: Any issues or decisions needed
     - Notes: Any other relevant context

3. **Review Current Topic**
   - Read `topics.md`
   - Show the current topic they're working on
   - Show the next topics in queue

4. **Check Git Status**
   - Run `git status` to show if there are any uncommitted changes
   - This helps identify if any work-in-progress exists

5. **Recent Decisions**
   - Read the last 2-3 entries from `decisions.md`
   - Show recent decisions for context

6. **Ask How to Proceed**
   - Based on the session context, ask the user:
     - "Would you like to continue with [current task from next steps]?"
     - "Or would you like to work on something else?"
   - Be ready to help with whatever they choose

## Important Notes
- Present information clearly and concisely
- The goal is to quickly get them back into the flow of work
- Be proactive in suggesting next actions based on the context
- If session-context.md doesn't exist or is empty, let them know this is a fresh start
