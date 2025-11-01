# Work Coordination System - Quick Start

**Purpose**: Enable safe parallel work execution without conflicts.

**Last Updated**: 2025-11-01

---

## ⚡ Quick Commands

### Check What's Available
```bash
.claude/state/work/check-overlap.sh
```
Shows all available, claimed, and completed work.

### Check Specific Work Item Before Claiming
```bash
.claude/state/work/check-overlap.sh phase-2-biomechanics
```
Shows if work is already claimed and by whom.

### Claim Work
1. Check it's available (above command)
2. Create/edit your claimed file: `.claude/state/work/claimed/[your-instance-id].md`
3. Add work under `## Currently Working On` section
4. Include: source, scope, status, progress

---

## 📁 File Structure

```
.claude/state/work/
├── available/           # Work ready to claim
│   ├── phase-2-biomechanics.md
│   ├── phase-3-syllabus.md
│   ├── phase-4-pedagogy.md
│   └── phase-5-youtube-enhancement.md
├── claimed/             # Active work (one file per instance)
│   ├── [your-id].md    # Your claimed work (you own this)
│   └── [other-id].md   # Others' work (read only)
└── completed/           # Finished work
    └── phase-1-architecture.md
```

---

## ✅ Simple Workflow

### 1. Before Starting Work

**Check what's available**:
```bash
.claude/state/work/check-overlap.sh
```

**Pick a work item** from available/ directory

**Check if claimed**:
```bash
.claude/state/work/check-overlap.sh [work-item-name]
```

### 2. Claim the Work

**Create your claimed file** (if first time):
```bash
cat > .claude/state/work/claimed/[your-instance-id].md << 'EOF'
# Work Claimed by [Your Instance ID]

**Instance**: [your-instance-id]
**Created**: [timestamp]
**Last Updated**: [timestamp]
**Status**: Active

## Currently Working On

### [Work Item Name]
- **Source**: available/[work-item].md
- **Claimed**: [timestamp]
- **Status**: In Progress
- **Scope**: [What you're doing - be specific]
- **Progress**: 0% - just claimed
- **Blockers**: None
- **Deliverables Completed**: None yet

## Completed

*None yet*

## Notes

*Any context*
EOF
```

**OR update existing** claimed file with new work item.

### 3. During Work

**Update progress regularly**:
- Edit your `.claude/state/work/claimed/[your-id].md`
- Update progress percentage or description
- Note any blockers
- List completed deliverables

### 4. Complete Work

**When finished**:
1. Create completion file in `completed/[work-name].md`
2. Move item from "Currently Working On" to "Completed" in your claimed file
3. Update available work item status (if needed)

---

## 🛡️ Key Rules

### ✓ DO
- **Read** all claimed/*.md files before starting (see what others are doing)
- **Write** only to your own claimed file
- **Be specific** about scope (what you're including and excluding)
- **Update progress** regularly
- **Check overlap** before claiming

### ✗ DON'T
- **Don't** edit other instances' claimed files
- **Don't** claim work without checking overlap
- **Don't** be vague about scope (causes overlaps)
- **Don't** forget to update progress

---

## 📋 Templates

### Minimal Claimed Work Entry
```markdown
### [Work Item Name]
- **Source**: available/[work-item].md
- **Claimed**: 2025-11-01 16:30
- **Status**: In Progress
- **Scope**: [Specific scope - what's included/excluded]
- **Progress**: 25% - [what's done so far]
- **Blockers**: [Any issues or "None"]
- **Deliverables Completed**: [List or "None yet"]
```

### Partial Claim (Splitting Work)
```markdown
### Phase 2: Biomechanics - Structural Principles ONLY
- **Source**: available/phase-2-biomechanics.md
- **Claimed**: 2025-11-01 16:30
- **Status**: In Progress
- **Scope**: Structural principles only (5-7 principles)
  - INCLUDES: Alignment, load transfer, stability, posture
  - EXCLUDES: Force, balance, efficiency, interaction principles
- **Progress**: 10% - researching sources
- **Blockers**: None
- **Deliverables Completed**: None yet
```

---

## 🔍 Common Scenarios

### Scenario 1: Work Item Fully Available
✅ Claim it and start work

### Scenario 2: Work Item Partially Claimed
**Option A**: Claim different part (if splittable)
**Option B**: Coordinate with claimer
**Option C**: Choose different work

### Scenario 3: Work Item Fully Claimed
**Option A**: Wait for completion
**Option B**: Choose different work
**Option C**: Coordinate to help (if possible)

### Scenario 4: Want to Split Large Work
**OK!** Claim specific part, be explicit about scope in claimed file

---

## 💡 Tips

**Be Specific**:
- ❌ Bad: "Working on Phase 2"
- ✅ Good: "Working on Phase 2 - Structural Principles only (5-7 principles). Excludes force/balance/efficiency."

**Update Often**:
- Update your claimed file during work
- Helps others see what's actively happening
- Helps you resume if interrupted

**Coordinate**:
- If you see similar work claimed, reach out or adjust scope
- Better to coordinate than duplicate

**Small Chunks**:
- Claim smaller pieces if possible
- Easier to complete
- Enables more parallelism

---

## 📚 Full Documentation

See `README.md` in `.claude/state/work/` for complete documentation.

---

*This quick-start gets you working safely in parallel. Read README.md for deeper understanding.*
