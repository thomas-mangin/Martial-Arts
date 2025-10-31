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

### Educational Article Series (Not Blog Posts)
**Decision**: Write educational article series designed for progressive learning, not standalone blog posts

**How this affects thinking**:
- Articles build on each other systematically
- Clear, descriptive titles over catchy/clickbait titles
- Comprehensive depth over quick readability
- Cross-reference earlier articles when building on concepts
- Self-consistency across entire series is critical
- Focus on completeness, not engagement metrics
- Professional educational tone, not casual conversational

**Article approach vs. Blog approach**:
- ✅ ARTICLE: "The Role of Weapons Training in Aikido Development"
- ❌ BLOG: "Why Your Aikido Teacher Won't Shut Up About Sword Training"
- ✅ ARTICLE: "Ikkyo: Biomechanics, Variations, and Progressive Training"
- ❌ BLOG: "The One Thing You're Getting Wrong About Ikkyo"

**Why**: Educational articles serve long-term learning and can be compiled into book. Blog posts optimize for clicks and shares, not depth.

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

### Ethical AI Disclosure in Published Articles
**Decision**: All published articles must include transparent disclosure of AI assistance
**Date**: 2025-10-31

**How this affects thinking**:
- Every published article includes "About This Article" section with AI attribution
- Clear statement: "Research, drafting, and revision conducted in collaboration with Claude AI (Anthropic)"
- Emphasize author as primary creator with AI as collaborative tool
- Author retains ownership of all technical content, personal experiences, and perspectives
- `/review-aikido` verifies attribution section is present before finalization
- Article template includes mandatory attribution section

**Attribution Format**:
```
## About This Article

**Author**: Thomas Mangin

**AI Assistance**: Research, drafting, and revision conducted in
collaboration with Claude AI (Anthropic). All technical content,
personal experiences, and perspectives reflect the author's knowledge
and understanding developed through training and practice.
```

**What this acknowledges**:
- AI assists with research synthesis, articulation, and structure
- Author provides all martial arts knowledge, experience, and judgment
- Collaborative process produces educational content at MA-level quality
- Transparency builds reader trust and maintains academic integrity

**Why**:
- Ethical responsibility to disclose AI involvement in content creation
- Maintains authenticity and reader trust
- Sets honest standard in era of AI-assisted writing
- Acknowledges AI as tool while preserving author's voice and expertise
- Demonstrates that AI assistance doesn't diminish quality or authenticity when used responsibly

**Reference**: `article/article-template.md` for standard format

---

## Content Strategy

### Multi-Audience Layering
**Decision**: Write for multiple audience profiles simultaneously (3-5 per article)

**How this affects thinking**:
- Every article should identify primary (1-2) and secondary (2-3) audiences
- Use layered content approach - accessible to beginners, challenging for advanced
- Tier practical applications by experience level when applicable
- Design explanations and examples for different reader types
- Check that no audiences are systematically excluded over time

**Why**: Single-audience writing excludes potential readers. Article series serves entire aikido community ecosystem.

**Reference**: research/audience-profiles.md for complete profiles

**Quarterly review**: Track which audiences are underserved, ensure balanced coverage.

### Progressive Article Series Structure
**Decision**: Organize content as progressive series where later articles build on earlier ones

**How this affects thinking**:
- Articles within a series must be written in logical order
- Cross-reference earlier articles when building on established concepts
- Ensure terminology and frameworks are consistent across all articles
- Readers should be able to read series start-to-finish for complete understanding
- Each article should still be comprehensible standalone (with references to prerequisites)
- Series could be compiled into cohesive book chapters

**Why**: Progressive learning is more effective than random standalone posts. Enables book publication.

### Comprehensive Educational Depth
**Decision**: Prioritize thoroughness and completeness over brevity and engagement

**How this affects thinking**:
- Cover topics comprehensively, not just highlights
- Include technical details and nuance
- Longer articles (1,500-3,000+ words) are acceptable if needed for completeness
- Don't sacrifice depth for "quick reads"
- Provide enough detail that readers don't need to seek other sources
- Reference supporting evidence from multiple sources (YouTube analysis, research)

**Why**: Educational articles aim to teach thoroughly. Blog posts aim to engage quickly. Different goals.

### Violence Context Awareness
**Decision**: Always specify violence context when discussing martial effectiveness

**How this affects thinking**:
- Don't conflate contexts: "Does it work in cage?" ≠ "Does it work for self-defense?"
- Acknowledge techniques effective in one context may be irrelevant in another
- Recognize different students train for different violence contexts
- Reference the four violence types: Monkey Dance, Predatory, Sport/Cage, War

**Why**: Collapsing all violence into "does it work in a fight?" creates confusion and dismisses valid training for different contexts.

**Reference**: research/divisive-topics.md (Violence Context Framework)

### Legal/Ethical Responsibility in Blog Writing
**Decision**: Always address legal and ethical context when discussing technique effectiveness, especially vital points or potentially excessive force

**How this affects thinking**:
- Effectiveness ≠ Appropriateness (just because it works doesn't mean it's legal/ethical)
- When discussing any technique, address THREE dimensions: tactical effectiveness, violence context, legal appropriateness
- Never promote techniques without discussing legal implications
- Acknowledge historical context problem (martial arts created when powerful classes had impunity)
- Highlight Aikido's legal advantage (control without killing = legally defensible for most scenarios)
- Educate readers about force continuum and proportionate response
- Include standard disclaimers when relevant ("not legal advice, laws vary by jurisdiction")

**Standard approach when discussing techniques**:
1. Explain WHY it works (biomechanics)
2. Acknowledge WHEN it's effective (threat level)
3. Discuss WHEN it's appropriate (legal/ethical context)
4. Suggest alternatives if force level problematic

**Why**: Readers have legal and ethical responsibility when applying martial arts. Teaching technique without context is irresponsible. Modern civilian self-defense is governed by law - trained martial artists held to higher standard and can face criminal charges for excessive force.

**Your Context**: French military background means understanding both violence reality AND legal constraints that govern civilian self-defense (different from military ROE).

**Reference**:
- research/legal-ethical-context.md (full framework)
- syllabus/vital-points-reference.md (anatomical targets and legal context)
- research/divisive-topics.md (Legal Context of Self-Defense section)

**Example application**:
> "Wing Chun's centerline attack with throat strike is biomechanically brilliant and devastatingly effective. However, throat strikes constitute deadly force and are only legally justified when facing an imminent deadly threat (weapon, multiple attackers, disparity of force). For typical self-defense scenarios (unarmed attacker, single opponent), control techniques like Aikido's ikkyo or nikyo are both effective AND legally defensible as proportionate force."

---

## Content Quality

### Critical and Collaborative Review
**Decision**: Article review should be highly critical and work collaboratively with user on improvements

**How this affects thinking**:
- Apply educational/book-level quality expectations (not casual blog standards)
- Point out weaknesses directly without sugar-coating
- Challenge vague statements, unsupported claims, and clichés
- Ask probing questions to deepen thinking
- Provide specific, actionable feedback with multiple revision options
- Work iteratively through improvements
- Don't accept "good enough" - push for excellence
- Check cross-references and consistency with earlier articles in series
- Verify completeness and educational depth

**Why**: This is educational article series that could become a book. Requires higher standards than blog posts.

### Self-Consistency Across Series
**Decision**: All articles must use consistent terminology, frameworks, and principles

**How this affects thinking**:
- Track terminology used in earlier articles (reference when reviewing)
- Ensure frameworks presented are compatible across articles
- If later article contradicts earlier one, either fix or explicitly acknowledge evolution
- Cross-references should be accurate and helpful
- Readers following series start-to-finish should not encounter contradictions

**Why**: Series credibility depends on internal consistency. Book compilation requires unified voice and approach.

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

### Crash Recovery State Tracking
**Decision**: Implement explicit state tracking in `.claude/state/` for crash recovery and task management
**Date**: 2025-10-31

**How this affects thinking**:
- Current objective is always preserved in `.claude/state/current-objective.md`
- Backlog of paused tasks maintained in `.claude/state/backlog.md`
- `/checkpoint` automatically saves state at session end
- `/resume` loads state and shows crash recovery notice if needed
- `/save-objective` provides explicit state save during work
- `/pause-task` enables seamless task switching with full context preservation
- No work is ever lost, even if Claude crashes or user needs to interrupt urgently

**State tracking includes**:
- Agreed objective and requirements
- Approach and reasoning
- Progress (completed, in progress, remaining)
- Blockers and questions
- Context files and references
- Pause reasons and priorities for backlog items

**Why**: Defensive programming ensures continuity. Crashes happen, priorities change, urgent work interrupts. State tracking ensures no context or work is ever lost, building user trust and enabling seamless resumption even after interruptions.

### Multi-Instance Support for Concurrent Sessions
**Decision**: Enable running multiple Claude Code instances simultaneously on same project without conflicts
**Date**: 2025-10-31

**How this affects thinking**:
- Instance-specific state isolated in `.claude/state/instances/[instance-id]/`
- Each instance gets timestamp-based ID (e.g., `2025-10-31-1945`)
- Shared files remain shared: `session-context.md`, `topics.md`, `backlog.md`, `decisions.md`
- Instance-specific files: `current-objective.md`, `session-info.md`
- `/resume` intelligently detects or creates instances based on arguments and state
- `/instances` command provides visibility into all active instances
- `/cleanup-instances` enables user-controlled cleanup of stale instances (>24h)
- Heartbeat tracking in `session-info.md` with activity logging
- Master registry in `.claude/state/registry.md` tracks all instances
- Backward compatible - works with or without instances

**Instance ID Strategy**:
- Timestamp-based: `YYYY-MM-DD-HHMM` format
- Self-documenting (know when instance started)
- Collision-free (unless starting two in same minute)
- Sorts chronologically automatically

**Smart Detection in /resume**:
- No args → Auto-detect active instances or create new
- `[instance-id]` → Resume specific instance explicitly
- `and work on [task]` → Create new instance for that task
- Checks git status for uncommitted instance changes
- Prompts user when multiple instances active

**User-Controlled Cleanup**:
- No automatic deletion of stale instances
- User decides when to archive, delete, or keep
- Prevents accidental data loss
- Stale = >24 hours since last heartbeat

**Why**:
- Enables true parallel workflows (e.g., article writing + research)
- Each instance maintains independent context
- No conflicts between concurrent sessions
- User can see what all instances are working on
- Preserves all benefits of crash recovery per-instance
- Backward compatible ensures smooth adoption

**Reference**: Command files updated - `/resume`, `/checkpoint`, `/save-objective`, `/pause-task`, `/instances`, `/cleanup-instances`

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

### Task Execution Autonomy
**Decision**: Once a task is agreed upon, execute autonomously without re-confirmation

**How this affects thinking**:
- If user says "do X", just do X - don't ask for confirmation again
- Don't ask to verify details after agreeing to execute the task
- Show work as it progresses, but don't wait for permission at each step
- Clarifying questions are appropriate BEFORE agreeing to the task, not AFTER
- Multi-file edits are normal (BAU) - just execute them
- Ask questions when genuinely unclear, not as defensive behavior

**Examples**:
- ✅ GOOD: User says "add these principles to biomechanics" → clarify what they mean → once agreed, execute all file edits
- ❌ BAD: User says "add these principles" → agree on approach → then ask "should I really edit all these files?"
- ✅ GOOD: "I'm not sure if this should go in category A or B - which do you prefer?"
- ❌ BAD: "We agreed to do this, but let me confirm the details again before executing"

**Why**: Efficient workflow. User trusts Claude to execute agreed-upon tasks. Asking for re-confirmation after agreement wastes time and breaks flow.

### Workflow Protocol for Consistent Interaction
**Decision**: Implement formal workflow protocol system documented in `.claude/docs/workflow-protocol.md`
**Date**: 2025-10-31

**How this affects thinking**:
- **Session start or work completion**: ALWAYS present overview of current and paused objectives
- **Task clarification**: When given a task, clarify and restate in specific terms, ask for confirmation ONCE
- **Execute completely**: After confirmation, save objective and execute fully without further confirmations (unless blocked)
- **State management**: Track active work in `current-objective.md`, paused work in `backlog.md`
- **Overview format**: Show active objective, paused tasks, system status - helps user decide next action

**Interaction pattern**:
1. Session start → Present overview → Ask what to work on
2. User gives task → Clarify specific details → Ask for confirmation once
3. User confirms → Save objective → Execute completely
4. Work completes → Clear objective → Present overview again

**When to ask questions during execution**:
- ✅ Genuine blocker requiring user decision
- ✅ Significant scope change discovered
- ✅ Critical information unavailable
- ❌ Defensive re-confirmation of agreed approach
- ❌ Permission to continue with agreed work

**Why**:
- Ensures efficient interaction (clarify once, execute completely)
- Maintains context continuity through overview presentations
- User always knows what's active vs. paused
- Reduces friction and redundant confirmations
- Clear state tracking enables crash recovery

**Reference**: `.claude/docs/workflow-protocol.md` for complete guidelines

---

## File Maintenance

**What belongs here**: Decisions that change HOW Claude should think, behave, or approach tasks going forward.

**What doesn't belong here**: Historical records of "what was implemented" - those go in session summaries.

**Maintenance**: Remove decisions once they're no longer active constraints. Archive to session summaries if needed for historical reference.

---

*Organized structure: Values → Style → Strategy → Quality → Architecture → Management*
