# Track Source - Register Martial Arts Content Creators

You are helping the user track martial arts content creators (bloggers, YouTube channels) and maintain their source registry.

## Purpose

Create and maintain profiles for martial arts content creators whose work the user wants to monitor for:
- Inspiration and ideas
- Points worthy of response
- Alternative perspectives to explore
- Community engagement
- Content quality references

## Content Types Supported

1. **Blogs/Websites**: Traditional written content
2. **YouTube Channels**: Video content creators

## Steps to Execute

### 1. **Detect Content Type**

Check the URL to determine if it's a blog or YouTube channel:
- **YouTube Channel**: URL contains `youtube.com/@` or `youtube.com/c/` or `youtube.com/channel/`
  - Create profile in `sources/youtube/registry/[name].md`
  - Use YouTube channel template (simpler format)
  - Reference `/youtube-fetch` for video analysis
- **Blog/Website**: All other URLs
  - Create profile in `sources/registry/[name].md`
  - Use full blog tracking template
  - Reference `/scan-sources` for content monitoring

### 2. **Gather Source Information**

If user provides all info inline:
```
/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"
/track-source https://www.youtube.com/@Tony_Sargeant
```

If user only provides name or partial info, ask for:
- **Name**: Full name of the creator/channel
- **URL**: Primary URL (blog or YouTube channel)
- **Discipline**: Martial art they practice/teach (Aikido, Karate, etc.)
- **Language**: Primary language of their content (optional, for blogs)
- **Focus**: What they mainly create about (optional, can be added later)

### 3. **Check if Source Exists**

- Generate filename: Convert name to lowercase-kebab-case (e.g., "Leo Tamaki" → "leo-tamaki", "Tony Sargeant" → "tony-sargeant")
- **For YouTube**: Check if `sources/youtube/registry/[filename].md` already exists
- **For Blogs**: Check if `sources/registry/[filename].md` already exists
- If exists: Ask if user wants to update it
- If new: Proceed to create

### 4. **Fetch Initial Information**

**For Blogs**: Use WebFetch to get initial context:
- Check if the blog is active
- Identify recent post titles (if visible)
- Get a sense of their writing style and topics
- This helps populate the profile better

**For YouTube Channels**: Use youtube-channel-info.py script to extract channel information:
- Run: `python scripts/youtube-channel-info.py "<channel_url>"`
- Script extracts:
  - Channel name and ID
  - Subscriber count
  - Recent video titles (up to 10)
  - Video view counts and durations
- Analyze video titles to determine:
  - Martial art discipline (Aikido, Karate, etc.)
  - Content themes (technique, philosophy, training, competition)
  - Teaching style/approach
- Use this information to populate the channel profile

### 5. **Ask Contextual Questions** (If Needed)

After fetching initial information, ask additional questions if needed:
- **Why tracking?** "What interests you about [name]'s work?"
- **Additional focus areas?** (If not clear from fetch) "What else should I know about their content?"
- **Notes?** "Any particular reason you want to track them?"

**For Blogs Only**:
- **Language?** "What language is their content in?" (YouTube can detect from fetch)
- **Active?** "Is this an active blog or historical archive?" (YouTube channels show activity)

### 6. **Create Source Profile**

#### For Blogs/Websites

Create file: `sources/registry/[name-kebab-case].md`

**Format**:

```markdown
# [Full Name]

**URL**: [Blog URL]
**Discipline**: [Martial art]
**Language**: [Primary language]
**Status**: Active | Inactive | Unknown

---

## Focus Areas

[List based on user input or web research]
- [Area 1 - e.g., Technical breakdowns]
- [Area 2 - e.g., Philosophical explorations]
- [Area 3 - e.g., Teaching methodology]

## Why Tracking

[User's reason for tracking this source]

## Notes

[Any additional context about this source]
- [Connection to user's work]
- [What makes their perspective valuable]
- [Unique aspects of their approach]

---

## Content Tracking

**Added**: [Today's date]
**Last Scanned**: Not yet scanned
**Total Posts Reviewed**: 0
**Ideas Generated**: 0
**Blog Posts Inspired**: 0

### Scan History
| Date | Posts Found | Ideas Generated | Status |
|------|-------------|-----------------|---------|
| - | - | - | - |

### Ideas Generated from This Source
*None yet. Run `/scan-sources [name]` to analyze their content.*

---

## Recent Posts Tracked

*Will be populated by /scan-sources command*

| Date | Title | URL | Analyzed | Notes |
|------|-------|-----|----------|-------|
| - | - | - | - | - |

---

## Related Topics in Your Blog

*Track connections between this source's content and your blog posts*

- [ ] Your post: [Title] - Inspired by/Response to: [Their post]

---

## Updates and Maintenance

**Last Profile Update**: [Today's date]

### Change Log
- [Today's date]: Profile created

---

*Use `/scan-sources [name]` to check for new content*
*Use `/scan-sources` to scan all tracked sources*
```

#### For YouTube Channels

Create file: `sources/youtube/registry/[name-kebab-case].md`

**Populate from WebFetch results**:
- Use channel name from fetch
- Use discipline/focus from fetch (if detected)
- Use description from fetch
- Include subscriber count if available
- List recent video topics/themes from fetch
- Note teaching/presentation style from fetch

**Format**:

```markdown
# [Channel Name] - YouTube Channel

**Channel URL**: [YouTube channel URL]

**Channel Type**: YouTube Channel

**Discipline/Focus**: [Martial art(s) from fetch - e.g., "Aikido", "Karate", "Multiple martial arts", etc.]

**Subscribers**: [Count if available from fetch, otherwise "Unknown"]

**Date Added**: [Today's date]

---

## Channel Overview

**Description**: [Use description from WebFetch]

**Content Themes**: [From WebFetch analysis]
- [Theme 1 - e.g., Technical breakdowns]
- [Theme 2 - e.g., Training methodology]
- [Theme 3 - e.g., Historical context]

**Teaching Style**: [From WebFetch - e.g., "Detailed technical explanations", "Philosophical approach", "Demonstration-focused", etc.]

**Why Tracking**:
- [Reason from user input]
- [What makes this channel valuable]
- [Connection to user's work]

**Recent Video Topics** (from channel page):
- [Recent topic 1]
- [Recent topic 2]
- [Recent topic 3]

---

## Content Tracking

### Registration Details
- **Date Added**: [Today's date]
- **Initial Status**: Active channel with [subscriber count or "subscribers"]
- **Videos Analyzed**: 0
- **Blog Ideas Generated**: 0

---

## Videos Analyzed

*No videos analyzed yet. Use /youtube-fetch with specific video URLs to analyze content and generate blog ideas.*

**To Analyze**:
1. Browse channel for relevant videos
2. Run `/youtube-fetch <video_url>` for videos of interest
3. Findings will be saved in sources/youtube/findings/

---

## Blog Ideas Generated

*Blog ideas will be added here as videos are analyzed with /youtube-fetch.*

---

## Notes

- Channel information extracted from channel page on [Today's date]
- Use `/youtube-fetch <video_url>` to analyze specific videos and generate blog ideas
- Profile will be enriched as videos are analyzed
- Check channel periodically for new content relevant to blog topics

---

*Last Updated: [Today's date]*
```

### 7. **Confirm and Guide**

After creating the profile, tell the user:

**For Blogs**:
```
✅ Source tracked: [Name]

📁 Profile saved: sources/registry/[filename].md

📋 Summary:
- Name: [Full name]
- URL: [Blog URL]
- Discipline: [Martial art]
- Status: [Active/Inactive]

🔍 Next steps:
1. Run `/scan-sources [name]` to analyze their recent content
2. Or run `/scan-sources` to scan all tracked sources
3. Review findings in sources/findings/

📝 You can manually edit the profile to add:
- More detailed focus areas
- Additional notes
- Updated URL if it changes
```

**For YouTube Channels**:
```
✅ YouTube channel tracked: [Channel Name]

📁 Profile saved: sources/youtube/registry/[filename].md

📋 Summary (extracted from channel page):
- Channel: [Channel name]
- URL: [YouTube channel URL]
- Discipline: [Martial art(s) detected or "Multiple martial arts"]
- Subscribers: [Count if available]
- Content Themes: [List 2-3 main themes detected]
- Status: Active

🔍 Next steps:
1. Visit the channel to find interesting videos: [channel URL]
2. Run `/youtube-fetch <video_url>` to analyze specific videos and generate blog ideas
3. Review findings in sources/youtube/findings/

📝 Notes:
- Channel information extracted from channel page
- Profile includes description, themes, and recent topics
- Use /youtube-fetch to analyze individual videos for detailed blog ideas
```

### 8. **Update Source Registry Index** (Optional)

Create or update `sources/registry/INDEX.md` with list of all tracked sources:

```markdown
# Tracked Sources

Total sources: [count]

| Name | Discipline | Status | Last Scanned | Ideas Generated |
|------|------------|--------|--------------|-----------------|
| [Name 1] | [Discipline] | Active | [Date] | [Count] |
| [Name 2] | [Discipline] | Active | [Date] | [Count] |

---

## By Discipline

### Aikido
- [Name 1] - [URL]
- [Name 2] - [URL]

### Karate
- [Name 1] - [URL]

### Other
- [Name 1] - [Discipline] - [URL]

---

*Use `/track-source [name] [url] [discipline]` to add new sources*
*Use `/scan-sources` to check all sources for new content*
```

## Important Guidelines

### Source Selection
- **Quality over quantity**: Focus on bloggers with substantial content
- **Diverse perspectives**: Include different disciplines and viewpoints
- **Active sources**: Prioritize blogs that publish regularly
- **Accessible**: Must be in a language the user can read/translate

### Profile Quality
- **Be specific**: Vague notes aren't helpful later
- **Context matters**: Why is this source worth tracking?
- **Connection**: How does it relate to user's work?
- **Honesty**: Note both agreements and disagreements

### Updating Profiles
If source already exists:
- Ask what to update
- Preserve scan history
- Update change log
- Don't overwrite custom notes

### Filename Convention
- Lowercase only
- Use hyphens for spaces
- No special characters
- Examples:
  - "Leo Tamaki" → `leo-tamaki.md`
  - "Lionel Froidure" → `lionel-froidure.md`
  - "O'Sensei Archive" → `o-sensei-archive.md`

## Integration with Workflow

After tracking a source, user can:
1. **Scan immediately**: `/scan-sources [name]`
2. **Scan later**: `/scan-sources` (scans all)
3. **Manual review**: Visit the blog directly and add notes to profile
4. **Update profile**: Re-run `/track-source` with updated info

## Examples

### Example 1: Full Information Provided
```
User: /track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"

Assistant actions:
1. Create sources/registry/leo-tamaki.md
2. Use WebFetch to check the blog
3. Ask contextual questions about why tracking
4. Create complete profile
5. Confirm creation
6. Suggest running /scan-sources leo-tamaki
```

### Example 2: Minimal Information
```
User: /track-source "Lionel Froidure"
Assistant actions:
1. Ask: "What's the blog URL?"
2. Ask: "What martial art does Lionel practice?"
3. Ask: "Why do you want to track him?"
4. Create profile with gathered info
5. Confirm and guide next steps
```

### Example 3: Updating Existing Source
```
User: /track-source "Leo Tamaki" (already exists)

Assistant actions:
1. Detect existing profile
2. Ask: "Leo Tamaki is already tracked. What would you like to update?"
3. Update specified fields
4. Preserve scan history
5. Add entry to change log
```

---

## Error Handling

### Invalid URL
- Note it in profile
- Mark as "URL needs verification"
- Suggest user visit manually

### Inactive Blog
- Mark status as "Inactive"
- Note last known active date if available
- Still useful for historical content

### Language Barrier
- Note the language
- Suggest translation tools if needed
- User can still track for reference

---

*After tracking sources, use `/scan-sources` to monitor their content*
