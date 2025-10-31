# Remaining Tasks for Article Series System

**Created**: 2025-10-31
**Context**: After restructuring from blog to educational article series

---

## What Was NOT Done (But May Be Needed)

### 1. Update Command Files (Optional)

**Location**: `.claude/commands/discuss.md`, `.claude/commands/extract.md`, `.claude/commands/review-aikido.md`

**Current State**: These command files may still reference "blog posts" in their internal instructions

**What to Do**:
- Read each command file
- Change any "blog post" references to "article"
- Update any instructions that assume blog-style writing (engagement focus)
- Update review-aikido to explicitly check for:
  - Series consistency (uses same terms as earlier articles)
  - Cross-references (builds on previous articles properly)
  - Comprehensive depth (no significant gaps)
  - Educational completeness (reader doesn't need other sources)

**Priority**: Medium - Commands still work, but internal language should match new approach

**How to Execute**:
```bash
# Read and update each command file
vim .claude/commands/discuss.md
vim .claude/commands/extract.md
vim .claude/commands/review-aikido.md
```

---

### 2. Decide on Directory Structure

**Current State**: Documentation references `articles/[series-name]/[article-name].md` but no `articles/` directory exists yet

**Options**:

**Option A: Keep blog/ directory**
- Rename `blog/` → `articles/`
- Pro: Clean naming
- Con: Breaks any existing references to blog/

**Option B: Create articles/ alongside blog/**
- Keep `blog/` for templates/guidelines
- Create `articles/` for actual content
- Pro: Clear separation of meta vs. content
- Con: Two directories with similar purpose

**Option C: Keep blog/ as-is**
- Just use `blog/` directory for everything
- Ignore the name mismatch
- Pro: No changes needed
- Con: Confusing name

**Priority**: Low - Can decide when actually writing first article

**Recommendation**: Create `articles/` directory structure when writing first article:
```bash
mkdir -p articles/
# Then create series subdirectories as needed:
# mkdir -p articles/biomechanics-foundations/
# mkdir -p articles/iwama-syllabus/
```

---

### 3. Update blog-series-structure.md (Optional)

**Location**: `blog/blog-series-structure.md`

**Current State**: Contains 10 series with blog-style catchy titles:
- "Why Your Aikido Teacher Won't Shut Up About Sword Training"
- "The One Thing You're Getting Wrong About Ikkyo"
- etc.

**What to Do**:
- Review each series
- Convert titles to educational article style:
  - Old: "Why Your Aikido Teacher Won't Shut Up About Sword Training"
  - New: "The Role of Weapons Training in Aikido Development"
- Update series descriptions for comprehensive educational approach
- Or: Delete this file and start fresh with educational series planning

**Priority**: Low - This is planning content, not system infrastructure

**Note**: Could also rename to `article-series-structure.md` for consistency

---

### 4. Create articles/ Directory Structure (When Ready)

**What**: Create organized directory structure for article series

**When**: Before writing first article

**Structure** (Suggested):
```
articles/
├── README.md                           # Navigation and overview
├── biomechanics-foundations/
│   ├── 01-newtons-third-law.md
│   ├── 02-kinetic-chain.md
│   └── ...
├── learning-journey/
│   ├── 01-five-stages-overview.md
│   └── ...
├── iwama-syllabus/
│   ├── techniques/
│   │   ├── 01-ikkyo-comprehensive.md
│   │   └── ...
│   ├── weapons/
│   │   ├── 01-seven-ken-suburi.md
│   │   ├── 02-twenty-jo-suburi.md
│   │   └── ...
│   └── progressive-training/
│       └── ...
└── ...
```

**Priority**: Medium - Create when actually starting to write

**How to Execute**:
```bash
cd /Users/thomas/MA
mkdir -p articles
# Create series directories as you start each series
```

---

### 5. Review Existing Discussions/ Directory

**Location**: `discussions/`

**Current State**: Unknown - may contain discussion drafts from old blog approach

**What to Do**:
- Review any existing discussion files
- Determine if they're blog-style explorations or article-worthy
- Either:
  - Migrate promising ones to article drafts
  - Archive old blog-style discussions
  - Keep for reference but don't use as-is

**Priority**: Low - Only needed if starting to write and want to review old ideas

---

### 6. Consider Updating posts/ Directory

**Location**: `posts/`

**Current State**: Empty (checked during session)

**What to Do**: Nothing immediately, but:
- Could rename to `articles/` if adopting Option A above
- Or leave empty as legacy directory
- Or delete entirely

**Priority**: Very Low - Directory is empty anyway

---

### 7. Create articles/README.md Navigation File (Future)

**What**: Create overview file that helps readers navigate article series

**Content Should Include**:
- List of all series with descriptions
- Recommended reading order
- Prerequisites map (which series to read first)
- Audience guidance (which series for which readers)

**Priority**: Low - Create after you have multiple series in progress

**Example Structure**:
```markdown
# Aikido Educational Article Series

## Complete Series

### Biomechanics Foundations (6 articles)
**Audience**: Beginners to Intermediate, Technical focus
**Prerequisites**: None - start here for technical understanding
1. Newton's Third Law in Aikido
2. The Kinetic Chain
...

### Learning Journey (5 articles)
**Audience**: All levels, Instructors
**Prerequisites**: None - foundational framework
...
```

---

### 8. Plan First Article Series to Write (Decision Needed)

**What**: Decide which series to start with

**Options from Existing Research**:
1. **Biomechanics Foundations** (~6 articles) - Technical strength
2. **Learning Journey** (~5 articles) - Broadly applicable
3. **Peace & Violence Context** (~5 articles) - Unique personal perspective
4. **Iwama Syllabus - Weapons** (~10 articles) - Capture your expertise
5. **Teaching Aikido** (~5 articles) - Practical for instructors

**Priority**: High - Decision needed before writing

**Recommendation**: Start with what you're most excited about, but consider:
- **Biomechanics** = Establishes technical credibility
- **Iwama Weapons** = Captures unique knowledge before you forget details
- **Learning Journey** = Broadest appeal, framework for other series

---

### 9. Update System Maintenance Agent (Optional)

**Location**: `.claude/agents/system-maintenance.md` (if exists)

**What**: Update system maintenance agent to recognize article series structure

**What to Check**:
- Token usage audits should consider article-guidelines.md (not blog-guidelines.md)
- File organization checks should recognize articles/ directory
- Sync operations should maintain series structure

**Priority**: Low - Only if you use system maintenance agent regularly

---

### 10. Consider Creating Article Series Planning Template (Future)

**What**: Template for planning a new article series before writing

**Content Should Include**:
- Series title and description
- Target audience (primary + secondary)
- Number of articles planned
- Prerequisites (which series/articles to read first)
- Article titles (educational style)
- Key concepts covered in each article
- Cross-references between articles
- Learning progression (how complexity builds)

**Priority**: Low - Create when starting to plan multiple series

**Location**: Could be `blog/series-planning-template.md`

---

## Execution Plan

### Immediate (Before Writing First Article):
1. ✅ **Decide on directory structure** (Option A, B, or C)
2. ✅ **Create articles/ directory** if using Option A or B
3. ✅ **Choose first series to write**

### Short-term (During First Article Writing):
4. ⏳ **Test current workflow** with /discuss → /extract → /review-aikido
5. ⏳ **Update command files if needed** based on how they perform with article approach
6. ⏳ **Create series subdirectory** for first series

### Medium-term (After 3-5 Articles Complete):
7. ⏳ **Review and refine article-guidelines.md** based on actual writing experience
8. ⏳ **Create articles/README.md** for navigation
9. ⏳ **Update blog-series-structure.md** or create new planning doc

### Long-term (After Multiple Series):
10. ⏳ **Create series planning template** for future series
11. ⏳ **Consider book compilation structure** and chapter organization
12. ⏳ **Review old discussions/** for article potential

---

## Quick Start When Ready to Write

1. Decide: Which series first?
2. Create: `mkdir -p articles/[series-name]/`
3. Plan: List 5-7 article titles in order
4. Write: `/discuss [first article topic]`
5. Extract: `/extract [discussion file]`
6. Draft: Expand to 1,500-3,000 words using article-template.md
7. Review: `/review-aikido [draft]` for depth and completeness
8. Revise: Multiple rounds until book-quality
9. Track: Update topics.md with progress

---

**Note**: This document can be deleted after executing remaining tasks, or kept as reference for "what wasn't done during the restructure."

**Created during**: /checkpoint command - session 2025-10-31-1700
