# System Design Principles

**Purpose**: Core principles that guide all work in this project

**Last Updated**: 2025-11-01

---

## 1. WHY-First Thinking ⭐ PRIMARY PRINCIPLE

**Principle**: When the WHY is clear, all other questions become easier to answer (WHAT, HOW, WHEN, WHERE, WHO).

### The Hierarchy

```
WHY (Most Important)
 ↓
WHAT (Decisions, outputs)
 ↓
HOW (Implementation)
 ↓
WHEN, WHERE, WHO (Execution details)
```

### Why This Matters

**Human Cognition**: Understanding purpose enables:
- Better decision-making (aligned with goals)
- Easier problem-solving (clear what success looks like)
- Natural prioritization (important vs. urgent clarity)
- Effective adaptation (can adjust approach while maintaining purpose)

**AI Resumption**: Future Claude instances need:
- Rationale to evaluate if decisions remain valid
- Context to understand assumptions and constraints
- Reasoning to continue work intelligently (not just mechanically)
- Alternatives to make different choices if context changes

**Collaboration**: User needs:
- Visibility into thinking quality (not just output quality)
- Ability to course-correct reasoning (not just outputs)
- Understanding of trade-offs and constraints
- Confidence that work is grounded in sound reasoning

### Application

**Before starting significant work**:
- WHY are we doing this? (Purpose, goal, problem being solved)
- WHY this approach? (Alternatives considered and rejected)
- WHY these priorities? (What makes them more important)
- WHY these boundaries? (Scope decisions and constraints)

**While documenting work**:
- Start with WHY (rationale, reasoning)
- Then WHAT (decisions, conclusions, outputs)
- Then HOW (methodology, approach)
- Then alternatives, assumptions, open questions

**In every file created or significantly modified**:
- Include "Design Decisions & Reasoning" section
- Document alternatives considered and rejected
- Make assumptions explicit
- Note open questions and uncertainties

---

## 2. MSc-Level Rigor

**Principle**: Apply academic-level standards to depth, evidence, and reasoning.

**User background**: MSc Computer Science (high standards for rigor and evidence)

**Requirements**:
- Claims must be evidence-based
- Sources must be credible and cited
- Reasoning must be explicit and logical
- Depth must go beyond surface-level
- Premature conclusions are unacceptable

**Application**:
- 5-10 minutes of web searches ≠ "research complete"
- Listing resources ≠ evaluating quality
- Finding textbooks ≠ studying content
- Surface understanding ≠ teaching-level mastery

---

## 3. Biomechanics Over Mysticism

**Principle**: Aikido is fundamentally biomechanical, not mystical. Ground all explanations in reproducible physical principles.

**Why**: (See `decisions.md` for full rationale)
- Biomechanical understanding is clear, teachable, works for all learners
- Mysticism excludes analytical learners and creates vagueness
- Scientific grounding enables MSc-level educational content

**Application**:
- Explain WHY techniques work (physics, anatomy, leverage)
- Translate traditional concepts into biomechanical language
- Use measurable principles (angles, forces, structure, timing)
- Avoid relying on vague concepts without concrete guidance

---

## 4. Session Continuity & State Preservation

**Principle**: System must enable effective resumption across sessions and instances.

**Why**:
- Work spans multiple sessions over days/weeks/months
- Multiple Claude instances may work simultaneously
- User must be able to resume work efficiently
- Progress must be preserved, not lost

**Requirements**:
- All significant thinking documented in files (not just in conversation)
- State explicitly tracked (current-objective.md, session-context.md)
- Instance coordination (registry.md, multi-instance support)
- Clear resumption points (/resume, /checkpoint)

**Application**:
- Use `/resume` at session start (load context)
- Use `/checkpoint` at session end (save and commit)
- Use `/save-objective` during work (crash recovery)
- Document WHY in files for future resumption

---

## 5. Scope Boundaries & Pragmatism

**Principle**: Define clear boundaries to prevent unlimited scope creep. Aim for "good enough to achieve goals", not "perfect omniscient knowledge".

**Why**:
- Every domain can expand infinitely (PhD-level study)
- Perfect is the enemy of good
- Functional sufficiency enables action
- Can expand boundaries if gaps discovered

**Application**:
- Define IN-SCOPE and OUT-OF-SCOPE explicitly
- Use 80/20 rule (20% of knowledge → 80% of effectiveness)
- Set "good enough" thresholds (functional sufficiency)
- Document assumptions and constraints
- Re-evaluate boundaries if context changes

---

## 6. Multi-Instance Parallelism

**Principle**: Leverage AI capability to run multiple agents/instances in parallel for complex work.

**Why**:
- AI can work on multiple tasks simultaneously (humans cannot)
- Parallel work is faster than sequential
- Different domains can be researched independently
- Integration happens after parallel exploration

**Requirements**:
- Clear instance coordination (registry.md)
- Isolated instance state (per-instance directories)
- Shared context (session-context.md, topics.md, decisions.md)
- Integration strategy (how parallel work combines)

**Application**:
- Use multiple instances for different objectives
- Use Task tool with multiple agents for parallel research
- Coordinate through shared files and registry
- Integrate outputs systematically

---

## 7. Progressive Learning & Iteration

**Principle**: Build knowledge systematically. Start with fundamentals, deepen over time. Iterate and refine.

**Why**:
- Cannot learn everything at once
- Foundations enable advanced understanding
- Early understanding is provisional (will evolve)
- Iteration reveals gaps and refinements

**Application**:
- Prioritize critical gaps first
- Build on existing strengths
- Accept that early frameworks will evolve
- Document evolution of thinking
- Revisit and refine as understanding deepens

---

## 8. User-Driven, AI-Assisted

**Principle**: User sets direction and validates decisions. AI assists, researches, and executes. User has final say.

**Why**:
- User's goals, context, and expertise matter
- AI makes assumptions that may be wrong
- User validates quality and alignment
- Collaboration produces better results than autonomy

**Application**:
- Ask clarifying questions before significant work
- Present reasoning for user validation
- Accept course corrections gracefully
- Don't declare work "complete" prematurely
- Document user feedback and decisions

---

## 9. Institutional Memory in Files

**Principle**: Knowledge lives in files, not conversations. Files persist, conversations don't.

**Why**:
- Conversations are ephemeral (lost after session)
- Files persist across sessions and instances
- Future Claude instances can read files, not past conversations
- User can review files independently

**Application**:
- Document decisions in files (`decisions.md`)
- Document research in files (`research/`)
- Document progress in files (`current-objective.md`)
- Document rationale in files (WHY sections)
- Don't rely on conversation history for continuity

---

## 10. Quality Over Speed

**Principle**: Thoughtful, thorough work is better than fast, shallow work.

**Why**:
- User has MSc-level expectations
- Premature conclusions waste time (require rework)
- Shallow understanding doesn't support teaching or writing
- Speed without quality is counterproductive

**Application**:
- Don't declare tasks "complete" after 5-10 minutes
- Don't accept surface-level understanding
- Take time to think deeply about WHY
- Accept that good work takes time
- Prioritize doing it right over doing it fast

---

## How to Apply These Principles

### At Session Start
1. Read workflow-protocol.md and CLAUDE.md
2. Resume with context (`/resume`)
3. Understand WHY you're doing current work
4. Check assumptions are still valid

### During Work
1. Start with WHY before jumping to solutions
2. Document thinking in files, not just outputs
3. Make assumptions explicit
4. Consider alternatives and trade-offs
5. Define success criteria

### Before Completing Tasks
1. Have I documented the WHY?
2. Are assumptions explicit?
3. Are alternatives considered?
4. Is reasoning sound and complete?
5. Will future Claude understand this?

### At Session End
1. Update current-objective.md with progress and thinking
2. Update session-context.md with status
3. Commit with `/checkpoint`
4. Leave clear resumption point

---

## Violations & Course Corrections

### Common Violations

**❌ Premature Completion**: Declaring work done after surface-level effort
- **Correction**: Define "done" criteria, apply MSc-level standards

**❌ Conclusions Without Reasoning**: Presenting WHAT without WHY
- **Correction**: Document WHY first, then WHAT and HOW

**❌ Assumption Blindness**: Operating on unstated assumptions
- **Correction**: Make assumptions explicit, note uncertainties

**❌ Scope Creep**: Expanding work without boundaries
- **Correction**: Define IN/OUT scope, set "good enough" thresholds

**❌ Shallow Research**: Web searches without evaluation
- **Correction**: Actual evaluation, not just listing resources

### How to Handle Course Corrections

When user provides feedback or correction:
1. **Accept gracefully** - Don't defend, learn
2. **Understand WHY** - Why was approach insufficient?
3. **Document learning** - What principle was violated?
4. **Update files** - Correct persistent documentation
5. **Apply forward** - Integrate lesson into future work

---

## Meta-Principle: These Principles Evolve

**Principle**: This document itself should evolve as we learn what works.

**Application**:
- Add new principles as patterns emerge
- Refine existing principles based on experience
- Document violations and corrections
- Update based on user feedback
- Treat as living document, not static rules

---

*These principles guide all work in this project. When in doubt, start with WHY.*
