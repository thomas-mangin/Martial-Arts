# Active Decisions

This document contains only **active decisions** that affect how Claude should think and behave. Closed/completed decisions are removed. Historical records are in session summaries.

---

## Content Quality & Review Standards

### Critical and Collaborative Review Approach
**Decision**: /review-aikido should be highly critical and work collaboratively with user on improvements

**How this affects thinking**:
- Apply MA-level quality expectations (not casual blog standards)
- Point out weaknesses directly without sugar-coating
- Challenge vague statements, unsupported claims, and clichés
- Ask probing questions to deepen thinking
- Provide specific, actionable feedback with multiple revision options
- Work iteratively through improvements
- Don't accept "good enough" - push for excellence

**Why**: This is MA-level work requiring high standards. User wants rigorous, honest feedback, not polite praise.

---

## Voice & Authenticity

### Honest Positioning: Writing from First Dan Perspective
**Decision**: Acknowledge experience level (first dan) and write from "on the journey" perspective, not as ultimate authority

**How this affects thinking**:
- Stages 1-3: Speak from direct personal experience (lived these stages)
- Stage 4: Speak from emerging understanding (currently working through this)
- Stage 5: Speak from observation (watching advanced practitioners, not yet embodied)
- Ultimate mastery: Cannot claim to fully understand yet

**Framing approach**:
- Use: "In my experience so far...", "What I've observed...", "My current understanding..."
- Avoid false authority: Not "This is how mastery definitively works"
- Acknowledge uncertainty about later stages
- Invite dialogue and correction from more experienced practitioners
- Present frameworks as working models, not absolute truth

**Why**: Authenticity builds credibility more than false expertise. First dan is ideal position - close enough to remember struggles, far enough to have useful perspective.

### Background and Real Experience Context
**Decision**: Ground voice in real experience, not fantasy or theory

**Key background elements that inform perspective**:
- Defended against knife attack before training - learned doesn't freeze under pressure
- Military background (French mountain infantry - les chasseurs) - one year intense physical training
- Witnessed PTSD in Iraq war veterans - observed their relationship to violence
- Critical insight: Those who faced real war avoid conflict and seek peace; those who never saw combat romanticize it

**How this affects thinking**:
- Can speak to pressure situations authentically (knife attack, military training)
- Understand gap between training and reality
- Value peace from understanding cost, not from weakness
- Position on peace vs. martial: Both/And - martially effective AND peace-oriented
- Real violence survivors seek peace; violence fantasists seek conflict

---

## Content Strategy

### Audience Targeting and Multi-Profile Content Strategy
**Decision**: Write for multiple audience profiles simultaneously (3-5 per post)

**How this affects thinking**:
- Every post should identify primary (1-2) and secondary (2-3) audiences
- Use layered content approach - accessible to beginners, challenging for advanced
- Tier practical takeaways by experience level when applicable
- Design hooks and examples for different reader types
- Check that no audiences are systematically excluded over time

**Why**: Single-audience writing excludes potential readers. Blog serves entire aikido community ecosystem.

**Quarterly review**: Track which audiences are underserved, ensure balanced coverage.

---

## System Architecture

### Documentation Refactoring: Agent-Based Architecture with Pyramidal Organization
**Decision**: Lean OVERVIEW.md + detailed docs loaded on-demand + autonomous agents

**How this affects thinking**:
- OVERVIEW.md must stay <500 words (currently ~414 words)
- Command files must stay <200 words each (lightweight wrappers only)
- Detailed content goes in .claude/docs/ (loaded when needed)
- Agent files contain full logic (loaded internally by agents)
- session-context.md should stay <1000 words (current state only, not history)

**Token targets** (measured by system-maintenance agent):
- /resume load: <10,000 tokens target
- 🟢 Green: Within target or <110%
- 🟡 Yellow: 110-130% (needs attention)
- 🔴 Red: >130% (must fix)

**Why**: 80-85% token reduction enables more complex workflows and longer conversations.

### Single Comprehensive Agent vs. Multiple Agents
**Decision**: When creating maintenance/utility agents, prefer single agent with multiple modes over multiple specialized agents

**How this affects thinking**:
- Agent can load complete system context internally (no user context bloat)
- Single agent is more coherent - understands entire system holistically
- Less error-prone - no risk of multiple agents getting out of sync
- Simpler user interface - one command, different modes

**Why**: Agents exist to handle complexity internally. Let them have full context and make holistic decisions.

---

## Git & Session Management

### Checkpoint Command Autonomy
**Decision**: /checkpoint executes fully autonomously without asking questions

**How this affects thinking**:
- Generate commit messages from changed files analysis
- Infer decisions from work done (don't ask)
- Create session summaries automatically
- Assume session-context.md and topics.md are current
- Be efficient: 30-60 seconds total execution

**Why**: User wants checkpoint to just work - analyze, commit, summarize, done.

### Checkpoint Command: Push to GitHub by Default
**Decision**: /checkpoint automatically pushes to GitHub after committing

**How this affects thinking**:
- Always push to remote if configured
- Graceful failure handling (complete checkpoint even if push fails)
- User sees confirmation that push succeeded

**Why**: Automatic GitHub backup of all work. Remote repository stays current.

---

## This File's Purpose

**What belongs here**: Decisions that change HOW Claude should think, behave, or approach tasks going forward.

**What doesn't belong here**: Historical records of "what was implemented" - those go in session summaries.

**Maintenance**: Remove decisions once they're no longer active constraints. Archive to session summaries if needed for historical reference.

---

*Last updated: 2025-10-30*
*Keep this file lean - only active/guiding decisions*
