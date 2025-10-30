# Checkpoint Current Session

You are helping the user save their current session state so they can resume work later.

## Steps to Execute

1. **Check Git Status**
   - Run `git status` to see what files have changed
   - List any untracked or modified files

2. **Commit Changes**
   - If there are uncommitted changes:
     - Show the user what changed (git diff summary)
     - Ask what commit message they want or suggest one based on the changes
     - Stage and commit all changes to the local git repo
     - DO NOT push to remote
   - If no changes, note that everything is already committed

3. **Update Session Context**
   - Read `session-context.md`
   - Ask the user:
     - What's the current status? (what they just finished/are working on)
     - What should be the next steps?
     - Are there any blockers or questions to note?
   - Update the session-context.md file with:
     - Current timestamp
     - Updated status, recent work, and next steps
     - Any blockers or notes

4. **Review Topics**
   - Read `topics.md`
   - Ask if they want to:
     - Update the current topic
     - Add any new topic ideas
     - Move current topic to completed if finished
   - Update topics.md if needed

5. **Log Decisions** (if any were made)
   - Ask if any important decisions were made this session
   - If yes, append to `decisions.md` with date, decision, and rationale

6. **Create Session Summary**
   - Generate a timestamped session summary file in `sessions/` directory
   - Filename format: `session-YYYY-MM-DD-HHMM.md` (e.g., `session-2025-10-30-0145.md`)
   - Include in the summary:
     - **Session Date & Time**: When the session occurred
     - **Duration**: Approximate session length based on conversation
     - **Main Focus**: What was the primary work/topic
     - **Accomplishments**: Bullet list of what was completed
     - **Key Decisions**: Any important decisions made (reference decisions.md)
     - **Challenges/Issues**: Problems encountered or unresolved questions
     - **Conversation Highlights**: Brief summary of key interactions/discussions
     - **Files Modified**: List of files created or changed
     - **Next Steps**: What to do in the next session
     - **Notes**: Any other relevant context
   - Write this summary file automatically (don't ask user to write it)
   - Base the summary on the conversation that happened during the session
   - Use the Write tool to create the file in sessions/

7. **Summary**
   - Show a brief summary of what was checkpointed
   - Mention the session summary file that was created
   - Remind them to use `/resume` when starting their next session

## Important Notes
- Be conversational but efficient
- Only commit to local git, never push
- Keep the session-context.md concise and actionable
- The goal is quick context saving, not extensive documentation
