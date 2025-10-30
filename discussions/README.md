# Discussion Notes

This directory contains structured notes from informal discussions about Aikido topics. These discussions serve as raw material for blog posts.

## Purpose

Discussion notes capture:
- **Informal explorations** of Aikido concepts and experiences
- **Key insights** that emerge through conversation
- **Questions and answers** that deepen understanding
- **Decisions** about approaches and interpretations
- **Raw ideas** that can be refined into blog posts

## Workflow

### 1. Capture Discussions
```
/discuss [topic-name]
```
- Have an informal conversation about an Aikido topic
- System asks probing questions
- Extracts key insights and structures them
- Creates a discussion note file

### 2. Review and Refine
- Read through discussion notes
- Add additional thoughts
- Identify which insights are blog-worthy

### 3. Extract to Blog Post
```
/extract discussions/topic-name-YYYY-MM-DD.md
```
- Pulls key ideas from discussion
- Creates initial blog post draft
- Structures insights into blog format
- References original discussion for context

## File Naming

Format: `topic-name-YYYY-MM-DD.md`

Examples:
- `irimi-principle-2025-10-30.md`
- `ukemi-and-learning-2025-10-31.md`
- `training-mindset-2025-11-01.md`

## Discussion Note Structure

Each discussion note includes:
- **Topic & Date**: What was discussed and when
- **Initial Questions**: What prompted the discussion
- **Key Insights**: Main points that emerged
- **Examples & Stories**: Concrete illustrations
- **Decisions Made**: Any conclusions or commitments
- **Questions Remaining**: Unresolved areas for further exploration
- **Blog Potential**: Which ideas could become posts
- **Related Topics**: Connections to other discussions

## Benefits

### For Thinking
- **Explore freely** without pressure to be polished
- **Ask questions** and work through understanding
- **Make connections** between different aspects of Aikido
- **Think out loud** and capture the process

### For Writing
- **Raw material** ready to be refined into posts
- **Authentic voice** captured in natural conversation
- **Depth of insight** from thorough exploration
- **Multiple angles** on topics for richer content

### For Progress
- **Track evolution** of understanding over time
- **Revisit ideas** that weren't ready initially
- **Connect discussions** to see patterns and themes
- **Build knowledge base** of personal Aikido insights

## Search and Discovery

Find specific topics or insights:

```bash
# Search for a concept across all discussions
grep -r "ma-ai" discussions/

# List discussions by date
ls -lt discussions/*.md

# Count total discussions
ls discussions/*.md | wc -l

# Find discussions mentioning specific technique
grep -l "ikkyo" discussions/*.md
```

## From Discussion to Blog Post

**Typical Path**:
1. `/discuss irimi-principle` → Have conversation
2. Review `discussions/irimi-principle-2025-10-30.md`
3. Add topic to `topics.md` if promising
4. `/extract discussions/irimi-principle-2025-10-30.md` → Generate draft
5. Refine draft in `posts/`
6. `/review-aikido posts/irimi-principle-2025-10-30.md`
7. Iterate to excellence

## Discussion Types

### Concept Exploration
Deep dive into an Aikido principle or concept
- What does it mean?
- How does it work in practice?
- Why does it matter?
- What are common misunderstandings?

### Experience Reflection
Processing a training experience or breakthrough
- What happened?
- What did you learn?
- How did it change your understanding?
- What questions remain?

### Technical Analysis
Breaking down a technique or movement
- How is it performed?
- What are the key principles?
- What are common mistakes?
- How does it connect to other techniques?

### Philosophical Inquiry
Exploring Aikido philosophy and values
- What is the underlying principle?
- How does it apply beyond the mat?
- What does it reveal about Aikido's nature?
- How does it connect to O-Sensei's vision?

## Tips for Productive Discussions

### Be Honest
- Share genuine questions and uncertainties
- Admit what you don't understand
- Express tentative ideas freely

### Go Deep
- Don't settle for surface explanations
- Ask "why" multiple times
- Explore implications and connections
- Challenge your own assumptions

### Stay Concrete
- Use specific examples from your training
- Reference particular experiences
- Name techniques and situations
- Ground abstractions in reality

### Capture Everything
- Even "obvious" insights may be valuable later
- Questions can become blog hooks
- Tangents might reveal connections
- Uncertainty shows authentic exploration

## Archive and Organization

### Active Discussions
Keep recent discussions easily accessible for reference

### Extracted Discussions
Mark discussions that have been turned into blog posts:
- Add `[EXTRACTED → post-name.md]` at the top
- Keep original discussion for reference
- Link blog post back to discussion

### Evergreen Discussions
Some discussions may feed multiple blog posts or be revisited over time

---

*Discussion notes are part of your creative process. They don't need to be perfect - they need to be honest and exploratory.*
