# YouTube Channel Analysis Agent

**Purpose**: Comprehensive analysis of YouTube channel transcripts to identify themes, teaching approaches, and blog post ideas.

**When to Use**: After downloading transcripts from a YouTube channel, use this agent to analyze the content systematically and create channel summary reports.

---

## Agent Capabilities

This agent analyzes YouTube channel transcripts to:
1. Identify major cross-video themes and teaching approaches
2. Document instructor's unique perspectives and style
3. Generate prioritized blog post ideas
4. Create comprehensive channel summary report
5. Update channel registry with analysis findings

---

## Usage

**Command**: `/analyze-youtube-channel <channel_name>`

**Examples**:
```bash
/analyze-youtube-channel tony-sargeant
/analyze-youtube-channel alexander-gent
/analyze-youtube-channel heins-approach
```

**Parameters**:
- `channel_name`: Registry name (e.g., "tony-sargeant", "heins-approach")
- Agent will automatically find transcripts and registry files

---

## What This Agent Does

### Phase 1: Discovery (5-10 minutes)
1. **Locate transcripts**: Find all transcript files for the channel
2. **Read registry**: Load existing channel information
3. **Sample assessment**: Read 5-10 representative transcripts to understand content style
4. **Count statistics**: Total videos, transcript availability, date ranges

### Phase 2: Theme Identification (15-25 minutes)
5. **Keyword search**: Grep across all transcripts for major Aikido concepts
6. **Pattern analysis**: Identify recurring topics across multiple videos
7. **Teaching style**: Analyze how instructor presents concepts (technical, philosophical, practical, etc.)
8. **Unique perspectives**: What makes this instructor different from others?

### Phase 3: Representative Sampling (20-40 minutes)
9. **Theme-based sampling**: For each major theme, read 3-5 representative video transcripts
10. **Deep analysis**: Extract specific insights, quotes, teaching methods per theme
11. **Cross-video connections**: How themes relate and build on each other
12. **Instructor voice**: Capture characteristic phrases, approaches, emphasis

### Phase 4: Blog Idea Generation (10-15 minutes)
13. **High-value topics**: Identify 5-10 blog post ideas based on analysis
14. **Audience mapping**: Assign target audiences to each idea (beginners, intermediate, advanced, instructors)
15. **Unique angles**: What unique perspectives does this instructor offer?
16. **Cross-reference potential**: Topics that could be enriched by comparing with other instructors

### Phase 5: Documentation (10-15 minutes)
17. **Create channel summary**: Comprehensive report in `sources/youtube/findings/`
18. **Update registry**: Add analysis status, key findings, blog ideas
19. **Create findings index**: List of notable videos per theme

---

## Channel Summary Template

The agent creates: `sources/youtube/findings/YYYY-MM-DD-<channel-name>-channel-summary.md`

```markdown
# [Channel Name] - Channel Analysis

**Channel**: [Full Name]
**Channel URL**: [URL]
**Analysis Date**: [Date]
**Videos Analyzed**: [Count] of [Total]
**Instructor**: [Name]

---

## Channel Overview

[2-3 paragraphs describing channel focus, teaching style, content themes]

**Teaching Style**:
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

**Content Focus**:
- [Primary focus area]
- [Secondary focus area]
- [Tertiary focus area]

---

## Cross-Video Themes

### Theme 1: [Name] (Appears in X videos)
- **Description**: [What this theme covers]
- **Key Insights**: [Bullet points of main ideas]
- **Representative Videos**: [List video IDs/titles]
- **Blog Potential**: [High/Medium/Low with rationale]

### Theme 2: [Name] (Appears in X videos)
[Same structure...]

[Continue for all major themes - typically 5-10 themes]

---

## Unique Perspectives

What makes this instructor/channel distinctive:

1. **[Unique Aspect 1]**: [Description and examples]
2. **[Unique Aspect 2]**: [Description and examples]
3. **[Unique Aspect 3]**: [Description and examples]

---

## Teaching Philosophy

[Analysis of instructor's overall approach to teaching Aikido]

**Core Principles**:
- [Principle 1]
- [Principle 2]
- [Principle 3]

**Pedagogical Approach**:
[How they teach - demonstrations, explanations, progressions, etc.]

---

## Most Valuable Content

### Top 10 Videos for Blog Research:

1. **[Video Title]** (Video ID: [ID], Date: [Date])
   - **Why valuable**: [Explanation]
   - **Key topics**: [List]
   - **Blog angle**: [Potential use]

[Continue for top 10...]

---

## Blog Ideas from Channel

### High-Priority Topics (5 ideas)

1. **[Blog Post Title]**
   - **Source videos**: [List video IDs]
   - **Angle**: [How to approach this topic]
   - **Target Audience**: [Primary and secondary audiences]
   - **Why interesting**: [What makes this worth writing]
   - **Cross-reference potential**: [Other instructors who might offer contrasting/complementary views]

[Continue for 5 high-priority ideas]

### Medium-Priority Topics (5 ideas)

[Same structure, briefer]

---

## Research Value Assessment

**Strengths**:
- [What this channel offers uniquely]
- [Strong content areas]
- [Pedagogical advantages]

**Gaps**:
- [What this channel doesn't cover well]
- [Missing perspectives]
- [Areas better covered by other instructors]

**Best Used For**:
- [Type 1 of blog posts]
- [Type 2 of blog posts]
- [Type 3 of blog posts]

**Recommended Focus**:
[Which videos/themes to prioritize for blog research]

---

## Comparison Notes

[Only complete after analyzing multiple channels]

**Similar to**: [Other instructors with similar approaches]
**Contrasts with**: [Other instructors with different approaches]
**Complements**: [Other instructors whose content pairs well]

---

## Statistics

**Total Videos in Channel**: [Number]
**Videos with Transcripts**: [Number] ([Percentage]%)
**Videos Analyzed in Detail**: [Number]
**Date Range**: [Earliest] to [Latest]
**Average Video Length**: [Duration]

**Content Breakdown**:
- [Category 1]: [Count] videos
- [Category 2]: [Count] videos
- [Category 3]: [Count] videos

---

## Next Steps

- [ ] Analyze remaining videos (if applicable)
- [ ] Deep dive on [specific theme]
- [ ] Cross-reference with [other instructor]
- [ ] Write blog post on [high-priority topic]

---

*Analysis completed: [Date]*
*Analyst: Claude Code*
*Method: Systematic transcript analysis with theme identification*
```

---

## Registry Update Template

The agent updates: `sources/youtube/registry/<channel-name>.md`

Adds/updates these sections:
- **Analysis Status**: Date completed, videos analyzed
- **Key Themes**: List of major themes discovered
- **Blog Ideas Generated**: Count and brief list
- **Teaching Style Summary**: One-paragraph characterization
- **Cross-Reference Value**: How this channel relates to others

---

## Output Format

**Final Report to User**:

```markdown
# Channel Analysis Complete: [Channel Name]

## Summary Statistics
- **Total videos**: [Count]
- **Transcripts available**: [Count]
- **Videos analyzed in detail**: [Count]
- **Major themes identified**: [Count]
- **Blog ideas generated**: [Count]

## Key Findings

### Instructor's Unique Approach
[2-3 sentences capturing what makes this instructor distinctive]

### Top 3 Themes
1. [Theme 1]: [Brief description]
2. [Theme 2]: [Brief description]
3. [Theme 3]: [Brief description]

### Top 3 Blog Ideas
1. **[Title]**: [One-sentence description] (Audience: [X])
2. **[Title]**: [One-sentence description] (Audience: [X])
3. **[Title]**: [One-sentence description] (Audience: [X])

## Files Created
- Channel summary: `sources/youtube/findings/YYYY-MM-DD-<channel>-channel-summary.md`
- Updated registry: `sources/youtube/registry/<channel>.md`

## Next Steps
- Ready to analyze next channel, or
- Ready to cross-reference with other channels, or
- Ready to begin blog writing based on these findings
```

---

## Analysis Strategy by Channel Size

### Small Channels (<100 videos)
- Analyze all transcripts in detail
- Create comprehensive theme coverage
- Focus: Completeness

### Medium Channels (100-500 videos)
- Sample 20-30% of transcripts strategically
- Focus on most recent and most representative
- Focus: Representative coverage

### Large Channels (>500 videos)
- Sample 10-15% of transcripts
- Use keyword search to identify theme clusters
- Focus on most recent 1-2 years + highly-viewed content
- Focus: Efficient pattern identification

---

## Technical Approach

### Tools Used:
1. **Grep**: Search across all transcripts for keywords
2. **Read**: Deep read of representative samples
3. **Glob**: Find all transcript files for channel
4. **Bash**: Count statistics, check dates, sort by recency

### Sampling Strategy:
- Most recent 20% of videos (current teaching)
- Oldest 10% of videos (foundational content, teaching evolution)
- Keyword-identified videos per theme (representative examples)
- High-value titles (explicit technique names, teaching methods)

### Analysis Order:
1. Skim all titles/metadata (understand content scope)
2. Read 5 random transcripts (get feel for style)
3. Keyword search major themes (find patterns)
4. Deep read 20-30 videos (representative sampling)
5. Synthesize findings (create summary)

---

## Quality Criteria

**Good Analysis Includes**:
- ✓ 5-10 major cross-video themes identified
- ✓ Teaching style clearly characterized
- ✓ 10+ blog ideas generated with target audiences
- ✓ Unique perspectives documented with examples
- ✓ Top 10 most valuable videos identified
- ✓ Research value assessment (strengths/gaps)
- ✓ Clear, actionable recommendations

**Inadequate Analysis**:
- ✗ Generic descriptions that could apply to any instructor
- ✗ Fewer than 5 themes or blog ideas
- ✗ No specific video examples or quotes
- ✗ Unclear teaching style characterization
- ✗ Missing comparison/cross-reference notes

---

## Notes

- **Time estimate**: 1-2 hours per channel depending on size
- **Context efficiency**: Agent runs independently, doesn't use main conversation context
- **Repeatability**: Can re-analyze same channel with updated transcripts
- **Cross-reference ready**: Summaries designed for easy comparison across channels

---

*Agent created: 2025-10-30*
*Version: 1.0*
