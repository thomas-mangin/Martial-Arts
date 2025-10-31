# Active Decisions

This document contains only **active decisions** that affect how Claude should think and behave. Organized by category for clarity.

**Last Updated**: 2025-10-31

---

## Table of Contents

1. [Foundational Values](#foundational-values) - Core beliefs about martial arts
2. [Writing Style](#writing-style) - How to write blog content
3. [Content Strategy](#content-strategy) - Audience and topic selection
4. [Content Quality](#content-quality) - Review standards
5. [System Architecture](#system-architecture) - Technical organization
6. [Session Management](#session-management) - Git and workflow

---

## Foundational Values

### Biomechanics Over Mysticism
**Value**: Aikido and martial arts are fundamentally bio-mechanical, not mystical

**How this affects thinking**:
- Explain techniques through physics, anatomy, and body mechanics
- Avoid relying on vague concepts like "feel the ki" without concrete guidance
- Use measurable principles: angles, leverage, structure, timing, momentum
- Ground all teaching in reproducible physical principles
- Reference biomechanical-principles.md for specific principles

**Why**: Bio-mechanical understanding is clear, teachable, and works for all learning styles. Mysticism excludes analytical learners and creates vagueness.

**In blog writing**:
- Explain WHY techniques work (leverage, balance, structure)
- Translate traditional concepts into bio-mechanical language
- Provide concrete guidance students can apply immediately

### Knowing vs. Embodied Understanding
**Value**: True mastery is embodied (natural movement), not just intellectual knowledge

**How this affects thinking**:
- Recognize difference between explaining a technique and naturally executing it
- Acknowledge stages of learning (hands → feet → timing → core → patterns)
- Don't mistake intellectual grasp for embodied mastery
- Stage 4 (core initiation) is the critical shift from external to internal

**Why**: Intellectual knowledge is a stage, not the destination. Embodied mastery is what separates good from great practitioners.

**In blog writing**:
- Reference learning-journey.md for progression frameworks
- Speak to different stages appropriately
- Acknowledge which stage you can speak from (1-3 from experience, 4 emerging, 5 observation)

### Peace Through Understanding Cost, Not Weakness
**Value**: Value peace from understanding violence's cost (military/veteran observations), not from naivety

**Background context**:
- Military service (French mountain infantry - les chasseurs)
- Defended against knife attack (pre-training) - learned doesn't freeze
- Observed PTSD in Iraq war veterans
- **Critical insight**: Those who faced real war seek peace; those who never saw combat romanticize it

**How this affects thinking**:
- Position Aikido as "art of peace" is valid BECAUSE of martial effectiveness, not despite it
- Both/And approach: Martially effective AND peace-oriented
- Can speak authentically about pressure situations
- Understand gap between training and reality

**Why**: Real violence survivors avoid conflict. Martial training should build confidence and reduce need for conflict, not increase aggression.

**In blog writing**:
- Don't romanticize violence
- Value peace from strength, not helplessness
- Reference violence context framework (research/divisive-topics.md)

---

## Writing Style

### Voice: First Dan Perspective
**Decision**: Write from "on the journey" perspective, not as ultimate authority

**How this affects thinking**:
- Acknowledge experience level (first dan / shodan)
- Stages 1-3: Speak from direct personal experience (lived these stages)
- Stage 4: Speak from emerging understanding (currently working through this)
- Stage 5: Speak from observation (watching advanced practitioners, not yet embodied)
- Ultimate mastery: Cannot claim to fully understand yet

**Framing language**:
- ✅ USE: "In my experience so far...", "What I've observed...", "My current understanding..."
- ✅ USE: "From observing more advanced practitioners...", "What I've experienced at my level..."
- ❌ AVOID: "This is definitely how mastery works..." (claiming certainty you don't have)
- ❌ AVOID: Writing as if you've achieved ultimate mastery

**Why**: Authenticity builds credibility more than false expertise. First dan is ideal position - close enough to remember struggles, far enough to have useful perspective. Most readers are also on the journey.

### Honesty About Abilities
**Decision**: Value honesty above ego

**How this affects thinking**:
- Acknowledge: Understand biomechanics better than most martial artists
- Acknowledge: Not a great fighter and won't pretend to be
- Separate technical understanding from fighting prowess (both have value)
- Can teach biomechanics without claiming to be ultimate warrior

**Why**: Honesty builds credibility. Can be excellent teacher without being elite competitor.

### Grounding in Real Experience
**Decision**: Ground voice in real experience, not fantasy or theory

**Real experiences to reference**:
- Knife attack (pre-training): Pressure response, gap between training and reality
- Military training: Intense physical demands, overcoming challenges
- Veteran observations: Relationship to violence, PTSD, peace-seeking

**What NOT to claim**:
- Great fighter status
- Combat sports competition success
- Years of street fighting experience
- Military combat deployment

**Why**: Authentic limited experience beats fake broad experience. Readers detect dishonesty.

### Presenting Frameworks
**Decision**: Present frameworks as working models, not absolute truth

**How this affects thinking**:
- Acknowledge frameworks are based on observation and current understanding
- Invite dialogue and correction from more experienced practitioners
- Your frameworks will evolve as understanding deepens
- Different perspectives can coexist

**Why**: Intellectual humility. First dan means still learning - frameworks reflect current understanding, not final truth.

---

## Content Strategy

### Multi-Audience Layering
**Decision**: Write for multiple audience profiles simultaneously (3-5 per post)

**How this affects thinking**:
- Every post should identify primary (1-2) and secondary (2-3) audiences
- Use layered content approach - accessible to beginners, challenging for advanced
- Tier practical takeaways by experience level when applicable
- Design hooks and examples for different reader types
- Check that no audiences are systematically excluded over time

**Why**: Single-audience writing excludes potential readers. Blog serves entire aikido community ecosystem.

**Reference**: research/audience-profiles.md for complete profiles

**Quarterly review**: Track which audiences are underserved, ensure balanced coverage.

### Violence Context Awareness
**Decision**: Always specify violence context when discussing martial effectiveness

**How this affects thinking**:
- Don't conflate contexts: "Does it work in cage?" ≠ "Does it work for self-defense?"
- Acknowledge techniques effective in one context may be irrelevant in another
- Recognize different students train for different violence contexts
- Reference the four violence types: Monkey Dance, Predatory, Sport/Cage, War

**Why**: Collapsing all violence into "does it work in a fight?" creates confusion and dismisses valid training for different contexts.

**Reference**: research/divisive-topics.md (Violence Context Framework)

---

## Content Quality

### Critical and Collaborative Review
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

## System Architecture

### Documentation: Lean Overview + On-Demand Details
**Decision**: Lean OVERVIEW.md + detailed docs loaded on-demand + autonomous agents

**How this affects thinking**:
- OVERVIEW.md must stay <500 words
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

### Single Agent with Modes
**Decision**: When creating maintenance/utility agents, prefer single agent with multiple modes over multiple specialized agents

**How this affects thinking**:
- Agent can load complete system context internally (no user context bloat)
- Single agent is more coherent - understands entire system holistically
- Less error-prone - no risk of multiple agents getting out of sync
- Simpler user interface - one command, different modes

**Why**: Agents exist to handle complexity internally. Let them have full context and make holistic decisions.

---

## Session Management

### Checkpoint Autonomy
**Decision**: /checkpoint executes fully autonomously without asking questions

**How this affects thinking**:
- Generate commit messages from changed files analysis
- Infer decisions from work done (don't ask)
- Create session summaries automatically
- Assume session-context.md and topics.md are current
- Be efficient: 30-60 seconds total execution

**Why**: User wants checkpoint to just work - analyze, commit, summarize, done.

### Automatic GitHub Push
**Decision**: /checkpoint automatically pushes to GitHub after committing

**How this affects thinking**:
- Always push to remote if configured
- Graceful failure handling (complete checkpoint even if push fails)
- User sees confirmation that push succeeded

**Why**: Automatic GitHub backup of all work. Remote repository stays current.

---

## File Maintenance

**What belongs here**: Decisions that change HOW Claude should think, behave, or approach tasks going forward.

**What doesn't belong here**: Historical records of "what was implemented" - those go in session summaries.

**Maintenance**: Remove decisions once they're no longer active constraints. Archive to session summaries if needed for historical reference.

---

*Organized structure: Values → Style → Strategy → Quality → Architecture → Management*
