# System Maintenance Command

Launches the system-maintenance agent to audit, clean, sync, and optimize the project structure.

## Usage

`/system-maintenance [mode]`

**Modes:**
- `audit` - Health check report (read-only)
- `cleanup` - Archive old sessions, clean completed TODOs
- `sync` - Update cross-references and INDEX files
- `optimize` - Reduce token bloat, reorganize if needed
- `full` - All modes in sequence (audit → cleanup → sync → optimize → audit)

**Examples:**
- `/system-maintenance audit` - Check system health
- `/system-maintenance cleanup` - Clean old content
- `/system-maintenance sync` - Update INDEX files
- `/system-maintenance optimize` - Reduce token usage
- `/system-maintenance full` - Complete maintenance run

## What It Does

The agent loads complete system knowledge internally and:

**Audit mode:**
- Measures token usage in all key files
- Validates file structure and cross-references
- Checks INDEX completeness
- Detects bloat and stale content
- Generates comprehensive health report

**Cleanup mode:**
- Archives session summaries >90 days old
- Removes completed TODOs
- Identifies obsolete files
- Cleans empty directories

**Sync mode:**
- Updates research/INDEX.md with all research files
- Ensures agent/command pairs are synchronized
- Fixes broken file references
- Updates directory listings in documentation

**Optimize mode:**
- Reduces OVERVIEW.md to target size
- Streamlines command files
- Optimizes session-context.md
- Moves detailed content to appropriate locations

**Full mode:**
- Runs complete maintenance cycle
- Provides before/after comparison
- Shows all improvements made

## When to Use

- **Monthly**: Run `audit` to check system health
- **Quarterly**: Run `full` for comprehensive maintenance
- **After major changes**: Run `sync` to update cross-references
- **When /resume feels slow**: Run `optimize` to reduce tokens
- **When concerned**: Run `audit` to see what needs attention

## Result

Comprehensive report with:
- Health status (🟢🟡🔴)
- Issues found and fixed
- Token usage analysis
- Recommendations for next steps
- List of files modified (if write mode)

## Agent Loads Internally

The agent has complete system knowledge:
- All documentation files
- All agent and command definitions
- All INDEX and tracking files
- Directory structure
- Token usage targets

You only see the final report - no context bloat.

## Recommended Frequency

- `/system-maintenance audit` - Monthly
- `/system-maintenance full` - Quarterly
- `/system-maintenance optimize` - When token usage creeps up
- `/system-maintenance sync` - After adding new files

---

*This command keeps your system lean and optimized without using your context window.*
