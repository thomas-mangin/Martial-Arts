# View Active Instances

Show all Claude Code instances currently working on this project, with status and progress.

## Usage

`/instances`

No arguments needed.

## What It Does

Displays comprehensive overview of all instances:
- Active instances with current work
- Idle instances (no recent activity)
- Stale instances (>24h old)
- Archived instances count

## Implementation

Read `.claude/state/registry.md` and all instance directories in `.claude/state/instances/`, then present formatted overview with:

1. **Active Instances** (heartbeat <1 hour):
   - Instance ID (timestamp)
   - Age (how long since created)
   - Last heartbeat (how long ago)
   - Current objective (from current-objective.md)
   - Progress summary

2. **Idle Instances** (heartbeat 1-24 hours):
   - Same info as active
   - Mark as idle/sleeping

3. **Stale Instances** (heartbeat >24 hours):
   - Same info
   - Suggest cleanup

4. **Statistics**:
   - Total, active, idle, stale, archived counts

5. **Helpful Commands**:
   - `/resume [instance-id]` to continue specific instance
   - `/cleanup-instances` to manage stale instances

---

*Quick visibility into all concurrent work across multiple Claude Code sessions.*
