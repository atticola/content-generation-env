# Test AI-Generated Content

**Instructions for testing AI agent's content generation**

---

## 🎯 How to Test

### Step 1: Copy the Prompt
Open one of these files:
- **Detailed version**: [AGENT_INSTRUCTIONS.md](AGENT_INSTRUCTIONS.md)
- **Quick version**: [COPY_PASTE_PROMPT.txt](COPY_PASTE_PROMPT.txt)

Copy the entire text.

### Step 2: Paste to AI Agent
Paste the prompt to:
- Claude (Anthropic)
- ChatGPT (OpenAI)
- Any other AI assistant with good Turkish language support

### Step 3: Get JSON Output
The AI should return a JSON object. Copy the entire JSON.

### Step 4: Save and Test
Paste the JSON below in the "AI Output" section, then test it.

---

## 📝 AI Output - Item #1 (Ateroskleroz)

**Paste the AI-generated JSON here:**

```json
[PASTE AI OUTPUT HERE]
```

---

## ✅ How to Validate the Output

### Option A: Manual Validation
1. **Save the JSON** to a file: `test-item-1.json`
2. **Manually add it** to `drafts/suggestion-EN.next.json`:
   ```bash
   # Open drafts/suggestion-EN.next.json
   # Find the "heart_health" group's "suggestionItem" array
   # Add the JSON object to the array
   ```
3. **Validate**:
   ```bash
   python3 validate.py
   ```

### Option B: Programmatic Test
Create a test script:

```python
import json

# 1. Load the AI output
ai_output = '''
[PASTE JSON HERE]
'''

# 2. Parse it
try:
    item = json.loads(ai_output)
    print("✅ Valid JSON!")
except json.JSONDecodeError as e:
    print(f"❌ Invalid JSON: {e}")
    exit(1)

# 3. Check required fields
required_fields = [
    'id', 'revision', 'createdDate', 'updatedDate',
    'createdBy', 'updatedBy', 'status', 'statusReason',
    'index', 'keywords', 'label', 'header',
    'contentShort', 'contentLong', 'imagePath',
    'readingFeatureEnabled', 'parameter',
    'readCount', 'likedCount', 'bookmarkedCount'
]

missing = [f for f in required_fields if f not in item]
if missing:
    print(f"❌ Missing fields: {missing}")
else:
    print("✅ All required fields present!")

# 4. Validate constraints
errors = []

# Header length
if not (48 <= len(item['header']) <= 80):
    errors.append(f"Header length: {len(item['header'])} (must be 48-80)")

# Content short length
if len(item['contentShort']) > 120:
    errors.append(f"Content short too long: {len(item['contentShort'])} (max 120)")

# Keywords count
keywords = item['keywords'].split(';')
if not (6 <= len(keywords) <= 14):
    errors.append(f"Keywords count: {len(keywords)} (must be 6-14)")

# Keywords trailing semicolon
if item['keywords'].endswith(';'):
    errors.append("Keywords have trailing semicolon")

# Check for forbidden HTML
forbidden = ['<a', '<script', '<style', '<iframe', '<object']
for tag in forbidden:
    if tag in item['contentLong'].lower():
        errors.append(f"Forbidden HTML tag found: {tag}")

if errors:
    print("\n❌ VALIDATION ERRORS:")
    for error in errors:
        print(f"   • {error}")
else:
    print("\n✅ ALL VALIDATIONS PASSED!")

# 5. Add to drafts file
print("\n📄 Ready to add to drafts/suggestion-EN.next.json")
```

---

## 📊 Quality Assessment Checklist

After getting AI output, check:

### Content Quality:
- [ ] Header is compelling and clear
- [ ] Content short creates interest
- [ ] Content long is well-structured
- [ ] Medical information is accurate
- [ ] Language is plain and accessible
- [ ] Disclaimer is included
- [ ] Tone is educational, not prescriptive

### Technical Quality:
- [ ] Valid JSON format
- [ ] All required fields present
- [ ] Header: 48-80 characters
- [ ] Content short: ≤ 120 characters
- [ ] Content long: 160-300 words
- [ ] Keywords: 6-14, semicolon-separated, no trailing ;
- [ ] Only allowed HTML tags used
- [ ] All HTML tags properly closed
- [ ] Image URL is HTTPS
- [ ] UUID is valid v4 format
- [ ] Dates are in ISO 8601 format

### Medical Safety:
- [ ] No diagnosis claims
- [ ] No specific drug recommendations
- [ ] No dosing information
- [ ] Includes appropriate disclaimer
- [ ] Encourages healthcare provider consultation
- [ ] Information is guideline-consistent

---

## 🔄 Iteration Process

If the AI output needs improvement:

### Common Issues & Fixes:

1. **Header too short/long**
   - Add instruction: "The header MUST be between 48-80 characters. Count carefully."

2. **Too many/few keywords**
   - Add instruction: "Include EXACTLY 6-14 keywords. No more, no less."

3. **Trailing semicolon in keywords**
   - Add instruction: "CRITICAL: Do NOT end keywords with semicolon. Last keyword should NOT have ; after it."

4. **Forbidden HTML tags**
   - Add instruction: "You can ONLY use these tags: <p>, <ul>, <ol>, <li>, <b>, <i>, <br>, <blockquote>. NO OTHER TAGS ALLOWED."

5. **Content too technical**
   - Add instruction: "Use simple Turkish. Explain all medical terms. Write for general public, not doctors."

6. **Missing disclaimer**
   - Add instruction: "MUST end with: <p><i>Bu bilgi eğitim amaçlıdır ve profesyonel tıbbi danışmanlığın yerini tutmaz.</i></p>"

---

## 📈 Compare Multiple AI Models

Test the same prompt with different AI models:

### Model Performance:

| Model | JSON Valid? | Meets Length? | HTML Clean? | Turkish Quality | Overall |
|-------|-------------|---------------|-------------|-----------------|---------|
| Claude 3.5 Sonnet | | | | | |
| GPT-4 | | | | | |
| Gemini Pro | | | | | |

---

## 💡 Tips for Better Results

### Prompt Improvements:

1. **Be very specific about lengths**:
   ```
   Header MUST be EXACTLY 48-80 characters. Count carefully before responding.
   ```

2. **Provide examples**:
   ```
   Example header (52 chars): "Ateroskleroz: Damar Sağlığınızı Nasıl Korursunuz? 🛡️"
   ```

3. **Emphasize constraints**:
   ```
   CRITICAL RULES (MUST FOLLOW):
   1. Header: 48-80 characters (count!)
   2. Keywords: NO trailing semicolon
   3. HTML: Only <p>, <ul>, <ol>, <li>, <b>, <i>, <br>, <blockquote>
   ```

4. **Request verification**:
   ```
   Before outputting, verify:
   - Counted header characters?
   - Removed trailing semicolon?
   - Used only allowed HTML tags?
   ```

---

## 🎯 Success Criteria

The AI output is ready for use when:

✅ Passes `python3 validate.py` with no errors
✅ Content is medically accurate
✅ Language is clear and accessible
✅ Tone is appropriate
✅ All technical requirements met
✅ You would be comfortable publishing it (after human review)

---

## 📝 Notes & Observations

**Test Date**: [Date]
**AI Model Used**: [Model name/version]
**Attempt Number**: [1, 2, 3...]

**What worked well**:
-
-

**What needed fixing**:
-
-

**Prompt modifications made**:
-
-

**Final result**:
- [ ] ✅ Ready to use
- [ ] ⚠️ Needs minor edits
- [ ] ❌ Needs major revision

---

## 🚀 Next Steps

Once you have validated AI output:

1. **Save the JSON** to a file
2. **Add to drafts** using the creation script or manually
3. **Validate** with `python3 validate.py`
4. **Review** for medical accuracy
5. **Create Pull Request** for team review
6. **Iterate** on remaining 17 topics

---

**Ready to test? Copy the prompt and paste it to your AI agent!** 🎯
