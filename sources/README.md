# Source Tracking and Content Monitoring

This directory contains the system for tracking martial arts bloggers and monitoring their content for inspiration, response, and engagement.

## Purpose

The source tracking system enables you to:
- **Track martial arts bloggers** from any discipline (Aikido, Karate, etc.)
- **Monitor their content** for new posts and updates
- **Extract key ideas** that could inspire your own blog posts
- **Identify points** worthy of response or alternative perspectives
- **Generate blog ideas** from their content
- **Build dialogue** with the broader martial arts community

## Directory Structure

```
sources/
├── registry/              # Tracked bloggers and their information
│   ├── leo-tamaki.md     # Example: Aikido blogger
│   └── lionel-froidure.md # Example: Karate blogger
├── findings/              # Content analysis and ideas extracted
│   ├── 2025-10-30/       # Findings organized by date
│   └── [topic-based]/    # Or organized by topic
└── README.md             # This file
```

## Commands

### `/track-source` - Register a Blogger
Add or update a martial arts blogger to track

**Usage**:
```bash
/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"
```

**What it creates**:
- Source profile in `sources/registry/[name].md`
- Includes: name, URL, discipline, focus areas, notes
- Tracks last scanned date
- Maintains content history

### `/scan-sources` - Monitor for New Content
Check tracked sources for new posts and analyze them

**Usage**:
```bash
/scan-sources               # Scan all sources
/scan-sources leo-tamaki    # Scan specific source
```

**What it does**:
1. Fetches recent content from tracked blogs
2. Identifies new posts since last scan
3. Analyzes content for:
   - Key arguments and points made
   - Ideas worth exploring
   - Claims that invite response or alternative perspectives
   - Topics that resonate with your interests
4. Creates findings report with:
   - Summary of new content
   - Extractable ideas for your blog
   - Discussion prompts
   - Response opportunities

**What it creates**:
- Findings report in `sources/findings/YYYY-MM-DD-[source-name].md`
- Updates source registry with last scan date
- Optionally adds ideas to topics.md

## Workflow

### 1. Track Sources
```bash
# Add martial artists you want to follow
/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"
/track-source "Lionel Froidure" "https://imaginarts.com" "Karate"
```

### 2. Scan Regularly
```bash
# Check for new content (weekly or when starting a session)
/scan-sources
```

### 3. Review Findings
- Read the findings report in `sources/findings/`
- Identify interesting ideas or points

### 4. Develop Content
Based on findings, you can:

**A) Discuss an idea you found**:
```bash
/discuss [idea from findings]
# Explore the idea from your perspective
```

**B) Create response post directly**:
```bash
cp blog-template.md posts/response-to-[topic].md
# Write your response or alternative perspective
```

**C) Add to topic ideas**:
- Add promising ideas to `topics.md` for later

## Source Registry Format

Each tracked source has a profile:

```markdown
# [Blogger Name]

**URL**: [Blog URL]
**Discipline**: [Aikido/Karate/etc.]
**Language**: [English/French/etc.]
**Status**: Active/Inactive

## Focus Areas
- [Primary topics they write about]
- [Teaching, philosophy, technique, etc.]

## Notes
- [Why you're tracking them]
- [What makes their perspective valuable]
- [Connection to your work]

## Content Tracking

**Last Scanned**: YYYY-MM-DD
**Total Posts Reviewed**: X
**Ideas Generated**: Y

### Recent Posts
| Date | Title | Analyzed | Ideas Generated |
|------|-------|----------|-----------------|
| YYYY-MM-DD | Post title | Yes | 2 |
```

## Findings Report Format

Each scan creates a findings report:

```markdown
# Content Findings: [Source Name] - YYYY-MM-DD

**Source**: [Name]
**URL**: [Blog URL]
**Scan Date**: YYYY-MM-DD
**New Posts Found**: X

---

## Post 1: [Title]

**URL**: [Post URL]
**Published**: [Date if available]

### Summary
[Brief summary of the post's main points]

### Key Arguments/Points
1. [Main argument 1]
2. [Main argument 2]
3. [Main argument 3]

### Potential Blog Ideas

**Idea 1: [Title of potential post]**
- **Type**: Response / Alternative Perspective / Inspired Exploration / Extension
- **Angle**: [How you'd approach it]
- **Connection**: [How it relates to the source post]
- **Your Perspective**: [Initial thoughts on what you'd say]

**Idea 2: [Title of potential post]**
...

### Response Opportunities
- [Points you could respond to]
- [Alternative perspectives you could offer]
- [Questions their post raises]

### Discussion Prompts
If you want to explore through /discuss:
- "[Prompt based on their content]"
- "[Question they raised]"

---

## Post 2: [Title]
[Repeat format]

---

## Actions Recommended

### Immediate
- [ ] Discuss: [Topic that seems most promising]
- [ ] Respond to: [Point that invites response]

### Add to Topics
- [ ] [Idea 1 - add to topics.md]
- [ ] [Idea 2 - add to topics.md]

### Further Research
- [ ] [Topic needing more investigation]

---

*Next scan recommended: [Date]*
```

## Use Cases

### 1. Finding Inspiration
Scan sources when you're looking for blog topic ideas
- "What are other martial artists writing about?"
- "What conversations are happening?"
- "What topics are relevant right now?"

### 2. Engaging in Dialogue
Respond to points made by other bloggers
- "They said X, but I think Y because..."
- "Building on their idea about Z..."
- "An alternative perspective on their argument..."

### 3. Comparative Analysis
Explore how different disciplines approach similar concepts
- Aikido vs. Karate perspectives on distance
- Different interpretations of similar principles
- Cross-discipline insights

### 4. Community Connection
Stay connected to broader martial arts discourse
- Know what topics are being discussed
- Contribute to ongoing conversations
- Build relationships with other practitioners

### 5. Quality Control
Learn from others' writing
- What works well in their posts?
- What structure do they use?
- How do they explain complex ideas?

## Integration with Your Workflow

### Discovery → Discussion → Blog

```bash
# 1. Find content
/scan-sources

# 2. Review findings
cat sources/findings/2025-10-30-leo-tamaki.md

# 3. Explore interesting idea
/discuss "irimi-timing-inspired-by-tamaki"

# 4. Extract to blog
/extract discussions/[file].md

# 5. Review
/review-aikido posts/[file].md

# 6. Publish
/checkpoint
```

### Direct Response

```bash
# 1. Find content
/scan-sources

# 2. Identify point to respond to
# Review findings report

# 3. Write response
cp blog-template.md posts/response-to-tamaki-on-timing.md

# 4. Review
/review-aikido posts/response-to-tamaki-on-timing.md

# 5. Publish
/checkpoint
```

## Best Practices

### Tracking Sources
- **Quality over quantity**: Track bloggers whose work genuinely interests you
- **Diverse perspectives**: Include different disciplines and viewpoints
- **Active blogs**: Focus on sources that post regularly
- **Accessible**: Prioritize blogs in languages you read

### Scanning
- **Regular rhythm**: Scan weekly or bi-weekly
- **Don't over-scan**: Too frequent scanning creates noise
- **Be selective**: Not every post needs deep analysis
- **Take notes**: Add personal reactions in findings

### Using Findings
- **Don't just copy**: Use as inspiration, not source material
- **Credit when appropriate**: Reference source if responding directly
- **Add your value**: What unique perspective do you bring?
- **Be respectful**: Even when disagreeing, maintain respect

### Ethical Considerations
- **Attribution**: Credit ideas when appropriate
- **Fair use**: Don't copy content, create original work
- **Respectful engagement**: Disagreement is fine, but be respectful
- **Add value**: Don't just summarize, add your perspective

## Tips

### Finding Good Sources
- Ask fellow practitioners for recommendations
- Look for bloggers cited by others
- Search for martial arts aggregators
- Follow social media recommendations

### Efficient Scanning
- Use /scan-sources at regular intervals
- Skim findings reports quickly
- Mark most interesting for deep reading
- Don't feel obligated to respond to everything

### Generating Ideas
- Look for gaps in their arguments
- Notice what they didn't mention
- Consider alternative interpretations
- Think about cross-discipline connections
- Question assumptions

## Search and Discovery

Find past findings:

```bash
# Search for topic across all findings
grep -r "ma-ai" sources/findings/

# List recent findings
ls -lt sources/findings/*.md | head -5

# Find findings from specific source
ls sources/findings/*leo-tamaki*.md

# Count total findings
ls sources/findings/*.md | wc -l
```

## Maintenance

### Regular Tasks
- Scan sources weekly
- Review findings reports
- Update source profiles when needed
- Mark inactive sources
- Add new sources as discovered

### Archive
- Keep findings indefinitely (they may inspire later posts)
- Update source last-scanned dates
- Track which findings led to blog posts

---

*This system helps you stay connected to the broader martial arts community while generating authentic content inspired by ongoing conversations.*
