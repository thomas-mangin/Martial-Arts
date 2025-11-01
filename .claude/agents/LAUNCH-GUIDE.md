# Agent Launch Guide

**Purpose**: How to launch and coordinate specialized agents for parallel knowledge base work
**Updated**: 2025-11-01

---

## Quick Start

**To launch agents for parallel Phases 2-5 execution:**

```bash
# 1. Check what work is available
.claude/state/work/check-overlap.sh

# 2. Launch agents using Task tool (multiple agents in parallel)
# See "Launching Multiple Agents in Parallel" section below

# 3. Monitor progress
# Check .claude/state/work/claimed/ directory for agent progress updates
```

---

## Available Agent Types

### Phase-Specific Agents

1. **Research Agent** (`.claude/agents/research-agent.md`)
   - **For**: Phase 2 - External Biomechanics Research
   - **Outputs**: Principle documentation, bibliography
   - **Launch when**: Need to document biomechanical principles from external sources

2. **Documentation Agent** (`.claude/agents/documentation-agent.md`)
   - **For**: Phase 3 - Iwama Syllabus Documentation
   - **Outputs**: Technique documentation (100-150 techniques)
   - **Launch when**: Need to document Aikido techniques systematically

3. **Pedagogical Agent** (`.claude/agents/pedagogical-agent.md`)
   - **For**: Phase 4 - Pedagogical Intelligence Collection
   - **Outputs**: Error documentation, teaching method documentation
   - **Launch when**: Need to capture teaching wisdom and common errors

4. **Analysis Agent** (`.claude/agents/analysis-agent.md`)
   - **For**: Phase 5 - YouTube Transcript Enhancement
   - **Outputs**: Timestamp catalogs, multi-source analyses, video indexes
   - **Launch when**: Need to structure and cross-reference video content

### Cross-Phase Agents

5. **Validation Agent** (`.claude/agents/validation-agent.md`)
   - **For**: Quality assurance across all phases
   - **Outputs**: Validation reports, gap analyses
   - **Launch when**: Need to verify completeness and quality

6. **Integration Agent** (`.claude/agents/integration-agent.md`)
   - **For**: Cross-domain knowledge connection
   - **Outputs**: Indexes, cross-reference matrices, learning pathways
   - **Launch when**: Substantial content exists and needs integration

---

## How to Launch an Agent

### Method 1: Using Task Tool (Recommended)

**For single agent**:
```
Use Task tool with:
- description: "Launch Research Agent for structural principles"
- prompt: "You are a Research Agent (see .claude/agents/research-agent.md).
           Your task: Document structural biomechanical principles for Phase 2.

           Process:
           1. Read your agent specification
           2. Check work overlap: .claude/state/work/check-overlap.sh phase-2-biomechanics
           3. Claim specific scope (structural principles only)
           4. Execute your work process
           5. Deliver outputs per your specification"
- subagent_type: "general-purpose"
```

**For multiple agents in parallel** (RECOMMENDED for Phases 2-5):
```
Send SINGLE message with multiple Task tool calls:

Task 1: Research Agent for Phase 2
Task 2: Documentation Agent for Phase 3
Task 3: Pedagogical Agent for Phase 4
Task 4: Analysis Agent for Phase 5
```

See "Launching Multiple Agents in Parallel" section for detailed example.

### Method 2: Manual Launch (Alternative)

**Steps**:
1. Read agent specification (`.claude/agents/[agent-type]-agent.md`)
2. Check work availability: `.claude/state/work/check-overlap.sh`
3. Claim work in new file: `.claude/state/work/claimed/[agent-id].md`
4. Follow agent's work process
5. Deliver outputs per agent's standards
6. Complete and document in `.claude/state/work/completed/`

**When to use**: For learning the system, debugging, or single-agent tasks.

---

## Launching Multiple Agents in Parallel

**Goal**: Execute Phases 2-5 simultaneously with multiple agents

**Approach**: Launch all 4 phase-specific agents in SINGLE message (parallel execution)

### Example: Full Parallel Launch

```
I want to launch 4 agents in parallel to execute Phases 2-5:

[Use Task tool 4 times in single message]

Task 1 - Research Agent:
- description: "Launch Research Agent for Phase 2"
- prompt: "You are a Research Agent (see .claude/agents/research-agent.md).

           Your task: Document biomechanical principles from external sources (Phase 2).

           Process:
           1. Read your specification: .claude/agents/research-agent.md
           2. Check overlap: .claude/state/work/check-overlap.sh phase-2-biomechanics
           3. Claim scope: Create .claude/state/work/claimed/research-agent-[timestamp].md
              - Claim PART of Phase 2 (e.g., structural principles only)
              - Document scope clearly (INCLUDES/EXCLUDES)
           4. Execute work:
              - Find 2-3 biomechanics textbooks (kinesiology, anatomy)
              - Extract 5-7 principles in your category
              - Document using templates/principle-template.md
              - Create bibliography
           5. Validate: Use validation/principle-validation-checklist.md
           6. Complete: Document deliverables

           Deliver: Principle docs in knowledge-base/principles/, bibliography in sources/books/"
- subagent_type: "general-purpose"

Task 2 - Documentation Agent:
- description: "Launch Documentation Agent for Phase 3"
- prompt: "You are a Documentation Agent (see .claude/agents/documentation-agent.md).

           Your task: Document Iwama Syllabus techniques systematically (Phase 3).

           Process:
           1. Read your specification: .claude/agents/documentation-agent.md
           2. Check overlap: .claude/state/work/check-overlap.sh phase-3-syllabus
           3. Claim scope: Create .claude/state/work/claimed/documentation-agent-[timestamp].md
              - Claim PART of Phase 3 (e.g., pins only: ikkyo through gokyo)
              - Document scope clearly (30-50 technique variations)
           4. Execute work:
              - For each technique, use templates/technique-template.md
              - Document: entry, kuzushi, control, finish (step-by-step)
              - Identify 2-3 biomechanical principles per technique
              - Note 2-3 common errors per technique
              - Cross-reference to principles
           5. Validate: Use validation/technique-completeness-checklist.md
           6. Complete: Document deliverables

           Deliver: Technique docs in knowledge-base/techniques/empty-hand/pins/"
- subagent_type: "general-purpose"

Task 3 - Pedagogical Agent:
- description: "Launch Pedagogical Agent for Phase 4"
- prompt: "You are a Pedagogical Agent (see .claude/agents/pedagogical-agent.md).

           Your task: Document common errors and teaching methods (Phase 4).

           Process:
           1. Read your specification: .claude/agents/pedagogical-agent.md
           2. Check overlap: .claude/state/work/check-overlap.sh phase-4-pedagogy
           3. Claim scope: Create .claude/state/work/claimed/pedagogical-agent-[timestamp].md
              - Claim PART of Phase 4 (e.g., beginner errors only)
              - Document scope clearly (40-50 errors)
           4. Execute work:
              - Identify common errors (stance, movement, power, timing, control)
              - For each error, use templates/error-template.md
              - Root cause analysis (which principles violated)
              - Document 2-3 correction methods per error
              - Cross-reference to techniques and principles
           5. Validate: Use validation/pedagogy-validation-checklist.md
           6. Complete: Document deliverables

           Deliver: Error docs in knowledge-base/pedagogy/errors/beginner/"
- subagent_type: "general-purpose"

Task 4 - Analysis Agent:
- description: "Launch Analysis Agent for Phase 5"
- prompt: "You are an Analysis Agent (see .claude/agents/analysis-agent.md).

           Your task: Create structured catalogs from YouTube transcripts (Phase 5).

           Process:
           1. Read your specification: .claude/agents/analysis-agent.md
           2. Check overlap: .claude/state/work/check-overlap.sh phase-5-youtube-enhancement
           3. Claim scope: Create .claude/state/work/claimed/analysis-agent-[timestamp].md
              - Claim PART of Phase 5 (e.g., Saito Sensei videos only)
              - Document scope clearly (which instructor, how many videos)
           4. Execute work:
              - Read transcripts from sources/youtube/transcripts/
              - Create timestamp catalogs for key moments
              - Note: technique demos, principle explanations, error corrections
              - Flag visual gaps (when transcript says 'watch this')
              - Create multi-source analyses for major topics
              - Cross-reference to techniques and principles
           5. Complete: Document deliverables

           Deliver: Catalogs in sources/youtube/catalogs/, analyses in sources/youtube/analyses/"
- subagent_type: "general-purpose"
```

**Result**: 4 agents execute in parallel, each claiming part of their phase's work.

---

## Coordination Patterns

### Pattern 1: Split Work by Category

**Phase 2 (Biomechanics)** - Split by principle category:
- Agent A: Structural principles (5-7 principles)
- Agent B: Force principles (5-7 principles)
- Agent C: Balance + Efficiency principles (5-7 principles)

**Phase 3 (Syllabus)** - Split by technique type:
- Agent A: Pins (ikkyo through gokyo - 30-50 variations)
- Agent B: Throws (irimi-nage, kaiten-nage, etc. - 40-60 variations)
- Agent C: Weapons (ken and jo kata - 20-30 techniques)

**Phase 4 (Pedagogy)** - Split by skill level:
- Agent A: Beginner errors (40-50 errors)
- Agent B: Intermediate errors (20-30 errors)
- Agent C: Advanced errors + teaching methods (15-20 errors + 15 methods)

**Phase 5 (YouTube)** - Split by instructor:
- Agent A: Saito Sensei videos (largest collection)
- Agent B: Saito (Hitohiro) Sensei videos
- Agent C: Other instructors

### Pattern 2: Sequential with Validation

**Phase execution**:
1. Launch phase-specific agents (research, documentation, pedagogical, analysis)
2. Agents execute, update progress regularly
3. When agent completes section, launch Validation Agent
4. Validation Agent checks quality, provides feedback
5. Phase-specific agent addresses critical issues
6. Continue until phase complete

**Integration**:
1. When substantial content exists, launch Integration Agent
2. Integration Agent creates indexes and cross-references
3. Updates indexes incrementally as more content added

### Pattern 3: Rolling Launch

**Instead of all at once**, launch agents as dependencies resolve:

**Week 1**: Launch Research Agents (Phase 2)
- Multiple agents for different principle categories
- Goal: Create 20-30 principle docs

**Week 2**: Launch Documentation Agents (Phase 3) + Continue Phase 2
- Phase 3 can reference Phase 2 principles (now available)
- Phase 2 agents continue if needed

**Week 3**: Launch Pedagogical Agents (Phase 4) + Continue Phase 2-3
- Phase 4 can reference Phase 2 principles and Phase 3 techniques

**Week 4**: Launch Analysis Agents (Phase 5) + Continue Phase 2-4
- Phase 5 can cross-reference all previous phases

**Ongoing**: Validation Agent + Integration Agent
- Validate as work progresses
- Integrate incrementally

---

## Monitoring Agent Progress

### Check Claimed Work

```bash
# See all claimed work
ls -la .claude/state/work/claimed/

# Read specific agent's progress
cat .claude/state/work/claimed/research-agent-2025-11-01-1600.md
```

**Look for**:
- **Status**: In Progress / Completed / Blocked
- **Progress**: Percentage and specific deliverables
- **Blockers**: Any issues preventing progress

### Check Completed Work

```bash
# See all completed work
ls -la .claude/state/work/completed/

# Read completion record
cat .claude/state/work/completed/phase-2-structural-principles.md
```

**Completion record shows**:
- What was delivered
- Where files are located
- Any notes or issues
- Handoff information

### Review Deliverables

**Check output locations**:
```bash
# Phase 2 outputs (principles)
ls knowledge-base/principles/structural/
ls knowledge-base/principles/force/

# Phase 3 outputs (techniques)
ls knowledge-base/techniques/empty-hand/pins/
ls knowledge-base/techniques/empty-hand/throws/

# Phase 4 outputs (errors, teaching methods)
ls knowledge-base/pedagogy/errors/beginner/
ls knowledge-base/pedagogy/teaching-methods/

# Phase 5 outputs (video catalogs)
ls sources/youtube/catalogs/
ls sources/youtube/analyses/
```

---

## Troubleshooting

### Problem: Agent claims work already claimed

**Solution**: Check overlap before claiming
```bash
.claude/state/work/check-overlap.sh [work-item-name]
```

If overlap exists, agent should claim DIFFERENT scope (different category, different subset).

### Problem: Agent can't find templates

**Solution**: Verify template location
```bash
ls templates/
# Should show: principle-template.md, technique-template.md, error-template.md, etc.
```

If missing, Phase 1 incomplete. Check `research/knowledge-architecture.md` for template requirements.

### Problem: Agent unsure what to claim

**Solution**: Read available work item
```bash
cat .claude/state/work/available/[phase-name].md
```

Available work items have "How to Split Work" sections with suggested scopes.

### Problem: Cross-references broken

**Solution**: Launch Validation Agent
```bash
# Validation Agent will check cross-references and report broken links
```

### Problem: Agent blocked on dependencies

**Examples**:
- Phase 3 agent needs Phase 2 principles (not yet documented)
- Phase 4 agent needs Phase 3 techniques (not yet documented)

**Solution**:
- Note "Cross-ref pending Phase X" in documentation
- Integration Agent will connect later when dependencies available
- Or wait for dependency phase to progress

---

## Best Practices

### For Users Launching Agents

1. **Launch multiple agents in parallel** (single message, multiple Task calls)
2. **Check overlap** before launching (avoid duplicate work)
3. **Provide clear scope** in launch prompt (what to claim, what to exclude)
4. **Monitor progress** regularly (check claimed files)
5. **Launch Validation Agent** periodically (catch issues early)
6. **Launch Integration Agent** when substantial content exists

### For Agents Executing Work

1. **Read your specification first** (understand your role and process)
2. **Check work overlap** before claiming (coordinate with others)
3. **Claim specific scope** (be precise about INCLUDES/EXCLUDES)
4. **Update progress regularly** (every 10-15 deliverables or major milestone)
5. **Use templates strictly** (ensures consistency)
6. **Validate before completing** (use appropriate checklist)
7. **Document deliverables clearly** (what, where, how many)

---

## Success Criteria

**Agent system succeeds when**:
- ✅ Multiple agents work in parallel without conflicts
- ✅ Work is claimed before execution (no surprises)
- ✅ Progress is visible (claimed files updated regularly)
- ✅ Outputs meet quality standards (validation passes)
- ✅ Knowledge domains integrated (indexes connect everything)
- ✅ User can see progress and deliverables clearly

---

## Next Steps After Launch

**After launching agents**:

1. **Monitor progress**: Check claimed files regularly
2. **Provide input when needed**: Agents may ask questions or note gaps
3. **Launch validation**: Periodically check quality
4. **Launch integration**: When content substantial, build knowledge web
5. **Iterate**: Based on validation feedback, refine and improve

**When all phases complete**:
- Full knowledge base documented
- Ready for educational content authoring
- Foundation solid for writing book/textbook-quality articles

---

*This guide enables safe parallel agent execution. Follow coordination patterns to avoid conflicts.*
