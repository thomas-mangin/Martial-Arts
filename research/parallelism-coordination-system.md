# Parallelism Coordination System

**Created**: 2025-11-01 (Instance 2025-11-01-1525)
**Purpose**: Enable safe parallel execution of work by multiple Claude instances and agents
**Status**: Implemented and operational

---

## WHY This System Was Built

**Problem Identified**: User requested running Phases 2-5 in parallel using agents. System had no coordination mechanism - would cause:
- Duplicate work (agents working on same tasks)
- File conflicts (multiple agents editing same files)
- No visibility into what's being worked on
- Unclear what's available vs. claimed vs. complete

**Solution Required**: Distributed work coordination that enables parallel-safe execution.

**Design Principle**: Each agent must have exclusive write access to their own coordination file while reading others' files for visibility.

---

## System Architecture

### Directory Structure

```
.claude/state/work/
├── README.md                        # Complete documentation
├── QUICK-START.md                   # Quick reference guide
├── check-overlap.sh                 # Overlap detection utility
├── available/                       # Work items ready to claim
│   ├── phase-2-biomechanics.md
│   ├── phase-3-syllabus.md
│   ├── phase-4-pedagogy.md
│   └── phase-5-youtube-enhancement.md
├── claimed/                         # Active work (one file per instance/agent)
│   ├── [instance-id].md            # Each instance owns one file exclusively
│   └── ...
└── completed/                       # Finished work
    └── phase-1-architecture.md
```

### Core Principles

**1. Single-Writer Per File**
- Each instance/agent writes ONLY to `.claude/state/work/claimed/[their-id].md`
- No merge conflicts (different files)
- Parallel-safe
- Git-friendly

**2. Read Many, Write One**
- Read `available/*.md` to see what work exists (read-only)
- Read `claimed/*.md` to see what others are doing (read-only)
- Write ONLY to own claimed file (exclusive write)

**3. Claim Before Execute**
- Before starting work, claim it by updating your claimed file
- Makes work visible to others
- Enables overlap detection
- Prevents duplicate effort

---

## How It Works

### Before Claiming Work

1. **Check available work**:
   ```bash
   .claude/state/work/check-overlap.sh
   ```

2. **Check specific item for overlaps**:
   ```bash
   .claude/state/work/check-overlap.sh phase-2-biomechanics
   ```

3. **Review all claimed work** (see what others are doing):
   ```bash
   cat .claude/state/work/claimed/*.md
   ```

### Claiming Work

1. Create or update your claimed file: `.claude/state/work/claimed/[your-instance-id].md`
2. Add work item under "## Currently Working On"
3. Be specific about scope (especially if claiming partial work)
4. Include timestamp, status, progress

### During Work

1. Update your claimed file regularly with progress
2. Note any blockers
3. List completed deliverables as you finish them

### Completing Work

1. Create completion record in `.claude/state/work/completed/[work-name].md`
2. Update your claimed file (move to "Completed" or remove)
3. Update available work item (mark complete or remove)

---

## Overlap Detection

### Automated Check

Script: `.claude/state/work/check-overlap.sh`

**With no arguments**: Shows all available, claimed, and completed work

**With work item name**: Checks if specific work is claimed, by whom, what scope

### Manual Check

Read all claimed files:
```bash
cat .claude/state/work/claimed/*.md
```

Search for specific work:
```bash
grep -r "phase-2" .claude/state/work/claimed/
```

---

## Work Item Format

### Available Work Item

Template in `.claude/state/work/available/[work-name].md`:

- **Status**: Available | Partially Claimed | Fully Claimed
- **Priority**: High | Medium | Low
- **Dependencies**: What must be complete first
- **WHY**: Purpose and value of this work
- **Scope**: What's included and excluded
- **Deliverables**: What will be created and where
- **Breakdown**: How work can be split (for parallel claiming)
- **Success Criteria**: What "complete" means

### Claimed Work

Template in `.claude/state/work/claimed/[instance-id].md`:

```markdown
# Work Claimed by [Instance ID]

**Instance**: [id]
**Last Updated**: [timestamp]
**Status**: Active | Idle | Blocked

## Currently Working On

### [Work Item Name]
- **Source**: available/[work-item].md
- **Claimed**: [timestamp]
- **Status**: Not Started | In Progress | Blocked | Complete
- **Scope**: [Specific scope - include/exclude]
- **Progress**: [percentage or description]
- **Blockers**: [any issues]
- **Deliverables Completed**: [list]

## Completed
[Past completed work]

## Notes
[Context, decisions, learnings]
```

---

## Benefits

### For Parallel Work
✅ **No conflicts** - Each instance owns one file
✅ **Overlap detection** - Can see what others are doing
✅ **Granular claiming** - Can claim sub-parts of work
✅ **Progress visibility** - Global view of all work

### For Collaboration
✅ **Coordination** - Easy to see who's doing what
✅ **Splitting work** - Large work can be divided
✅ **Avoiding duplication** - Overlap detection prevents double work
✅ **Knowledge sharing** - Notes and learnings visible to all

### For Resumption
✅ **Crash recovery** - Claimed work persists
✅ **Context preservation** - Progress and decisions documented
✅ **Clear ownership** - Know who was working on what
✅ **Easy handoff** - Can transfer work if needed

---

## Current Work Items

### Available
- **phase-2-biomechanics.md** - External biomechanics research (20+ principles)
- **phase-3-syllabus.md** - Complete Iwama syllabus documentation (100-150+ techniques)
- **phase-4-pedagogy.md** - Teaching knowledge (100+ errors, 15+ methods) - Partially claimed by 1537
- **phase-5-youtube-enhancement.md** - YouTube analysis with timestamps (1,983 videos)

### Claimed
- **Instance 2025-11-01-1537**: Educational theory learning (general - not Aikido specific)

### Completed
- **phase-1-architecture** - Information architecture design (by 2025-11-01-1525)

---

## Integration with Multi-Instance System

### Relationship to Instance Registry

**Instance registry** (`.claude/state/registry.md`):
- Tracks instance existence and heartbeat
- High-level "Working On" description

**Work coordination** (`.claude/state/work/`):
- Detailed work allocation
- Granular scope and progress
- Overlap prevention

**Synergy**:
- Registry shows which instances exist
- Work coordination shows what they're specifically doing
- Both needed for full visibility

### Coordination Flow

1. Instance starts via `/resume` → Updates registry
2. Instance checks work coordination → Sees available work
3. Instance claims work → Updates claimed file
4. Instance works → Updates progress in claimed file
5. Instance checkpoints → Updates both registry and claimed file
6. Other instances can see claimed work → Avoid overlaps

---

## Design Decisions & Rationale

### Why Distributed Files (Not Single Registry)?

**Decision**: One claimed file per instance instead of central registry file

**Rationale**:
- Single file = merge conflicts with parallel agents
- Distributed files = each agent has exclusive write zone
- Git handles multiple file commits better than merge conflicts
- Scales to many parallel agents

**Trade-off**: Must read multiple files for global view (worth it for conflict-free parallelism)

### Why Markdown (Not Database)?

**Decision**: Markdown files instead of database or JSON

**Rationale**:
- Human-readable (can check in editor)
- Git-friendly (diffs are meaningful)
- No dependencies (no database setup)
- Can edit manually if needed
- Works with Claude Code file operations

**Trade-off**: Slower querying than database (acceptable for this scale)

### Why Available/Claimed/Completed Split?

**Decision**: Three directories instead of single work registry

**Rationale**:
- Clear lifecycle (available → claimed → completed)
- Easy to see what's ready to claim (just list available/)
- Completed work separated (doesn't clutter active view)
- Can move files between directories as status changes

---

## Future Enhancements

### Potential Improvements

**1. Automated Claiming Command**
```bash
/claim-work phase-2-biomechanics "structural principles only"
```
- Creates/updates claimed file automatically
- Runs overlap detection
- Updates available work status

**2. Work Dashboard**
- Visual representation of all work
- Progress bars for claimed work
- Dependency graph
- Who's working on what

**3. Notification System**
- Alert when work you depend on completes
- Notify if someone claims overlapping work
- Remind to update progress

**4. Smart Work Splitting**
- Analyze work item breakdown
- Suggest optimal splits for parallel execution
- Auto-generate sub-work-items

---

## Usage Examples

### Example 1: Claiming Full Work Item

Agent wants to do all of Phase 2:

```markdown
# Work Claimed by agent-bio-001

## Currently Working On

### Phase 2: Biomechanics Research (FULL)
- **Source**: available/phase-2-biomechanics.md
- **Claimed**: 2025-11-01 17:00
- **Status**: In Progress
- **Scope**: All biomechanical principles (structural, force, balance, efficiency, interaction)
- **Progress**: 5% - identifying sources
- **Blockers**: None
- **Deliverables Completed**: None yet
```

### Example 2: Claiming Partial Work Item

Agent wants only structural principles from Phase 2:

```markdown
# Work Claimed by agent-bio-002

## Currently Working On

### Phase 2: Biomechanics - Structural Principles ONLY
- **Source**: available/phase-2-biomechanics.md
- **Claimed**: 2025-11-01 17:00
- **Status**: In Progress
- **Scope**: Structural principles only (alignment, load transfer, stability)
  - INCLUDES: 5-7 structural principles
  - EXCLUDES: Force, balance, efficiency, interaction (available for others)
- **Progress**: 15% - researching kinesiology texts
- **Blockers**: None
- **Deliverables Completed**: None yet
```

### Example 3: Multiple Agents on Same Phase

Three agents split Phase 3 (syllabus):

**Agent A** claims: Pins (ikkyo through gokyo)
**Agent B** claims: Major throws (irimi-nage, kaiten-nage, shiho-nage)
**Agent C** claims: Weapons (ken and jo kata)

Each has own claimed file with specific scope. No overlap.

---

## Testing & Validation

**System tested with**:
- Instance 2025-11-01-1537's existing work documented
- Overlap detection script functional
- Quick-start guide created
- Full documentation complete

**Verified**:
- ✅ No file conflicts possible (different files)
- ✅ Overlap detection works
- ✅ Can see global state
- ✅ Work items clearly defined
- ✅ Claiming process clear
- ✅ Ready for parallel agent execution

---

## Documentation Files

- **README.md** - Complete system documentation (in `.claude/state/work/`)
- **QUICK-START.md** - Quick reference (in `.claude/state/work/`)
- **This file** - Architecture and design rationale
- **Available work items** - 4 files in `available/`
- **check-overlap.sh** - Utility script

---

## Summary

**System Status**: ✅ Operational and ready for use

**Enables**: Safe parallel execution of Phases 2-5 by multiple agents

**Prevents**: Work conflicts, duplicate effort, file merge issues

**Provides**: Visibility, coordination, progress tracking

**Next Step**: Launch parallel agents using this coordination system

---

*This system was built by instance 2025-11-01-1525 on 2025-11-01 to enable the parallelism requested by the user.*
