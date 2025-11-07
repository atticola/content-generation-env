# GitHub Privacy Guide

**How to manage your content safely on GitHub**

---

## ✅ Current Status: SAFE

Your current repository is **safe to be public** because:
- ✅ Contains only framework code and templates
- ✅ No real health content yet
- ✅ No patient information
- ✅ No proprietary medical sources
- ✅ No personal data
- ✅ Empty data files are just structure

---

## 🔓 What's OK to Keep Public

### Safe to Share:
- ✅ **Python scripts** (create_item.py, edit_item.py, etc.)
- ✅ **Documentation** (README.md, guides, etc.)
- ✅ **Schemas** (suggestion.schema.json)
- ✅ **Templates** (.github templates, prompts)
- ✅ **Empty/example data files**
- ✅ **Agent specifications** (agent.md)
- ✅ **.gitignore and config files**

### Why It's Valuable Public:
- 📖 **Open source contribution** to health content management
- 🎓 **Educational** for others building similar systems
- 💼 **Portfolio piece** showing project organization
- 🤝 **Community collaboration** potential

---

## 🔒 What Should Be Private

### Keep Private:
- 🔒 **Real health content** before publication
- 🔒 **Draft articles** with unpublished information
- 🔒 **Review files** with reviewer names/comments
- 🔒 **MY_CONTENT_SOURCES.md** with proprietary sources
- 🔒 **CONTENT_PLAN.md** once filled with real plans
- 🔒 **Internal discussions** and strategy
- 🔒 **Unpublished medical data**

### Why Keep Private:
- ⚠️ **Pre-publication content** shouldn't be public
- ⚠️ **Reviewer names** - privacy concerns
- ⚠️ **Proprietary sources** - licensing issues
- ⚠️ **Draft medical info** - quality control before release

---

## 🛡️ Two Recommended Approaches

### **Approach 1: Two Repositories (Recommended)**

#### Public Repo (Current One):
```
content-generation-env/
  ├── Scripts, docs, templates    ← Keep public
  ├── Empty schema files          ← Keep public
  ├── Agent prompts              ← Keep public
  └── Framework only             ← Keep public
```

**Use case**: Share the framework, methodology, templates

#### Private Repo (Create New):
```
content-generation-content/  (PRIVATE)
  ├── data/suggestion-EN.json          ← Real content
  ├── drafts/suggestion-EN.next.json   ← Real drafts
  ├── reviews/                         ← Real reviews
  ├── MY_CONTENT_SOURCES.md           ← Real sources
  └── CONTENT_PLAN.md                 ← Real plans
```

**Use case**: Actual content creation and management

#### How to Set This Up:
```bash
# 1. Create new private repo on GitHub
# (Go to GitHub → New Repository → Check "Private")

# 2. On your computer, create new folder
mkdir ../content-generation-content
cd ../content-generation-content

# 3. Copy only content files
cp ../content-generation-env/data/*.json data/
cp ../content-generation-env/drafts/*.json drafts/
cp ../content-generation-env/*.md .

# 4. Initialize private repo
git init
git remote add origin https://github.com/YOUR-USERNAME/content-generation-content.git

# 5. Copy scripts (optional - or reference from public repo)
cp ../content-generation-env/*.py .

# 6. Commit and push
git add .
git commit -m "Initial private content repo"
git push -u origin main
```

---

### **Approach 2: One Private Repository**

Make your current repository private when you start adding real content.

#### How to Make Repo Private:
1. Go to your GitHub repository
2. Click **Settings** (top right)
3. Scroll to bottom → **Danger Zone**
4. Click **"Change repository visibility"**
5. Select **"Make private"**
6. Confirm by typing repository name

#### When to Make Private:
- ⏰ **Before** adding real health content
- ⏰ **Before** adding proprietary medical sources
- ⏰ **Before** adding reviewer names/comments

---

## 📝 Using .gitignore Properly

Your `.gitignore` now has a **CONTENT PRIVACY SECTION**.

### When Files are Empty (Now):
Keep them committed - they're just templates.

### When You Add Real Content:
Uncomment the relevant lines in `.gitignore`:

```bash
# Edit .gitignore and uncomment these:
data/suggestion-EN.json
drafts/suggestion-EN.next.json
reviews/*.review.json
MY_CONTENT_SOURCES.md
CONTENT_PLAN.md
```

### Then Remove from Git Tracking:
```bash
# Remove files from git (keeps local copy)
git rm --cached data/suggestion-EN.json
git rm --cached drafts/suggestion-EN.next.json
git rm --cached MY_CONTENT_SOURCES.md
git rm --cached CONTENT_PLAN.md

# Commit the removal
git commit -m "Remove sensitive content files from tracking"

# Push
git push
```

Now these files stay on your computer but don't get pushed to GitHub.

---

## 🔍 What's Currently Public in Your Repo

Let me list what you've committed:

### Framework Files (OK Public):
- ✅ All Python scripts (*.py)
- ✅ All documentation (*.md)
- ✅ Schema files (schemas/*.json)
- ✅ Empty data files (data/*.json, drafts/*.json)
- ✅ GitHub templates (.github/)
- ✅ Agent prompts (agent/prompts/)
- ✅ .gitignore

### Potentially Sensitive (Check):
- ⚠️ **CONTENT_PLAN.md** - Currently has planning templates (OK for now)
- ⚠️ **MY_CONTENT_SOURCES.md** - Currently empty template (OK for now)

**Action**: Once you fill these with real sources/plans, either:
1. Make repo private, OR
2. Remove these files from tracking

---

## ✅ Best Practices

### Before Each Commit:
```bash
# Review what you're committing
git status
git diff

# Check for sensitive data
grep -r "proprietary" .
grep -r "internal" .
grep -r "draft" data/ drafts/

# Only commit if safe
git add .
git commit -m "Safe commit message"
git push
```

### Regular Privacy Audit:
```bash
# Check what's public
git ls-files

# Look for potentially sensitive files
find . -name "*.json" -o -name "MY_CONTENT*"

# Review file contents before committing
```

### Use Descriptive Commit Messages:
```bash
# Good - clear what was changed
git commit -m "Add validation script for health content"
git commit -m "Update documentation for content creation"

# Bad - might hint at sensitive info
git commit -m "Add internal medical guidelines"
git commit -m "Draft content for upcoming campaign"
```

---

## 🚨 If You Accidentally Commit Sensitive Data

### If Just Committed (Not Pushed Yet):
```bash
# Undo last commit, keep changes
git reset --soft HEAD~1

# Remove sensitive file
git rm --cached sensitive-file.json

# Commit again without sensitive file
git commit -m "Update without sensitive data"
```

### If Already Pushed to GitHub:
1. **Remove file from history**:
   ```bash
   # Use BFG Repo-Cleaner or git-filter-branch
   # This is complex - better to make repo private instead
   ```

2. **Simpler solution**: Make repository private
   - Go to Settings → Danger Zone → Make Private

3. **Contact GitHub** if contains truly sensitive data
   - They can help purge from cache

---

## 📋 Privacy Checklist

Before making commits with real content:

### Pre-Content Creation:
- [ ] Decided: Public framework + Private content, OR all private?
- [ ] Updated .gitignore with content privacy section
- [ ] Tested .gitignore works (create test file, verify not tracked)

### When Adding Real Content:
- [ ] Reviewed all files being committed
- [ ] No patient information
- [ ] No proprietary medical sources
- [ ] No unpublished health information
- [ ] No reviewer names or internal comments
- [ ] Repository privacy setting matches content sensitivity

### Regular Maintenance:
- [ ] Audit public files monthly
- [ ] Review .gitignore is up to date
- [ ] Check no sensitive data in commit history
- [ ] Verify repo visibility setting is correct

---

## 💡 Recommended Setup (Summary)

### For Your Use Case:

**Option A: Keep Current Approach (Best for Sharing Framework)**
```
✅ Current repo: PUBLIC
   - Framework, scripts, docs, templates
   - Great for portfolio and open source

✅ Create new repo: PRIVATE
   - All real content
   - Working drafts and reviews
   - Internal sources and plans
```

**Option B: Switch to Private Now**
```
🔒 Make current repo: PRIVATE
   - Everything in one place
   - Simpler to manage
   - Less open source contribution
   - Still good for portfolio (you can show screenshots)
```

---

## 🎯 My Recommendation for You

Based on your setup, I recommend **Option A** (two repos):

### Why:
1. ✅ Your framework is excellent - worth sharing publicly
2. ✅ Helps other health content creators
3. ✅ Great portfolio piece showing technical + domain expertise
4. ✅ Keeps actual health content properly private
5. ✅ Clear separation of concerns

### Next Steps:
1. **For now**: Current repo is fine as-is (it's just framework)
2. **Before real content**: Create private repo for actual articles
3. **Update .gitignore**: Uncomment content privacy section when needed
4. **Work in private repo**: Do all content creation there

---

## 📞 Quick Reference

```bash
# Check what's tracked
git ls-files

# Remove file from tracking (keep locally)
git rm --cached FILENAME

# Make repo private
# GitHub → Settings → Danger Zone → Change visibility

# Check for sensitive data before commit
git diff --cached

# Review commit history
git log --oneline
```

---

## 🤔 FAQ

### Q: My repo is public now. Is that a problem?
**A**: No! Currently you only have framework/templates (no real content), so it's perfectly safe.

### Q: When should I make it private?
**A**: Before adding real health content, proprietary sources, or reviewer information.

### Q: Can I make it public again later?
**A**: Yes, but be careful - once something's been public, it may be cached/archived elsewhere.

### Q: What about images?
**A**: Store image URLs, not the actual images. Ensure images are licensed for public use.

### Q: Should I worry about commit history?
**A**: Only if you previously committed sensitive data. Current commits are all safe.

---

**Bottom Line**: Your current public repo is **completely fine**. It's a great framework! Just be mindful when you start adding real content - that's when privacy matters.

---

**Last Updated**: 2025-11-07
