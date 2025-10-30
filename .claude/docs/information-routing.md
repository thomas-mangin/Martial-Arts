# Information Routing Guide

**Purpose**: Define where different types of information should be stored in the system to maintain clean architecture and prevent misplacement.

**Last Updated**: 2025-10-30

---

## The Problem

When users share information during sessions, it's not always clear where to store it:
- Is this a decision about how I should behave?
- Is this conceptual knowledge about Aikido?
- Is this session-specific context?
- Is this a permanent reference?

Putting information in the wrong place creates:
- Bloated files that should stay lean (decisions.md, session-context.md)
- Missing information that should be persistent (research files)
- Confused architecture that defeats the token optimization

---

## Information Routing Rules

### 1. decisions.md - Behavioral Instructions Only

**Store here**: Decisions that change HOW Claude should think, behave, or approach tasks

**Examples that belong**:
- "Be highly critical during reviews, not polite"
- "Write from first dan perspective, acknowledge uncertainty about advanced stages"
- "Always specify violence context when discussing effectiveness" ← Just the instruction
- "Push to GitHub by default when checkpointing"

**Examples that DON'T belong**:
- Four types of violence and their characteristics ← This is conceptual knowledge
- Tony Sargeant's teaching methods ← This is research findings
- What happened in previous session ← This is session history
- List of blog post ideas ← This is content planning

**Test**: Ask "Is this telling Claude HOW to behave/think, or WHAT the knowledge is?"
- HOW = decisions.md
- WHAT = research/ or elsewhere

---

### 2. research/ - Conceptual Knowledge & Frameworks

**Store here**: Knowledge about Aikido, martial arts, teaching, biomechanics - anything that informs content

**Files and their purposes**:

| File | Content Type | Examples |
|------|--------------|----------|
| **core-values.md** | Your fundamental beliefs | Teaching philosophy, mastery concepts, style positions |
| **divisive-topics.md** | Community debates & controversies | Peace vs. martial, ki vs. biomechanics, **violence contexts** |
| **learning-journey.md** | How learning/mastery works | Knowing vs. embodied, progression stages |
| **biomechanical-principles.md** | Technical/mechanical knowledge | 23+ principles, how body mechanics work |
| **contextual-design-framework.md** | How context shapes technique | Weapons, time, environment factors |
| **weapons-training-framework.md** | Ken/jo relationship to taijutsu | How weapons develop skills |
| **stance-principles.md** | Kamae, footwork, structure | Technical stance knowledge |
| **demonstration-robotization.md** | Teaching trap findings | How demo style affects learning |
| **audience-profiles.md** | Reader types and needs | Who you're writing for |
| **areas-needing-development.md** | Topics to explore via /discuss | Development queue |

**Test**: Ask "Will I reference this when writing blog posts?"
- YES = research/
- NO = probably somewhere else

**When in doubt**: If it's about Aikido/martial arts concepts, it goes in research/

---

### 3. session-context.md - Current State Only

**Store here**: Where you are NOW, what you're doing NOW, what's next NOW

**Belongs**:
- Current status (what you're working on)
- Recent work (this session or last 1-2 sessions)
- Next steps (immediate actions)
- Active blockers/questions
- Brief notes about current context

**Doesn't belong**:
- Complete session history (use session-summaries/ for archives)
- Permanent decisions (those go in decisions.md)
- Conceptual knowledge (that goes in research/)
- Completed work from weeks ago

**Target size**: <1000 words (current snapshot only)

---

### 4. topics.md - Content Planning

**Store here**: Blog topics queue, ideas, completion tracking, audience coverage

**Belongs**:
- Current topic being worked on
- Next topics in priority order
- Topic ideas for future
- Completed topics archive
- Audience coverage tracking

**Doesn't belong**:
- Actual blog content (that goes in posts/ or discussions/)
- Research about topics (that goes in research/)
- Session work notes (that goes in session-context.md)

---

### 5. sources/ - External Content & Findings

**Store here**: Content from other creators, analysis of their work, tracking bloggers/channels

**Structure**:
```
sources/
├── bloggers/
│   └── [blogger-name]/
│       ├── profile.md
│       └── posts/
├── youtube/
│   ├── channels/
│   │   └── [channel-name]/
│   │       ├── channel-info.md
│   │       └── videos.json
│   ├── transcripts/
│   └── findings/
│       └── [date]-[channel]-analysis.md
```

**Test**: Ask "Did someone else create this, or did I find it externally?"
- YES = sources/
- NO = research/ or posts/

---

### 6. posts/ and discussions/ - Your Content

**discussions/**: Informal explorations via /discuss
**posts/**: Blog post drafts and finals

**Doesn't belong**:
- Research frameworks (those go in research/)
- Session notes (those go in session-context.md)
- External content (that goes in sources/)

---

### 7. .claude/ - System Architecture

**Store here**: How the system itself works, not what you know about Aikido

**Subdirectories**:
- `agents/` - Agent definitions
- `commands/` - Slash command wrappers
- `docs/` - System documentation (like this file)

**Doesn't belong**:
- Aikido knowledge (that's research/, not system docs)
- Content (that's posts/ or discussions/)
- Session state (that's session-context.md)

---

### 8. README.md - Repository Introduction

**Store here**: Getting started information, command reminders, GitHub display content

**Belongs**:
- Quick start guide (what to do when you open the project)
- Essential commands reminder (/resume, /checkpoint, etc.)
- Link to more detailed documentation (help/ or help.md)
- Project purpose/overview
- Prerequisites and setup

**Doesn't belong**:
- Detailed workflows (that's help.md or help/)
- System architecture (that's .claude/docs/)
- Aikido knowledge (that's research/)

**Test**: "Would this help me remember what to do when I come back to this project?"

---

### 9. help.md (or help/) - User Documentation

**Store here**: Detailed how-to guides for using the system

**Current**: Single help.md file
**Future consideration**: Restructure as help/ folder with topic-specific files to keep reasonable chunk sizes

**Belongs**:
- Detailed workflow explanations
- Command usage examples
- Troubleshooting guides
- Best practices for using the system

**Doesn't belong**:
- System internals (that's .claude/docs/)
- Quick reference (that should be in README.md)
- Aikido content (that's research/)

---

### 10. scripts/ - Utility Code

**Store here**: Python scripts, shell scripts, automation code

**Purpose**: Code that commands and agents use to accomplish tasks

**Examples**:
- YouTube transcript downloaders
- Batch processing scripts
- Data transformation utilities

**Doesn't belong**:
- Agent definitions (those go in .claude/agents/)
- Command wrappers (those go in .claude/commands/)

---

### 11. syllabus/ - Technical Aikido Reference

**Store here**: Technical Aikido syllabus information - how to perform techniques correctly

**Purpose**: Reference material for:
- Teaching material authorship
- Technical accuracy verification
- Technique descriptions
- Training progression frameworks

**Structure**:
- `techniques/` - Individual technique files
- `weapons/` - Weapons kata and training
- `attacks/` - Attack types and progression
- `ranks/` - Rank-specific requirements

**Doesn't belong**:
- Your opinions/frameworks (that's research/)
- External instructor content (that's sources/)
- Blog posts (that's posts/)

**Test**: "Is this describing HOW to perform Aikido techniques correctly?"

---

### 12. sessions/ - Historical Session Summaries

**Store here**: Auto-generated session summaries from /checkpoint

**Purpose**: Historical record of what was accomplished each session

**Auto-generated**: This directory is populated automatically, not manually edited

**Doesn't belong**:
- Current session state (that's session-context.md)
- Manual notes (use session-context.md or discussions/)

---

### 13. blog/ - Writing Standards & Templates

**Store here**: Blog writing rules, templates, guidelines

**Purpose**: Reference material for blog post creation

**Examples**:
- blog-template.md - Template for new posts
- blog-guidelines.md - Writing standards
- blog-series-structure.md - Series planning

**Doesn't belong**:
- Actual blog content (that's posts/)
- Research frameworks (that's research/)
- System documentation (that's .claude/docs/)

---

### 14. PROJECT-STATUS.md - High-Level Project Overview

**Store here**: Project phases, roadmap, major milestones, strategic direction

**Belongs**:
- Current phase of work
- Completed milestones
- Upcoming phases and goals
- High-level progress tracking
- Strategic priorities

**Doesn't belong**:
- Current session details (that's session-context.md)
- Tactical task tracking (that's topics.md)
- Historical details (that's sessions/)

**Test**: "Is this about the project's overall direction and phases?"
**Update frequency**: Monthly or after major milestones (not every session)

---

## Decision Tree for Routing Information

When user shares information, ask:

**1. Is this telling me HOW to behave/think?**
- YES → decisions.md
- NO → Continue...

**2. Is this technical Aikido instruction (HOW to perform techniques)?**
- YES → syllabus/
- NO → Continue...

**3. Is this conceptual knowledge about Aikido/martial arts/teaching (frameworks, philosophy)?**
- YES → research/ (pick appropriate file from table above)
- NO → Continue...

**4. Is this about current session state/progress?**
- YES → session-context.md
- NO → Continue...

**5. Is this about overall project phases/roadmap/strategic direction?**
- YES → PROJECT-STATUS.md
- NO → Continue...

**6. Is this a blog topic idea or content plan?**
- YES → topics.md
- NO → Continue...

**7. Is this external content or analysis of someone else's work?**
- YES → sources/
- NO → Continue...

**8. Is this blog writing standards/templates/guidelines?**
- YES → blog/
- NO → Continue...

**9. Is this getting-started/command-reference information?**
- YES → README.md
- NO → Continue...

**10. Is this detailed user documentation/workflows?**
- YES → help.md (or help/ in future)
- NO → Continue...

**11. Is this system/architecture information?**
- YES → .claude/docs/
- NO → Continue...

**12. Is this utility code/scripts?**
- YES → scripts/
- NO → Ask user where it should go

---

## Example: Violence Contexts Framework

**User shares**: "There are different kinds of fights - monkey dance (ego), predatory violence (criminal), sport fighting (agreed rules), war. Each is different and requires different responses. Arm grab defenses look useless for men in monkey dance but crucial for women escaping predatory attack. Most martial arts judged by cage fighting lens."

**Routing process**:

1. ❌ Is this HOW I should behave? No - it's conceptual knowledge, not a behavioral instruction
2. ✅ Is this conceptual knowledge about martial arts? YES!
3. Which research file? → Addresses "effectiveness debates" and "competition" → **research/divisive-topics.md**

**What MIGHT go to decisions.md**: "Always specify violence context when discussing effectiveness" ← This is the behavioral instruction

**What goes to research/**: The entire framework explaining the four contexts and their differences ← This is the knowledge

---

## Maintaining Clean Architecture

**Regular maintenance**:
- Audit decisions.md quarterly - remove outdated decisions, archive if needed
- Keep session-context.md to current state - move old work to session-summaries/
- Add new research files when topics grow large enough to warrant separate file
- Update this routing guide when you discover new patterns

**When creating new files**:
- Ask: "Why doesn't this fit in existing files?"
- Ensure new file has clear, distinct purpose
- Update relevant indexes (research/INDEX.md, this guide)
- Keep naming consistent with existing structure

---

## Quick Reference Table

| Information Type | Destination | Test Question |
|-----------------|-------------|---------------|
| Behavioral instruction | decisions.md | "How should I behave?" |
| Technical Aikido instruction | syllabus/ | "Is this HOW to perform techniques correctly?" |
| Aikido frameworks/philosophy | research/ | "Is this conceptual knowledge for blog posts?" |
| Current session state | session-context.md | "Is this about NOW?" |
| Project phases/roadmap | PROJECT-STATUS.md | "Is this overall strategic direction?" |
| Blog topics/planning | topics.md | "Is this content planning?" |
| External content | sources/ | "Did someone else create this?" |
| Your blog content | posts/, discussions/ | "Is this my writing?" |
| Blog writing standards | blog/ | "Is this about HOW to write blog posts?" |
| Getting started guide | README.md | "Will this help me remember what to do?" |
| Detailed user docs | help.md (help/) | "Is this a how-to guide for users?" |
| System documentation | .claude/docs/ | "Is this about how the system works internally?" |
| Utility code | scripts/ | "Is this executable code?" |
| Session history | sessions/ | "Auto-generated by /checkpoint" |

---

*Use this guide to maintain clean information architecture and prevent file bloat.*
