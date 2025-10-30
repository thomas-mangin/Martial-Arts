# Detailed Workflows

## Session Lifecycle

### Starting a Session

1. User runs `/resume`
2. Command reads:
   - `session-context.md` - Current status, recent work, next steps
   - `topics.md` - Current topic and queue
   - `decisions.md` - Recent decisions (last 2-3)
   - Git status - Any uncommitted changes
3. Display concise summary
4. Ask how to proceed based on context

### During a Session

- Update `session-context.md` as work progresses
- Add ideas to `topics.md` as they emerge
- Log important decisions to `decisions.md`
- Keep work organized in proper directories
- Refer to research files when needed for authenticity

### Ending a Session

1. User runs `/checkpoint`
2. Command executes:
   - Check git status for uncommitted changes
   - Commit all changes to local git (never push)
   - Update `session-context.md` with current status
   - Review and update `topics.md`
   - Log any new decisions to `decisions.md`
   - Create timestamped session summary in `sessions/`
3. Display summary of what was saved

## Blog Writing Workflows

### Approach A: Discussion-Based (Recommended)

**When to use**: When exploring new ideas or complex topics

**Steps:**
1. `/resume` - See where you left off
2. `/discuss [topic-name]` - Agent facilitates informal conversation
   - Asks probing questions
   - Extracts insights from responses
   - Records examples and stories
   - Saves structured note to `discussions/[topic]-YYYY-MM-DD.md`
3. Review discussion note
4. `/extract discussions/[file].md` - Agent transforms discussion to blog draft
   - Analyzes blog potential
   - Structures insights logically
   - Creates initial draft in `posts/[topic]-YYYY-MM-DD.md`
   - Identifies gaps to fill
5. Develop draft
   - Expand sections
   - Fill gaps
   - Refine language
   - Add examples
6. `/review-aikido posts/[file].md` - Agent reviews quality
   - Checks terminology (Japanese, macrons, romanization)
   - Verifies technical accuracy
   - Assesses clarity and structure
   - Validates against core values
7. Revise based on feedback
8. Finalize
   - Update `topics.md` (move to completed)
   - Add any follow-up topics discovered
9. `/checkpoint` - Save and commit

**Benefits:**
- Captures authentic voice through conversation
- Develops ideas organically
- Creates reusable discussion notes
- Reduces writer's block

### Approach B: Direct Writing

**When to use**: When you have a clear idea and just need to write

**Steps:**
1. `/resume` - Load session context
2. Choose topic from `topics.md` or add new one
3. Create post: `cp blog/blog-template.md posts/[topic-name]-YYYY-MM-DD.md`
4. Write content following `blog/blog-guidelines.md`
5. `/review-aikido posts/[file].md` - Quality check
6. Revise based on feedback
7. Finalize and update `topics.md`
8. `/checkpoint` - Save and commit

**Benefits:**
- Fastest approach for clear ideas
- Direct control over structure
- Good for shorter posts

### Approach C: Source-Inspired (Blog Content)

**When to use**: To engage with martial arts community content

**Steps:**
1. `/track-source "[Name]" "[URL]" "[Discipline]"` - Register blogger
   - Agent creates profile in `sources/registry/`
   - Records URL, discipline, focus areas
2. `/scan-sources [name]` - Monitor for new content
   - Agent fetches recent posts
   - Identifies new content since last scan
   - Analyzes arguments and key points
   - Generates blog topic ideas
   - Saves findings to `sources/findings/YYYY-MM-DD-[name].md`
3. Review findings report
4. Choose inspired topic
5. Either:
   - **Option A**: `/discuss [topic]` → `/extract` → develop
   - **Option B**: Write directly from template
6. `/review-aikido posts/[file].md`
7. Revise and finalize
8. Update `topics.md`, note source connection
9. `/checkpoint`

**Benefits:**
- Engages with community conversations
- Provides response opportunities
- Cross-pollination of ideas
- Builds relationships with other bloggers

### Approach D: YouTube-Inspired

**When to use**: When discovering valuable video content

**Steps:**
1. `/youtube-fetch [url]` - Download and analyze
   - Agent downloads transcript using yt-dlp
   - Extracts metadata (title, channel, duration, date)
   - Analyzes content for themes and concepts
   - Generates 3-5 blog topic ideas
   - Creates findings report in `sources/youtube/findings/`
   - Updates/creates channel registry
2. Review findings report
3. Choose inspired topic
4. Either:
   - **Option A**: `/discuss [topic]` → `/extract` → develop
   - **Option B**: Write directly from template
5. `/review-aikido posts/[file].md`
6. Revise and finalize
7. Update `topics.md`, credit video with link if directly inspired
8. `/checkpoint`

**Benefits:**
- Cross-discipline insights
- Visual content inspiration
- Responds to popular topics
- Reaches different audiences

## Content Quality Standards

### Length
- **Sweet spot**: 800-1200 words
- **Minimum**: 600 words (for focused technique posts)
- **Maximum**: 1800 words (for deep dives)

### Structure
- Title & metadata
- Introduction (100-200 words) - Hook and context
- Main content (2-4 sections, 500-1500 words)
- Practical takeaways (3-5 bullet points)
- Conclusion (100-150 words) - Summary and call to action
- Optional: Resources, glossary, related posts

### Content Categories
- **Technique**: Specific waza analysis with biomechanics
- **Philosophy**: Principles, concepts, martial arts wisdom
- **Training**: Practice methods, tips, progression
- **History**: Lineage, development, context
- **Personal Reflection**: Journey, insights, stories

### Tone Guidelines
- Knowledgeable but humble (share expertise, admit limitations)
- Accessible but not patronizing (explain clearly, respect intelligence)
- Personal but not self-centered (use experience, serve reader)
- Respectful of tradition but not dogmatic (honor roots, think critically)

## Authenticity System

### Core Values Check

Before writing on certain topics, consult `research/core-values.md`:
- Teaching philosophy (biomechanics over mysticism)
- Mastery concepts (knowing vs. embodied understanding)
- Style perspectives (Iwama critique, relaxation emphasis)
- Aikido philosophy positions (peace vs. martial effectiveness)

**When to check:**
- Writing about teaching methods
- Discussing Aikido philosophy
- Comparing styles or approaches
- Taking controversial positions

### Divisive Topics Handling

Before writing on controversial topics, consult `research/divisive-topics.md`:
- Aikido-specific debates (peace vs. martial, Iwama vs. blending, ki vs. biomechanics)
- General martial arts debates (kata vs. alive training, traditional vs. modern, competition)
- Cross-discipline debates (hard vs. soft, weapons vs. empty hand)

**Framework:**
1. Acknowledge multiple valid perspectives
2. State your position clearly with reasoning
3. Avoid false dichotomies (often "both/and" not "either/or")
4. Anticipate and address counter-arguments respectfully

### Learning Journey Framework

When writing about mastery/progression, apply concepts from `research/learning-journey.md`:
- **Knowing** (intellectual understanding) vs. **Embodied** (natural movement)
- Journey from conscious thinking to automatic response
- Kata as alphabet (foundation, not scripture)
- Teaching implications at different mastery levels

## Agent Workflows

### /discuss Agent

**Purpose**: Explore topics through conversational dialogue

**Process:**
1. Receive topic from user
2. Load research files (`core-values.md`, `divisive-topics.md`, `learning-journey.md`)
3. Engage in conversation:
   - Ask probing questions
   - Deepen understanding
   - Extract insights
   - Record examples and stories
4. Identify blog-worthy ideas
5. Create structured discussion note
6. Save to `discussions/[topic]-YYYY-MM-DD.md`

**User sees**: Questions, conversation, final discussion note location

### /extract Agent

**Purpose**: Transform discussion into blog draft

**Process:**
1. Read specified discussion note file
2. Analyze blog potential:
   - Identify thesis
   - Extract key points
   - Find concrete examples
   - Determine structure
3. Assess if sufficient material exists
4. Create structured blog draft:
   - Use user's authentic voice
   - Preserve their phrasing
   - Structure insights logically
   - Mark gaps clearly
5. Save to `posts/[topic]-YYYY-MM-DD.md`
6. Update discussion note with extraction status

**User sees**: Analysis, draft location, gaps identified, next steps

### /review-aikido Agent

**Purpose**: Review blog post quality before publishing

**Process:**
1. Read specified blog post file
2. Review against criteria:
   - **Terminology**: Japanese spelling, macrons, romanization
   - **Technical accuracy**: Facts about techniques, history, principles
   - **Clarity**: Accessibility for new readers, explanations
   - **Structure**: Organization, flow, completeness
   - **Authenticity**: Alignment with core values, handling of divisive topics
3. Generate detailed feedback
4. Provide recommendation (ready to publish / needs revisions)

**User sees**: Comprehensive review with specific issues and recommendations

### /scan-sources Agent

**Purpose**: Monitor tracked bloggers for new content

**Process:**
1. Load source registry from `sources/registry/`
2. Fetch recent posts from tracked blogs
3. Identify new content since last scan
4. Analyze posts:
   - Key arguments and points
   - Relevant themes
   - Connection to Aikido
5. Generate blog topic ideas:
   - Response opportunities
   - Alternative perspectives
   - Inspired explorations
6. Create findings report
7. Save to `sources/findings/YYYY-MM-DD-[source].md`
8. Update source profile with scan results

**User sees**: Summary of new posts, blog ideas generated, findings report location

### /youtube-fetch Agent

**Purpose**: Download and analyze YouTube video transcripts

**Process:**
1. Download transcript using yt-dlp script
2. Extract metadata (title, channel, duration, date)
3. Read and analyze transcript:
   - Identify key themes
   - Extract martial arts concepts
   - Note teaching approaches
   - Find cross-discipline insights
4. Generate 3-5 blog topic ideas with full details
5. Create findings report
6. Save to `sources/youtube/findings/YYYY-MM-DD-[video_id].md`
7. Update/create channel registry

**User sees**: Video summary, blog ideas, findings report location

---

*Read this file when you need detailed workflow guidance. Not loaded by default.*
