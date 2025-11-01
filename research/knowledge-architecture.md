# Knowledge Architecture for Educational Authoring

**Purpose**: Define the complete knowledge domains needed to support serious educational authoring about Aikido (Iwama style). This is the foundation for all research and information collection.

**Last Updated**: 2025-11-01

---

## Overview

This document defines:
- What knowledge domains exist
- What information must be captured in each
- How domains relate to each other
- What constitutes "complete" for each domain
- Information structures needed

**Principle**: We cannot collect knowledge effectively without knowing how to organize it.

---

## Knowledge Domain Map

```
┌─────────────────────────────────────────────────────────────┐
│                    EDUCATIONAL CONTENT                       │
│              (What we eventually author)                     │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │
                    Built from foundation:
                              │
┌─────────────────────────────────────────────────────────────┐
│                   KNOWLEDGE FOUNDATION                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────┐  ┌──────────────────┐                │
│  │   TECHNICAL      │  │  BIOMECHANICAL   │                │
│  │    SYLLABUS      │◄─┤   PRINCIPLES     │                │
│  │                  │  │                  │                │
│  │ • Techniques     │  │ • Universal laws │                │
│  │ • Variations     │  │ • Body mechanics │                │
│  │ • Progressions   │  │ • Physics/anatomy│                │
│  └────────┬─────────┘  └────────┬─────────┘                │
│           │                     │                            │
│           │    ┌────────────────┘                            │
│           │    │                                             │
│           ▼    ▼                                             │
│  ┌──────────────────┐  ┌──────────────────┐                │
│  │   PEDAGOGICAL    │  │  PHILOSOPHICAL/  │                │
│  │   INTELLIGENCE   │  │   CONTEXTUAL     │                │
│  │                  │  │                  │                │
│  │ • Common errors  │  │ • Purpose/ethics │                │
│  │ • Teaching       │  │ • Application    │                │
│  │ • Learning       │  │ • History        │                │
│  └──────────────────┘  └──────────────────┘                │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Domain 1: Technical Syllabus

**What it is**: Complete documentation of all techniques in the Iwama Aikido curriculum.

### Scope

#### 1.1 Empty-Hand Techniques (Taijutsu)
**Fundamental Techniques (Kihon Waza)**:
- Ikkyo (omote/ura)
- Nikyo (omote/ura)
- Sankyo (omote/ura)
- Yonkyo (omote/ura)
- Gokyo (omote/ura)
- Irimi-nage
- Kaiten-nage
- Tenchi-nage
- Koshi-nage
- Kote-gaeshi
- Shiho-nage
- Aiki-otoshi
- Sumi-otoshi
- Etc.

**Attack Types** (for each technique):
- Katate-dori (single-hand grab)
- Ryote-dori (two-hand grab)
- Kata-dori (shoulder grab)
- Mune-dori (chest grab)
- Shomen-uchi (front strike)
- Yokomen-uchi (side strike)
- Tsuki (thrust)
- Etc.

**Training Contexts**:
- Suwari-waza (seated techniques)
- Hanmi-handachi (mixed seated/standing)
- Tachi-waza (standing techniques)

#### 1.2 Weapons (Aiki-ken and Aiki-jo)
**Aiki-ken (Sword)**:
- Suburi (solo practice - 7 kata)
- Kumitachi (paired practice - 10 kata)
- Ken tai jo (sword vs. jo)

**Aiki-jo (Staff)**:
- Suburi (solo practice - 20 movements)
- Kumijo (paired practice - 13 kata)
- Jo tai jo (staff vs. staff)

**Weapons Integration**:
- Relationship between weapons and taijutsu
- Principle transfer
- Timing and ma-ai (distance)

#### 1.3 Progressive Structure
- Beginner curriculum (what to learn first)
- Intermediate progressions
- Advanced refinements
- Testing requirements (kyu/dan levels)

### Information to Capture (Per Technique)

For each technique, we need:

1. **Basic Identification**
   - Name (Japanese and English)
   - Category (pin, throw, etc.)
   - Attack type
   - Training context (suwari/tachi/hanmi-handachi)
   - Variation (omote/ura)

2. **Technical Execution**
   - Initial positioning (kamae)
   - Entry (footwork, body angle, timing)
   - Breaking balance (kuzushi - direction, method)
   - Control/execution phase
   - Finishing position/pin
   - Key technical points

3. **Biomechanical Analysis**
   - Which principles are at play (references to Domain 2)
   - How each principle manifests in this technique
   - Why the technique works (mechanical explanation)

4. **Progressive Learning**
   - Prerequisites (what must be learned first)
   - Beginner version (simplified, fundamental)
   - Intermediate refinements
   - Advanced refinements
   - Mastery-level subtleties

5. **Variations and Applications**
   - Standard variations (different entries, angles)
   - Response to resistance
   - Dynamic/flowing applications
   - Multiple attackers considerations

6. **Cross-References**
   - Related techniques (similar principles)
   - Techniques this enables learning
   - Weapons connections (if applicable)

### What "Complete" Means

Technical Syllabus is complete when:
- ✓ All techniques in Iwama curriculum are documented
- ✓ All attack variations are covered
- ✓ All training contexts are addressed
- ✓ Technical execution is clear enough to learn from
- ✓ Biomechanical principles are identified for each
- ✓ Progressive learning paths are defined
- ✓ Cross-references are comprehensive

### Information Structure Needed

See: `templates/technique-template.md` (to be created)

---

## Domain 2: Biomechanical Principles

**What it is**: Universal principles of body mechanics, physics, and anatomy that explain why techniques work.

### Scope

#### 2.1 Structural Principles
How the body creates and maintains structural integrity:
- Alignment and posture
- Load transfer through skeleton vs. muscles
- Joint mechanics and limitations
- Stability vs. mobility
- Center of gravity and base
- Root and connection to ground

#### 2.2 Force Generation and Transfer
How force is created and transmitted:
- Ground reaction forces
- Kinetic chain principles
- Hip rotation and power generation
- Wave motion through body
- Leverage and mechanical advantage
- Timing and coordination

#### 2.3 Balance and Movement
Understanding balance and its disruption:
- Types of balance (static, dynamic, reactive)
- Breaking balance (kuzushi) mechanics
- Recovery mechanisms
- Prediction and anticipation
- Ma-ai (distance/spacing)

#### 2.4 Efficiency and Economy
Minimizing effort, maximizing effect:
- Minimal muscle activation
- Natural body mechanics
- Relaxation vs. tension
- Breathing and internal coordination
- Sustainability and fatigue prevention

#### 2.5 Partner Interaction
Principles specific to working with another person:
- Blending and matching
- Leading and following
- Connection and sensitivity
- Receiving and giving force
- Breaking structure vs. moving through structure

### Information to Capture (Per Principle)

For each principle, we need:

1. **Identification**
   - Name
   - Category (structural, force, balance, etc.)
   - Aliases (what different instructors call it)

2. **Definition**
   - Clear, precise definition
   - What it IS
   - What it is NOT (common confusions)

3. **Scientific Basis**
   - Anatomical explanation (what body parts/systems)
   - Physical explanation (force, leverage, momentum, etc.)
   - Engineering analogs (if applicable)
   - Sources (kinesiology texts, research, etc.)

4. **Manifestation in Aikido**
   - How it appears in techniques
   - Examples (primary techniques that demonstrate it)
   - Visual/kinesthetic indicators

5. **Teaching Approach**
   - How to explain to students
   - Effective metaphors and analogies
   - Demonstration methods
   - Experiential exercises to feel it
   - Common misunderstandings and corrections

6. **Relationships**
   - Related principles (complements, prerequisites)
   - Techniques that use this principle (cross-reference to Domain 1)
   - Progression (simple → complex applications)

### What "Complete" Means

Biomechanical Principles is complete when:
- ✓ Principles are exhaustive (cover all phenomena we observe)
- ✓ Scientifically grounded (backed by anatomy/physics/kinesiology)
- ✓ Clearly defined and explained
- ✓ Teaching approaches are effective
- ✓ All techniques can be explained by principles
- ✓ No unexplained "magic" or mystery

### Information Structure Needed

See: `templates/principle-template.md` (to be created)

### External Research Required

- Kinesiology textbooks
- Biomechanics resources
- Anatomy references
- Physics (classical mechanics)
- Structural engineering principles
- Sports science research
- Motor learning literature

---

## Domain 3: Pedagogical Intelligence

**What it is**: Knowledge about how people learn Aikido, what they get wrong, and how to teach effectively.

### Scope

#### 3.1 Common Errors
Systematic documentation of what practitioners do wrong:
- Beginner errors (fundamental misunderstandings)
- Intermediate errors (refinement issues)
- Advanced errors (subtle problems)
- Universal errors (across all levels)

#### 3.2 Learning Progressions
How mastery develops:
- Stages of learning (unconscious incompetence → unconscious competence)
- What each stage looks like
- Typical timelines and milestones
- Prerequisites and dependencies
- Plateaus and breakthroughs

#### 3.3 Teaching Methodology
Effective approaches to instruction:
- How to introduce techniques
- Demonstration methods
- Verbal cues and explanations
- Correction approaches
- Drill design and practice methods
- Solo training guidance
- Partner training guidance

#### 3.4 Assessment and Correction
How to identify and fix problems:
- Observation skills (what to watch for)
- Diagnostic approaches (root cause analysis)
- Correction strategies
- Feedback methods
- Testing and evaluation

### Information to Capture

#### 3.1.1 Per Error Type

For each common error:

1. **Identification**
   - Name/description of error
   - Which technique(s) it appears in
   - Which level (beginner/intermediate/advanced)
   - Prevalence (how common)

2. **Description**
   - What the practitioner does wrong (observable)
   - What it looks/feels like
   - How to recognize it as instructor
   - How it manifests (outcomes, indicators)

3. **Root Cause**
   - Why they do it (misunderstanding, physical limitation, fear, habit)
   - Which principle is being violated (cross-reference to Domain 2)
   - Underlying misconception

4. **Correction**
   - How to explain what's wrong
   - How to demonstrate correct version
   - Drills/exercises to fix it
   - Cues and metaphors that work
   - Progressive correction (stages)

5. **Prevention**
   - How to teach to avoid this error
   - What to emphasize from the start
   - Warning signs to watch for

#### 3.1.2 Per Teaching Method

For each teaching approach:

1. **Method Description**
   - What it is
   - When to use it
   - Who it works for (learning styles, levels)

2. **Implementation**
   - How to apply it
   - Examples in practice
   - Variations

3. **Effectiveness**
   - What it achieves
   - What it doesn't achieve
   - Evidence/experience supporting it

### What "Complete" Means

Pedagogical Intelligence is complete when:
- ✓ Common errors are comprehensively documented
- ✓ Learning progressions are clearly mapped
- ✓ Teaching methods are validated and effective
- ✓ Instructors can use this to teach better
- ✓ Self-directed learners can use this to learn better
- ✓ Errors can be diagnosed and corrected systematically

### Information Structure Needed

See: `templates/error-template.md` (to be created)
See: `templates/teaching-method-template.md` (to be created)

### Sources

- Personal teaching experience
- Observations from sensei
- Student feedback
- YouTube instructor analysis (teaching methods)
- Education/pedagogy research
- Motor learning research

---

## Domain 4: Philosophical and Contextual

**What it is**: The "why" behind Aikido - purpose, ethics, application contexts, history.

### Scope

#### 4.1 Purpose and Philosophy
- What Aikido is for
- O-Sensei's vision and intent
- Modern interpretations
- Peace/violence dialectic
- Martial effectiveness vs. spiritual development

#### 4.2 Ethical and Legal Context
- When/how to apply techniques
- Legal implications of use
- Ethical considerations
- Responsibility of knowledge

#### 4.3 Historical and Traditional Context
- Lineage (Ueshiba → Saito → current)
- Evolution of techniques
- Cultural context (Japanese martial tradition)
- Traditional training methods
- Modern adaptations

#### 4.4 Application Contexts
- Self-defense realities
- Military/law enforcement applications
- Sport/competition (where applicable)
- Health/fitness applications
- Psychological/spiritual applications

### Information to Capture

This domain is less structured than others, but needs:

1. **Documented Perspectives**
   - Various viewpoints on purpose/philosophy
   - Your veteran/military perspective
   - Traditional perspectives
   - Modern perspectives

2. **Ethical Frameworks**
   - When force is justified
   - How to apply techniques responsibly
   - Legal boundaries
   - Moral considerations

3. **Historical Documentation**
   - Lineage verification
   - Technique evolution
   - Cultural context
   - Traditional practices

### What "Complete" Means

Philosophical/Contextual is complete when:
- ✓ Multiple perspectives are documented
- ✓ Ethical frameworks are clear
- ✓ Historical accuracy is verified
- ✓ Application contexts are realistic
- ✓ Purpose is articulated clearly

### Information Structure Needed

Less templated, more essay/discussion format.
See: `templates/philosophical-discussion-template.md` (to be created)

---

## Cross-Domain Integration

**Critical**: These domains are not silos. They must be connected.

### Integration Points

1. **Technique ↔ Principle**
   - Every technique references principles that explain it
   - Every principle lists techniques that use it
   - Two-way navigation

2. **Technique ↔ Common Errors**
   - Every technique documents common errors
   - Every error references which technique(s)
   - Error explanations reference which principle was violated

3. **Principle ↔ Common Errors**
   - Errors explained by principle violations
   - Understanding principle prevents/corrects errors

4. **Principle ↔ Teaching Methods**
   - How to teach each principle
   - Which methods work for which principles

5. **All Domains ↔ Philosophical Context**
   - Why we teach techniques this way (philosophy)
   - Why principles matter (purpose)
   - Ethics of application

### Cross-Reference System Requirements

Need ability to:
- From any technique → see all related principles, errors, teaching notes
- From any principle → see all techniques using it, how to teach it
- From any error → see principle explanation, correction methods
- Navigate the knowledge web fluidly

---

## Completeness Criteria (Overall)

The knowledge foundation is ready for authoring when:

1. **Comprehensive**
   - All techniques documented
   - All principles identified and explained
   - Common errors captured
   - Teaching methods validated

2. **Validated**
   - Scientifically grounded (biomechanics)
   - Traditionally accurate (Iwama lineage)
   - Practically tested (works in training)
   - Multi-source confirmed (multiple instructors/resources agree)

3. **Integrated**
   - Cross-references are complete
   - Knowledge web is navigable
   - Connections are clear
   - No orphaned information

4. **Usable**
   - Can support authoring (test by writing sample chapter)
   - Instructors can use it to teach
   - Students can use it to learn
   - Clear and well-organized

5. **Extensible**
   - Structure allows additions
   - Can grow as we learn more
   - Can accommodate new discoveries

---

## Information Architecture Summary

### File/Directory Structure (Proposed)

```
knowledge-base/
├── techniques/
│   ├── empty-hand/
│   │   ├── pins/
│   │   │   ├── ikkyo-omote-katatedori.md
│   │   │   ├── ikkyo-ura-katatedori.md
│   │   │   └── ...
│   │   ├── throws/
│   │   └── ...
│   └── weapons/
│       ├── ken/
│       └── jo/
├── principles/
│   ├── structural/
│   ├── force/
│   ├── balance/
│   └── ...
├── pedagogy/
│   ├── common-errors/
│   │   ├── beginner/
│   │   ├── intermediate/
│   │   └── advanced/
│   ├── teaching-methods/
│   └── learning-progressions/
├── philosophy/
│   ├── purpose/
│   ├── ethics/
│   └── history/
└── indexes/
    ├── technique-index.md
    ├── principle-index.md
    ├── error-index.md
    ├── cross-reference-technique-to-principle.md
    ├── cross-reference-principle-to-technique.md
    └── ...
```

### Templates Needed

1. `templates/technique-template.md` - For documenting techniques
2. `templates/principle-template.md` - For documenting principles
3. `templates/error-template.md` - For documenting common errors
4. `templates/teaching-method-template.md` - For teaching approaches
5. `templates/philosophical-discussion-template.md` - For contextual discussions

### Validation Checklists Needed

1. `validation/technique-completeness-checklist.md`
2. `validation/principle-validation-checklist.md`
3. `validation/pedagogy-validation-checklist.md`
4. `validation/integration-validation-checklist.md`

---

## Next Steps

1. ✓ Define knowledge domains (this document)
2. ⧖ Create templates for each domain
3. ⧖ Create validation checklists
4. ⧖ Test by documenting one complete example from each domain
5. ⧖ Refine based on testing
6. ⧖ Begin systematic knowledge capture

---

*This architecture will evolve as we learn what works and what doesn't. It's a living document.*
