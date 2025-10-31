# Information Architecture Reorganization Plan

**Created**: 2025-10-31
**Purpose**: Reorganize files according to refined routing rules based on user feedback

---

## Overview

This plan reorganizes existing content to properly separate:
1. **Behavioral decisions** (how Claude should think/act)
2. **Core values/beliefs** (foundational principles)
3. **Writing style guidance** (how to write blog posts)
4. **Research findings** (analysis of external content)
5. **Technical reference** (biomechanics, syllabus)

---

## Phase 1: Restructure decisions.md

### Current State
- `decisions.md` (152 lines) - Mix of behavioral decisions and some duplication with core-values.md
- `research/core-values.md` (544 lines) - Contains values, beliefs, AND writing guidance

### Proposed Action

**Replace decisions.md with categorized structure:**

**New categories:**
1. **Foundational Values** - Core beliefs about martial arts
   - Biomechanics over mysticism (BELIEF)
   - Knowing vs. embodied understanding (BELIEF about learning)
   - Peace through understanding cost (BELIEF informed by experience)

2. **Writing Style** - How to write blog content
   - Voice: First dan perspective (from core-values.md)
   - Honesty about abilities (from core-values.md)
   - Grounding in real experience (from core-values.md)
   - Presenting frameworks as working models (from core-values.md)

3. **Content Strategy** - Audience and topic selection
   - Multi-audience layering (existing in decisions.md)
   - Violence context awareness (existing in decisions.md)

4. **Content Quality** - Review standards
   - Critical and collaborative review (existing in decisions.md)

5. **System Architecture** - Technical organization
   - Documentation structure (existing in decisions.md)
   - Single agent with modes (existing in decisions.md)

6. **Session Management** - Git and workflow
   - Checkpoint autonomy (existing in decisions.md)
   - Automatic GitHub push (existing in decisions.md)

**Files involved:**
- Create: `decisions-NEW.md` (✅ DONE - ready for review)
- Move content from: `research/core-values.md` → `decisions-NEW.md`
- Delete after merge: Old `decisions.md`
- Rename: `decisions-NEW.md` → `decisions.md`

**What stays in research/**:
- Update `core-values.md` to become a lean reference file pointing to decisions.md
- OR delete `core-values.md` entirely since content moves to decisions.md

---

## Phase 2: Create blog/blog-voice-guide.md

### Current State
- `research/core-values.md` contains "How to Use This File" sections with blog writing guidance
- `blog/blog-guidelines.md` exists but doesn't cover voice/authenticity

### Proposed Action

**Create: `blog/blog-voice-guide.md`**

**Content to include:**
- How to frame writing from first dan perspective
- When to reference which stage of learning
- Examples of authentic vs. inauthentic phrasing
- How to use core values when writing blog posts
- Cross-references to:
  - decisions.md (for values and style decisions)
  - research/learning-journey.md (for stage frameworks)
  - research/divisive-topics.md (for controversial topics)

**Files involved:**
- Create: `blog/blog-voice-guide.md`
- Extract from: `research/core-values.md` (teaching implications, blog topic ideas)

---

## Phase 3: Create findings/ Directory for Analysis Summaries

### Current State
- `sources/youtube/findings/` - Contains YouTube video analyses
- `sources/findings/` - Contains blog analysis (Leo Tamaki)
- `research/tony-sargeant-evidence-summary.md` - Summary of video analysis (seems misplaced)
- `research/teaching-transmission-gap.md` - Based on Tony's videos but contains YOUR framework

### Proposed Action

**Create new top-level directory: `findings/`**

**Purpose**: Summaries and insights from analyzing external content (videos, blogs, papers)

**Structure:**
```
findings/
├── youtube/
│   ├── tony-sargeant-evidence-summary.md (MOVE from research/)
│   ├── heins-approach-summary.md
│   ├── alexander-gent-summary.md
│   └── ...
├── blogs/
│   └── leo-tamaki-findings.md (MOVE from sources/findings/)
└── INDEX.md (new - catalog of all findings)
```

**Routing rule addition:**
- **findings/** = "Summaries and insights from analyzing external content"
- Different from **sources/** which contains raw external content
- Different from **research/** which contains YOUR frameworks and beliefs

**Keep in research/:**
- `teaching-transmission-gap.md` - This is YOUR framework/analysis, not just summary of Tony's content

**Files involved:**
- Create: `findings/` directory
- Create: `findings/INDEX.md`
- Move: `research/tony-sargeant-evidence-summary.md` → `findings/youtube/tony-sargeant-evidence-summary.md`
- Move: `sources/findings/*` → `findings/blogs/`
- Update: All references to moved files

---

## Phase 4: Route SYSTEM_REVIEW.md Content

### Current State
- `SYSTEM_REVIEW.md` (405 lines) - One-time system audit from previous session
- Contains recommendations, file analysis, priority lists

### Proposed Action

**Analyze SYSTEM_REVIEW.md and route each section:**

1. **Critical Issues** (lines 40-71)
   - ✅ .gitignore - Create if not exists
   - ✅ README.md - Already exists
   - ✅ Initial commit - Already done

2. **Important Issues** (lines 74-108)
   - Some addressed, some still relevant
   - Extract actionable items → Add to PROJECT-STATUS.md backlog

3. **Nice-to-Have Improvements** (lines 110-255)
   - Extract valuable suggestions → Add to PROJECT-STATUS.md future enhancements
   - Archive rest

4. **Architecture Review** (lines 289-308)
   - Positive assessment of architecture
   - Archive to `sessions/` as historical system audit

**Final disposition:**
- Archive: Move entire SYSTEM_REVIEW.md → `sessions/system-review-2025-10-30.md`
- Extract: Actionable items → `PROJECT-STATUS.md`
- Delete: Original `SYSTEM_REVIEW.md` from root

**Files involved:**
- Move: `SYSTEM_REVIEW.md` → `sessions/system-review-2025-10-30.md`
- Update: `PROJECT-STATUS.md` with extracted backlog items
- Delete: Root `SYSTEM_REVIEW.md`

---

## Phase 5: Create biomechanics/ Subdirectory

### Current State
- `research/biomechanical-principles.md` (1,293 lines, 52KB) - Very large single file with 25+ principles

### Proposed Action

**Create: `research/biomechanics/` subdirectory**

**Structure:**
```
research/biomechanics/
├── INDEX.md (overview + quick reference of all principles)
├── foundation/
│   ├── 01-leverage.md
│   ├── 02-gravity.md
│   ├── 03-balance.md
│   ├── 04-newtons-laws.md
│   └── ...
├── application/
│   ├── 11-surface-area.md
│   ├── 12-target-selection.md
│   ├── 13-triangle-deflection.md
│   └── ...
└── advanced/
    ├── 18-tension-disconnects.md
    ├── 19-joint-vulnerability.md
    ├── 20-weapons-assumption.md
    └── ...
```

**Each principle file contains:**
- Principle name and description
- Scientific basis (physics, anatomy)
- Aikido applications
- Teaching implications
- Blog post ideas
- Cross-references to other principles

**INDEX.md contains:**
- Quick reference table of all principles
- Navigation to categories
- Blog topics tracker (consolidated from individual files)

**Benefits:**
- Load individual principles on-demand (token savings)
- Easier to maintain and update
- Clear scientific organization
- Scalable as more principles are discovered

**Files involved:**
- Create: `research/biomechanics/` directory structure
- Split: `research/biomechanical-principles.md` → 25+ individual files
- Create: `research/biomechanics/INDEX.md` with overview
- Keep: Original file temporarily for reference during split
- Delete: `research/biomechanical-principles.md` after verification

---

## Phase 6: Consolidate Research Indexes

### Current State
- `research.md` (351 lines) - Detailed overview at root level
- `research/INDEX.md` (88 lines) - Quick reference inside research/
- Duplication and confusion about which to use

### Proposed Action

**Delete `research.md` from root**

**Enhance `research/INDEX.md` as the single source:**
- Keep quick reference format (load fast)
- Add brief "purpose of research/" explanation at top
- Point to README.md for getting started

**Update README.md:**
- Add pointer to research/INDEX.md
- Brief explanation: "For research frameworks and values, see research/INDEX.md"

**Files involved:**
- Delete: `research.md` (root level)
- Update: `research/INDEX.md` (enhance if needed)
- Update: `README.md` (add pointer to research/)

---

## Phase 7: Move 'How to Write' Guidance to blog/

### Current State
- `research/core-values.md` contains sections like:
  - "How to Use This File"
  - "Potential Blog Topics" lists
  - "Teaching Implications" that are really writing guidance

### Proposed Action

**Create: `blog/blog-voice-guide.md`** (covered in Phase 2)

**Extract from core-values.md:**
- All "How to use for blog writing" sections
- All "Potential blog topics" lists (consolidate)
- All "Teaching implications" that are really "how to write about this"

**What stays in decisions.md:**
- The actual values/beliefs
- The actual experiences/background

**Files involved:**
- Create: `blog/blog-voice-guide.md`
- Extract from: `research/core-values.md`
- Possibly delete: `research/core-values.md` if all content moves to decisions.md

---

## Phase 8: Update Routing Guide

### Current State
- `.claude/docs/information-routing.md` - Comprehensive but needs new categories

### Proposed Action

**Add new routing categories:**

**15. findings/ - Analysis Summaries**
- **Store here**: Summaries and insights from analyzing external content
- **Belongs**: Video analysis summaries, blog analysis summaries, paper reviews
- **Doesn't belong**: Raw external content (that's sources/), Your frameworks (that's research/)
- **Test**: "Is this a summary of what SOMEONE ELSE created?"

**16. research/biomechanics/ - Physical Principles**
- **Store here**: Individual biomechanical principles with scientific basis
- **Belongs**: Leverage, gravity, balance, joint mechanics, etc.
- **Doesn't belong**: Conceptual frameworks (those stay in research/), Teaching methods
- **Test**: "Is this a physical principle I can link to science?"

**Update decision tree:**
- Add findings/ check before sources/
- Add biomechanics/ as sub-category of research/

**Update quick reference table:**
- Add findings/ and research/biomechanics/ rows

**Files involved:**
- Update: `.claude/docs/information-routing.md`

---

## Summary of File Operations

### Files to CREATE
1. `decisions-NEW.md` → `decisions.md` (✅ DONE - ready for review)
2. `blog/blog-voice-guide.md`
3. `findings/` directory structure
4. `findings/INDEX.md`
5. `research/biomechanics/` directory structure
6. `research/biomechanics/INDEX.md`
7. 25+ individual biomechanics principle files

### Files to MOVE
1. `research/tony-sargeant-evidence-summary.md` → `findings/youtube/`
2. `sources/findings/*` → `findings/blogs/`
3. `SYSTEM_REVIEW.md` → `sessions/system-review-2025-10-30.md`
4. `research/biomechanical-principles.md` → Split into `research/biomechanics/*.md`

### Files to UPDATE
1. `decisions.md` (replace with new categorized version)
2. `research/core-values.md` (remove moved content, possibly delete entirely)
3. `research/INDEX.md` (if needed)
4. `README.md` (add research/ pointer)
5. `PROJECT-STATUS.md` (add extracted backlog from SYSTEM_REVIEW)
6. `.claude/docs/information-routing.md` (add new categories)
7. All files with references to moved files

### Files to DELETE
1. Old `decisions.md` (after merge)
2. `research.md` (root level - redundant)
3. `SYSTEM_REVIEW.md` (after archiving to sessions/)
4. `research/core-values.md` (possibly - if all content moves)
5. `research/biomechanical-principles.md` (after splitting verified)

---

## Execution Order

**Session 1 (Current):**
- Review this plan
- Checkpoint
- User approves plan

**Session 2 (Next):**
1. Phase 1: Replace decisions.md ✅ (NEW version ready for review)
2. Phase 6: Consolidate research indexes (quick)
3. Phase 4: Route SYSTEM_REVIEW.md (archive + extract)
4. Phase 7: Create blog-voice-guide.md
5. Checkpoint

**Session 3 (Later):**
6. Phase 3: Create findings/ directory structure
7. Phase 5: Create biomechanics/ subdirectory (largest task)
8. Phase 8: Update routing guide
9. Final verification and cleanup
10. Checkpoint

---

## Validation Checklist

After reorganization, verify:
- [ ] All content from core-values.md properly routed
- [ ] decisions.md has clear categories
- [ ] No orphaned references to moved files
- [ ] All new directories have INDEX.md files
- [ ] Routing guide covers all new categories
- [ ] README.md accurately describes structure
- [ ] Git history preserves content (use git mv when possible)

---

## Risks and Mitigations

**Risk**: Breaking references to moved files
**Mitigation**: Search all .md files for references before moving, update them

**Risk**: Losing content during reorganization
**Mitigation**: Git commits after each phase, verify content before deleting originals

**Risk**: Creating confusing structure
**Mitigation**: Clear INDEX.md in each new directory, update routing guide immediately

**Risk**: Too much work in one session
**Mitigation**: Split into 2-3 sessions with checkpoints between

---

## Questions for Review

1. **decisions.md structure**: Approve the 6 categories (Values, Style, Strategy, Quality, Architecture, Management)?

2. **core-values.md fate**: Delete entirely (content moves to decisions.md) or keep as lean pointer file?

3. **findings/ location**: Top-level directory or subdirectory of sources/?

4. **biomechanics/ split**: Do now (Phase 5) or defer until file grows beyond 2000 lines?

5. **Execution timeline**: All in next session or split across 2-3 sessions?

---

*Review this plan, approve/modify, then we'll checkpoint and execute.*
