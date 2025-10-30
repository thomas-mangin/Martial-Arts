# Troubleshooting Guide

## Session State Issues

### session-context.md is missing or empty

**Symptoms:**
- `/resume` shows no previous context
- File doesn't exist or has no content

**Causes:**
- Fresh project start
- `/checkpoint` wasn't run at end of previous session
- File was accidentally deleted

**Solutions:**
1. Check if this is intentional fresh start
2. Ask user where they'd like to begin
3. Create new session-context.md with current status
4. Remind user to run `/checkpoint` at end of sessions

### session-context.md seems outdated

**Symptoms:**
- Context doesn't match recent work
- Dates are old
- Next steps don't make sense

**Causes:**
- `/checkpoint` wasn't run at end of previous session
- Work was done but not saved

**Solutions:**
1. Check git log for recent commits: `git log --oneline -10`
2. Check for uncommitted changes: `git status`
3. Review recent files modified: `ls -lt posts/ discussions/ | head -20`
4. Ask user what they were working on
5. Update session-context.md with accurate current state
6. Remind user to run `/checkpoint` regularly

## Topic Management Issues

### topics.md is missing or empty

**Symptoms:**
- No blog topics listed
- File doesn't exist

**Causes:**
- Fresh project start
- File was accidentally deleted

**Solutions:**
1. Create new topics.md with template structure
2. Ask user what topics they want to work on
3. Populate with initial ideas

### Current topic doesn't match actual work

**Symptoms:**
- Context says working on Topic A, but files show Topic B

**Causes:**
- topics.md wasn't updated when switching topics
- Work was exploratory and topic changed

**Solutions:**
1. Check recent files to determine actual current topic
2. Update topics.md to reflect reality
3. Update session-context.md for consistency

## File Organization Issues

### Posts in wrong directory

**Symptoms:**
- Blog posts in root directory instead of posts/
- Discussion notes not in discussions/

**Causes:**
- Files created manually without following structure
- Old workflow before directories existed

**Solutions:**
1. Move files to correct locations:
   - Blog posts → `posts/`
   - Discussion notes → `discussions/`
   - Session summaries → `sessions/`
2. Update topics.md references if needed
3. Commit changes: `/checkpoint`

### Can't find a file mentioned in context

**Symptoms:**
- session-context.md or topics.md references file that doesn't exist

**Causes:**
- File was renamed or moved
- File was deleted
- Reference was never created

**Solutions:**
1. Search for similar filenames: `find . -name "*[keyword]*"`
2. Check git history: `git log --all --full-history -- path/to/file`
3. Ask user if file still exists or was renamed
4. Update references to reflect current state

## Git Issues

### Uncommitted changes piling up

**Symptoms:**
- `git status` shows many uncommitted files
- Changes from multiple sessions not committed

**Causes:**
- `/checkpoint` not being run at end of sessions
- User forgot to save work

**Solutions:**
1. Review uncommitted changes: `git status` and `git diff`
2. Group related changes and commit incrementally
3. Use descriptive commit messages
4. Run `/checkpoint` to save current state

### Accidentally committed wrong files

**Symptoms:**
- Git history shows files that shouldn't be tracked
- Sensitive information in commits

**Causes:**
- Files not in .gitignore
- Bulk commit without review

**Solutions:**
1. For most recent commit: `git reset --soft HEAD~1` (undo commit, keep changes)
2. Remove sensitive files from staging: `git reset HEAD [file]`
3. Add files to .gitignore if needed
4. Recommit correctly
5. **Never force push** unless explicitly requested

### Want to undo last commit

**Symptoms:**
- User regrets last commit

**Solutions:**
1. Undo commit but keep changes: `git reset --soft HEAD~1`
2. Undo commit and discard changes: `git reset --hard HEAD~1` (⚠️ destructive)
3. Create new commit that reverses changes: `git revert HEAD`
4. Always prefer `--soft` unless user explicitly wants to discard

## Agent/Command Issues

### Agent taking too long

**Symptoms:**
- Agent seems stuck or unresponsive
- No progress updates

**Causes:**
- Agent reading large files
- Network issues (for /scan-sources, /youtube-fetch)
- Complex analysis taking time

**Solutions:**
1. Be patient - agents handle complex tasks internally
2. Check for error messages
3. If truly stuck, ask user if they want to cancel and try again
4. For network issues, retry after a moment

### Agent returned error

**Symptoms:**
- Agent failed to complete task
- Error message displayed

**Common Causes & Solutions:**

**File not found:**
- Check file path is correct
- Use `ls` or `find` to locate file
- Verify file actually exists

**Python script error (youtube-fetch):**
- Check if yt-dlp is installed: `yt-dlp --version`
- Check if video has captions available
- Try different video URL format

**Web fetch failed (scan-sources):**
- Blog may be temporarily down
- URL may have changed
- Network connectivity issue
- Try again later or verify URL

**Invalid input:**
- Check command syntax matches documentation
- Verify required parameters provided
- Check for typos in file paths

### Command not doing what expected

**Symptoms:**
- Output doesn't match documentation
- Unexpected behavior

**Solutions:**
1. Read command documentation: `.claude/docs/commands-reference.md`
2. Check command syntax in documentation
3. Verify input format is correct
4. Check if command implementation was recently updated
5. Ask user to clarify what they expected vs. what happened

## Content Quality Issues

### Review finding many issues

**Symptoms:**
- `/review-aikido` returns extensive list of problems
- Post quality seems low

**Causes:**
- First draft, not yet polished
- Rushed writing
- Not following blog-guidelines.md
- Technical inaccuracies

**Solutions:**
1. This is normal for first drafts - review is catching issues as designed
2. Address issues systematically:
   - Fix terminology first
   - Then technical accuracy
   - Then clarity and structure
3. Reference blog/blog-guidelines.md for standards
4. Reference research files for authenticity
5. Run `/review-aikido` again after revisions
6. Iterate until quality is acceptable

### Post doesn't match authentic voice

**Symptoms:**
- Review flags authenticity concerns
- Post sounds generic or contradicts core values

**Causes:**
- Not consulting research files before writing
- Trying to sound "professional" instead of genuine
- Not applying user's specific frameworks and beliefs

**Solutions:**
1. Read research/core-values.md to understand user's positions
2. Check research/divisive-topics.md if topic is controversial
3. Apply research/learning-journey.md frameworks where relevant
4. Rewrite sections to reflect genuine beliefs
5. Use specific examples from user's experience
6. Run `/review-aikido` again to verify authenticity

## Discussion/Extract Issues

### Discussion note seems incomplete

**Symptoms:**
- `/extract` reports insufficient material for blog post
- Discussion note is very short

**Causes:**
- Discussion was cut short
- Topic needs more exploration
- User didn't have much to say on topic

**Solutions:**
1. Run `/discuss` again to deepen exploration
2. Ask more specific questions about the topic
3. Look for related angles to explore
4. Consider if topic is actually blog-worthy
5. Combine with other related discussions

### Extract created draft with many gaps

**Symptoms:**
- Extracted blog draft has many [TK] or [EXPAND] markers
- Structure is thin

**Causes:**
- This is normal - extract creates initial structure
- Discussion provided insights but not full post content

**Solutions:**
1. This is expected behavior - extract is starting point
2. Fill gaps by:
   - Expanding on key points
   - Adding examples
   - Developing arguments
   - Including practical takeaways
3. Reference research files for additional material
4. Run `/review-aikido` after development

## Research File Issues

### Can't remember what research files exist

**Symptoms:**
- Unsure which research files to consult
- Need quick reference

**Solutions:**
1. Read research/INDEX.md for complete list
2. Key files:
   - core-values.md - Your beliefs and positions
   - divisive-topics.md - Controversial topics framework
   - learning-journey.md - Mastery progression framework
   - biomechanical-principles.md - Technical principles
3. Load specific files only when needed for current topic

### Research file seems outdated

**Symptoms:**
- Information doesn't match current beliefs
- User mentions beliefs have evolved

**Causes:**
- Views have naturally evolved over time
- New experiences led to refined understanding

**Solutions:**
1. Update the research file with current understanding
2. Log the evolution in decisions.md with date and rationale
3. Note if this affects any published posts (may need updates)
4. Use updated understanding going forward

## System Performance Issues

### /resume taking too long

**Symptoms:**
- Long wait when running /resume
- High token usage

**Causes:**
- This should be rare with new optimized structure
- May be reading too many detailed docs

**Solutions:**
1. Verify OVERVIEW.md is being loaded (not old CLAUDE.md)
2. Ensure agents are reading detailed docs internally
3. Check session-context.md isn't excessively long
4. Recent decisions in decisions.md should be limited to last 2-3

### Running out of context window

**Symptoms:**
- Token limit warnings
- Can't load necessary files

**Causes:**
- Very long blog posts or discussions
- Reading too many detailed documents at once

**Solutions:**
1. Work with one blog post at a time
2. Don't load detailed docs unless needed for current task
3. Keep session-context.md concise (current state only, not history)
4. Archive old content in sessions/ directory
5. Use agents to handle file reading internally

---

## Getting Help

If issues persist:
1. Check git log to understand recent changes: `git log --oneline -10`
2. Review recent session summaries in sessions/ directory
3. Check PROJECT-STATUS.md for high-level project state
4. Ask user for clarification on what they're trying to accomplish

---

*Read this file when encountering issues. Not loaded by default.*
