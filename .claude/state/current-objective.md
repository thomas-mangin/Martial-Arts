# Current Objective

**Last Updated**: 2025-10-31 (current session)
**Status**: In Progress

---

## Agreed Objective

Implement multi-instance support for Claude Code to enable running multiple concurrent sessions on the same project without conflicts.

---

## Key Requirements

### Instance Isolation
- Timestamp-based instance IDs (YYYY-MM-DD-HHMM format)
- Instance-specific state in `.claude/state/instances/[id]/`
- Each instance has own `current-objective.md` and `session-info.md`
- No collisions between concurrent sessions

### Shared Resources
- `session-context.md`, `topics.md`, `decisions.md`, `backlog.md` remain shared
- All instances see same project-wide state
- Backlog includes instance tags for paused tasks

### Smart Instance Detection
- `/resume` auto-detects or creates instance based on context
- `/resume [instance-id]` explicitly resumes specific instance
- `/resume and work on [task]` creates new instance for task
- Detects uncommitted changes to infer active instance
- Prompts user when multiple instances active

### Instance Visibility
- `/instances` command shows all active, idle, and stale instances
- Master registry in `.claude/state/registry.md`
- Heartbeat tracking in session-info.md
- Stale detection (>24 hours since last heartbeat)

### User-Controlled Cleanup
- No automatic cleanup of stale instances
- `/cleanup-instances` provides interactive management
- Options: Archive, Delete, or Keep stale instances
- User decides when to clean up old sessions

### Backward Compatibility
- System works with or without instances
- Legacy `.claude/state/current-objective.md` still supported
- All commands check for instance mode before operating
- Graceful migration path

---

## Approach & Reasoning

**Directory Structure:**
```
.claude/state/
├── registry.md                    # Master index
├── backlog.md                     # Shared backlog
├── instances/
│   ├── 2025-10-31-1430/          # Instance 1
│   │   ├── current-objective.md
│   │   └── session-info.md
│   ├── 2025-10-31-1945/          # Instance 2
│   │   ├── current-objective.md
│   │   └── session-info.md
│   └── _archived/                 # User-archived
```

**Implementation Strategy:**
1. Create directory structure and templates
2. Implement new commands (`/instances`, `/cleanup-instances`)
3. Update existing commands for instance awareness:
   - `/resume` - Smart detection and instance loading
   - `/checkpoint` - Instance-specific state save
   - `/save-objective` - Instance isolation
   - `/pause-task` - Instance tagging in backlog
4. Update CLAUDE.md quick reference
5. Document migration path
6. Test with simulated multi-instance scenario

**Why this approach:**
- Timestamp IDs are self-documenting and collision-free
- Registry provides visibility without needing to scan directories
- Heartbeat system enables stale detection
- User-controlled cleanup prevents accidental data loss
- Backward compatibility ensures smooth adoption

---

## Progress

**Completed:**
- ✅ Architecture design finalized
- ✅ Directory structure created (`.claude/state/instances/` + `_archived/`)
- ✅ Registry template created (`.claude/state/registry.md`)
- ✅ Session-info template created
- ✅ `/instances` command created
- ✅ `/cleanup-instances` command created
- ✅ `/resume` updated with smart instance detection
- ✅ `/checkpoint` updated for instance awareness
- ✅ `/save-objective` updated for instance isolation
- ✅ `/pause-task` updated with instance tagging
- ✅ CLAUDE.md updated with multi-instance documentation

**In Progress:**
- Saving this objective to document current state
- About to add decision to decisions.md

**Remaining:**
- Document migration path for existing users
- Add decision entry to decisions.md
- Consider testing with actual multi-instance scenario

---

## Blockers / Questions

None - implementation is complete and ready for use.

---

## Context References

**Created Files:**
- `.claude/state/registry.md` - Master instance index
- `.claude/state/instances/.template-session-info.md` - Template for session info
- `.claude/commands/instances.md` - View all instances command
- `.claude/commands/cleanup-instances.md` - Cleanup tool

**Modified Files:**
- `.claude/commands/resume.md` - Smart instance detection
- `.claude/commands/checkpoint.md` - Instance-aware saving
- `.claude/commands/save-objective.md` - Instance isolation
- `.claude/commands/pause-task.md` - Instance tagging
- `.claude/CLAUDE.md` - Multi-instance documentation

**Related Documentation:**
- `.claude/docs/workflow-protocol.md` - Interaction protocol
- `.claude/state/backlog.md` - Shared task backlog

---

## Notes

**Key Design Choices:**
1. Timestamp-based IDs - Simple, collision-free, self-documenting
2. User-controlled cleanup - No automatic deletion to prevent data loss
3. Smart detection in `/resume` - Infers intent from arguments and state
4. Shared vs isolated files - Project-wide shared, work-specific isolated
5. Backward compatibility - Works with or without instances

**Migration Path:**
- Existing users continue working normally (legacy mode)
- First multi-instance use triggers instance creation
- Old `.claude/state/current-objective.md` remains functional
- No breaking changes to existing workflows

**Testing Considerations:**
- Could test by simulating two instances with different objectives
- Verify registry updates correctly
- Check heartbeat tracking works
- Confirm cleanup tool interactive flow
- Validate smart detection logic

---

*This file tracks the multi-instance implementation objective for crash recovery and continuity.*
