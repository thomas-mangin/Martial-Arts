# Track Source - Register Martial Arts Bloggers

You are helping the user track martial arts bloggers and maintain their source registry.

## Purpose

Create and maintain profiles for martial arts bloggers whose content the user wants to monitor for:
- Inspiration and ideas
- Points worthy of response
- Alternative perspectives to explore
- Community engagement
- Content quality references

## Steps to Execute

### 1. **Gather Source Information**

If user provides all info inline:
```
/track-source "Leo Tamaki" "https://www.leotamaki.com" "Aikido"
```

If user only provides name or partial info, ask for:
- **Name**: Full name of the blogger/author
- **URL**: Primary blog or website URL
- **Discipline**: Martial art they practice/teach (Aikido, Karate, etc.)
- **Language**: Primary language of their content (optional)
- **Focus**: What they mainly write about (optional, can be added later)

### 2. **Check if Source Exists**

- Generate filename: Convert name to lowercase-kebab-case (e.g., "Leo Tamaki" → "leo-tamaki")
- Check if `sources/registry/[filename].md` already exists
- If exists: Ask if user wants to update it
- If new: Proceed to create

### 3. **Fetch Initial Information** (Optional)

If URL is provided, use WebFetch to get initial context:
- Check if the blog is active
- Identify recent post titles (if visible)
- Get a sense of their writing style and topics
- This helps populate the profile better

### 4. **Ask Contextual Questions**

To create a useful profile, ask:
- **Why tracking?** "What interests you about [name]'s work?"
- **Focus areas?** "What do they typically write about? (technique, philosophy, training methods, history, etc.)"
- **Language?** "What language is their content in?"
- **Notes?** "Any particular reason you want to track them? (similar perspective, different discipline, inspiring writing, etc.)"
- **Active?** "Is this an active blog or historical archive?"

### 5. **Create Source Profile**

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

### 6. **Confirm and Guide**

After creating the profile, tell the user:

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

### 7. **Update Source Registry Index** (Optional)

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
