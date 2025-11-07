# Project Overview: Suggestion CMS

**A Complete Content Management System for Health Education Articles**

---

## 🎯 What We Built

This is a complete, production-ready content management system designed specifically for creating, reviewing, and publishing health education content. It includes:

- ✅ **Structured data model** with JSON schemas
- ✅ **Easy-to-use Python scripts** for non-coders
- ✅ **Automated validation** to catch errors
- ✅ **Review workflow** with multi-role support
- ✅ **GitHub integration** with automated checks
- ✅ **Comprehensive documentation** for all users

---

## 📂 Complete File Structure

```
content-generation-env/
│
├── 📄 README.md                      ← Start here! Complete guide
├── 📄 QUICK_START.md                 ← 5-minute getting started guide
├── 📄 PROJECT_OVERVIEW.md            ← This file
├── 📄 .gitignore                     ← Git configuration
│
├── 🐍 create_item.py                 ← Script: Create new articles
├── 🐍 edit_item.py                   ← Script: Edit existing articles
├── 🐍 validate.py                    ← Script: Validate content
│
├── 📁 data/                          ← Published content (LIVE)
│   └── suggestion-EN.json            ← Production data file
│
├── 📁 drafts/                        ← Work in progress (DRAFT)
│   └── suggestion-EN.next.json       ← Staging data file
│
├── 📁 reviews/                       ← Review feedback
│   └── {item-id}.review.json         ← Per-item reviews (created automatically)
│
├── 📁 schemas/                       ← Data validation rules
│   └── suggestion.schema.json        ← JSON Schema specification
│
├── 📁 agent/                         ← AI agent instructions
│   ├── agent.md                      ← Complete system specification
│   └── prompts/
│       ├── create_item.prompt.md     ← Creation prompt for AI
│       └── edit_item.prompt.md       ← Editing prompt for AI
│
└── 📁 .github/                       ← GitHub automation
    ├── CODEOWNERS                    ← Define reviewers
    ├── pull_request_template.md      ← PR template
    ├── workflows/
    │   └── validate.yml              ← Automated validation CI
    └── ISSUE_TEMPLATE/
        ├── content_request.md        ← Template for new content requests
        └── edit_request.md           ← Template for edit requests
```

---

## 🚀 Key Features

### 1. **User-Friendly Scripts**
No coding knowledge required! Just run:
```bash
python3 create_item.py    # Create new article
python3 edit_item.py      # Edit existing article
python3 validate.py       # Check if content is valid
```

### 2. **Comprehensive Validation**
Automatic checks for:
- ✅ Required fields present
- ✅ Correct data formats (dates, UUIDs, URLs)
- ✅ Content length requirements
- ✅ HTML tag restrictions
- ✅ Keyword formatting
- ✅ Status transitions

### 3. **Multi-Role Review System**
Three types of reviewers:
- 🏥 **Medical Reviewers** - Clinical accuracy
- 📦 **Product Reviewers** - Product fit and UX
- ✏️ **Content Editors** - Language, tone, SEO

### 4. **GitHub Integration**
- Automated validation on every Pull Request
- Required reviews from code owners
- Issue templates for content requests
- PR templates with checklists

### 5. **Content Lifecycle Management**
Articles flow through clear states:
```
DRAFT → IN_REVIEW → CHANGES_REQUESTED → APPROVED → ACTIVE
                                                      ↓
                                                  INACTIVE
```

---

## 👥 User Roles

### Content Creator (You!)
**What you do:**
- Create new health articles using `create_item.py`
- Edit articles using `edit_item.py`
- Respond to reviewer feedback

**Skills needed:**
- Basic Terminal usage
- Understanding of health topics
- Ability to write clear, plain language

**Tools you'll use:**
- `create_item.py` - Main creation tool
- `edit_item.py` - Main editing tool
- `validate.py` - Quality checker
- `README.md` - Your guide

---

### Medical Reviewer
**What you do:**
- Review articles for medical accuracy
- Check that guidelines are followed
- Ensure no unsafe claims or advice

**Review categories:**
- Clinical accuracy
- Guideline compliance
- Appropriate disclaimers
- Safety concerns

---

### Product Reviewer
**What you do:**
- Check if content fits the product
- Review user experience
- Ensure consistency with brand

**Review categories:**
- Product fit
- User experience
- Brand consistency
- Feature integration

---

### Content Editor
**What you do:**
- Polish language and tone
- Optimize keywords for SEO
- Ensure localization quality

**Review categories:**
- Language quality
- Tone consistency
- Keyword optimization
- Bilingual accuracy

---

## 📊 Data Model

### Suggestion Group
A collection of related articles:
```json
{
  "status": "ACTIVE",
  "name": "Heart Health",
  "key": "heart_health",
  "suggestionItem": [...]
}
```

### Suggestion Item
A single article:
```json
{
  "id": "uuid-v4",
  "revision": 1,
  "createdDate": "2025-11-07T10:00:00.000Z",
  "updatedDate": "2025-11-07T10:00:00.000Z",
  "createdBy": "creator-name",
  "updatedBy": "creator-name",
  "status": "DRAFT",
  "statusReason": "CREATED",
  "index": 0,
  "keywords": "heart;kalp;health;sağlık",
  "label": "cardiology",
  "header": "Understanding Heart Health ❤️",
  "contentShort": "Learn about heart health basics.",
  "contentLong": "<p>...</p>",
  "imagePath": "https://...",
  "readingFeatureEnabled": false,
  "parameter": [],
  "readCount": 0,
  "likedCount": 0,
  "bookmarkedCount": 0
}
```

---

## 🔒 Content Rules

### Headers
- Length: 48-80 characters
- One emoji allowed (optional)
- Clear and helpful (no clickbait)
- Sentence case

### Content Short
- Max 120 characters
- No HTML
- Teaser/preview text

### Content Long
- 160-300 words
- HTML with specific tags only
- No links, scripts, or external content

### Keywords
- 6-14 keywords
- Semicolon-separated
- Mix Turkish and English
- No trailing semicolon

### Images
- HTTPS URLs only
- License-cleared
- Neutral medical illustrations preferred

### Medical Content
- ✅ Educational and informational
- ✅ Guideline-consistent
- ✅ Includes disclaimers
- ❌ No diagnosis
- ❌ No drug dosing
- ❌ No treatment recommendations

---

## 🔄 Workflows

### Creating New Content
```
1. Run: python3 create_item.py
2. Answer guided questions
3. Run: python3 validate.py
4. Create Pull Request
5. Wait for reviews
6. Address feedback if needed
7. Get approval
8. Merge to production
```

### Editing Existing Content
```
1. Run: python3 edit_item.py
2. Select item to edit
3. Make changes
4. Run: python3 validate.py
5. Update Pull Request
6. Reviews and approval
7. Merge to production
```

### Review Process
```
1. Reviewer opens PR
2. Reads content
3. Adds comments to review file
4. Sets severity (high/medium/low)
5. Creator addresses comments
6. Updates content
7. Marks comments as resolved
8. Reviewer approves
9. Content moves to ACTIVE status
```

---

## 🛠️ Technical Details

### Requirements
- Python 3.6 or higher
- Git (for version control)
- GitHub account (for collaboration)
- Text editor (any)

### Dependencies
None for the Python scripts! They use only standard library modules:
- `json` - For JSON handling
- `uuid` - For generating unique IDs
- `datetime` - For timestamps
- `sys` - For system operations
- `re` - For pattern matching

### GitHub Actions
The automated validation workflow uses:
- `ajv-cli` - JSON Schema validator
- Python 3 - For custom checks

---

## 📈 Metrics & Analytics

Each article tracks:
- **readCount** - How many times it was read
- **likedCount** - How many users liked it
- **bookmarkedCount** - How many users saved it

These start at 0 and are updated by your application.

---

## 🔐 Security Considerations

### What's Protected
- ✅ HTML tags are restricted (no XSS)
- ✅ No external links allowed
- ✅ No script tags
- ✅ HTTPS-only images
- ✅ Schema validation on every change

### What to Watch
- ⚠️ Review file permissions
- ⚠️ GitHub access controls
- ⚠️ Image hosting security
- ⚠️ Medical content accuracy

---

## 🎓 Learning Resources

### For Content Creators
1. Start with `QUICK_START.md`
2. Read `README.md` sections 1-5
3. Practice with `create_item.py`
4. Review existing items in `data/suggestion-EN.json`

### For Reviewers
1. Read `agent/agent.md` sections 6-7 (Content Rules & Guardrails)
2. Understand the review file format (section 2.2)
3. Learn the comment resolution loop (section 16)

### For Developers
1. Study `schemas/suggestion.schema.json`
2. Review the Python scripts
3. Understand the GitHub workflows
4. Read `agent/agent.md` completely

---

## 🐛 Common Issues & Solutions

### Issue: "File not found"
**Cause**: Running script from wrong directory
**Fix**: `cd /path/to/content-generation-env`

### Issue: "Invalid JSON"
**Cause**: Syntax error in JSON file
**Fix**: Use JSON validator or restore from backup

### Issue: Validation errors
**Cause**: Content doesn't meet requirements
**Fix**: Read error messages, use `edit_item.py` to fix

### Issue: Can't run scripts
**Cause**: Permissions
**Fix**: `chmod +x *.py`

### Issue: Merge conflicts
**Cause**: Multiple people editing same item
**Fix**: Coordinate with team, resolve in GitHub

---

## 🔮 Future Enhancements

Potential improvements you could add:

### Content Features
- [ ] Image upload functionality
- [ ] Rich text editor
- [ ] Preview functionality
- [ ] Version comparison
- [ ] Content templates library

### Workflow Features
- [ ] Automated assignment of reviewers
- [ ] Review deadline tracking
- [ ] Content calendar
- [ ] Publication scheduling
- [ ] Analytics dashboard

### Technical Features
- [ ] Web interface (no Terminal needed)
- [ ] API endpoints
- [ ] Automated backups
- [ ] Content migration tools
- [ ] Multi-language support expansion

---

## 📞 Support

### Getting Help
1. **Documentation**: Read `README.md` and `QUICK_START.md`
2. **Validation**: Run `python3 validate.py` for specific errors
3. **Examples**: Check existing items in `data/suggestion-EN.json`
4. **Team**: Ask your reviewers or project lead

### Reporting Issues
Use GitHub issues with the templates:
- Bug reports
- Feature requests
- Content requests
- Edit requests

---

## 🎉 Success Criteria

You'll know the system is working when:

✅ **Content creators** can create articles without coding
✅ **Validation** catches all errors before review
✅ **Reviewers** can easily provide feedback
✅ **Process** flows smoothly from draft to published
✅ **Quality** is consistent across all content
✅ **Collaboration** happens efficiently via GitHub

---

## 📝 Changelog

### Version 1.0.0 (2025-11-07)
- ✅ Initial release
- ✅ Complete folder structure
- ✅ Python helper scripts
- ✅ JSON schema validation
- ✅ GitHub integration
- ✅ Comprehensive documentation
- ✅ Example templates
- ✅ Multi-role review system

---

## 🙏 Credits

**Built for**: Content creators who want to focus on writing, not coding

**Design philosophy**: Simple, safe, and scalable

**Core principles**:
- User-friendly for non-coders
- Comprehensive validation
- Clear workflows
- Medical content safety
- Collaborative reviews

---

## 📖 Additional Reading

- `README.md` - Complete user guide
- `QUICK_START.md` - Get started in 5 minutes
- `agent/agent.md` - Full system specification
- `agent/prompts/` - Detailed content guidelines
- `.github/pull_request_template.md` - PR checklist
- `schemas/suggestion.schema.json` - Technical schema

---

**You're all set! Start creating amazing health education content! 🚀**

**Questions?** Check the README or ask your team lead.
