# Work Coordination System

**Purpose**: Enable safe parallel execution of work by multiple Claude instances and agents without conflicts or duplication.

**Last Updated**: 2025-11-01

---

## Problem This Solves

**Without coordination**:
- Multiple agents might work on same tasks
- File conflicts when writing to shared files
- No visibility into what's being worked on
- Duplicate effort
- Unclear what's available vs. claimed vs. complete

**With this system**:
- Each instance/agent has own claimed work file (no conflicts)
- Central view of available work
- Overlap detection before claiming
- Progress visibility across all instances
- Git-friendly (multiple files, clear ownership)

---

## Directory Structure

```
.claude/state/work/
├── README.md                    # This file - system documentation
├── available/                   # Work items ready to be claimed
│   ├── phase-2-biomechanics.md
│   ├── phase-3-syllabus.md
│   ├── phase-4-pedagogy.md
│   └── phase-5-youtube.md
├── claimed/                     # Active work (one file per instance/agent)
│   ├── 2025-11-01-1525.md      # Instance/agent owns this file exclusively
│   ├── 2025-11-01-1537.md
│   └── agent-biomechanics-001.md
└── completed/                   # Finished work items
    └── phase-1-architecture.md
```

---

## Core Principles

### 1. Single-Writer Per File
**Rule**: Each instance/agent ONLY writes to their own file in `claimed/`

**Benefits**:
- No merge conflicts
- Parallel-safe
- Git-friendly
- Clear ownership

### 2. Read Many, Write One
**Pattern**:
- Read `available/` to see what work exists (read-only)
- Read ALL `claimed/*.md` to see what others are doing (read-only)
- Write ONLY to `claimed/[my-id].md` (exclusive write)

### 3. Claim Before Execute
**Rule**: Before starting work, claim it by writing to your claimed file

**Why**:
- Makes work visible to others
- Enables overlap detection
- Prevents duplicate effort

### 4. Granular Work Items
**Rule**: Break work into claimable chunks

**Why**:
- Enables parallel work on same phase
- Reduces overlap risk
- Allows partial claiming

---

## File Formats

### Available Work Item

Template: `.claude/state/work/available/[work-name].md`

```markdown
# [Work Item Name]

**Status**: Available | Partially Claimed | Fully Claimed
**Priority**: High | Medium | Low
**Dependencies**: [What must be complete first]
**Estimated Effort**: Small | Medium | Large

## WHY This Work Matters

[Explanation of purpose and value]

## Scope

### What This Includes
- [Specific item 1]
- [Specific item 2]

### What This Excludes
- [Out of scope item 1]
- [Out of scope item 2]

## Deliverables

- [Deliverable 1 with location]
- [Deliverable 2 with location]

## Breakdown (Claimable Parts)

Can be split into smaller pieces if needed:

- [ ] Sub-task 1 (can be claimed independently)
- [ ] Sub-task 2 (can be claimed independently)
- [ ] Sub-task 3 (can be claimed independently)

## Success Criteria

- [Criterion 1 - how to know when complete]
- [Criterion 2]

## Resources

- [Template to use]
- [Reference docs]
- [Source materials]
```

### Claimed Work

Template: `.claude/state/work/claimed/[instance-id].md`

```markdown
# Work Claimed by [Instance/Agent ID]

**Instance**: [instance-id]
**Created**: [timestamp]
**Last Updated**: [timestamp]
**Status**: Active | Idle | Blocked

## Currently Working On

### [Work Item 1 Name]
- **Source**: available/[filename].md
- **Claimed**: [timestamp]
- **Status**: Not Started | In Progress | Blocked | Complete
- **Scope**: [What parts claimed - full or partial]
- **Progress**: [percentage or description]
- **Blockers**: [if any]
- **Deliverables Completed**: [list]

### [Work Item 2 Name]
[Same format]

## Completed (Move to completed/ when done)

### [Completed Work Item]
- **Completed**: [timestamp]
- **Deliverables**: [what was created]
- **Notes**: [anything useful for others]

## Notes

[Any context, decisions, learnings]
```

### Completed Work

Template: `.claude/state/work/completed/[work-name].md`

```markdown
# [Work Item Name] - COMPLETED

**Completed By**: [instance-id]
**Completed**: [timestamp]
**Status**: Complete

## What Was Delivered

- [Deliverable 1] - Location: [path]
- [Deliverable 2] - Location: [path]

## Scope Completed

[What was included in this completion]

## Notes

[Useful context for future work or users]

## Validation

- [ ] Meets success criteria
- [ ] Deliverables in correct locations
- [ ] Documentation complete
- [ ] Cross-references updated (if applicable)
```

---

## Workflow

### Before Claiming Work

1. **Check available work**:
   ```
   ls .claude/state/work/available/
   ```

2. **Read work item**:
   ```
   cat .claude/state/work/available/phase-X-name.md
   ```

3. **Check if already claimed**:
   ```
   grep -r "phase-X-name" .claude/state/work/claimed/
   ```

4. **Review all claimed work** (see what others are doing):
   ```
   cat .claude/state/work/claimed/*.md
   ```

### Claiming Work

1. **Create or update your claimed file**:
   ```
   .claude/state/work/claimed/[your-instance-id].md
   ```

2. **Add work item to your claimed file**:
   - Include: what you're claiming, scope, timestamp
   - Be specific about what parts if partial claim

3. **Update available work item** (optional):
   - Mark as "Partially Claimed" if you're only taking part
   - Mark as "Fully Claimed" if you're taking all

### During Work

1. **Update progress regularly**:
   - Update your claimed file with progress
   - Note any blockers
   - List completed deliverables

2. **Update last updated timestamp**

### Completing Work

1. **Finalize deliverables**:
   - Ensure all deliverables are in correct locations
   - Documentation complete
   - Cross-references updated

2. **Move to completed**:
   - Create file in `.claude/state/work/completed/[work-name].md`
   - Include what was delivered, where, and any notes

3. **Update your claimed file**:
   - Move item from "Currently Working On" to "Completed"
   - Or remove from claimed file entirely if moved to completed/

4. **Update available work item**:
   - Mark as complete
   - Or remove if fully completed

---

## Overlap Detection

### Manual Check (Before Claiming)

```bash
# See all claimed work
cat .claude/state/work/claimed/*.md

# Search for specific work item
grep -r "phase-X" .claude/state/work/claimed/

# Check your own work
cat .claude/state/work/claimed/[your-id].md
```

### Automated Check (Future Enhancement)

Create script or command that:
1. Reads proposed work
2. Reads all claimed/*.md files
3. Detects overlaps in scope
4. Reports conflicts
5. Suggests coordination

---

## Best Practices

### 1. Be Specific in Claiming
**Bad**: "Working on Phase 2"
**Good**: "Working on Phase 2 - Structural Principles only (5-7 principles). Excludes force, balance, efficiency principles."

### 2. Update Progress Regularly
- Update your claimed file during work
- Helps others see what's actively happening
- Helps you resume if interrupted

### 3. Communicate Blockers
- If blocked, note it in your claimed file
- Others can see and potentially help
- Prevents work from appearing stuck

### 4. Small, Clear Work Items
- Break large work into claimable chunks
- Makes parallel work easier
- Reduces overlap risk

### 5. Complete Fully or Hand Off Clearly
- Finish what you claim, or
- Document what's done and what remains
- Makes it easy for others to continue

---

## Future Enhancements

### Commands (To Be Built)

```bash
# Check what work is available
/check-available-work

# Claim work
/claim-work [work-item] [scope]

# Update progress
/update-work-progress [work-item] [status] [progress]

# Complete work
/complete-work [work-item]

# View all active work (across all instances)
/view-active-work

# Detect overlaps
/check-work-overlaps
```

### Automated Overlap Detection

Build tool that:
- Parses work items and claimed work
- Identifies scope overlaps
- Suggests conflict resolution
- Warns before claiming

### Work Visualization

Dashboard showing:
- Available work (not claimed)
- Active work (claimed, in progress)
- Completed work
- Who's working on what
- Progress across all work items

---

## Example: Claiming Phase 2 Work

### 1. Check Available

```bash
cat .claude/state/work/available/phase-2-biomechanics.md
```

Sees: Phase 2 has structural, force, balance, efficiency principles

### 2. Check Claimed

```bash
cat .claude/state/work/claimed/*.md
```

Sees: No one has claimed Phase 2 yet

### 3. Claim Part of It

Update `.claude/state/work/claimed/agent-bio-001.md`:

```markdown
# Work Claimed by agent-bio-001

**Instance**: agent-bio-001
**Last Updated**: 2025-11-01 16:30

## Currently Working On

### Phase 2: Biomechanics - Structural Principles Only
- **Source**: available/phase-2-biomechanics.md
- **Claimed**: 2025-11-01 16:30
- **Status**: In Progress
- **Scope**: Structural principles only (alignment, load transfer, stability)
  - INCLUDES: 5-7 structural principles
  - EXCLUDES: Force, balance, efficiency principles (available for others)
- **Progress**: 10% - researching kinesiology sources
- **Deliverables Completed**: None yet
```

### 4. Do the Work

Research, document principles, update progress regularly

### 5. Complete

When done, move to completed/ and update available work item

---

## Migration from Old System

**Old approach** (pre-work-coordination):
- Work tracked in instance objectives only
- No central visibility
- Manual coordination required
- Risk of conflicts

**New approach** (with work-coordination):
- Work items in `available/`
- Claims in `claimed/[instance-id].md`
- Completions in `completed/`
- System prevents conflicts

**Existing instances should**:
1. Document their current work in claimed/[instance-id].md
2. Following new format going forward
3. Gradually migrate to work item claiming

---

*This system enables safe, scalable parallel work execution across multiple Claude instances and agents.*
