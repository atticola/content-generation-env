# Quick Start Guide

**5-Minute Guide to Creating Your First Health Article**

---

## Step 1: Open Terminal

1. Find the **Terminal** app on your computer
2. Navigate to this project folder:
   ```bash
   cd /Users/selahattincolakoglu/NonWork/SeloCodes/content-generation-env
   ```

---

## Step 2: Run the Creation Script

Type this command and press Enter:

```bash
python3 create_item.py
```

---

## Step 3: Answer the Questions

The script will ask you simple questions. Here's an example:

### Question 1: Group
```
Which group should this go in?
Options: latest_read, popular, heart_health
```
**Choose**: `heart_health` (or any group you want)

### Question 2: Category
```
What category is this?
Examples: cardiology, lipids, prevention, lifestyle
```
**Choose**: `cardiology` (or appropriate category)

### Question 3: Title
```
Write a compelling title (48-80 characters)
```
**Example**: `Understanding LDL Cholesterol 🛡️`

### Question 4: Teaser
```
Write a short teaser (max 120 characters)
```
**Example**: `Learn what LDL is and why it matters for your heart health.`

### Question 5: Main Content
```
Now for the main content (HTML format)
Type or paste your content (press Enter twice when done):
```
**Example**:
```html
<p><b>What is LDL Cholesterol?</b></p>
<p>LDL (Low-Density Lipoprotein) cholesterol is often called "bad" cholesterol. When LDL levels are too high, it can build up in your arteries.</p>
<ul>
  <li><b>Why it matters:</b> High LDL increases heart attack and stroke risk</li>
  <li><b>What you can do:</b> Healthy diet, exercise, and medication if needed</li>
  <li><b>Regular check-ups:</b> Get your cholesterol tested regularly</li>
</ul>
<p><i>This information is for educational purposes. Consult your doctor for personalized advice.</i></p>
```
*Press Enter twice when done*

### Question 6: Keywords
```
Enter keywords (6-14 words, separated by semicolons)
```
**Example**: `LDL;kolesterol;cholesterol;kalp;heart;cardiology;sağlık;health`

### Question 7: Image
```
Image URL (must start with https://)
```
**Example**: `https://example.com/images/heart-health.png`

---

## Step 4: Done!

You'll see a success message like this:

```
✅ SUCCESS!
================================================================

📄 Item created with ID: 1b3f1b6a-8c1b-4a2a-8c39-6a7d2f6a9f11
📁 Added to group: heart_health
📝 Status: DRAFT

📂 Files created:
   - drafts/suggestion-EN.next.json (updated)
   - reviews/1b3f1b6a-8c1b-4a2a-8c39-6a7d2f6a9f11.review.json (review stub)

🎯 NEXT STEPS:
   1. Review your content in drafts/suggestion-EN.next.json
   2. Create a Pull Request when ready for review
   3. Tag appropriate reviewers (medical, product, content)
```

---

## Step 5: Validate Your Work

Before submitting, check that everything is correct:

```bash
python3 validate.py
```

If you see `✅ Validation passed!`, you're good to go!

If you see errors, use the edit script to fix them:

```bash
python3 edit_item.py
```

---

## Common Issues

### "Command not found"
**Solution**: Make sure you're in the right folder. Run:
```bash
pwd
```
You should see: `/Users/selahattincolakoglu/NonWork/SeloCodes/content-generation-env`

### "Header too short" or "Header too long"
**Solution**: Your title must be 48-80 characters. Count them and adjust.

### "Forbidden HTML tag"
**Solution**: Only use these tags: `<p>`, `<ul>`, `<ol>`, `<li>`, `<b>`, `<i>`, `<br>`, `<blockquote>`

---

## Tips for Success

### Writing Good Headers
✅ **Good**: "Understanding LDL Cholesterol and Heart Health 🛡️" (55 chars)
❌ **Too Short**: "LDL Info" (8 chars)
❌ **Too Long**: "Everything You Ever Wanted to Know About LDL Cholesterol and Why It Matters" (78 chars)

### Writing Good Keywords
✅ **Good**: `LDL;kolesterol;cholesterol;kalp;heart;cardiology;sağlık;health` (8 keywords)
❌ **Bad**: `health;wellness` (only 2 keywords)
❌ **Bad**: `ldl;kolesterol;cholesterol;kalp;heart;` (trailing semicolon!)

### Using HTML Tags
✅ **Good**:
```html
<p>This is a paragraph.</p>
<ul>
  <li>Point 1</li>
  <li>Point 2</li>
</ul>
```

❌ **Bad**:
```html
<p>This is a paragraph.    ← Missing closing tag!
<a href="link">Click here</a>    ← Links not allowed!
```

---

## Next Steps

Once you've created your first item:

1. **Review it** - Open `drafts/suggestion-EN.next.json` and check your work
2. **Edit if needed** - Run `python3 edit_item.py` to make changes
3. **Validate** - Run `python3 validate.py` to ensure it's correct
4. **Submit for review** - Create a Pull Request on GitHub

---

## Need More Help?

- 📖 **Full documentation**: Read `README.md`
- 📋 **Content rules**: Check `agent/agent.md`
- 🛠️ **Edit existing items**: Run `python3 edit_item.py`
- ✅ **Validate content**: Run `python3 validate.py`

---

**You're ready to create amazing health education content! 🎉**
