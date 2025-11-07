# Batch Content Creation Guide

**How to create all 18 content items efficiently**

---

## 🎯 Quick Start

You have **18 health education topics** ready to create! Here's how to do it efficiently:

---

## 📋 Pre-Creation Checklist

Before you start creating content in batch:

### 1. Review the Content Plan
- [ ] Open [CONTENT_PLAN.md](CONTENT_PLAN.md)
- [ ] Read through all 18 topics
- [ ] Understand the structure

### 2. Gather Your Sources
- [ ] Open [MY_CONTENT_SOURCES.md](MY_CONTENT_SOURCES.md)
- [ ] Add your medical guidelines and references
- [ ] Prepare image sources (HTTPS URLs)
- [ ] Note any custom instructions

### 3. Prepare Your Workspace
- [ ] Open Terminal in this folder
- [ ] Have CONTENT_PLAN.md visible for reference
- [ ] Have a text editor ready for drafting content
- [ ] Clear distractions - focus time!

---

## 🚀 Creation Strategy

### Option 1: Sequential (Recommended for First Time)
Create items one by one, validate each, build confidence.

**Time**: ~30-45 min per item
**Best for**: First time, learning the system

### Option 2: Batch Draft
Draft all content long sections first, then create items in bulk.

**Time**: ~2-3 hours for all 18
**Best for**: Experienced users

### Option 3: Grouped by Theme
Create related items together (e.g., all lipid content).

**Time**: ~1 hour per theme group
**Best for**: Subject matter focus

---

## 📝 Step-by-Step: Creating One Item

### Step 1: Choose Your Topic
Pick from CONTENT_PLAN.md (start with #1 if unsure)

### Step 2: Prepare Your Content
Before running the script, have ready:
- ✅ Header (48-80 chars)
- ✅ Content short (max 120 chars)
- ✅ Content long (160-300 words, HTML)
- ✅ Keywords (6-14, semicolon-separated)
- ✅ Image URL (HTTPS)

### Step 3: Run Creation Script
```bash
python3 create_item.py
```

### Step 4: Answer Questions
The script will guide you through:
1. Group selection (latest_read, popular, heart_health)
2. Label/category
3. Header
4. Content short
5. Content long (multi-line, press Enter twice when done)
6. Keywords
7. Image URL

### Step 5: Validate
```bash
python3 validate.py
```

Fix any errors using `edit_item.py` if needed.

### Step 6: Mark Complete
Update CONTENT_PLAN.md - change ⏳ to ✅

---

## 📊 Suggested Creation Order

### Priority 1: Core Concepts (Create First)
1. ✅ Item #1: Ateroskleroz nedir?
2. ✅ Item #2: Kan yağları ve çeşitleri
3. ✅ Item #3: LDL ve kalp hastalığı
4. ✅ Item #6: Kalp krizi nasıl oluşur?

**Why**: These are foundational - other content builds on them.

### Priority 2: Prevention & Awareness
5. ✅ Item #8: Kalp krizi önlenebilir mi?
6. ✅ Item #11: Günlük hayatta kalp sağlığı
7. ✅ Item #5: Türkiye'de KKH durumu

**Why**: Positive, actionable content that engages readers.

### Priority 3: Specific Topics
8. ✅ Item #4: İyi vs kötü kolesterol
9. ✅ Item #13: LDL ve trigliserid farkı
10. ✅ Item #12: Risk hesaplama
11. ✅ Item #15: LDL hedefleri kişisel mi?

**Why**: Educational deep-dives for curious readers.

### Priority 4: Special Conditions
12. ✅ Item #7: İnme nasıl oluşur?
13. ✅ Item #9: Genç yaşta kalp krizi
14. ✅ Item #10: Belirtisiz kalp krizi
15. ✅ Item #14: Diyabet ve damar sağlığı
16. ✅ Item #17: Ailesel hiperkolesterolemi

**Why**: Important but more specific audiences.

### Priority 5: Treatment & Adherence
17. ✅ Item #16: Lipid düşürücü tedaviler
18. ✅ Item #18: Tedaviye devam önemi

**Why**: For patients already in care.

---

## 🎨 Content Templates

### Quick HTML Template (Generic):
```html
<p><b>Main Topic Title</b></p>
<p>Introduction in 1-2 sentences explaining what this is about and why it matters.</p>
<ul>
  <li><b>Key Point 1:</b> Explanation here</li>
  <li><b>Key Point 2:</b> Explanation here</li>
  <li><b>Key Point 3:</b> Explanation here</li>
</ul>
<p><i>Bu bilgi eğitim amaçlıdır ve profesyonel tıbbi danışmanlığın yerini tutmaz.</i></p>
```

### Medical Explainer Template:
```html
<p><b>Condition or Topic Name</b></p>
<p>Clear definition in plain Turkish. One or two sentences.</p>
<p><b>Neden önemli:</b> Brief explanation of risk or impact.</p>
<ol>
  <li><b>Belirtiler:</b> What to watch for</li>
  <li><b>Önleme:</b> How to reduce risk</li>
  <li><b>Ne zaman doktora:</b> When to seek help</li>
</ol>
<p><i>Bu içerik bilgilendirme amaçlıdır. Her zaman doktorunuza danışın.</i></p>
```

---

## ⚡ Speed Tips

### Prepare Content in Advance:
1. Write all your `contentLong` sections in a text editor first
2. Save them in a separate document
3. Copy/paste when running `create_item.py`

### Use Consistent Patterns:
- Reuse similar keyword structures
- Use the same disclaimers
- Follow the same HTML patterns

### Validate in Batches:
- Create 3-5 items
- Run `validate.py` once for all
- Fix any issues together

---

## ✅ Quality Checklist

For each item, verify:

### Content Quality:
- [ ] Header is clear and compelling (48-80 chars)
- [ ] Content short is engaging (max 120 chars)
- [ ] Content long follows template (160-300 words)
- [ ] Medical information is accurate
- [ ] Language is plain and accessible
- [ ] Disclaimer included for medical content

### Technical Quality:
- [ ] Only allowed HTML tags used
- [ ] All HTML tags properly closed
- [ ] Keywords: 6-14, semicolon-separated, no trailing ;
- [ ] Image URL is HTTPS
- [ ] No specific drug dosing or diagnostic criteria
- [ ] Validation passes with no errors

### Medical Safety:
- [ ] No diagnosis claims
- [ ] No treatment prescriptions
- [ ] Encourages healthcare provider consultation
- [ ] Guideline-consistent information
- [ ] Appropriate disclaimers

---

## 🐛 Common Issues & Quick Fixes

### Issue: Header too short/long
**Fix**: Count characters. Adjust. Use emojis to add 1-2 chars if needed.

### Issue: Keywords - trailing semicolon
**Fix**: Remove the last `;` at the end of your keyword list.

### Issue: Keywords - too few
**Fix**: Add more synonyms, Turkish + English variants.

### Issue: HTML tag error
**Fix**: Check all tags are closed: `<p>text</p>` not `<p>text`

### Issue: Content too short
**Fix**: Expand with more detail, examples, or additional points.

### Issue: Image URL not HTTPS
**Fix**: Find a secure image source, or use placeholder: `https://example.com/images/health-placeholder.png`

---

## 📈 Progress Tracking

### Daily Goal:
- [ ] Create 2-3 items per day = Done in 1 week

### Weekly Goal:
- [ ] Week 1: Items 1-6 (Core concepts)
- [ ] Week 2: Items 7-12 (Prevention & risk)
- [ ] Week 3: Items 13-18 (Special topics)

### Track Your Progress:
```bash
# See all created items
python3 edit_item.py
# (It shows a list at the start)
```

---

## 🎯 Daily Workflow

### Morning (Create Mode):
1. Review 2-3 topics from CONTENT_PLAN.md
2. Draft content long sections
3. Prepare keywords and headers
4. Create items using `create_item.py`

### Afternoon (Review Mode):
1. Run `validate.py` on all items
2. Fix any errors with `edit_item.py`
3. Review content for quality
4. Update CONTENT_PLAN.md progress

### End of Day:
1. Save any work in progress
2. Note any questions for reviewers
3. Plan next day's topics

---

## 💡 Pro Tips

### 1. Create a Content Template Document
Save your recurring elements:
- Standard disclaimers
- Common HTML structures
- Frequently used keywords
- Image URLs

### 2. Batch Similar Content
Group by label:
- All `lipids` content together
- All `cardiology` content together
- All `prevention` content together

### 3. Use Find & Replace
If you need to update something across multiple items:
- Draft content in editor
- Use find/replace for consistency
- Then paste into creation script

### 4. Save Validation Output
```bash
python3 validate.py > validation_report.txt
```
Review errors all at once.

### 5. Keep Notes
Track:
- Which keywords work well
- Which headers resonate
- Content that needs revision
- Questions for reviewers

---

## 🚦 Quality Gates

Before marking an item as "complete":

### Gate 1: Self-Review
- Read content as if you're a patient
- Check for clarity and accuracy
- Verify all links and references

### Gate 2: Validation
- `python3 validate.py` passes with no errors
- No warnings (or acceptable warnings only)

### Gate 3: Final Check
- Compare against CONTENT_PLAN.md requirements
- All key points covered
- Appropriate tone and style
- Medical disclaimers in place

---

## 📞 When You Need Help

### Technical Issues:
```bash
# Test JSON files
python3 test_json.py

# Fix JSON problems
python3 fix_json.py

# Verify environment
python3 verify_setup.py
```

### Content Questions:
- Check CONTENT_PLAN.md for guidance
- Review existing items in data/suggestion-EN.json
- Consult medical guidelines in MY_CONTENT_SOURCES.md
- Ask your medical reviewer

### Process Questions:
- Read README.md
- Check QUICK_START.md
- Review agent/prompts/ for detailed guidelines

---

## 🎉 Completion Celebration

When you finish all 18 items:

1. Run final validation:
   ```bash
   python3 validate.py
   ```

2. Review your work:
   ```bash
   python3 edit_item.py
   # Browse through all created items
   ```

3. Update CONTENT_PLAN.md:
   - Mark all items ✅
   - Update progress tracker

4. Prepare for review:
   - Create Pull Request (if using GitHub)
   - Tag appropriate reviewers
   - Include your CONTENT_PLAN.md as reference

5. Take a break! You've created a comprehensive health education library! 🎉

---

## 📚 Reference Links

- **Content Planning**: [CONTENT_PLAN.md](CONTENT_PLAN.md)
- **Your Sources**: [MY_CONTENT_SOURCES.md](MY_CONTENT_SOURCES.md)
- **Quick Start**: [QUICK_START.md](QUICK_START.md)
- **Full Guide**: [README.md](README.md)
- **Setup Info**: [SETUP_COMPLETE.md](SETUP_COMPLETE.md)

---

**Ready to start? Pick your first topic from CONTENT_PLAN.md and let's go! 🚀**

```bash
python3 create_item.py
```
