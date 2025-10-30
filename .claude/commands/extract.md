# Extract Command - Transform Discussion to Blog Draft

Launches the extract agent to transform discussion notes into structured blog post drafts.

## Usage

`/extract discussions/[filename].md`

**Examples:**
- `/extract discussions/teaching-relaxation-2025-10-30.md`
- `/extract discussions/biomechanics-of-irimi-2025-10-30.md`

## What It Does

The extract agent will:
1. Read and analyze the discussion note
2. Assess blog potential and readiness
3. Create structured blog draft in `posts/` directory
4. Preserve authentic insights and voice
5. Mark gaps that need development
6. Provide next steps guidance

## Result

Blog draft saved as `posts/[topic-name]-YYYY-MM-DD.md`

Ready to develop and review with: `/review-aikido posts/[filename].md`

## When to Use

After discussion is complete and ready to become a blog post. Part of the recommended workflow:

`/discuss` → `/extract` → develop → `/review-aikido` → `/checkpoint`

## Note

Extraction creates a first draft, not final content. Expect to expand, refine, and iterate based on review feedback.
