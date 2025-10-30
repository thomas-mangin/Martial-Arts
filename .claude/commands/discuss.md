# Discuss Command - Explore Topics Through Conversation

Launches the discuss agent to explore Aikido topics through informal conversation.

## Usage

`/discuss [topic-name]`

**Examples:**
- `/discuss teaching-relaxation`
- `/discuss biomechanics-of-irimi`
- `/discuss iwama-approach-critique`

## What It Does

The discuss agent will:
1. Engage in conversational dialogue about the topic
2. Ask probing questions to deepen understanding
3. Extract key insights from your responses
4. Record examples and stories
5. Create structured discussion note in `discussions/` directory
6. Highlight blog-worthy ideas

## Result

Discussion note saved as `discussions/[topic-name]-YYYY-MM-DD.md`

Ready to extract to blog draft with: `/extract discussions/[filename].md`

## When to Use

Before writing, to explore ideas informally and develop understanding. Part of the recommended discussion-based workflow:

`/discuss` → `/extract` → develop → `/review-aikido` → `/checkpoint`
