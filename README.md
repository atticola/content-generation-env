# Health Content Generation Environment

**A complete system for creating, reviewing, and managing health education content**

---

## 🚀 Quick Start

### Create Content (No coding needed!)
```bash
./create.sh
```
Follow the prompts to create a new health education article.

### Edit Content
```bash
./edit.sh
```
Browse and edit existing articles.

### Validate Content
```bash
./validate.sh
```
Check for errors before submitting.

---

## 📚 Documentation

### Getting Started
- **[Start Here](docs/getting-started/START_HERE.md)** - Navigation hub
- **[Quick Start Guide](docs/getting-started/QUICK_START.md)** - 5-minute tutorial
- **[Setup Complete](docs/getting-started/SETUP_COMPLETE.md)** - What was built

### Guides
- **[Batch Creation Guide](docs/guides/batch_create_guide.md)** - Create multiple items efficiently
- **[GitHub Privacy Guide](docs/guides/GITHUB_PRIVACY_GUIDE.md)** - Managing public/private repos

### Reference
- **[Project Overview](docs/reference/PROJECT_OVERVIEW.md)** - Complete system overview
- **[Content Plan](docs/reference/CONTENT_PLAN.md)** - All 18 topics planned

### AI-Assisted Content Generation
- **[Single Item Prompts](docs/ai-prompts/single-item/)** - Generate one item at a time
- **[Batch Generation](docs/ai-prompts/batch-generation/)** - Generate all items at once

---

## 📁 Project Structure

```
content-generation-env/
├── README.md                 ← You are here
├── create.sh                 ← Create new content (shortcut)
├── edit.sh                   ← Edit content (shortcut)
├── validate.sh               ← Validate content (shortcut)
│
├── scripts/                  ← Python helper scripts
│   ├── create_item.py
│   ├── edit_item.py
│   ├── validate.py
│   └── ...
│
├── docs/                     ← All documentation
│   ├── getting-started/      ← Quick start guides
│   ├── guides/               ← How-to guides
│   ├── reference/            ← Reference documentation
│   └── ai-prompts/           ← AI generation prompts
│
├── templates/                ← User templates
│   └── MY_CONTENT_SOURCES.md
│
├── data/                     ← Published content (production)
│   └── suggestion-EN.json
│
├── drafts/                   ← Work in progress
│   └── suggestion-EN.next.json
│
├── reviews/                  ← Review feedback
├── schemas/                  ← Validation schemas
├── agent/                    ← AI agent specifications
└── .github/                  ← GitHub automation
```

---

## 🎯 Content Types

This system manages health education content covering:

### Topics (18 total)
1. Atherosclerosis (Ateroskleroz)
2. Blood lipids types
3. LDL and heart disease
4. Good vs bad cholesterol
5. CVD situation in Turkey
6. How heart attacks occur
7. How strokes occur
8. Heart attack prevention
9. Young heart attacks
10. Silent heart attacks
11. Daily heart health
12. Risk assessment
13. LDL vs triglycerides
14. Diabetes and vascular health
15. Personalized LDL targets
16. Lipid-lowering therapies
17. Familial hypercholesterolemia
18. Treatment adherence

### Content Groups
- **latest_read** - The Newest articles
- **popular** - Popular Health Topics
- **heart_health** - Heart Health focused

---

## 🛠️ Common Commands

### Content Management
```bash
# Create new item
./create.sh

# Edit existing item
./edit.sh

# Validate all content
./validate.sh
```

### Direct Script Access
```bash
# Run scripts directly (if needed)
python3 scripts/create_item.py
python3 scripts/edit_item.py
python3 scripts/validate.py
python3 scripts/fix_json.py
python3 scripts/test_json.py
python3 scripts/verify_setup.py
python3 scripts/add_batch_items.py
```

### AI-Assisted Generation
```bash
# Single item generation
open docs/ai-prompts/single-item/COPY_PASTE_PROMPT.txt

# Batch generation (all 17 items)
open docs/ai-prompts/batch-generation/BATCH_GENERATE_ALL_17.txt
```

---

## ✅ Content Rules

### Headers
- **Length**: 48-80 characters
- **Style**: Clear benefit, one emoji optional
- **Example**: "Ateroskleroz Nedir? Damar Sağlığınızı Koruyun 🛡️"

### Content Short
- **Length**: Max 120 characters
- **Format**: No HTML, plain text
- **Purpose**: Teaser/preview

### Content Long
- **Length**: 160-300 words
- **Format**: HTML with restricted tags only
- **Allowed tags**: `<p>`, `<ul>`, `<ol>`, `<li>`, `<b>`, `<i>`, `<br>`, `<blockquote>`
- **Forbidden**: Links, scripts, external content

### Keywords
- **Count**: 6-14 keywords
- **Format**: Semicolon-separated, NO trailing semicolon
- **Language**: Mix Turkish and English
- **Example**: `ateroskleroz;atherosclerosis;kalp krizi;heart attack`

### Medical Content
- ✅ **DO**: Educate, inform, include disclaimers
- ❌ **DON'T**: Diagnose, prescribe drugs, replace medical advice

---

## 🔄 Workflow

### 1. Create Content
```bash
./create.sh
# Answer questions interactively
```

### 2. Validate
```bash
./validate.sh
# Check for errors
```

### 3. Review
- Content goes to medical, product, and editorial reviewers
- Feedback stored in `reviews/` folder

### 4. Revise (if needed)
```bash
./edit.sh
# Address reviewer feedback
```

### 5. Publish
- Approved content moves from `drafts/` to `data/`
- Status changes from DRAFT → ACTIVE

---

## 🤖 AI-Assisted Generation

This system supports AI-generated content:

### Single Item
1. Open: `docs/ai-prompts/single-item/COPY_PASTE_PROMPT.txt`
2. Copy prompt
3. Paste to Claude or ChatGPT
4. Get JSON response
5. Add to drafts

### Batch (All 17 items)
1. Open: `docs/ai-prompts/batch-generation/BATCH_GENERATE_ALL_17.txt`
2. Copy prompt
3. Paste to Claude (recommended)
4. Get JSON array
5. Run: `python3 scripts/add_batch_items.py`

**Time savings**: ~16 hours vs manual creation!

---

## 🔒 Security & Privacy

### Current Repository (Public)
- ✅ Framework and scripts - safe to share
- ✅ Documentation - educational value
- ✅ Empty data templates - no sensitive info

### When Adding Real Content
- 🔒 Make repository private, OR
- 🔒 Use separate private repo for content
- 🔒 See: [GitHub Privacy Guide](docs/guides/GITHUB_PRIVACY_GUIDE.md)

---

## 📊 Content Lifecycle

```
DRAFT → IN_REVIEW → CHANGES_REQUESTED → APPROVED → ACTIVE
                                                      ↓
                                                  INACTIVE
```

### States
- **DRAFT**: Being created
- **IN_REVIEW**: Sent for review
- **CHANGES_REQUESTED**: Needs revisions
- **APPROVED**: Ready to publish
- **ACTIVE**: Published and live
- **INACTIVE**: Archived

---

## 🎓 Learning Resources

### New to the System?
1. Read: [Start Here](docs/getting-started/START_HERE.md)
2. Try: `./create.sh` - Create test item
3. Learn: [Quick Start](docs/getting-started/QUICK_START.md)

### Advanced Usage
1. Batch creation: [Batch Guide](docs/guides/batch_create_guide.md)
2. AI generation: [AI Prompts](docs/ai-prompts/)
3. System details: [Project Overview](docs/reference/PROJECT_OVERVIEW.md)

---

## 🐛 Troubleshooting

### Validation Errors
```bash
# See specific errors
./validate.sh

# Fix common issues
python3 scripts/fix_json.py

# Test JSON validity
python3 scripts/test_json.py
```

### Script Issues
```bash
# Verify environment setup
python3 scripts/verify_setup.py
```

### Common Issues
- **"File not found"** - Make sure you're in project root directory
- **"Invalid JSON"** - Run `python3 scripts/fix_json.py`
- **"Validation failed"** - Read error messages, use `./edit.sh` to fix

---

## 👥 Team Roles

### Content Creators
- Create new articles using `./create.sh`
- Edit based on reviewer feedback
- Focus on clear, accessible language

### Medical Reviewers
- Review clinical accuracy
- Check guideline consistency
- Ensure appropriate disclaimers

### Product Reviewers
- Review UX and product fit
- Check brand consistency
- Verify feature integration

### Content Editors
- Polish language and tone
- Optimize keywords for SEO
- Ensure localization quality

---

## 📈 Metrics

Each article tracks:
- **readCount** - Number of views
- **likedCount** - User likes
- **bookmarkedCount** - User saves

---

## 🔧 Technical Details

### Requirements
- Python 3.6+
- No external dependencies (uses standard library only)
- Git (for version control)
- GitHub account (for collaboration)

### Validation
- JSON Schema validation
- HTML tag restrictions
- Content length checks
- Keyword format validation
- Medical content safeguards

---

## 📞 Support

### Documentation
- **Getting Started**: [docs/getting-started/](docs/getting-started/)
- **How-To Guides**: [docs/guides/](docs/guides/)
- **Reference**: [docs/reference/](docs/reference/)

### Quick Help
```bash
# View available commands
ls scripts/

# Check system status
python3 scripts/verify_setup.py

# Validate content
./validate.sh
```

---

## 🎉 Quick Wins

### Create Your First Article (5 minutes)
```bash
./create.sh
```

### Generate 17 Articles with AI (1 hour)
```bash
open docs/ai-prompts/batch-generation/BATCH_GENERATE_ALL_17.txt
# Copy, paste to Claude, get results
python3 scripts/add_batch_items.py
```

### Validate Everything
```bash
./validate.sh
```

---

## 📝 Version

**Version**: 1.0.0
**Last Updated**: 2025-11-07
**Status**: ✅ Production Ready

---

## 🚀 Let's Create!

Everything is ready for you to create amazing health education content.

**Start here**: `./create.sh` or read [START_HERE.md](docs/getting-started/START_HERE.md)

**Questions?** Check the [documentation](docs/) or run `python3 scripts/verify_setup.py`

---

**Built for content creators who want to focus on writing, not coding** ❤️
