# Quick Start Guide - Enhanced Content Generation Workflow

**Updated**: 2025-11-07
**Version**: 2.0 (Enhanced with Images & Review System)

This guide helps you generate all 18 health education content items with enhanced visuals and reviewer comments functionality.

---

## 🎯 What's New in Version 2.0

### ✨ Enhancements
1. **Enhanced Image System**
   - More visually appealing prompts (not flat/simple)
   - Detailed specifications for clickable images
   - Rich color palettes and gradients
   - Professional editorial illustration style

2. **Reviewer Comments System**
   - Schema now includes `imagePrompt` field
   - Review template with comment sections
   - Export to markdown for easier review

3. **Original Title Preservation**
   - New batch prompt strictly preserves your original Turkish titles
   - No more AI changing "Ateroskleroz nedir?" to something else

4. **Readable Review Format**
   - Export items to markdown files
   - Both Turkish and English versions
   - Easy for reviewers to read and comment

---

## 📋 Complete Workflow

### Step 1: Generate All 18 Items with AI

**File to use**: `docs/ai-prompts/batch-generation/GENERATE_ALL_18_ENHANCED.txt`

1. Open the file above
2. Copy the entire content
3. Paste into Claude or ChatGPT
4. Wait for complete JSON array with all 18 items
5. Save the output

**What you get**:
- ✅ All 18 items with EXACT original Turkish titles
- ✅ Enhanced image prompts (100-150 words, visually rich)
- ✅ Bilingual keywords
- ✅ Proper medical disclaimers
- ✅ Valid JSON ready to import

---

### Step 2: Import Generated Items

**Script**: `scripts/add_batch_items.py`

```bash
python3 scripts/add_batch_items.py path/to/generated-items.json
```

This will:
- Parse the JSON array
- Generate UUIDs for each item
- Add timestamps and metadata
- Distribute items to correct groups
- Save to `drafts/suggestion-EN.next.json`

---

### Step 3: Validate Content

**Script**: `scripts/validate.py`

```bash
python3 scripts/validate.py
```

Checks:
- ✅ JSON structure
- ✅ Required fields present
- ✅ Header length (48-80 chars)
- ✅ Keywords format (no trailing semicolon)
- ✅ HTML tags allowed only
- ✅ Schema compliance

Fix any errors before proceeding.

---

### Step 4: Export to Markdown for Review

**Script**: `scripts/export_to_markdown.py`

```bash
python3 scripts/export_to_markdown.py --source drafts --output-dir exports/review_2025_11_07
```

This creates individual `.md` files for each item:
- Readable format with all content
- Turkish version clearly shown
- Section for reviewer comments
- Image prompt visible
- Validation checklist included

**Output**: `exports/review_2025_11_07/` directory with 18 markdown files

---

### Step 5: Review Process

**Reviewers can**:
1. Open markdown files in any text editor
2. Read content in readable format (not JSON)
3. Add comments in designated sections
4. Mark severity (low/medium/high)
5. Propose changes
6. Sign off with approval decision

**Review roles**:
- 🩺 Medical Reviewer: Check accuracy, safety, disclaimers
- 📱 Product Reviewer: Check UX, tone, formatting
- ✍️ Content Reviewer: Check grammar, clarity, style

---

### Step 6: Generate Images

**For each item**:

1. **Get the image prompt** from markdown file or master document
2. **Use AI image generator**:
   - Midjourney (recommended for quality)
   - DALL-E 3 (good balance)
   - Stable Diffusion (customizable)
   - Adobe Firefly (commercial-safe)

3. **Generate image** with the prompt
4. **Optimize**:
   ```bash
   # Resize to 1280x720
   # Convert to WebP
   # Compress to <150KB
   ```

5. **Upload to CDN** and get HTTPS URL
6. **Update JSON** with final image URL

---

### Step 7: Update Image URLs

**Script**: `scripts/edit_item.py`

```bash
python3 scripts/edit_item.py
```

For each item:
1. Select the item
2. Choose field: `imagePath`
3. Enter the HTTPS URL
4. Save

---

### Step 8: Final Validation

```bash
python3 scripts/validate.py
```

Ensure:
- ✅ All 18 items present
- ✅ All image URLs are HTTPS
- ✅ All required fields complete
- ✅ No validation errors

---

### Step 9: Move to Production

When ready:

```bash
cp drafts/suggestion-EN.next.json data/suggestion-EN.json
```

Or commit and create PR if using GitHub workflow.

---

## 🎨 Image Generation Details

### Quick Image Workflow

For each of 18 items:

1. **Find prompt** in `content-items/ALL_18_ITEMS_MASTER.md`
2. **Copy prompt** to image AI
3. **Generate** multiple options (3-4)
4. **Pick best** option
5. **Check safe zone**: Crop to 9:9 center - does it still work? ✅
6. **Optimize**: Resize, convert WebP, compress
7. **Upload** and get URL
8. **Update** item with URL

### Image Quality Checklist

Before uploading, verify:
- [ ] 16:9 aspect ratio (1280x720px)
- [ ] Main subject centered in 9:9 safe zone
- [ ] No text or typography
- [ ] File size <150KB
- [ ] WebP or JPEG format
- [ ] Visually appealing (not flat/simple)
- [ ] Professional quality
- [ ] Related to content topic

---

## 📝 Review Comment System

### How to Add Comments

When reviewing markdown files, add comments in this format:

```markdown
#### 🔴 🔵 Comment by Dr. Ahmet Yılmaz
**Field**: `contentLong`
**Severity**: High
**Status**: Open

The statement about cholesterol levels needs clarification. Current wording
might be misinterpreted as medical advice.

**Proposed Change**:
Replace "Kolesterol seviyeniz 200'ün üzerindeyse" with
"Kolesterol seviyeniz hedef değerlerin üzerindeyse"
```

**Severity icons**:
- 🟢 Low (suggestions, minor improvements)
- 🟡 Medium (needs attention, affects quality)
- 🔴 High (must fix, safety or accuracy issue)

**Status icons**:
- 🔵 Open (needs action)
- ✅ Accepted (change made)
- ❌ Rejected (won't change, with reason)

---

## 🚀 Speed Tips

### Generate All Content in 1 Hour

1. **5 min**: Copy prompt from `GENERATE_ALL_18_ENHANCED.txt`
2. **15 min**: Wait for AI to generate all 18 items
3. **5 min**: Save JSON and import with script
4. **5 min**: Run validation
5. **10 min**: Export to markdown
6. **20 min**: Quick review of all items

Total: ~1 hour for all 18 content items (text only)

### Generate All Images in 2-3 Hours

1. **2 hours**: Generate 18 images (6-7 min each)
2. **30 min**: Optimize all images
3. **30 min**: Upload and update URLs

Total: ~3 hours for all 18 images

**Combined**: 4 hours total for complete content with images

---

## 📂 File Structure Reference

```
content-generation-env/
├── content-items/              # NEW: Individual markdown files
│   ├── 01-ateroskleroz-nedir.md
│   ├── 02-kan-yaglari-nedir.md
│   ├── 03-ldl-kolesterol.md
│   └── ALL_18_ITEMS_MASTER.md  # Master reference
│
├── docs/
│   ├── ai-prompts/
│   │   ├── batch-generation/
│   │   │   └── GENERATE_ALL_18_ENHANCED.txt  # ⭐ Use this
│   │   └── image-generation/
│   │       ├── ENHANCED_IMAGE_PROMPTS.txt
│   │       └── QUICK_IMAGE_GUIDE.md
│   │
│   └── reference/
│       ├── CONTENT_PLAN.md              # Original 18 titles
│       └── IMAGE_SPECIFICATIONS.md       # Updated specs
│
├── scripts/
│   ├── add_batch_items.py       # Import generated JSON
│   ├── export_to_markdown.py    # NEW: Export for review
│   ├── validate.py              # Validation
│   └── edit_item.py             # Update fields
│
├── templates/
│   └── CONTENT_REVIEW_TEMPLATE.md  # NEW: Review template
│
├── data/
│   └── suggestion-EN.json       # Production data
│
└── drafts/
    └── suggestion-EN.next.json  # Draft/staging data
```

---

## ⚠️ Important Notes

### Title Preservation
The new `GENERATE_ALL_18_ENHANCED.txt` prompt **strictly preserves** your original Turkish titles:
- ✅ "Ateroskleroz (Damar Sertliği/Tıkanıklığı) Nedir?"
- ❌ "What is Atherosclerosis?" (wrong - was happening before)

### Image Quality
The enhanced prompts create **visually appealing** images:
- ✅ Gradients, layers, depth, lighting effects
- ❌ Simple flat circles or basic shapes (too boring)

### Reviewer Comments
The review system is built into schema and templates:
- Comments can be added during review
- Three reviewer roles (medical, product, content)
- Severity levels and dispositions tracked

---

## 🆘 Troubleshooting

### Problem: AI changed my titles
**Solution**: Use `GENERATE_ALL_18_ENHANCED.txt` - it has strict instructions to preserve exact titles

### Problem: Images are too simple/flat
**Solution**: The enhanced prompts include visual richness keywords - make sure AI uses the full prompt

### Problem: Can't add reviewer comments
**Solution**: Use markdown export feature - easier than editing JSON directly

### Problem: Validation errors
**Solution**: Check these common issues:
- Trailing semicolon in keywords
- Header not 48-80 chars
- ContentShort >120 chars
- Image URL not HTTPS
- Missing required fields

---

## 📞 Quick Reference Commands

```bash
# Generate content (copy prompt first, then paste to AI)
# docs/ai-prompts/batch-generation/GENERATE_ALL_18_ENHANCED.txt

# Import generated JSON
python3 scripts/add_batch_items.py generated.json

# Validate
python3 scripts/validate.py

# Export for review
python3 scripts/export_to_markdown.py --source drafts

# Edit item
python3 scripts/edit_item.py

# Move to production
cp drafts/suggestion-EN.next.json data/suggestion-EN.json
```

---

## ✅ Success Checklist

Before considering content "done":

- [ ] All 18 items generated with exact Turkish titles
- [ ] All items validated with no errors
- [ ] All items have enhanced image prompts
- [ ] All images generated and optimized
- [ ] All image URLs updated (HTTPS)
- [ ] Medical review completed
- [ ] Content review completed
- [ ] Product review completed
- [ ] All reviewer comments addressed
- [ ] Final validation passed
- [ ] Moved to production data file

---

## 🎓 Learning Resources

- **Image Specs**: `docs/reference/IMAGE_SPECIFICATIONS.md`
- **Content Plan**: `docs/reference/CONTENT_PLAN.md`
- **Master Reference**: `content-items/ALL_18_ITEMS_MASTER.md`
- **Schema**: `schemas/suggestion.schema.json`

---

**Questions?** Check the README.md or documentation in `docs/` directory.

**Ready to start?** → Go to Step 1 and copy `GENERATE_ALL_18_ENHANCED.txt`! 🚀
