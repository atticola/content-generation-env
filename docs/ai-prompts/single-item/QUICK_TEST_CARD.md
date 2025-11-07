# 🚀 Quick Test Card

**Test AI content generation in 3 minutes**

---

## ⚡ Speed Test Instructions

### 1️⃣ **Copy This Text** (30 seconds)

Open: [COPY_PASTE_PROMPT.txt](COPY_PASTE_PROMPT.txt)

Or copy this shortened version:

```
Create health content in Turkish about atherosclerosis (ateroskleroz).

Output valid JSON with these fields:
- id: UUID v4
- revision: 1
- createdDate/updatedDate: 2025-11-07T10:30:00.000Z format
- createdBy/updatedBy: "ai-agent"
- status: "DRAFT"
- statusReason: "CREATED"
- index: 999
- label: "cardiology"
- header: 48-80 chars with emoji (e.g., "Ateroskleroz Nedir? 🛡️")
- contentShort: max 120 chars, no HTML
- contentLong: 160-300 words HTML (<p>, <ul>, <li>, <b>, <i> only)
- keywords: 6-14, semicolon-separated, NO trailing semicolon
  Example: "ateroskleroz;atherosclerosis;damar tıkanıklığı;plak;kolesterol;kalp krizi;heart attack"
- imagePath: "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800"
- readingFeatureEnabled: false
- parameter: []
- readCount/likedCount/bookmarkedCount: 0

Content should explain:
- What atherosclerosis is
- How plaque builds up
- Why it matters (heart attack/stroke)
- Prevention basics
- Include disclaimer: "Bu bilgi eğitim amaçlıdır ve profesyonel tıbbi danışmanlığın yerini tutmaz."

Plain Turkish. Educational tone. No diagnosis or drug advice.

OUTPUT ONLY JSON.
```

### 2️⃣ **Paste to AI** (1 minute)

- Claude: https://claude.ai
- ChatGPT: https://chat.openai.com
- Any AI with Turkish support

### 3️⃣ **Get & Test JSON** (1 minute)

Copy the JSON response, then:

```bash
# Quick validation
python3 -m json.tool < response.json

# Full validation
# (Add JSON to drafts/suggestion-EN.next.json first)
python3 validate.py
```

---

## ✅ Expected Output Example

```json
{
  "id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "revision": 1,
  "createdDate": "2025-11-07T10:30:00.000Z",
  "updatedDate": "2025-11-07T10:30:00.000Z",
  "createdBy": "ai-agent",
  "updatedBy": "ai-agent",
  "status": "DRAFT",
  "statusReason": "CREATED",
  "index": 999,
  "keywords": "ateroskleroz;atherosclerosis;damar tıkanıklığı;plak;plaque;kolesterol;cholesterol;kalp krizi;heart attack;inme;stroke",
  "label": "cardiology",
  "header": "Ateroskleroz Nedir? Damar Sağlığınızı Koruyun 🛡️",
  "contentShort": "Damar tıkanıklığına neden olan ateroskleroz hakkında bilmeniz gerekenleri öğrenin.",
  "contentLong": "<p><b>Ateroskleroz Nedir?</b></p><p>Ateroskleroz, damar duvarlarında plak adı verilen yağlı birikintilerin oluşmasıyla karakterize bir durumdur. Bu plaklar zamanla damarları daraltabilir ve kan akışını kısıtlayabilir.</p><p><b>Neden önemli:</b> Ateroskleroz kalp krizi ve inme gibi ciddi sağlık sorunlarına yol açabilir.</p><ul><li><b>Nasıl oluşur:</b> Yüksek kolesterol, kan damarlarının iç yüzeyinde birikerek plak oluşturur.</li><li><b>Risk faktörleri:</b> Yüksek kolesterol, yüksek tansiyon, sigara, diyabet ve hareketsiz yaşam.</li><li><b>Önleme:</b> Sağlıklı beslenme, düzenli egzersiz, sigarayı bırakma ve düzenli sağlık kontrolleri.</li></ul><p><i>Bu bilgi eğitim amaçlıdır ve profesyonel tıbbi danışmanlığın yerini tutmaz.</i></p>",
  "imagePath": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800",
  "readingFeatureEnabled": false,
  "parameter": [],
  "readCount": 0,
  "likedCount": 0,
  "bookmarkedCount": 0
}
```

---

## 🔍 Quick Checks

**Before accepting output:**

- [ ] Header between 48-80 chars? Count: `echo "header" | wc -c`
- [ ] Content short ≤ 120 chars?
- [ ] Keywords have NO trailing semicolon?
- [ ] Only allowed HTML tags used?
- [ ] Medical disclaimer included?
- [ ] Valid JSON format?

---

## 💾 Save Good Output

If validation passes:

```bash
# Option 1: Use creation script
python3 create_item.py
# (Copy-paste values from JSON)

# Option 2: Manual add
# Open drafts/suggestion-EN.next.json
# Find "heart_health" group
# Add JSON to suggestionItem array
# Save and validate
```

---

## 🔄 If Output Needs Fixing

Common fixes:

**Header too long?**
```
"Ateroskleroz: Damar Sağlığı ve Korunma Yolları 🛡️"  (too long)
→ "Ateroskleroz Nedir? Damar Sağlığınızı Koruyun 🛡️"  (good)
```

**Trailing semicolon?**
```
"keyword1;keyword2;keyword3;"  (bad)
→ "keyword1;keyword2;keyword3"  (good)
```

**Forbidden HTML?**
```
<a href="...">link</a>  (forbidden)
→ Just remove links entirely
```

---

## 📞 Need More Details?

- **Full instructions**: [AGENT_INSTRUCTIONS.md](AGENT_INSTRUCTIONS.md)
- **Testing guide**: [TEST_AI_OUTPUT.md](TEST_AI_OUTPUT.md)
- **Content plan**: [CONTENT_PLAN.md](CONTENT_PLAN.md)

---

**Ready? Copy the prompt above and test! ⚡**
