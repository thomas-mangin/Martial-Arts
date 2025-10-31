# Detailed Workflows

## Session Lifecycle

### Starting a Session

1. User runs `/resume`
2. Command executes:
   - Detects or creates instance (multi-instance support)
   - Reads shared state:
     - `session-context.md` - Current status, recent work, next steps
     - `topics.md` - Current article and queue
     - `decisions.md` - Recent decisions (last 2-3)
     - `.claude/state/backlog.md` - Paused tasks
   - Reads instance-specific state:
     - `.claude/state/instances/[instance-id]/current-objective.md` - Active work (crash recovery)
   - Checks `.claude/state/registry.md` - Shows other active instances
   - Checks git status - Any uncommitted changes
3. Displays concise summary:
   - Active objective (if any)
   - Paused tasks in backlog
   - Other active instances
   - System status
4. Asks how to proceed based on context

### During a Session

**Instance-Specific Updates**:
- Use `/save-objective` to save current work (crash recovery)
- Update `current-objective.md` with progress, blockers, next steps

**Shared Updates**:
- Update `session-context.md` when major milestones reached
- Add article ideas to `topics.md` as they emerge
- Log important decisions to `decisions.md`
- Keep work organized in proper directories

**Reference as Needed**:
- Refer to research files for authenticity
- Check article guidelines for quality standards
- Review series structure for consistency

### Ending a Session

1. User runs `/checkpoint`
2. Command executes autonomously:
   - Checks git status for uncommitted changes
   - Commits all changes to local git
   - Pushes to GitHub automatically
   - Updates instance heartbeat in `session-info.md`
   - Marks instance as "Idle" in registry
   - Analyzes session to create summary
   - Creates timestamped session summary in `sessions/`
3. Displays summary of what was saved

**Instance Management**:
- Each instance checkpoints independently
- Other active instances remain unaffected
- Idle instances can be resumed or cleaned up later

### Task Switching (Mid-Session)

**When urgent work interrupts current task:**

1. User runs `/pause-task [reason]`
2. Command executes:
   - Documents current progress in detail
   - Moves current objective to backlog with:
     - Progress made
     - Blockers encountered
     - Next steps clearly identified
     - Context files needed to resume
   - Clears current-objective.md to template
   - Updates registry
3. Ready for new task
4. Later: Any instance can resume paused task from backlog

---

## Article Writing Workflows

**Note**: Articles are educational content designed for progressive learning and book compilation, not standalone blog posts. MSc-level quality standards apply.

### Approach A: Discussion-Based (Recommended)

**When to use**: Exploring new ideas or complex topics

**Steps:**
1. `/resume` - Load session state and see where you left off
2. `/discuss [topic-name]` - Agent facilitates informal conversation
   - Asks probing questions to deepen understanding
   - Extracts insights from your responses
   - Records specific examples and stories
   - Identifies key concepts and frameworks
   - Saves structured note to `discussions/[topic]-YYYY-MM-DD.md`
3. Review discussion note (verify captured your thinking)
4. `/extract discussions/[file].md` - Agent transforms discussion to article draft
   - Analyzes educational potential
   - Structures insights for progressive learning
   - Creates initial draft in `articles/[series]/[topic]-YYYY-MM-DD.md`
   - Identifies gaps requiring further development
5. Develop draft
   - Expand sections for comprehensive depth
   - Fill identified gaps
   - Add concrete examples and applications
   - Ensure consistency with earlier articles in series
   - Cross-reference related articles
6. `/review-aikido articles/[file].md` - Agent performs quality review
   - Checks terminology (Japanese, macrons, romanization)
   - Verifies technical accuracy and completeness
   - Assesses educational depth and clarity
   - Validates consistency with earlier articles in series
   - Confirms alignment with core values
   - Verifies AI attribution section present
7. Revise based on critical feedback
   - Address all issues identified
   - Re-run `/review-aikido` until quality standards met
8. Finalize
   - Update `topics.md` (mark complete, update series progress)
   - Add any follow-up article ideas discovered
   - Note audience profiles addressed
9. `/checkpoint` - Save, commit, and push to GitHub

**Benefits:**
- Captures authentic voice through conversation
- Develops ideas organically before writing
- Creates reusable discussion notes
- Reduces writer's block
- Ensures educational depth through iteration

**Target Length**: 1,500-3,000+ words (comprehensive coverage prioritized over brevity)

### Approach B: Direct Writing

**When to use**: Clear idea with strong understanding, ready to write

**Steps:**
1. `/resume` - Load session context
2. Choose article from `topics.md` or identify new topic
3. Determine series placement (check `article/article-series-structure.md`)
4. Create article from template:
   - `cp article/article-template.md articles/[series]/[topic-name]-YYYY-MM-DD.md`
5. Write content following guidelines:
   - Read `article/article-guidelines.md` for quality standards
   - Read `article/article-voice-guide.md` for tone and perspective
   - Ensure consistency with earlier articles in same series
   - Include cross-references to prerequisite articles
6. `/review-aikido articles/[file].md` - Quality check
7. Revise based on feedback (iterate until standards met)
8. Finalize and update `topics.md`
9. `/checkpoint` - Save, commit, and push

**Benefits:**
- Fastest approach for clear ideas
- Direct control over structure and flow
- Good for technical how-to articles

**Note**: Less effective for exploring complex or nuanced topics

### Approach C: Source-Inspired (Blogger Content)

**When to use**: Engaging with martial arts community content, finding inspiration

**Steps:**
1. `/track-source "[Name]" "[URL]" "[Discipline]"` - Register blogger
   - Agent creates profile in `sources/registry/`
   - Records URL, discipline, focus areas, scan history
2. `/scan-sources [name]` - Monitor for new content (or scan all sources)
   - Agent fetches recent posts
   - Identifies new content since last scan
   - Analyzes arguments and key points
   - Generates article topic ideas (response, alternative perspective, inspired exploration)
   - Saves findings to `sources/findings/YYYY-MM-DD-[name].md`
3. Review findings report
   - Identify topics that fit your article series
   - Note which series the idea belongs to
   - Consider how it connects to existing articles
4. Choose inspired topic and develop:
   - **Option A**: `/discuss [topic]` → `/extract` → develop (recommended for complex topics)
   - **Option B**: Write directly from template (for clear ideas)
5. `/review-aikido articles/[file].md`
6. Revise and finalize
7. Update `topics.md`, note source connection
8. `/checkpoint`

**Benefits:**
- Engages with community conversations
- Provides response opportunities
- Cross-pollination of ideas
- Builds awareness of other perspectives

**Important**: Transform their ideas through your framework - don't just respond reactively

### Approach D: YouTube-Inspired

**When to use**: Discovering valuable video content for cross-validation or inspiration

**Steps:**
1. `/youtube fetch [url]` - Download and analyze (supports single videos or full channels)
   - Agent downloads transcript using yt-dlp
   - Extracts metadata (title, channel, duration, date)
   - Analyzes content for themes, concepts, teaching methods
   - Generates 3-5 article topic ideas with full details
   - Creates findings report in `sources/youtube/findings/`
   - Updates/creates channel registry
2. Review findings report
   - Identify universal principles applicable to Aikido
   - Note cross-discipline insights
   - Consider how concepts fit your article series
   - Check for cross-validation opportunities (multiple instructors agree)
3. Choose inspired topic and develop:
   - **Option A**: `/discuss [topic]` → `/extract` → develop (recommended)
   - **Option B**: Write directly from template
4. `/review-aikido articles/[file].md`
5. Revise and finalize
6. Update `topics.md`, credit video with link if directly inspired
7. `/checkpoint`

**Benefits:**
- Cross-discipline insights (Karate, Judo, BJJ, Wing Chun, etc.)
- Visual content inspiration
- Cross-validation across multiple instructors (1,983 transcripts available)
- Responds to concepts being actively taught

**Research Base Available**:
- 1,983 transcripts across 5 major channels
- 5 distinct teaching philosophies documented
- Universal agreements identified (weapons training, effectiveness, etc.)
- Productive contrasts documented (internal development approaches, etc.)

**Important Notes**:
- Transcripts for research and inspiration only
- Never reproduce long excerpts verbatim
- Look for universal biomechanical principles
- Credit instructor if directly inspired

---

## Article Quality Standards

### Educational Depth (Not Blog Engagement)

**Length**:
- **Target**: 1,500-3,000+ words for comprehensive coverage
- **Acceptable minimum**: 1,200 words for focused technical articles
- **No maximum**: Completeness prioritized over brevity
- **Do NOT sacrifice depth for "quick reads"**

**Comprehensive Coverage**:
- Explain WHY techniques work (biomechanics, physics, anatomy)
- Provide enough detail that readers don't need other sources
- Include progressive learning path (beginner → advanced applications)
- Address common mistakes and how to correct them
- Provide concrete training methods and drills

### Structure (Progressive Series Approach)

**Article Organization**:
- Clear, descriptive title (not clickbait)
- Metadata (series, article number, audiences, prerequisites)
- About This Article (AI attribution - MANDATORY)
- Introduction (200-300 words) - Context and learning objectives
- Main content (3-6 sections, 1,200-2,700 words total)
- Practical applications (tiered by experience level when applicable)
- Conclusion (150-200 words) - Summary and next steps
- Optional: References, glossary, related articles

**Series Considerations**:
- Articles build on each other systematically
- Cross-reference earlier articles when building on concepts
- Maintain consistent terminology throughout series
- Readers should be able to read series start-to-finish for complete understanding
- Each article still comprehensible standalone (with prereq references)

### Content Categories

Organized by series (see `article/article-series-structure.md`):
- **Biomechanics & Movement** - Technical analysis with physics/anatomy
- **Learning Journey & Mastery** - Progression frameworks and stages
- **Peace, Violence & Context** - Philosophy grounded in reality
- **Teaching & Transmission** - Instructional methods and approaches
- **Iwama Syllabus Documentation** - Complete technical reference

### Tone & Voice

**First Dan Perspective** - On the journey, not ultimate authority:
- Acknowledge experience level (shodan, not master)
- Stages 1-3: Speak from direct personal experience
- Stage 4: Speak from emerging understanding
- Stage 5: Speak from observation of advanced practitioners
- Use framing: "In my experience...", "What I've observed...", "My current understanding..."
- Avoid claiming certainty beyond your level

**Grounded in Real Experience**:
- Reference actual experiences (knife attack, military training, veteran observations)
- Don't claim experiences you don't have (competition success, combat deployment, etc.)
- Honesty about abilities (understand biomechanics well, not a great fighter)
- Present frameworks as working models, not absolute truth

**Educational Tone**:
- Professional but accessible
- Knowledgeable but humble
- Explain clearly without patronizing
- Respect reader intelligence
- Acknowledge limitations and uncertainties

### Multi-Audience Layering

**Every article should identify**:
- Primary audiences (1-2): Main target readers
- Secondary audiences (2-3): Additional value provided

**Audience Profiles** (see `research/audience-profiles.md`):
- By experience: Beginners, Intermediate, Advanced
- By role: Students, Instructors, Dojo Owners
- By interest: Technical, Philosophical, Practical, Historical, Syllabus Reference

**Layered Content Approach**:
- Accessible to beginners, challenging for advanced
- Tier practical applications by experience level
- Use examples that resonate with different audiences
- No audiences systematically excluded over time

### Mandatory Quality Checks

**Before finalizing any article**:
1. ✅ AI attribution section present (see article-template.md)
2. ✅ Terminology correct (Japanese spelling, macrons, romanization)
3. ✅ Technical accuracy verified
4. ✅ Consistent with earlier articles in series
5. ✅ Comprehensive educational depth (not surface-level)
6. ✅ Aligned with core values (biomechanics over mysticism, etc.)
7. ✅ Violence context specified when discussing effectiveness
8. ✅ Legal/ethical considerations addressed when applicable
9. ✅ Multiple audiences addressed
10. ✅ Clear learning objectives and takeaways

**Use `/review-aikido` to verify all quality standards**

---

## Authenticity System

### Core Values Check

Before writing on certain topics, consult `research/core-values.md`:
- Biomechanics over mysticism (explain WHY techniques work)
- Knowing vs embodied understanding (stages of mastery)
- Peace through understanding cost (veteran perspective, not naivety)

**When to check**:
- Writing about teaching methods
- Discussing Aikido philosophy
- Comparing styles or approaches
- Taking positions on controversial topics

### Divisive Topics Framework

Before writing on controversial topics, consult `research/divisive-topics.md`:
- Violence Context Framework (4 types: Monkey Dance, Predatory, Sport/Cage, War)
- Legal/Ethical Context (force continuum, proportionate response)
- Aikido debates (peace vs martial, Iwama vs blending, ki vs biomechanics)
- General martial arts debates (kata vs alive training, traditional vs modern)
- Cross-discipline debates (hard vs soft, weapons vs empty hand)

**Framework for controversial topics**:
1. Acknowledge multiple valid perspectives
2. State your position clearly with reasoning
3. Avoid false dichotomies (often "both/and" not "either/or")
4. Anticipate and address counter-arguments respectfully
5. Specify context (what works for self-defense ≠ what works in cage)

### Learning Journey Framework

When writing about mastery/progression, apply `research/learning-frameworks.md`:
- 5 Stages: Hands → Feet → Timing → Core → Patterns
- Knowing (intellectual) vs Embodied (natural movement)
- Kata as alphabet (foundation, not scripture)
- Stage-appropriate teaching methods

**Application**:
- Write to appropriate stage for topic
- Don't mistake intellectual grasp for embodied mastery
- Acknowledge which stages you speak from (experience vs observation)

---

## Agent Workflows (Internal Details)

### /discuss Agent

**Purpose**: Explore topics through conversational dialogue

**Internal Process**:
1. Receive topic from user
2. Load research files internally:
   - `core-values.md` - Foundational beliefs
   - `divisive-topics.md` - Controversial topics framework
   - `learning-frameworks.md` - Mastery models
   - `user-profile.md` - Author background and expertise
3. Engage in conversation:
   - Ask probing questions to deepen understanding
   - Challenge assumptions gently
   - Extract insights and key concepts
   - Record concrete examples and stories
   - Identify educational frameworks emerging
4. Identify article-worthy ideas
5. Create structured discussion note
6. Save to `discussions/[topic]-YYYY-MM-DD.md`

**User sees**: Questions, conversation flow, final discussion note location

### /extract Agent

**Purpose**: Transform discussion into educational article draft

**Internal Process**:
1. Read specified discussion note file
2. Analyze educational potential:
   - Identify core thesis and learning objectives
   - Extract key concepts and frameworks
   - Find concrete examples and applications
   - Determine logical structure for progressive learning
   - Assess sufficiency of material
3. Create structured article draft:
   - Use author's authentic voice
   - Preserve original phrasing where possible
   - Structure for educational depth (not blog engagement)
   - Include cross-references to related concepts
   - Mark gaps clearly for further development
4. Save to `articles/[series]/[topic]-YYYY-MM-DD.md`
5. Update discussion note with extraction status

**User sees**: Analysis, draft location, gaps identified, development recommendations

### /review-aikido Agent

**Purpose**: Review article quality before publishing (critical, not encouraging)

**Internal Process**:
1. Read specified article file
2. Load quality standards internally:
   - `article-guidelines.md` - Comprehensive quality standards
   - `article-series-structure.md` - Series organization and consistency
   - Earlier articles in same series (for consistency check)
3. Review against all criteria:
   - **Terminology**: Japanese spelling, macrons, romanization
   - **Technical accuracy**: Facts about techniques, history, principles
   - **Educational depth**: Completeness, comprehensive coverage
   - **Clarity**: Accessibility for target audiences
   - **Structure**: Organization, flow, logical progression
   - **Series consistency**: Terminology, frameworks compatible with earlier articles
   - **Authenticity**: Alignment with core values, divisive topics handled properly
   - **AI attribution**: "About This Article" section present and correct
   - **Legal/ethical context**: Addressed when discussing technique effectiveness
4. Generate detailed critical feedback
5. Provide recommendation: ready to publish / needs revisions (be honest)

**User sees**: Comprehensive critical review with specific issues and actionable recommendations

**Approach**: Highly critical, collaborative, MSc-level expectations (not casual blog standards)

### /scan-sources Agent

**Purpose**: Monitor tracked bloggers for new content

**Internal Process**:
1. Load source registry from `sources/registry/`
2. Fetch recent posts from tracked blogs
3. Identify new content since last scan
4. Analyze posts:
   - Key arguments and positions
   - Relevant themes for Aikido
   - Connection to your article series
5. Generate article ideas:
   - **Response**: Direct response to their argument
   - **Alternative Perspective**: Different viewpoint on same topic
   - **Inspired Exploration**: Their post sparked related idea
6. Create findings report with actionable ideas
7. Save to `sources/findings/YYYY-MM-DD-[source].md`
8. Update source profile with scan results

**User sees**: Summary of new posts, article ideas generated, findings report location

### /youtube fetch Agent

**Purpose**: Download and analyze YouTube video transcripts

**Internal Process**:
1. Download transcript using yt-dlp (script: `scripts/youtube-transcript.py`)
2. Extract metadata (title, channel, duration, upload date)
3. Convert transcript to readable text format
4. Analyze content:
   - Identify key themes and concepts
   - Extract martial arts principles
   - Note teaching approaches and methods
   - Find cross-discipline insights applicable to Aikido
   - Identify biomechanical explanations
5. Generate 3-5 article topic ideas with full details:
   - How concept applies to Aikido
   - Which series it fits into
   - Key points to explore
6. Create findings report with analysis and recommendations
7. Save to `sources/youtube/findings/YYYY-MM-DD-[video_id].md`
8. Update/create channel registry profile

**User sees**: Video summary, article ideas, findings report location

### /youtube analyze Agent

**Purpose**: Re-analyze existing transcript for additional insights

**Similar to fetch, but**:
- Reads existing transcript and metadata
- Performs deeper analysis
- Extracts additional article ideas
- Updates findings report

---

*Read this file when you need detailed workflow guidance. Not loaded by default.*
