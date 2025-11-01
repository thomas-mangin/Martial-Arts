# Phase 3: Iwama Syllabus - Complete Technical Documentation

**Status**: Available
**Priority**: High
**Dependencies**:
- Phase 1 (Information Architecture) - COMPLETE ✅
- Phase 2 (Biomechanics) - Partial dependency (can start before Phase 2 complete)
**Estimated Effort**: Very Large (months of systematic documentation)

---

## WHY This Work Matters

**Purpose**: Create comprehensive technical documentation of all Iwama Aikido techniques to textbook-level depth.

**Problem it solves**:
- Iwama syllabus exists but is not comprehensively documented
- Techniques are known by name but full biomechanical breakdowns don't exist
- Progressive learning structure not clearly defined
- Cannot write educational content without complete technique foundation

**Impact**:
- Provides complete technical reference for all Iwama techniques
- Enables educational authoring (can reference complete technique docs)
- Supports teaching (comprehensive breakdown for instructors)
- Preserves detailed technical knowledge systematically

---

## Scope

### What This Includes

**Empty-Hand Techniques (Taijutsu)**:
- All fundamental techniques (kihon waza):
  - Ikkyo through Gokyo (5 pins) - omote and ura variations
  - Irimi-nage, kaiten-nage, tenchi-nage, shiho-nage, koshi-nage, kote-gaeshi, etc.
- All attack types for each technique:
  - Katate-dori, ryote-dori, kata-dori, mune-dori
  - Shomen-uchi, yokomen-uchi, tsuki
  - Others as applicable
- All training contexts:
  - Suwari-waza (seated)
  - Hanmi-handachi (mixed)
  - Tachi-waza (standing)

**Weapons (Aiki-ken and Aiki-jo)**:
- Aiki-ken suburi (7 kata)
- Aiki-ken kumitachi (paired practice kata)
- Aiki-jo suburi (20 movements)
- Aiki-jo kumijo (13 kata)
- Ken tai jo (sword vs. staff)
- Weapons-to-taijutsu connections

**Progressive Structure**:
- Beginner curriculum (what to learn first)
- Intermediate progressions
- Advanced refinements
- Testing requirements mapping (kyu/dan levels)

**Cross-Referencing**:
- Technique-to-principle mapping (which principles each technique uses)
- Related technique connections
- Technique families and variations

### What This Excludes

- Biomechanical principle documentation (that's Phase 2)
- Common errors documentation (that's Phase 4 - though techniques should list errors)
- Teaching methodology (that's Phase 4 - though techniques should have teaching notes)
- YouTube video analysis (that's Phase 5 - though can reference videos)

**Note**: Technique documentation DOES include principle references, error listings, and teaching notes - but detailed principle/error/method docs are in other phases.

---

## Deliverables

**1. Complete Technique Documentation (100-150+ techniques)**
- **Location**: `knowledge-base/techniques/empty-hand/[category]/[technique-attack-context].md`
- **Template**: `templates/technique-template.md`
- **Categories**:
  - `knowledge-base/techniques/empty-hand/pins/` (ikkyo, nikyo, sankyo, yonkyo, gokyo variants)
  - `knowledge-base/techniques/empty-hand/throws/` (irimi-nage, kaiten-nage, shiho-nage, etc.)
  - `knowledge-base/techniques/empty-hand/projections/` (tenchi-nage, koshi-nage, etc.)

**2. Weapons Kata Documentation (40+ kata/movements)**
- **Location**: `knowledge-base/techniques/weapons/ken/` and `/jo/`
- **Template**: Adapted technique template for kata
- **Includes**: All suburi, kumitachi, kumijo

**3. Iwama Syllabus Structure Document**
- **Location**: `research/iwama-syllabus-structure.md`
- **Contents**: Complete syllabus organization, progressive structure, testing requirements

**4. Technique Index**
- **Location**: `knowledge-base/indexes/technique-index.md`
- **Contents**: Complete list of all techniques with attack/context variations

**5. Cross-Reference Indexes**
- **Location**: `knowledge-base/indexes/`
- **Files**:
  - `technique-to-principle-index.md` (which techniques use which principles)
  - `principle-to-technique-index.md` (which principles appear in which techniques)
  - `technique-family-index.md` (related techniques grouped)

---

## Breakdown (Can Be Claimed Separately)

This work can be split by technique category or type:

### Part A: Five Pins (Ikkyo through Gokyo)
- [ ] Document ikkyo (all attacks, all contexts, omote/ura)
- [ ] Document nikyo (all attacks, all contexts, omote/ura)
- [ ] Document sankyo (all attacks, all contexts, omote/ura)
- [ ] Document yonkyo (all attacks, all contexts, omote/ura)
- [ ] Document gokyo (all attacks, all contexts, omote/ura)
- **Estimated effort**: Large (30-50 technique variations total)

### Part B: Major Throws
- [ ] Document irimi-nage (all attacks/contexts)
- [ ] Document kaiten-nage (all attacks/contexts)
- [ ] Document shiho-nage (all attacks/contexts)
- [ ] Document kote-gaeshi (all attacks/contexts)
- [ ] Other major throws
- **Estimated effort**: Large (30-40 technique variations)

### Part C: Projections and Specialty Techniques
- [ ] Document tenchi-nage, koshi-nage, sumi-otoshi
- [ ] Document aiki-otoshi and other specialized techniques
- [ ] Document suwari-waza specific techniques
- **Estimated effort**: Medium (15-25 techniques)

### Part D: Aiki-ken (Sword)
- [ ] Document 7 ken suburi
- [ ] Document kumitachi kata
- [ ] Document ken-related principles
- **Estimated effort**: Medium (15-20 kata/movements)

### Part E: Aiki-jo (Staff)
- [ ] Document 20 jo suburi
- [ ] Document 13 kumijo kata
- [ ] Document jo-related principles
- **Estimated effort**: Medium-Large (30+ movements/kata)

### Part F: Ken tai Jo & Weapons Integration
- [ ] Document ken tai jo applications
- [ ] Document weapons-to-taijutsu connections
- [ ] Explain principle transfer between weapons and empty-hand
- **Estimated effort**: Medium

### Part G: Syllabus Structure & Indexes
- [ ] Create complete syllabus structure document
- [ ] Create technique index
- [ ] Create all cross-reference indexes
- [ ] Ensure progressive learning pathways clear
- **Estimated effort**: Medium

**Note**: Parts A-F can be worked in parallel by different agents. Part G requires A-F to be substantially complete.

---

## Success Criteria

**Completeness**:
- ✅ All fundamental Iwama techniques documented
- ✅ All major attack variations covered
- ✅ All training contexts (suwari/tachi/hanmi-handachi) addressed
- ✅ All weapons kata documented
- ✅ Syllabus structure clearly defined

**Quality**:
- ✅ Each technique uses `templates/technique-template.md` format
- ✅ Technical execution described step-by-step (teachable from doc)
- ✅ Biomechanical principles identified and explained
- ✅ Progressive learning (beginner→advanced) documented
- ✅ At least 2-3 common errors noted per technique
- ✅ Teaching notes included
- ✅ Techniques pass `validation/technique-completeness-checklist.md`

**Integration**:
- ✅ All techniques cross-referenced to principles
- ✅ Related techniques linked
- ✅ Technique index complete and navigable
- ✅ Cross-reference indexes accurate

**Usability**:
- ✅ Can learn technique from documentation (with hands-on practice)
- ✅ Instructors can use docs to teach
- ✅ Supports educational authoring (can reference techniques in content)

---

## Resources

**Templates**:
- `templates/technique-template.md` - Use for every technique

**Validation**:
- `validation/technique-completeness-checklist.md` - Check each technique

**Existing Work**:
- `syllabus/` directory - May have existing syllabus info (verify and enhance)

**Source Materials**:
- Personal training knowledge (primary source)
- Saito Sensei books/videos (if available)
- YouTube demonstrations (Phase 5 will enhance with timestamps)
- Sensei consultations (if available)

**Architecture Reference**:
- `research/knowledge-architecture.md` - Domain 1 section explains technique documentation

---

## Notes

**Personal knowledge critical**: Much of this requires your direct training knowledge and teaching experience. Agents may need to flag where your input is essential.

**Iterative depth**: Can do first-pass documentation of all techniques, then deepen with more detail in second pass.

**Video integration**: Phase 5 will add video timestamps - initial docs can note "need video reference" where helpful.

**Principle dependency**: Can document techniques before all principles are documented (Phase 2), but will need to add principle references later.

**Progressive approach**:
1. Document fundamental techniques first (what beginners learn)
2. Then intermediate techniques
3. Then advanced variations
4. This mirrors actual learning progression

---

*This is the largest single work item. Highly recommended to split among multiple agents or work in phases (fundamentals first, then build out).*
