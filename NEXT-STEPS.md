# Next Steps: Social Media Content Generation
## Setup Complete - Ready for Agent Engagement

---

## ✅ What's Been Completed

### 1. Social Media Expert Agent Created
**Location**: `/.agents/agent-prompts/social-media-expert.md`

This comprehensive 1000+ line agent has expertise in:
- Quote extraction from book chapters
- Engagement question creation
- Platform-specific content strategy
- Hashtag optimization
- Trauma-informed content guidelines
- Community management
- Analytics and optimization

### 2. Organized Folder Structure
```
social/
├── _reference/                 # Pattern examples and guides
├── content-library/           # Actual content CSVs
│   ├── quotes/               # Quote spreadsheets
│   └── questions/            # Question spreadsheets
├── images/                    # Generated graphics
│   ├── raw/                  # Bulk exports
│   └── scheduled/            # Ready to post
└── automation/                # Workflow docs
    ├── canva-templates/      # Template specs
    ├── AUTOMATED-WORKFLOW.md
    └── SOCIAL-MEDIA-AUTOMATION-PLAN.md
```

### 3. Naming Conventions Established
- **CSV Files**: `[content-type]_[voice]_YYYYMM.csv`
- **Images**: `YYYYMMDD_[type]_[voice]_[num]_[platform].png`
- Consistent, chronological, easy to organize

### 4. Reference Materials Organized
- Pattern examples moved to `_reference/`
- Example CSV format provided
- Automation guides documented
- Canva template specifications detailed

---

## ⏸️ PAUSE HERE - Manual Task Required

### You Need To: Create the Social Media Expert Agent

**Steps:**
1. Go to your Claude agent creation interface
2. Create a new agent called **"Social Media Expert"**
3. Copy the contents from: `/.agents/agent-prompts/social-media-expert.md`
4. Paste into the agent's system prompt
5. Save/activate the agent

**Why This Can't Be Automated:**
The agent creation process is a manual UI action in your Claude interface. Once you've created the agent, you can then invoke it programmatically for content generation.

---

## 🚀 After Agent Creation - Content Generation Phase

### Step 1: Invoke Social Media Expert Agent

**Task Assignment:**
```
Generate 50 quotes of each voice type from Chapters 1-4 of "From Chaos to Clarity":

Voice Types:
- 50 Empowered voice quotes
- 50 Empathetic voice quotes
- 50 Frustrated/Angry voice quotes

Source Chapters:
- Chapter 1: Acknowledging the Complexities
- Chapter 2: The Mask Behind the Charm
- Chapter 4: Recognizing the Chaos
- (Include any other completed chapters)

Output Format:
Create CSV files following the naming convention:
- quotes_empowered_202501.csv
- quotes_empathetic_202501.csv
- quotes_frustrated_202501.csv

Save to: /social/content-library/quotes/

CSV Structure:
Content Type, Quote Text, Voice, Template Style, Hashtags, Platform, Notes
```

### Step 2: Generate Engagement Questions

**Task Assignment:**
```
Generate 50 engagement questions based on themes from Chapters 1-4:

Question Categories:
- 15 Recognition & Validation questions
- 15 Community Support questions
- 10 Practical Guidance questions
- 10 Hope & Recovery questions

Output Format:
Create CSV files:
- questions_community_202501.csv
- questions_validation_202501.csv
- questions_education_202501.csv

Save to: /social/content-library/questions/

CSV Structure:
Content Type, Quote Text, Voice, Template Style, Hashtags, Platform, Notes
```

### Step 3: Review Generated Content

**Quality Check:**
- Verify voice distribution (45% Empowered, 40% Empathetic, 15% Frustrated)
- Ensure quotes are standalone powerful (no context needed)
- Check character counts (65-280 characters ideal)
- Verify hashtag relevance and optimization
- Confirm all sources are noted

### Step 4: Canva Template Creation

**Follow Guide**: `/social/automation/canva-templates/template-specs.md`

**Create 5 Templates:**
1. Empowered Statement (Deep Teal background)
2. Engagement Question (Soft Cream with Sage accent)
3. Punch Quote (Charcoal/dramatic)
4. Empathetic Educational (Sage Green, serif font)
5. Call-to-Action (Split design)

**Enable Bulk Create:**
- Add dynamic text field
- Connect to CSV column: `Quote Text`
- Enable auto-resize to fit
- Test with 5 sample quotes

### Step 5: Bulk Generate Images

**Process:**
1. Open Template 1 (Empowered)
2. Bulk Create → Upload `quotes_empowered_202501.csv`
3. Generate all 50 images
4. Resize for platforms (IG, FB, PIN, LI, TW)
5. Export to `/social/images/raw/202501_quotes_empowered/`
6. Repeat for all voice types and questions

**Expected Output:**
- 150 quote graphics (50 × 3 voice types)
- 50 question graphics
- **Total: 200 images** from one CSV upload session

### Step 6: Schedule via Canva Content Planner

**Setup:**
1. Open Canva Content Planner
2. Connect Instagram, Facebook, Pinterest, LinkedIn, Twitter
3. Select all 200 generated images
4. Set posting schedule:
   - 3 posts/day: 9 AM, 1 PM, 7 PM
   - Mix voice types and content types
   - Balance throughout week

**Schedule Pattern:**
- Monday: Empowered (start week strong)
- Tuesday: Engagement Question (community building)
- Wednesday: Educational/Validation (midweek value)
- Thursday: Empathetic (supportive)
- Friday: Empowered/Hope (weekend transition)
- Saturday: Reflective (rest day)
- Sunday: Inspiration/Resources (week prep)

**Add Captions:**
- Copy hashtags from CSV
- Use caption templates from automation guide
- Include call-to-action (save, share, comment)

### Step 7: Launch & Monitor

**Week 1:**
- Posts auto-publish from Canva
- Respond to all comments within 24 hours
- Monitor engagement metrics
- Adjust posting times if needed

**Weekly Review:**
- Check top 3 performing posts
- Note patterns (voice, topic, format)
- Adjust content mix if needed

**Monthly:**
- Full analytics review
- Generate next batch (50 more of each type)
- Create template variations for visual refresh

---

## 📊 Expected Timeline

### Immediate (Today):
- ⏸️ **USER ACTION**: Create Social Media Expert agent

### Day 1 After Agent Creation:
- Invoke agent to generate all 200 content pieces (quotes + questions)
- Review and approve CSV files
- Total time: 30-60 minutes (agent does the work)

### Day 2:
- Create 5 Canva templates with Bulk Create enabled
- Test with 5 sample quotes from each CSV
- Total time: 2-3 hours (one-time setup)

### Day 3:
- Bulk generate all 200 images via Canva
- Export in platform-specific sizes
- Total time: 1-2 hours (mostly automated)

### Day 4:
- Schedule all 200 posts in Canva Content Planner
- Set up posting times and captions
- Total time: 2-3 hours (one-time setup)

### Day 5+:
- Auto-posting begins!
- Daily engagement: 20-30 mins
- Weekly review: 15 mins
- Monthly generation: 1-2 hours

---

## 📈 What This Achieves

**Content Volume:**
- 200 unique social media posts
- 3 posts/day = 66 days of content
- With rotation and template variations = 6+ months of content

**Platforms Covered:**
- Instagram (primary)
- Facebook
- Pinterest
- LinkedIn
- Twitter/X

**Growth Potential:**
- Months 1-3: Build to 500-1000 followers
- Months 4-6: Grow to 2000-3000 followers
- Book Launch: Audience ready to buy

**Time Investment:**
- Setup: 8-10 hours (one time)
- Monthly: 2-3 hours (new content generation)
- Daily: 20-30 mins (engagement)

---

## 🎯 Success Metrics

### Month 1:
- 100-200 new followers across platforms
- 3-5% engagement rate
- Baseline audience established

### Month 2:
- 200-400 new followers (cumulative 300-600)
- 5-8% engagement rate
- Top-performing content identified

### Month 3:
- 300-600 new followers (cumulative 600-1200)
- 8-12% engagement rate
- Community actively engaging

### Book Launch (Month 6):
- 1000-2000 engaged followers
- Email list of 500-1000 subscribers
- 50-100 advance reviews secured
- Launch day sales from established audience

---

## 📝 Quick Reference

### Key Files:
- **Agent Prompt**: `/.agents/agent-prompts/social-media-expert.md`
- **Workflow Guide**: `/social/automation/AUTOMATED-WORKFLOW.md`
- **Template Specs**: `/social/automation/canva-templates/template-specs.md`
- **This Document**: `/social/NEXT-STEPS.md`

### Key Folders:
- **Content CSVs**: `/social/content-library/quotes/` and `/questions/`
- **Generated Images**: `/social/images/raw/`
- **Scheduled Images**: `/social/images/scheduled/`

### Next Immediate Action:
**Create the Social Media Expert agent, then invoke it to generate 200 content pieces.**

---

## ❓ Questions or Issues?

Common troubleshooting scenarios are documented in:
- `/social/automation/AUTOMATED-WORKFLOW.md` (Canva-specific)
- `/social/automation/SOCIAL-MEDIA-AUTOMATION-PLAN.md` (Strategy)
- `/social/README.md` (Folder organization)

**Ready to generate content once agent is created!** 🚀
