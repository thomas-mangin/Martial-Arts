# YouTube Analyze Command

You are helping the user analyze an already-downloaded YouTube transcript to extract blog ideas.

## Command Format

`/youtube-analyze <video_id_or_path>`

**Examples**:
- `/youtube-analyze KGFEDrQRWSo`
- `/youtube-analyze sources/youtube/transcripts/KGFEDrQRWSo.txt`

## When to Use

- When transcript is already downloaded (via /youtube-fetch)
- To re-analyze a video with fresh perspective
- To extract additional blog ideas from previously analyzed content

## Steps to Execute

1. **Load Transcript and Metadata**
   - If given video ID: look for `sources/youtube/transcripts/<video_id>.txt` and `.json`
   - If given path: read that file directly
   - Load metadata from corresponding JSON file

2. **Deep Content Analysis**
   - Read entire transcript carefully
   - Identify:
     - **Main Themes**: What are the core topics?
     - **Teaching Methods**: How does the instructor explain concepts?
     - **Demonstrations**: What techniques or principles are shown?
     - **Philosophy**: What underlying principles are discussed?
     - **Stories/Examples**: Concrete examples or anecdotes used
     - **Unique Insights**: What's different or novel about this content?
     - **Cross-Discipline Elements**: How does this relate to Aikido?

3. **Extract Quotable Concepts**
   - Identify key phrases or concepts that resonate
   - Note teaching metaphors or analogies
   - Find "quotable moments" (paraphrase, don't copy verbatim)

4. **Generate Blog Ideas**
   - Create 3-5 blog topic ideas inspired by the content
   - For each idea:
     - **Title**: Compelling blog post title
     - **Type**: Response / Alternative Perspective / Inspired Exploration / Extension / Comparative Analysis
     - **Angle**: The specific approach or argument
     - **Connection to Aikido**: How does this apply to Aikido specifically?
     - **Target Audiences**: 3-5 audience profiles
     - **Key Points**: 3-4 main points to develop
     - **Hook**: Opening hook idea
     - **Takeaways**: Practical takeaways for readers
     - **Source Inspiration**: What from the video inspired this (paraphrased)

5. **Create or Update Findings Report**
   - Save to: `sources/youtube/findings/<date>-<video_id>.md`
   - If report already exists, add new analysis with timestamp
   - Include:
     - Video metadata
     - Content analysis
     - Blog ideas with full details
     - Discussion prompts
     - Next steps

6. **Display Results**
   - Summarize key insights from transcript
   - Present blog ideas with brief descriptions
   - Recommend which ideas are highest priority
   - Suggest next actions

## Analysis Quality Standards

- **Depth**: Go beyond surface-level observations
- **Specificity**: Identify specific concepts, not just general themes
- **Aikido Connection**: Always link back to Aikido practice/philosophy
- **Originality**: Generate original ideas inspired by (not copied from) content
- **Audience Awareness**: Consider which audiences would benefit from each idea
- **Actionability**: Ensure ideas are concrete enough to write about

## Output Format

```markdown
# YouTube Video Analysis: [Title]

**Video**: [Title]
**Channel**: [Channel Name]
**URL**: [URL]
**Duration**: [Duration]
**Analyzed**: [Date and time]

## Content Summary

[2-3 paragraph summary of what the video covers]

## Key Themes

1. [Theme 1]: [Description]
2. [Theme 2]: [Description]
3. [Theme 3]: [Description]

## Notable Concepts/Quotes (paraphrased)

- [Concept 1]
- [Concept 2]
- [Concept 3]

## Blog Ideas Generated

### 1. [Blog Title]
- **Type**: [Response/Alternative/Inspired/Extension/Comparative]
- **Angle**: [Specific approach]
- **Aikido Connection**: [How it relates to Aikido]
- **Target Audiences**: [3-5 profiles]
- **Key Points**:
  1. [Point 1]
  2. [Point 2]
  3. [Point 3]
- **Hook**: [Opening hook idea]
- **Source Inspiration**: [What from video inspired this]

[Repeat for each idea]

## Discussion Prompts

- [Prompt 1 for /discuss command]
- [Prompt 2 for /discuss command]

## Recommended Next Steps

1. [Action 1]
2. [Action 2]
3. [Action 3]
```

## Important Notes

- **Original Thinking**: Transform video content into YOUR original ideas
- **Copyright**: Never reproduce long transcript excerpts in blog posts
- **Attribution**: Credit video/channel if directly inspired
- **Quality Filter**: Not all videos yield good blog ideas - be honest about fit
- **Cross-Discipline**: Look for universal principles applicable to Aikido
