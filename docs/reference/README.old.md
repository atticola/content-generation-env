# Suggestion Content Management System

A simple system for creating and managing health education content with built-in review workflows.

---

## 📚 What is This?

This is a content management system (CMS) designed for creating health education articles (called "suggestion items"). Think of it as a mini publishing platform where:

- **Content creators** write health articles
- **Reviewers** check the articles for accuracy
- **Editors** polish the language and keywords
- Everything is tracked and validated automatically

---

## 🏗️ How It's Organized

```
content-generation-env/
├── data/                          # Published content (live)
│   └── suggestion-EN.json
├── drafts/                        # Work in progress
│   └── suggestion-EN.next.json
├── reviews/                       # Review feedback for each item
│   └── {item-id}.review.json
├── schemas/                       # Rules for valid content
│   └── suggestion.schema.json
├── agent/                         # Instructions for AI agents
│   ├── agent.md
│   └── prompts/
├── .github/                       # GitHub automation
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── create_item.py                 # Easy script to create content
├── edit_item.py                   # Easy script to edit content
├── validate.py                    # Check if content is valid
└── README.md                      # This file!
```

---

## 🚀 Quick Start (For Non-Coders)

### Prerequisites

You just need Python installed on your computer. Most computers already have it!

To check, open Terminal and type:
```bash
python3 --version
```

If you see a version number like `Python 3.x.x`, you're good to go!

---

### Creating Your First Article

1. **Open Terminal** in this folder
2. **Run the creation script**:
   ```bash
   python3 create_item.py
   ```
3. **Answer the questions** - the script will guide you through everything
4. **Done!** Your article is now in `drafts/suggestion-EN.next.json`

**Example walkthrough:**
```
Welcome to Suggestion Item Creator!

1. Which group should this go in?
   Options: latest_read, popular, heart_health
   (default: latest_read): heart_health

2. What category is this?
   Examples: cardiology, lipids, prevention, lifestyle
   (default: cardiology): cardiology

3. Write a compelling title (48-80 characters)
   You can include ONE emoji if you like
   (default: Understanding Your Heart Health ❤️): Know Your LDL Cholesterol 🛡️

4. Write a short teaser (max 120 characters)
   This appears in preview cards
   (default: Learn about heart health and how to protect it.): Learn what LDL is and why it matters for your heart.

5. Now for the main content (HTML format)
   [Type your content here...]
```

---

### Editing an Existing Article

1. **Open Terminal** in this folder
2. **Run the edit script**:
   ```bash
   python3 edit_item.py
   ```
3. **Find your article** - you'll see a list of all articles with their IDs
4. **Choose what to edit** - header, content, keywords, etc.
5. **Done!** Your changes are saved

---

### Checking If Everything is Valid

Before submitting your work, run the validation script:

```bash
python3 validate.py
```

This checks:
- ✅ All required fields are present
- ✅ Dates are in correct format
- ✅ No forbidden HTML tags
- ✅ Keywords are properly formatted
- ✅ Headers are the right length

**If you see errors**, go back and fix them using `edit_item.py`

---

## 📋 Content Rules (Keep These in Mind)

### Headers (Titles)
- **Length**: 48-80 characters
- **Style**: Clear and helpful, not clickbait
- **Emoji**: You can use ONE if it fits (optional)
- **Example**: "Understanding LDL Cholesterol 🛡️"

### Content Short (Teaser)
- **Length**: Maximum 120 characters
- **No HTML**: Plain text only
- **Purpose**: Appears in preview cards
- **Example**: "Learn what LDL cholesterol is and why managing it matters for heart health."

### Content Long (Main Article)
- **Length**: 160-300 words
- **Format**: HTML with these tags only:
  - `<p>` - Paragraphs
  - `<ul>` and `<ol>` - Lists
  - `<li>` - List items
  - `<b>` - Bold text
  - `<i>` - Italic text
  - `<br>` - Line break
  - `<blockquote>` - Quotes

**❌ Never use**: `<script>`, `<style>`, `<iframe>`, `<object>`, `<a>` (links)

### Keywords
- **Count**: 6-14 keywords
- **Format**: Separated by semicolons (`;`)
- **Language**: Mix Turkish and English for better search
- **No trailing semicolon!**
- **Example**: `LDL;kolesterol;cholesterol;kalp;heart;cardiology;kardiyoloji;sağlık;health`

### Images
- **Must be HTTPS URLs** (starting with `https://`)
- Use license-cleared images only
- Prefer neutral medical illustrations

---

## 🏥 Medical Content Guidelines

When writing about medical topics:

✅ **DO:**
- Use plain language (avoid jargon)
- Include disclaimers (e.g., "This is not medical advice")
- Focus on education and awareness
- Use guideline-consistent phrasing

❌ **DON'T:**
- Make diagnostic claims
- Provide specific drug dosages
- Replace professional medical advice
- Use scary or alarmist language

---

## 🔄 The Content Lifecycle

Every article goes through these stages:

1. **DRAFT** - You're creating it
2. **IN_REVIEW** - Sent to reviewers
3. **CHANGES_REQUESTED** - Reviewers want changes
4. **APPROVED** - Reviewers approved it
5. **ACTIVE** - Published and live
6. **INACTIVE** - Archived

You'll mostly work with **DRAFT** status. Reviewers handle the rest.

---

## 👥 Review Process

### Who Reviews What?

- **Medical Reviewers** - Check medical accuracy
- **Product Reviewers** - Check if it fits the product
- **Content Editors** - Check language, tone, and keywords

### How Reviews Work

1. You create/edit content using the scripts
2. Reviews go into `reviews/{item-id}.review.json`
3. Reviewers add comments with severity levels:
   - **high** - Must fix before publishing
   - **medium** - Should fix
   - **low** - Nice to fix
4. You address comments and update the item
5. Once all "high" severity issues are resolved, it can be approved

---

## 📁 File Structure Explained

### `data/suggestion-EN.json`
**What it is**: The published, live content that users see

**When to touch it**: Only when merging approved changes from drafts

### `drafts/suggestion-EN.next.json`
**What it is**: Your working copy where you create and edit

**When to touch it**: This is where you do all your work!

### `reviews/{item-id}.review.json`
**What it is**: Feedback from reviewers for a specific item

**Structure**:
```json
{
  "medical": [
    {
      "id": "rv-1",
      "author": "Dr. Smith",
      "comment": "Please clarify the risk factors section",
      "severity": "high",
      "field": "contentLong",
      "proposed": "Add age and family history",
      "disposition": "open"
    }
  ],
  "product": [],
  "context": []
}
```

### `schemas/suggestion.schema.json`
**What it is**: The technical rules that define valid content

**When to touch it**: Rarely - only when changing the system structure

---

## 🛠️ Helper Scripts

### `create_item.py`
**Purpose**: Create a new article from scratch

**How to use**:
```bash
python3 create_item.py
```

**What it does**:
- Guides you through all required fields
- Generates a unique ID automatically
- Creates a review stub
- Saves everything in the right place

---

### `edit_item.py`
**Purpose**: Edit an existing article

**How to use**:
```bash
python3 edit_item.py
```

**What it does**:
- Shows all existing articles
- Lets you pick which one to edit
- Provides a menu of what you can change
- Updates revision numbers automatically

---

### `validate.py`
**Purpose**: Check if your content follows all the rules

**How to use**:
```bash
python3 validate.py                              # Check both files
python3 validate.py drafts/suggestion-EN.next.json   # Check specific file
```

**What it checks**:
- Required fields present
- Correct data types
- Valid dates and UUIDs
- Header and content lengths
- Keywords format
- No forbidden HTML tags

---

## 🎯 Common Workflows

### Workflow 1: Create New Content

```bash
# Step 1: Create the item
python3 create_item.py

# Step 2: Validate it
python3 validate.py

# Step 3: If validation passes, create a Pull Request on GitHub
# (Ask your team lead about GitHub access)
```

---

### Workflow 2: Edit Existing Content

```bash
# Step 1: Edit the item
python3 edit_item.py

# Step 2: Validate your changes
python3 validate.py

# Step 3: Update your Pull Request or create a new one
```

---

### Workflow 3: Address Review Comments

1. Check your review file: `reviews/{your-item-id}.review.json`
2. Look for comments with `"disposition": "open"`
3. Edit your item to address the comments:
   ```bash
   python3 edit_item.py
   ```
4. Validate:
   ```bash
   python3 validate.py
   ```
5. Update the review file to mark comments as `"accepted"` or `"rejected"`

---

## 🐛 Troubleshooting

### "File not found" error
**Problem**: Script can't find the necessary files

**Solution**: Make sure you're running the script from the project folder:
```bash
cd /path/to/content-generation-env
python3 create_item.py
```

---

### "Invalid JSON" error
**Problem**: The JSON file has syntax errors

**Solution**: Use a JSON validator to find the error, or restore from backup

---

### "Validation failed" errors
**Problem**: Your content doesn't follow the rules

**Solution**: Read the error messages carefully. They tell you exactly what's wrong:
- "Header too long" → Shorten your header
- "Invalid status" → Use one of: DRAFT, IN_REVIEW, etc.
- "Keywords: Too few" → Add more keywords

---

### Can't run Python scripts
**Problem**: Permission denied

**Solution**: Make the scripts executable:
```bash
chmod +x create_item.py edit_item.py validate.py
```

---

## 📖 Content Templates

### Generic Health Topic Template

```html
<p><b>Main Topic Here</b></p>
<p>Brief introduction in 1-2 sentences explaining what this is about.</p>
<ul>
  <li><b>Key point 1:</b> Explanation of the first important point</li>
  <li><b>Key point 2:</b> Explanation of the second important point</li>
  <li><b>Key point 3:</b> Explanation of the third important point</li>
</ul>
<p><i>This content is for educational purposes and not a substitute for professional medical care.</i></p>
```

---

### Medical Explainer Template

```html
<p><b>Condition Name</b></p>
<p>Clear definition in plain language. One or two sentences.</p>
<p><b>Why it matters:</b> Brief explanation of the risk or impact.</p>
<ol>
  <li><b>Signs & Symptoms:</b> What to look out for</li>
  <li><b>Prevention:</b> How to reduce risk</li>
  <li><b>When to seek help:</b> When to see a doctor</li>
</ol>
<p><i>This content is informational only. Always consult your healthcare provider.</i></p>
```

---

## 📞 Getting Help

### For Content Questions
- Check the topic library in `agent/agent.md` (Section 8)
- Review existing items in `data/suggestion-EN.json`
- Ask your medical/content reviewers

### For Technical Issues
- Run `python3 validate.py` to see what's wrong
- Check this README's Troubleshooting section
- Contact your technical lead

### For Process Questions
- Review the workflow diagrams in `agent/agent.md`
- Check the GitHub Pull Request template
- Ask your project manager

---

## 🎓 Learn More

### Understanding the System
- Read `agent/agent.md` for the complete specification
- Check `agent/prompts/` for detailed content guidelines
- Review existing items to see examples

### Understanding JSON
JSON is just a way to organize data. Here's a tiny tutorial:

```json
{
  "name": "John",           ← Text in quotes
  "age": 30,                ← Numbers without quotes
  "active": true,           ← Boolean (true/false)
  "hobbies": ["reading", "coding"],  ← List (array)
  "address": {              ← Nested object
    "city": "Istanbul"
  }
}
```

**Important rules:**
- Use double quotes `"` not single quotes `'`
- No trailing commas after the last item
- Close all brackets and braces

---

## ✅ Pre-Submit Checklist

Before creating a Pull Request, check:

- [ ] Ran `python3 validate.py` with no errors
- [ ] Header is 48-80 characters
- [ ] Content short is under 120 characters
- [ ] Content long uses only allowed HTML tags
- [ ] Keywords: 6-14 items, semicolon-separated, no trailing semicolon
- [ ] Image URL starts with `https://`
- [ ] Medical content includes appropriate disclaimers
- [ ] No diagnosis, dosing, or treatment claims
- [ ] Plain language (avoid jargon)
- [ ] Review stub created in `reviews/` folder

---

## 🎉 You're Ready!

You now have everything you need to create and manage health education content. Remember:

1. **Use the scripts** - They do most of the work for you
2. **Validate often** - Catch errors early
3. **Follow the templates** - They ensure consistency
4. **Ask for help** - Your reviewers are there to support you

**Happy creating! 🚀**

---

## 📝 Quick Reference

| Task | Command |
|------|---------|
| Create new item | `python3 create_item.py` |
| Edit existing item | `python3 edit_item.py` |
| Validate content | `python3 validate.py` |
| List all items | `python3 edit_item.py` (shows list first) |
| Check file structure | `tree` or `ls -R` |

| Status | Meaning |
|--------|---------|
| DRAFT | Being created |
| IN_REVIEW | Waiting for reviewers |
| CHANGES_REQUESTED | Needs edits |
| APPROVED | Ready to publish |
| ACTIVE | Live/published |
| INACTIVE | Archived |

| Valid HTML Tags | Purpose |
|----------------|---------|
| `<p>` | Paragraph |
| `<ul>`, `<ol>` | Lists |
| `<li>` | List item |
| `<b>` | Bold |
| `<i>` | Italic |
| `<br>` | Line break |
| `<blockquote>` | Quote |

---

**Version**: 1.0.0
**Last Updated**: 2025-11-07
**Maintainer**: Platform Team
