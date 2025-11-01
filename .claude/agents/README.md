# Agent Type Registry

**Purpose**: Specialized agents for executing Phases 2-5 work

---

## Available Agent Types

### 1. Research Agent (`research-agent.md`)
- **Purpose**: External knowledge acquisition and principle documentation
- **Primary work**: Phase 2 (Biomechanics Research)
- **Capabilities**: Literature research, principle extraction, scientific validation
- **Outputs**: Principle docs, bibliography

### 2. Documentation Agent (`documentation-agent.md`)
- **Purpose**: Systematic template-based documentation
- **Primary work**: Phase 3 (Syllabus), parts of Phase 4
- **Capabilities**: Technical documentation, template usage, cross-referencing
- **Outputs**: Technique docs, systematic documentation

### 3. Pedagogical Agent (`pedagogical-agent.md`)
- **Purpose**: Teaching knowledge capture
- **Primary work**: Phase 4 (Pedagogy)
- **Capabilities**: Error identification, correction methods, teaching wisdom
- **Outputs**: Error docs, teaching method docs

### 4. Analysis Agent (`analysis-agent.md`)
- **Purpose**: Video and source analysis
- **Primary work**: Phase 5 (YouTube Enhancement)
- **Capabilities**: Video analysis, timestamp cataloging, multi-source comparison
- **Outputs**: Timestamp catalogs, cross-reference analysis

### 5. Validation Agent (`validation-agent.md`)
- **Purpose**: Quality assurance
- **Primary work**: Cross-phase validation
- **Capabilities**: Checklist validation, completeness checking, gap identification
- **Outputs**: Validation reports, quality recommendations

### 6. Integration Agent (`integration-agent.md`)
- **Purpose**: Knowledge web building
- **Primary work**: Cross-phase integration
- **Capabilities**: Index creation, cross-referencing, relationship mapping
- **Outputs**: Indexes, cross-reference matrices

---

## How to Use

### Launching an Agent

**Via Task tool**:
```
Use Task tool with description including agent type:
"Launch Research Agent for Phase 2 structural principles"
```

**Manual launch**:
1. Read agent specification (`.claude/agents/[agent-type]-agent.md`)
2. Follow agent's work process
3. Claim work in coordination system
4. Execute using agent's capabilities
5. Deliver outputs per agent's standards

### Agent-to-Work Mapping

**Phase 2: Biomechanics**
→ Research Agent (1-5 agents, split by category)

**Phase 3: Syllabus**
→ Documentation Agent (1-3 agents, split by technique type)

**Phase 4: Pedagogy**
→ Pedagogical Agent (primary) + Documentation Agent (support)

**Phase 5: YouTube**
→ Analysis Agent (1-5 agents, split by instructor)

**All Phases**:
→ Validation Agent (quality assurance)
→ Integration Agent (cross-referencing)

---

## Agent Coordination

**All agents must**:
1. Check work availability (`.claude/state/work/check-overlap.sh`)
2. Claim work in coordination system
3. Update progress regularly
4. Use templates and validation checklists
5. Complete and document deliverables

**Agents coordinate through**:
- Work coordination system (claiming, tracking)
- Shared templates (consistent format)
- Validation checklists (quality standards)
- Cross-references (knowledge connections)

---

*Each agent type has detailed specification in its own file. Read before launching.*
