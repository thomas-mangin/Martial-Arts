# How to Use Your Aikido Blog Workflow System

Welcome! This guide explains how to use the blog writing and session continuity system that's been set up for your MA thesis project.

---

## Quick Start Guide

### Starting a Work Session

1. **Open Claude Code** in this directory
2. **Type `/resume`** - This will:
   - Show you where you left off
   - Display your current topic and next steps
   - Remind you of the workflow
   - Help you get back into context immediately

### During Your Work Session

1. **Writing a new blog post:**
   ```bash
   # Copy the template
   cp blog-template.md posts/my-topic-2025-10-30.md

   # Edit the file with your content
   # Follow the structure in blog-guidelines.md
   ```

2. **As you work:**
   - Add new topic ideas to `topics.md` as they come to you
   - Keep notes in `session-context.md` if needed
   - Log any important decisions in `decisions.md`

3. **Before finishing a post:**
   ```bash
   /review-aikido posts/my-topic-2025-10-30.md
   ```
   - This reviews your post for quality
   - Checks terminology, accuracy, clarity, structure
   - Gives you specific feedback for improvements

### Ending a Work Session

1. **Type `/checkpoint`** - This will:
   - Commit your changes to git (local only, no remote push)
   - Update your session context
   - Save your progress
   - Prepare everything for next time

---

## File Structure Overview

### Files You'll Edit Regularly:

**topics.md**
- Where you track blog topics
- Add ideas here as they come
- Mark what you're currently working on
- Archive completed topics

**session-context.md**
- Your current status and next steps
- Gets updated automatically by /checkpoint
- You can also edit manually to add notes

**posts/[your-blog-post].md**
- Your actual blog posts
- Copy from blog-template.md to start
- Follow structure in blog-guidelines.md

**decisions.md**
- Important decisions you make
- Why you chose certain approaches
- Reference for later

**sessions/[timestamped].md**
- Automatic session summaries created by /checkpoint
- Historical record of each work session
- Review at a glance what was accomplished
- Search across sessions to find topics or decisions

### Reference Files (Read, Don't Usually Edit):

**blog-template.md**
- Template for new posts
- Copy this file to start writing
- Don't edit the original

**blog-guidelines.md**
- Complete writing guide
- Structure recommendations
- Content quality standards
- Refer to this when writing

**help.md**
- This file!
- Your user guide

**.claude/claude.md**
- Documentation for Claude Code
- Helps AI understand your system
- You don't need to read this

---

## The Essential Commands

### `/resume` - Start Your Session
**When**: Beginning of every work session
**What it does**:
- Loads your previous session context
- Shows current topic and next steps
- Displays recent decisions
- Checks git status
- Gets you oriented quickly

**Example output**:
```
📍 Current Status: Writing blog post about irimi principle
📝 Recent Work: Completed draft introduction and first section
⏭️  Next Steps:
   1. Write practical takeaways section
   2. Review with /review-aikido
   3. Revise based on feedback
```

### `/checkpoint` - Save Your Session
**When**: End of every work session
**What it does**:
- Commits changes to local git
- Updates session-context.md
- Reviews topics.md
- Logs decisions
- **Creates timestamped session summary** in sessions/ folder
- Saves your complete state

**You'll be asked**:
- What commit message to use (or accept suggested one)
- Current status update
- What your next steps should be
- Any blockers or questions
- Any decisions to log

**Session Summary**:
Each checkpoint automatically creates a file like `sessions/session-2025-10-30-0145.md` containing:
- What was accomplished this session
- Key interactions and discussions
- Decisions made
- Files modified
- Next steps

This creates a historical record you can review later!

### `/review-aikido` - Review Your Post
**When**: After drafting a blog post
**What it does**:
- Checks Aikido terminology and spelling
- Verifies technical accuracy
- Assesses clarity and readability
- Evaluates structure
- Provides actionable feedback

**Usage**:
```bash
/review-aikido posts/principle-of-irimi-2025-10-30.md
```

### `/discuss` - Explore Topic Through Conversation
**When**: When you want to explore an Aikido topic informally before writing
**What it does**:
- Has conversational dialogue about the topic
- Asks probing questions to deepen thinking
- Extracts key insights from your responses
- Creates structured discussion notes
- Identifies blog-worthy ideas
- Records decisions and questions

**Usage**:
```bash
/discuss irimi-principle
```

**Benefits**:
- Think through ideas before committing to draft
- Capture authentic insights in your voice
- Explore freely without pressure to be polished
- Create raw material for blog posts

### `/extract` - Transform Discussion into Blog Draft
**When**: After a discussion, when ready to create a blog post
**What it does**:
- Reads your discussion notes
- Pulls out key insights and examples
- Creates structured blog post draft
- Identifies gaps that need filling
- Provides starting point for refinement

**Usage**:
```bash
/extract discussions/irimi-principle-2025-10-30.md
```

**Result**: Initial blog draft in posts/ ready for development and review

### `/track-source` - Register Martial Arts Bloggers
**When**: When you discover a blogger worth monitoring
**What it does**:
- Creates profile for a martial arts blogger
- Records their URL, discipline, focus areas
- Tracks scan history
- Maintains source registry

**Usage**:
```bash
/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"
```

**Benefits**:
- Monitor other martial artists' content
- Find inspiration from the community
- Identify response opportunities
- Build cross-discipline insights

### `/scan-sources` - Monitor Blogger Content
**When**: Regularly (weekly/bi-weekly) to find new content
**What it does**:
- Fetches recent posts from tracked bloggers
- Identifies new content since last scan
- Analyzes posts for key arguments and ideas
- Generates blog topic ideas
- Creates findings report

**Usage**:
```bash
/scan-sources              # Scan all tracked sources
/scan-sources leo-tamaki   # Scan specific source
```

**Result**: Findings report in sources/findings/ with blog ideas, response opportunities, and discussion prompts

---

## Complete Blog Writing Workflow

You have three approaches for creating blog posts:

### Approach A: Discussion-Based (Recommended)
Start with informal exploration, then extract to draft

**1. Start Session**
```bash
/resume
```

**2. Explore Topic Through Discussion**
```bash
/discuss irimi-principle
```
- Have natural conversation about the topic
- Answer probing questions
- Share experiences and insights
- Discussion note saved automatically in discussions/

**3. Extract to Blog Draft**
```bash
/extract discussions/irimi-principle-2025-10-30.md
```
- Creates initial draft in posts/
- Structures your insights from discussion
- Identifies gaps to fill

**4. Develop Draft**
- Expand thin sections
- Add missing details
- Refine language and flow
- Fill identified gaps

**5. Review & Iterate**
```bash
/review-aikido posts/irimi-principle-2025-10-30.md
```
- Get critical feedback
- Revise based on feedback
- Re-review until MA-level quality

**6. Finalize**
- Update topics.md (mark complete)
- Run /checkpoint

### Approach B: Direct Writing
Write directly from template

**1. Start Session**
```bash
/resume
```

**2. Choose/Add Topic**
- Edit `topics.md`
- Add new ideas to "Topic Ideas" section
- Move one to "Current Topic" section

**3. Create New Post**
```bash
cp blog-template.md posts/principle-of-irimi-2025-10-30.md
```
Naming convention: `[topic-slug]-YYYY-MM-DD.md`

**4. Write Your Post**
- Open `blog-guidelines.md` for reference
- Fill in the template sections
- Aim for 800-1200 words
- Use clear structure:
  - Introduction (100-200 words)
  - Main content (2-4 sections)
  - Practical takeaways (3-5 points)
  - Conclusion (100-150 words)

**5. Review Your Post**
```bash
/review-aikido posts/principle-of-irimi-2025-10-30.md
```
- Read the feedback carefully
- Note any errors or improvements needed

**6. Revise**
- Make improvements based on review
- Check Japanese terminology
- Verify any facts
- Improve clarity where needed

**7. Optional: Review Again**
If you made significant changes:
```bash
/review-aikido posts/principle-of-irimi-2025-10-30.md
```

**8. Finalize**
- Update `topics.md`:
  - Clear "Current Topic"
  - Move topic to "Completed Topics"
- Add completion note to `session-context.md` if desired

**9. End Session**
```bash
/checkpoint
```

### Approach C: Source-Inspired
Discover ideas from other martial arts bloggers

**1. Track Sources**
```bash
/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"
```
- Add martial arts bloggers to monitor
- Can be from any discipline (Aikido, Karate, etc.)

**2. Scan for Content**
```bash
/scan-sources
```
- Check tracked blogs for new posts
- Analyze content for key ideas
- Generate blog topic ideas
- Create findings report

**3. Review Findings**
- Read sources/findings/[report].md
- Identify interesting ideas or response opportunities
- Note which ideas resonate

**4. Explore or Write**

**Option A: Explore through discussion first**:
```bash
/discuss [idea from findings]
```
Then extract to blog draft

**Option B: Write response directly**:
```bash
cp blog-template.md posts/response-to-[topic].md
```
Write your perspective

**5. Review & Iterate**
```bash
/review-aikido posts/[file].md
```
- Get critical feedback
- Revise until excellent

**6. Finalize**
- Update topics.md
- Run /checkpoint

---

## Topics Management

### topics.md Structure

```markdown
## Current Topic
The one you're actively writing about

## Next Topics Queue
Priority-ordered list of what to write next

## Topic Ideas
Brainstorming space for future posts

## Completed Topics
Archive of finished posts
```

### Adding a Topic Idea
Just edit `topics.md` and add to the "Topic Ideas" section:
```markdown
## Topic Ideas
- The role of ma-ai in Aikido practice
- Understanding musubi (connection)
- Training solo vs. with partners
```

### Starting a New Topic
Move from ideas to "Current Topic":
```markdown
## Current Topic
The role of ma-ai in Aikido practice
```

---

## Session Context Management

### What is session-context.md?

It's your checkpoint file that maintains continuity between work sessions. Think of it as your "save game" file.

### Key Sections:

**Current Status**: What you're working on right now
**Recent Work**: What you accomplished (updated by /checkpoint)
**Next Steps**: What to do next (helps you resume quickly)
**Blockers/Questions**: Anything preventing progress
**Notes**: Additional context

### Manual Updates

You can edit this file anytime to add notes:
```markdown
## Notes
- Need to research O-Sensei's writings on irimi
- Found good video demonstration to reference
- Consider adding diagram of footwork
```

---

## Decision Logging

### When to Log a Decision

Log decisions when you:
- Choose a particular approach or structure
- Decide on terminology conventions
- Make commitments about posting schedule
- Set standards or guidelines
- Choose tools or methods

### Format

```markdown
## 2025-10-30

### [Decision Title]
**Decision**: What you decided
**Rationale**: Why you made this choice
**Impact**: What this means going forward (optional)
```

### Example

```markdown
## 2025-10-30

### Blog Post Length Standard
**Decision**: Target 800-1200 words per post, with flexibility for complex topics
**Rationale**: Long enough for depth, short enough to maintain reader attention
**Impact**: Will guide scope of topics chosen
```

---

## Git Workflow

### Important: Local Only

- All commits stay on your local machine
- Nothing gets pushed to remote servers
- `/checkpoint` handles commits automatically
- You're safe to experiment and revise

### Manual Git Commands

You can still use git normally:
```bash
# Check status
git status

# See what changed
git diff

# View commit history
git log --oneline

# Create a branch if needed
git checkout -b experimental-post
```

### If You Want to Push

If you decide to push to a remote:
```bash
# Add remote (one time)
git remote add origin <your-repo-url>

# Push when ready
git push -u origin main
```

But `/checkpoint` will never push automatically - you control this.

---

## Tips and Best Practices

### Daily Workflow

**Start of day:**
1. `/resume` to orient yourself
2. Review next steps
3. Start working

**During work:**
- Focus on one post at a time
- Add topic ideas as they occur
- Use blog-guidelines.md as reference
- Review frequently

**End of day:**
1. `/checkpoint` to save state
2. Everything is committed and ready for next time

### Writing Tips

**Quality over quantity:**
- Better to write one great post than three mediocre ones
- Use `/review-aikido` liberally
- Revise based on feedback

**Stay organized:**
- Keep topics.md updated
- Clear notes in session-context.md
- One post at a time in "Current Topic"

**Reference guidelines:**
- `blog-guidelines.md` has everything you need
- Covers structure, tone, terminology
- Common pitfalls to avoid

### Managing Topics

**Capture ideas immediately:**
- When inspiration strikes, add to topics.md
- Don't worry about perfect wording
- Refine later when you choose the topic

**Prioritize in queue:**
- Most important/urgent at top
- Less urgent below
- Rearrange as priorities shift

**Archive completed:**
- Move finished posts to "Completed Topics"
- Include date for reference
- Keeps active list clean

---

## Troubleshooting

### "I forgot to use /checkpoint"

No problem! Your files are still there. Just:
1. Manually commit if needed: `git add . && git commit -m "Your message"`
2. Update session-context.md with where you left off
3. Use `/checkpoint` next time

### "What was I working on?"

1. `/resume` will show you
2. Check `session-context.md` for latest status
3. Check `topics.md` for current topic
4. Check `git log` for recent commits

### "I made changes but don't want to commit them"

```bash
# See what changed
git status

# Discard changes to specific file
git checkout -- filename.md

# Or stash changes for later
git stash
```

### "I want to start over on a post"

```bash
# If not committed yet
git checkout -- posts/my-post.md

# If already committed
git log  # find the commit before you started
git checkout <commit-hash> -- posts/my-post.md
```

### "Claude doesn't remember our last session"

This is normal! Claude Code starts fresh each session. That's why we have:
- `/resume` command to load context
- `session-context.md` to track state
- `.claude/claude.md` for Claude to understand the system

The files maintain continuity, not the AI's memory.

---

## Command Reference

### Essential Commands

| Command | When | Purpose |
|---------|------|---------|
| `/resume` | Start of session | Load context, see next steps |
| `/checkpoint` | End of session | Save state, commit changes |
| `/review-aikido <file>` | After drafting | Review post quality |

### File Commands

```bash
# Create new post from template
cp blog-template.md posts/new-topic-2025-10-30.md

# List all posts
ls posts/

# See recent changes
git diff

# View a specific post
cat posts/my-post.md
```

---

## File Quick Reference

### Files to Edit
- `topics.md` - Your topic pipeline
- `session-context.md` - Current status and notes
- `decisions.md` - Important choices
- `posts/*.md` - Your blog posts

### Files to Reference
- `blog-template.md` - Copy this for new posts
- `blog-guidelines.md` - Writing guide
- `help.md` - This guide

### System Files
- `.claude/claude.md` - Claude's documentation
- `.claude/commands/*.md` - Command definitions

---

## Getting Help

### Within the System

1. **Read this file** (`help.md`)
2. **Check blog-guidelines.md** for writing questions
3. **Ask Claude** - Just ask your question in the chat

### Common Questions

**"What should I write about?"**
- Check topics.md for ideas
- Ask Claude to brainstorm based on your interests
- Think about your Aikido experience and insights

**"How long should my post be?"**
- Target: 800-1200 words
- Minimum: 600 words
- Maximum: 2000 words (only if needed)

**"How do I know if my post is good?"**
- Use `/review-aikido` to get feedback
- Check against blog-guidelines.md
- Read it aloud to yourself
- Does it provide value to readers?

**"Can I change the template?"**
- Yes! It's a starting point
- Adapt sections to your topic
- Keep the general structure (intro, body, conclusion)

**"What if I want to work on multiple posts?"**
- Focus on one at a time in "Current Topic"
- Keep others in "Next Topics Queue"
- You can draft multiple, but complete one before moving on

---

## Your Workflow at a Glance

```
START → /resume → [Review context]
   ↓
WORK  → Edit topics.md (if needed)
   ↓      Copy template → Write post → /review-aikido
   ↓      Revise → Finalize → Update topics.md
   ↓
END   → /checkpoint → [Commits & saves]
   ↓
DONE! Ready for next session
```

---

## Remember

✅ **Do:**
- Use `/resume` at start of every session
- Use `/checkpoint` at end of every session
- Reference blog-guidelines.md when writing
- Review posts with `/review-aikido` before finalizing
- Keep topics.md updated
- Log important decisions

❌ **Don't:**
- Edit blog-template.md (copy it instead)
- Push to remote without intending to
- Work on multiple posts simultaneously
- Skip the review step
- Forget to checkpoint

---

## Next Steps

Ready to start? Here's what to do:

1. **Run `/checkpoint` now** to commit this initial setup
2. **Add some topic ideas** to topics.md
3. **Choose your first topic** and start writing
4. **Follow the workflow** outlined above

Happy writing! 🥋

---

*Need to update this guide? Edit `/Users/thomas/MA/help.md`*
*Last updated: 2025-10-30*
