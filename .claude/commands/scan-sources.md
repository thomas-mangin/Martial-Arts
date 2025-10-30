# Scan-Sources Command - Monitor Bloggers for Content

Launches the scan-sources agent to monitor tracked bloggers for new content and extract blog ideas.

## Usage

- `/scan-sources` - Scan all tracked sources
- `/scan-sources [name]` - Scan specific source

**Examples:**
- `/scan-sources leo-tamaki`
- `/scan-sources`

## What It Does

The scan-sources agent will:
1. Fetch recent posts from tracked blogs
2. Identify new content since last scan
3. Analyze posts for key arguments and ideas
4. Generate 2-4 blog topic ideas per post
5. Create findings report with actionable ideas
6. Update source profiles with scan results

## Result

Findings saved in `sources/findings/YYYY-MM-DD-[source-name].md`

Includes:
- Post summaries and key arguments
- Blog ideas (with type, angle, audience, Aikido relevance)
- Response opportunities
- Discussion prompts for /discuss
- Recommended actions

## When to Use

Weekly or bi-weekly to find new content and inspiration. Part of source-inspired workflow:

`/scan-sources` → review findings → `/discuss [topic]` → `/extract` → develop → `/review-aikido`

## Note

First scan may find 3-5 posts. Subsequent scans typically find 0-2 new posts. Quality over quantity.
