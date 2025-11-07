# Agent Instructions for Content Creation

**Copy and paste these instructions to an AI agent to generate health content**

---

## 📋 CONTEXT

You are creating health education content for a Turkish healthcare application. The content will help people understand cardiovascular health, cholesterol, and heart disease prevention.

**Your Role**: Health content writer following strict medical content guidelines
**Audience**: General public in Turkey (Turkish language, plain terms)
**Format**: JSON output following exact schema requirements

---

## 🎯 TASK: Create Item #1 - Ateroskleroz Nedir?

### Content Requirements:

**Topic**: Ateroskleroz (damar sertliği/tıkanıklığı) nedir?
**Group**: `heart_health`
**Label**: `cardiology`
**Language**: Turkish (with bilingual keywords)

### Output Specifications:

#### 1. Header (48-80 characters, including emoji):
- Must be 48-80 characters
- Include exactly ONE emoji (optional but recommended)
- Clear benefit or question format
- Sentence case (not all caps)
- Example style: "Ateroskleroz Nedir? Damar Sağlığınızı Koruyun 🛡️"

#### 2. Content Short (max 120 characters):
- Maximum 120 characters
- No HTML tags
- No line breaks
- Imperative or value statement
- Teaser that makes people want to read more

#### 3. Content Long (160-300 words, HTML format):
**CRITICAL**: Only use these HTML tags:
- `<p>` - paragraphs
- `<ul>`, `<ol>` - lists
- `<li>` - list items
- `<b>` - bold
- `<i>` - italic
- `<br>` - line breaks
- `<blockquote>` - quotes

**FORBIDDEN**: NO `<a>`, `<script>`, `<style>`, `<iframe>`, `<object>`, or ANY other tags

**Structure to follow**:
```html
<p><b>Ateroskleroz Nedir?</b></p>
<p>[1-2 sentence introduction explaining what atherosclerosis is in plain Turkish]</p>
<p><b>Neden önemli:</b> [Brief explanation of why it matters - risk of heart attack/stroke]</p>
<ul>
  <li><b>Nasıl oluşur:</b> [How plaque builds up in arteries]</li>
  <li><b>Risk faktörleri:</b> [Main risk factors - cholesterol, blood pressure, smoking]</li>
  <li><b>Önleme:</b> [Prevention - lifestyle changes, medical management]</li>
</ul>
<p><i>Bu bilgi eğitim amaçlıdır ve profesyonel tıbbi danışmanlığın yerini tutmaz.</i></p>
```

#### 4. Keywords (6-14 keywords, semicolon-separated):
- Mix Turkish and English terms
- 6-14 keywords required
- Semicolon-separated (`;`)
- NO trailing semicolon
- Example: `ateroskleroz;atherosclerosis;damar tıkanıklığı;plak;plaque;kolesterol;cholesterol;kalp krizi;heart attack;inme;stroke;damar sağlığı;vascular health`

#### 5. Image Path:
- Must be HTTPS URL
- Use placeholder: `https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800`
- (This is a medical/health related stock image)

### Medical Content Guidelines:

**DO**:
- ✅ Use plain Turkish language
- ✅ Explain medical terms simply
- ✅ Focus on education and awareness
- ✅ Include disclaimer at end
- ✅ Encourage consulting healthcare provider
- ✅ Use guideline-consistent information

**DO NOT**:
- ❌ Make diagnostic claims
- ❌ Provide specific drug names or dosages
- ❌ Give specific medical advice
- ❌ Use alarming or fear-based language
- ❌ Include specific statistics unless provided
- ❌ Replace professional medical consultation

### Key Points to Cover:

1. **Definition**: What is atherosclerosis (ateroskleroz)?
2. **Mechanism**: How plaque forms in arteries (damar duvarında plak oluşumu)
3. **Consequences**: Can lead to heart attack (kalp krizi) or stroke (inme)
4. **Risk Factors**: High cholesterol, high blood pressure, smoking, diabetes
5. **Prevention**: Lifestyle changes, managing risk factors
6. **Action**: Consult healthcare provider for assessment

### Tone:
- Informative and educational
- Clear and accessible
- Encouraging but not prescriptive
- Non-alarmist
- Supportive

---

## 📤 OUTPUT FORMAT

Provide ONLY a valid JSON object with these exact fields:

```json
{
  "id": "[Generate UUID v4]",
  "revision": 1,
  "createdDate": "[Current UTC timestamp: YYYY-MM-DDTHH:mm:ss.sssZ]",
  "updatedDate": "[Same as createdDate]",
  "createdBy": "ai-agent",
  "updatedBy": "ai-agent",
  "status": "DRAFT",
  "statusReason": "CREATED",
  "index": 999,
  "keywords": "[Your keywords here - 6-14, semicolon-separated, NO trailing semicolon]",
  "label": "cardiology",
  "header": "[Your header here - 48-80 chars with emoji]",
  "contentShort": "[Your content short here - max 120 chars, no HTML]",
  "contentLong": "[Your HTML content here - 160-300 words, allowed tags only]",
  "imagePath": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800",
  "readingFeatureEnabled": false,
  "parameter": [],
  "readCount": 0,
  "likedCount": 0,
  "bookmarkedCount": 0
}
```

---

## ✅ VALIDATION CHECKLIST

Before providing output, verify:
- [ ] Header is 48-80 characters
- [ ] Content short is ≤ 120 characters
- [ ] Content long is 160-300 words
- [ ] Only allowed HTML tags used
- [ ] All HTML tags properly closed
- [ ] Keywords: 6-14 items, semicolon-separated, NO trailing semicolon
- [ ] Keywords mix Turkish and English
- [ ] Medical disclaimer included
- [ ] No diagnosis or treatment advice
- [ ] Plain language used
- [ ] Timestamp is in correct format (YYYY-MM-DDTHH:mm:ss.sssZ)
- [ ] UUID is valid v4 format

---

## 🚀 BEGIN CONTENT CREATION

Now generate the JSON content for:
**Topic**: Ateroskleroz (damar sertliği/tıkanıklığı) nedir?

Focus on:
- Clear explanation of what atherosclerosis is
- How plaque builds up in blood vessel walls
- Why it matters (heart attack and stroke risk)
- Main risk factors
- Basic prevention message
- Encouragement to consult healthcare provider

Remember: Plain Turkish, educational tone, include medical disclaimer, use only allowed HTML tags.

**OUTPUT ONLY THE JSON - NO OTHER TEXT**
