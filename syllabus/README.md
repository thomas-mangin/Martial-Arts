# Aikido Syllabus Reference System

This directory contains **factual information** about Takemusu/Iwama Aikido techniques, progression, and terminology. This is NOT interpretation or analysis—that lives in `/research/`. This is the technical reference.

---

## Purpose

This syllabus system provides:
1. **Technical accuracy** for `/discuss` conversations
2. **Fact-checking** for `/review-aikido` quality checks
3. **Quick reference** for Japanese terminology and technique details
4. **Progression understanding** for writing audience-appropriate content
5. **Lineage documentation** for school-specific variations

---

## Directory Structure

```
/syllabus/
├── README.md                    # This file
├── overview.md                  # Lineage, philosophy, grading structure
├── terminology.md               # Quick Japanese-English reference
├── attacks.md                   # All attack types explained
├── ranks/                       # Rank-specific requirements
│   ├── rokkyu.md               # 6th kyu
│   ├── gokyu.md                # 5th kyu
│   ├── yonkyu.md               # 4th kyu
│   ├── sankyu.md               # 3rd kyu
│   ├── nikyu.md                # 2nd kyu
│   ├── ikkyu.md                # 1st kyu
│   ├── shodan.md               # 1st dan
│   ├── nidan.md                # 2nd dan
│   ├── sandan.md               # 3rd dan
│   └── yondan.md               # 4th dan
├── techniques/                  # One file per technique
│   ├── ikkyo.md
│   ├── nikyo.md
│   ├── sankyo.md
│   ├── yonkyo.md
│   ├── gokyo.md
│   ├── rokkyo.md
│   ├── shiho-nage.md
│   ├── irimi-nage.md
│   ├── kote-gaeshi.md
│   ├── kaiten-nage.md
│   ├── tenchi-nage.md
│   ├── koshi-nage.md
│   ├── kokyu-nage.md
│   └── ... (add as needed)
├── weapons/                     # Weapons techniques
│   ├── ken/                    # Sword
│   │   ├── suburi.md          # Solo cutting practice
│   │   ├── kumitachi.md       # Paired sword practice
│   │   └── ...
│   ├── jo/                     # Staff
│   │   ├── suburi.md          # Solo striking practice
│   │   ├── kata.md            # Solo forms
│   │   ├── kumijo.md          # Paired staff practice
│   │   └── ...
│   └── paired/                 # Ken tai jo, etc.
│       └── ken-tai-jo.md
└── attacks/                     # (Currently attacks.md, may expand)
```

---

## How This System Works

### For `/discuss` Sessions
When exploring Aikido topics, I'll reference:
- **terminology.md**: Ensure correct Japanese terms
- **attacks.md**: Understand which attacks are used when
- **techniques/[name].md**: Get technical details about specific techniques
- **overview.md**: Understand progression and teaching philosophy

**Example**: Discussing "Teaching Ikkyo to Beginners"
→ Reference `techniques/ikkyo.md` to see:
- Which grade it's introduced (Rokkyu)
- Common errors for beginners
- Teaching progression
- Key biomechanical principles

### For `/review-aikido` Quality Checks
When reviewing blog posts, I'll verify:
- **Japanese spelling**: Check terminology.md for correct romanization
- **Technical accuracy**: Compare descriptions against technique files
- **Audience appropriateness**: Match content difficulty to rank progression
- **Lineage correctness**: Ensure Iwama-specific details are accurate

**Example**: Reviewing a post about "Irimi-nage for Intermediate Students"
→ Check `techniques/irimi-nage.md`:
- Is it introduced at the right grade level in the post?
- Are common errors mentioned accurately?
- Does description match Iwama/Takemusu approach?
- Is weapon connection (yokomenuchi) acknowledged?

### For Blog Writing
When you write blog posts, reference:
- Which techniques are appropriate for target audience's level
- Correct terminology with proper macrons
- School-specific variations (Iwama vs. other styles)
- Progressive learning expectations

---

## Template for Technique Files

Each technique file should include:

```markdown
# [Technique Name]

**Japanese**: [With macrons]
**Translation**: [English meaning]
**Category**: [Pin/Projection/etc.]

## Description
[What the technique is]

## Syllabus Progression
[Table showing when technique is taught at each grade]

## Variations
- By direction (omote/ura)
- By attack (shomenuchi/yokomenuchi/etc.)
- By practice mode (tachiwaza/suwariwaza/hanmihandachi)
- By form (kihon/kinonagare)

## Key Biomechanical Principles
[Numbered principles with framework links]

## Common Errors
[Organized by skill level: beginner/intermediate/advanced]

## Learning Journey Connections
[Which stages of mastery apply]

## School/Lineage Variations
[Your school vs. others]

## Video Evidence
[Links to Tony Sargeant/Alexander Gent videos]

## Teaching Notes
[Key teaching points, progression, common fixes]

## Personal Notes
[Your first-dan perspective]
```

---

## Separation from `/research/`

| `/syllabus/` (This Directory) | `/research/` (Analysis) |
|------------------------------|------------------------|
| **Factual information** | **Interpretation** |
| Technique descriptions | Biomechanical principles analysis |
| Grading requirements | Learning journey frameworks |
| Terminology definitions | Teaching philosophy |
| "Ikkyo is taught at Rokkyu" | "Why ikkyo is pedagogically first" |
| "Omote and ura variations" | "How direction relates to strategy" |
| School-specific details | Cross-school comparisons |

**Example of separation**:
- **Syllabus** (`techniques/ikkyo.md`): "Ikkyo controls the elbow using a circular cutting motion, introduced at Rokkyu"
- **Research** (`biomechanical-principles.md`): "Ikkyo demonstrates Principle #1 (Leverage) because the elbow acts as a fulcrum..."

---

## Current Status

### Complete
✅ `overview.md` - Grading structure, philosophy, progression
✅ `terminology.md` - Japanese-English quick reference
✅ `attacks.md` - All attack types explained
✅ `techniques/ikkyo.md` - Example technique (pin)
✅ `techniques/irimi-nage.md` - Example technique (projection)

### To Be Added (As Needed)
⏳ `ranks/*.md` - Individual rank requirement files
⏳ `techniques/*.md` - Additional technique files (nikyo, sankyo, yonkyo, gokyo, rokkyo, shiho-nage, kote-gaeshi, kaiten-nage, etc.)
⏳ `weapons/ken/*.md` - Sword techniques details
⏳ `weapons/jo/*.md` - Staff techniques details

---

## How to Add Content

### Adding a New Technique
1. Create file: `techniques/[technique-name].md`
2. Use the template structure above
3. Fill in syllabus progression from your grading PDF
4. Add video references where available
5. Include your personal notes (first-dan perspective)

### Adding Rank Details
1. Create file: `ranks/[rank-name].md`
2. Extract requirements from syllabus PDF
3. Organize by section (Taisabaki, Suwariwaza, Tachiwaza, etc.)
4. Note focus attack/theme for that rank
5. Include training time requirements

### Adding Weapons Content
1. Create files in `weapons/ken/` or `weapons/jo/`
2. Document suburi, kata, kumitachi/kumijo details
3. Reference Alexander Gent's extensive jo/ken content
4. Link to taijutsu (empty-hand) equivalents

---

## Integration with Other Systems

### Blog Guidelines
`blog/blog-guidelines.md` should reference:
- "Check technique names against `/syllabus/terminology.md`"
- "Verify technical accuracy using `/syllabus/techniques/`"

### Slash Commands
`/.claude/commands/review-aikido.md` will check:
- Japanese terminology spelling (terminology.md)
- Technique descriptions (techniques/*.md)
- Audience appropriateness (overview.md ranks)

`/.claude/commands/discuss.md` will reference:
- Syllabus for realistic progression expectations
- Technique files for accurate discussion
- Attacks for understanding context

---

## Maintenance

- Update files when you learn new details
- Add video references as you identify relevant Tony/Alexander clips
- Expand technique files as you write about specific techniques
- Note lineage variations as you discover them
- Keep personal notes current (first-dan perspective)

---

## Source

**Primary Source**: Aikido Syllabus Booklet - Takemusu/Iwama Style
**Lineage**: Saito Morihiro Sensei (Iwama)
**Your Training**: First dan (shodan) perspective

---

*This is a living reference system. Add content as needed for blog writing and quality assurance.*
*Last Updated: 2025-10-30*
