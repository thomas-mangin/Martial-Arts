# Extract Command - Transform Discussion to Article Draft

Launches the extract agent to transform discussion notes into structured article drafts.

## Usage

`/extract discussions/[filename].md`

**Examples:**
- `/extract discussions/teaching-relaxation-2025-10-30.md`
- `/extract discussions/biomechanics-of-irimi-2025-10-30.md`

## What It Does

The extract agent will:
1. Read and analyze the discussion note
2. Assess article potential and readiness
3. Create structured article draft in `articles/` directory
4. Organize for educational depth (not blog engagement)
5. Preserve authentic insights and voice
6. Mark gaps that need development
7. Provide next steps guidance

**Target Output**: 1,500-3,000+ words for comprehensive coverage

## Result

Article draft saved as `articles/[topic-name]-YYYY-MM-DD.md`

Ready to develop and review with: `/review-aikido articles/[filename].md`

## When to Use

After discussion is complete and ready to become an article. Part of the recommended workflow:

`/discuss` → `/extract` → develop → `/review-aikido` → `/checkpoint`

## Note

Extraction creates a first draft, not final content. Expect to expand, refine, and iterate based on review feedback.
