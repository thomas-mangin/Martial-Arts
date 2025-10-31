# Checkpoint Current Session

You are helping the user save their current session state so they can resume work later.

**IMPORTANT: This command should execute autonomously without asking questions. Generate commit messages, infer decisions from work done, and create session summaries automatically.**

## Steps to Execute

1. **Check Git Status**
   - Run `git status` to see what files have changed
   - Note any untracked or modified files

2. **Commit Changes Automatically**
   - If there are uncommitted changes:
     - Analyze the changed files to understand what was done
     - Generate a descriptive commit message based on the changes (look at file names, git diff summary)
     - Stage and commit all changes with the generated message
     - Show user what was committed
   - If no changes, note that everything is already committed

3. **Save Critical State** (Crash Recovery)
   - Check if `.claude/state/current-objective.md` exists and has content
   - If it has a real objective (not template), preserve it in session summary
   - Check if `.claude/state/backlog.md` has active tasks
   - If backlog has tasks, note them in session summary
   - This ensures no work is lost if Claude crashes or restarts

4. **Session Context Already Updated**
   - Assume `session-context.md` was updated during the session
   - Do NOT ask user to update it again
   - Just note that context will be saved in session summary

5. **Topics File**
   - Assume `topics.md` is current
   - Do NOT ask for updates
   - Will be reflected in session summary if changed

6. **Infer Decisions Automatically**
   - Look at conversation history and files changed
   - If major architectural changes, new systems created, or significant choices made:
     - Add decision to `decisions.md` automatically
     - Include date, decision, and rationale based on work done
   - Do NOT ask user if decisions were made - infer from context

7. **Create Session Summary Automatically**
   - Generate timestamped session summary in `sessions/` directory
   - Filename: `session-YYYY-MM-DD-HHMM.md` (use current timestamp)
   - **Analyze the session automatically**:
     - Review conversation history for main focus and accomplishments
     - Look at git diff / changed files for technical work done
     - Identify key decisions from major changes
     - Note any challenges or blockers mentioned
     - Extract next steps from context
   - **Include in summary**:
     - Session Date & Time
     - Duration (approximate from conversation length)
     - Main Focus (infer from work done)
     - Accomplishments (bullet list from files changed + conversation)
     - Key Decisions (reference decisions.md if updated)
     - Challenges/Issues (if any mentioned)
     - Conversation Highlights (key exchanges)
     - Files Modified (from git status/diff)
     - Next Steps (from session-context.md or infer)
     - Notes (any other relevant context)
   - Write summary automatically - no user input needed

8. **Push to GitHub**
   - Check if git remote is configured: `git remote -v`
   - If remote exists, push to GitHub: `git push origin main`
   - If push succeeds, confirm to user
   - If push fails (e.g., no remote, authentication issues), inform user but don't block checkpoint completion

9. **Summary**
   - Show a brief summary of what was checkpointed
   - Mention the session summary file that was created
   - Confirm push to GitHub (if successful)
   - Remind them to use `/resume` when starting their next session

## Important Notes
- **Execute autonomously** - no questions, just do the checkpoint
- **Infer don't ask** - generate commit messages, identify decisions, create summaries automatically
- **Analyze the session** - review conversation and file changes to understand what happened
- Commits are made locally and then pushed to GitHub
- If push fails, inform user but complete checkpoint anyway
- Be efficient - this should take 30-60 seconds total
- **Note**: Detailed documentation is in `.claude/docs/` and loaded by agents on-demand
- session-context.md should only contain current session state, not full documentation

## Commit Message Generation Guidelines
- Look at changed files to understand the work
- Use descriptive messages that explain what changed and why
- Format: "Action: brief description\n\nDetails if needed"
- Examples:
  - "Update session context after blog post writing"
  - "Add new discussion notes for relaxation topic"
  - "Refactor documentation for better organization"
  - "Create first blog post draft on irimi principle"
