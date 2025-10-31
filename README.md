# Social Media Content System
## "From Chaos to Clarity" - Truth Over Tactics Brand

---

## Directory Structure

```
social/
├── _reference/                    # Reference guides and examples (not actual content)
│   ├── ENGAGEMENT-PATTERNS.md     # Example engagement question patterns
│   ├── QUOTE-PATTERNS.md          # Example quote patterns and structure
│   └── content-library-EXAMPLE.csv # Example CSV format for Canva Bulk Create
│
├── content-library/               # Actual content for posting (CSV files)
│   ├── quotes/                    # Quote content spreadsheets
│   │   ├── quotes_empowered_YYYYMM.csv
│   │   ├── quotes_empathetic_YYYYMM.csv
│   │   └── quotes_frustrated_YYYYMM.csv
│   └── questions/                 # Engagement question spreadsheets
│       ├── questions_community_YYYYMM.csv
│       ├── questions_validation_YYYYMM.csv
│       └── questions_education_YYYYMM.csv
│
├── images/                        # Generated graphics from Canva
│   ├── raw/                       # Bulk generated images (not yet scheduled)
│   │   ├── YYYYMM_quotes_empowered/
│   │   ├── YYYYMM_quotes_empathetic/
│   │   └── YYYYMM_questions/
│   └── scheduled/                 # Images ready for or already scheduled
│       ├── YYYYMM_week1/
│       ├── YYYYMM_week2/
│       └── YYYYMM_week3/
│
└── automation/                    # Workflow documentation and templates
    ├── SOCIAL-MEDIA-AUTOMATION-PLAN.md    # Full automation strategy
    ├── AUTOMATED-WORKFLOW.md               # Step-by-step Canva workflow
    └── canva-templates/                    # Template specs and links
        └── template-specs.md

```

---

## Naming Conventions

### CSV Files (Content Library)

**Format:** `[content-type]_[voice/category]_YYYYMM.csv`

**Examples:**
- `quotes_empowered_202501.csv` - Empowered voice quotes generated January 2025
- `quotes_empathetic_202501.csv` - Empathetic voice quotes generated January 2025
- `quotes_frustrated_202501.csv` - Frustrated/angry voice quotes generated January 2025
- `questions_community_202501.csv` - Community engagement questions
- `questions_validation_202501.csv` - Validation-focused questions
- `questions_education_202501.csv` - Educational engagement questions

**CSV Structure:**
All CSV files should follow this column structure:
```
Content Type, Quote Text, Voice, Template Style, Hashtags, Platform, Notes
```

### Image Files (Generated Graphics)

**Format:** `YYYYMMDD_[content-type]_[voice]_[number]_[platform].png`

**Examples:**
- `20250115_quote_empowered_001_IG.png` - Instagram square (1080x1080)
- `20250115_quote_empowered_001_FB.png` - Facebook landscape (1200x630)
- `20250115_question_community_012_IG.png` - Instagram engagement question
- `20250115_quote_frustrated_005_PIN.png` - Pinterest vertical (1000x1500)

**Platform Codes:**
- `IG` = Instagram (1080x1080 or 1080x1920 for stories)
- `FB` = Facebook (1200x630)
- `PIN` = Pinterest (1000x1500)
- `LI` = LinkedIn (1200x627)
- `TW` = Twitter/X (1200x675)

### Folder Organization

**Monthly Batch Folders:**
- `202501_quotes_empowered/` - All empowered quotes generated in January 2025
- `202501_week1/` - Week 1 of January scheduled content

**Rationale:**
- YYYYMM format sorts chronologically
- Descriptive names indicate content clearly
- Easy to archive older content
- Simple to find specific content types

---

## Workflow Overview

### Phase 1: Content Generation (Using Social Media Expert Agent)

1. **Engage Social Media Expert Agent**
   - Task: "Extract 50 quotes and 50 engagement questions from Chapters 1-4"
   - Agent mines book chapters for quotable content
   - Agent creates engagement questions based on themes
   - Output: CSV files in `content-library/` directory

2. **Review & Approve**
   - Review generated CSV files for quality
   - Ensure voice balance (Empowered 45%, Empathetic 40%, Frustrated 15%)
   - Verify hashtags are optimized
   - Make any necessary edits

### Phase 2: Visual Production (Canva Bulk Create)

1. **Upload CSV to Canva Template**
   - Open saved Canva template with dynamic fields
   - Use Bulk Create feature to upload CSV
   - Generate all images automatically (text auto-sizes)

2. **Export Images**
   - Export in platform-specific sizes
   - Download to `images/raw/YYYYMM_[content-type]/` folder
   - Verify quality and formatting

### Phase 3: Scheduling (Canva Content Planner)

1. **Map to Calendar**
   - Open Canva Content Planner
   - Select images from `images/raw/` folder
   - Apply posting schedule (e.g., 9 AM, 1 PM, 7 PM daily)

2. **Add Captions & Hashtags**
   - Copy hashtags from CSV
   - Add caption using templates from automation guide
   - Include calls-to-action (save, share, comment)

3. **Schedule & Publish**
   - Set auto-publish for all platforms
   - Move images to `images/scheduled/YYYYMM_week#/` folder
   - Monitor first week for engagement

### Phase 4: Engagement & Analytics

1. **Daily Engagement (20-30 mins)**
   - Respond to all comments within 24 hours
   - Like and comment on 10-20 posts in your niche
   - Share relevant content to Stories

2. **Weekly Review (15 mins)**
   - Check top 3 performing posts
   - Note patterns (topics, voice, format)
   - Adjust upcoming content if needed

3. **Monthly Deep Dive (1 hour)**
   - Review all engagement metrics
   - Identify top 10 posts and analyze
   - Update hashtag sets based on performance
   - Plan next month's content strategy

---

## Content Balance Guidelines

### Voice Distribution (Per 100 Posts)
- **Empowered Voice**: 45-50 posts
- **Empathetic Voice**: 40-45 posts
- **Frustrated/Angry Voice**: 10-15 posts

### Content Type Mix (Per Week)
- **Quote Graphics**: 14-16 posts (2-3/day)
- **Engagement Questions**: 5-7 posts (1/day)
- **Educational Carousels**: 2-3 posts
- **Personal Stories/Testimonials**: 1-2 posts
- **Book Updates/CTAs**: 1-2 posts

### Platform Frequency
- **Instagram**: 3 posts/day + 3-5 Stories/day
- **Facebook**: 2 posts/day
- **Pinterest**: 5-10 pins/day (scheduled)
- **LinkedIn**: 3-4 posts/week
- **Twitter/X**: 5-7 posts/day

---

## Current Status

### Completed:
✅ Social Media Expert Agent created in `.agents/agent-prompts/`
✅ Folder structure established
✅ Naming conventions defined
✅ Reference guides organized
✅ Automation workflow documented

### Next Steps:
1. ⏸️ **PAUSE** - User creates Social Media Expert agent manually
2. 📝 Engage Social Media Expert agent to generate:
   - 50 Empowered voice quotes from Chapters 1-4
   - 50 Empathetic voice quotes from Chapters 1-4
   - 50 Frustrated voice quotes from Chapters 1-4
   - 50 Engagement questions from Chapters 1-4
3. 🎨 Create Canva templates with dynamic fields
4. 🚀 Begin bulk production and scheduling

---

## Quick Reference

### File Locations:
- **Agent Prompt**: `/.agents/agent-prompts/social-media-expert.md`
- **Reference Patterns**: `/social/_reference/`
- **Automation Guide**: `/social/automation/AUTOMATED-WORKFLOW.md`
- **Content CSVs**: `/social/content-library/quotes/` and `/questions/`
- **Images**: `/social/images/raw/` → `/scheduled/`

### Key Documents:
- **Full Automation Plan**: `/social/automation/SOCIAL-MEDIA-AUTOMATION-PLAN.md`
- **Canva Workflow**: `/social/automation/AUTOMATED-WORKFLOW.md`
- **Example CSV Format**: `/social/_reference/content-library-EXAMPLE.csv`
- **Example Patterns**: `/social/_reference/ENGAGEMENT-PATTERNS.md` and `QUOTE-PATTERNS.md`

---

## Notes

- The `_reference/` folder uses underscore prefix per project convention (see main CLAUDE.md)
- Pattern files in `_reference/` are examples only, not actual content for posting
- All actual content for posting lives in `content-library/` as CSV files
- Social Media Expert agent will generate content directly into CSV format
- Follow naming conventions strictly for easy organization and archiving
- YYYYMM format ensures chronological sorting

---

**Ready to generate content when Social Media Expert agent is created!**
