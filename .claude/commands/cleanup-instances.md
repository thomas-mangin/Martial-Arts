# Cleanup Stale Instances

Interactive tool to manage stale instances (no heartbeat >24 hours).

## Usage

`/cleanup-instances`

No arguments needed - fully interactive.

## What It Does

1. **Scan for stale instances** (>24h since last heartbeat)
2. **Show each stale instance** with:
   - Instance ID
   - Age and last heartbeat
   - Last known work/objective
   - File locations
3. **Present options** for each:
   - **Archive**: Move to `_archived/`, preserve all data
   - **Delete**: Remove completely
   - **Keep**: Mark as intentionally kept (skip in future scans)
4. **Execute user choices**
5. **Update registry.md**

## Interactive Flow

```
Found 2 stale instances:

1. 2025-10-30-0900 (38 hours old)
   Last work: Quick typo fixes in documentation
   Last heartbeat: 2025-10-30 09:15
   Options: [A]rchive  [D]elete  [K]eep

2. 2025-10-29-1600 (2 days old)
   Last work: Research review task (incomplete)
   Last heartbeat: 2025-10-29 16:45
   Options: [A]rchive  [D]elete  [K]eep

What would you like to do?
```

User responds with choices, tool executes them.

## Implementation Notes

- Move archived instances to `.claude/state/instances/_archived/[instance-id]/`
- Delete removes directory completely
- Keep marks instance in registry (add note "Kept by user on [date]")
- Update registry.md after all operations
- Show summary of actions taken

---

*User-controlled cleanup ensures no work is lost accidentally.*
