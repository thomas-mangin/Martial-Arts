# Claude Code Cheat Sheet

## Keyboard Shortcuts

### Display & Output
- `Tab` - **Toggle thinking display** (Thinking on/off)
- `Ctrl+O` - Toggle verbose output
- `Ctrl+L` - Clear terminal screen

### Session Control
- `Ctrl+C` - Cancel current input/generation
- `Ctrl+D` - Exit Claude Code session
- `Esc + Esc` - Rewind code/conversation to previous state

### Permission Modes
- `Shift+Tab` or `Alt+M` - Toggle modes (Auto-Accept, Plan, Normal)

### Input Helpers
- `Ctrl+R` - Reverse search command history
- `Ctrl+V` (Mac/Linux) or `Alt+V` (Windows) - Paste image from clipboard

### Multiline Input
- `\ + Enter` - Quick escape method (default)
- `Option+Enter` - macOS alternative
- `Shift+Enter` - After `/terminal-setup`
- `Ctrl+J` - Line feed character

## Quick Command Prefixes

- `/` - Slash commands (e.g., `/help`, `/resume`, `/checkpoint`)
- `#` - Add to memory (CLAUDE.md)
- `!` - Direct bash command execution
- `@` - File path mention with autocomplete

## Essential Slash Commands

### Session Management
- `/resume` - Load previous session state
- `/checkpoint` - Save state and commit to git
- `/clear` - Clear conversation history

### Content Creation
- `/discuss [topic]` - Explore topics through conversation
- `/extract [file]` - Transform discussion into article draft
- `/review-aikido [file]` - Review article quality

### Content Discovery
- `/track-source [name] [url] [discipline]` - Register bloggers
- `/scan-sources [name]` - Monitor for new content
- `/youtube fetch [url]` - Download video/channel transcripts
- `/youtube analyze [video_id]` - Re-analyze transcripts

### System
- `/system-maintenance [mode]` - Audit, clean, sync, optimize
- `/help` - Show help
- `/vim` - Enable vim editor mode

## Tips

- **Always start sessions with `/resume`** to load context
- **Always end sessions with `/checkpoint`** to save work
- Press `Tab` to see my thinking process in real-time
- Use `Esc + Esc` if I make a mistake and you want to roll back
- Use `@` to quickly reference files without typing full paths
