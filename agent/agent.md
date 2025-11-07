# Agent: Suggestion CMS (Creation & Editing Only)

## 0) Repository Layout (GitHub)
```
repo-root/
  data/
    suggestion-EN.json             # canonical dataset
  drafts/
    suggestion-EN.next.json        # agent working copy (unpublished)
  reviews/
    <itemId>.review.json           # structured reviewer feedback per item
  schemas/
    suggestion.schema.json         # JSON Schema
  agent/
    agent.md                       # this spec
    prompts/
      create_item.prompt.md
      edit_item.prompt.md
  .github/
    CODEOWNERS
    pull_request_template.md
    ISSUE_TEMPLATE/
      content_request.md
      edit_request.md
    workflows/
      validate.yml                 # CI: schema + lint + policy
```


## 1) Scope
The agent creates and edits **suggestion items** inside the JSON structure found in `suggestion-EN`. Publishing, analytics, and orchestration are out of scope.

## 2) Target JSON Model

### 2.0 States (Lifecycle)
Allowed `status` values for items: `DRAFT` → `IN_REVIEW` → `CHANGES_REQUESTED` → `APPROVED` → `ACTIVE` | `INACTIVE`.
- Agent emits `DRAFT` on creation unless explicitly told to publish.
- Moving to `IN_REVIEW` assigns reviewers.
- Only human reviewers can set `APPROVED`.
- Agent may set `ACTIVE` after `APPROVED`.


- Root: `{ "data": SuggestionGroup[] }`
- `SuggestionGroup`: `{ status, name, key, suggestionItem[] }`
- `suggestionItem[]`: ordered list of articles/cards.

### 2.1 Required fields for each suggestion item
- `id`: UUID v4. Immutable.
- `revision`: integer ≥ 1. Increment on each edit.
- `createdDate`, `updatedDate`: ISO 8601 with `Z` (UTC).
- `createdBy`, `updatedBy`: agent or human identifier.
- `status`: `DRAFT` | `IN_REVIEW` | `CHANGES_REQUESTED` | `APPROVED` | `ACTIVE` | `INACTIVE`.
- `statusReason`: short reason. E.g., `CREATED`, `SENT_FOR_REVIEW`, `REVIEW_CHANGES`, `APPROVED_FOR_PUBLISH`, `ARCHIVED`.
- `index`: non‑negative integer for ordering.
- `keywords`: semicolon‑separated; bilingual where relevant.
- `label`: one word category. Lowercase.
- `header`: short, compelling title. 48–80 chars.
- `contentShort`: teaser ≤ 120 chars.
- `contentLong`: HTML body (see 4.2).
- `imagePath`: HTTPS URL.
- `readingFeatureEnabled`: boolean.
- `parameter`: array (optional; default `[]`).
- `readCount`, `likedCount`, `bookmarkedCount`: integers ≥ 0 (default `0`).
- `review`: object (optional) for **embedded** comments (see 3.1) when storing feedback inline instead of `reviews/<id>.review.json`.

### 2.2 Review object (inline option)
```json
{
  "medical": [ {"id":"rv-1","author":"Dr X","comment":"...","severity":"high","field":"contentLong","proposed":"...","disposition":"open"} ],
  "product": [ {"id":"rv-2","author":"PM Y","comment":"...","severity":"medium","field":"header","proposed":"...","disposition":"open"} ],
  "context": [ {"id":"rv-3","author":"Editor Z","comment":"...","severity":"low","field":"keywords","proposed":"...","disposition":"open"} ]
}
```
Fields: `id` (string), `author` (string), `comment` (string), `severity` (`low|medium|high`), `field` (string path), `proposed` (string or object), `disposition` (`open|accepted|rejected`).

### 2.3 Suggestion group invariants
- `status` must be `ACTIVE` for publishing. Groups may contain items in any state during editing.

- `status` must be `ACTIVE` to accept new items.
- `key` is a stable identifier (e.g., `latest_read`).
- `name` is a display label (e.g., `The Newest`).

## 3) Creation Workflow
1. Input: topic, label, target group `key`.
2. Create item with `status=DRAFT` and defaults.
3. Validate and write to `drafts/suggestion-EN.next.json`.
4. Open a Pull Request (PR) that adds the item and requests review (Section 12).

## 4) Editing Workflow
1. Locate item by `id`.
2. Apply changes. Do not change `id` or `createdDate`.
3. Increment `revision`; update `updatedDate/By`.
4. If edits respond to review, set `status=IN_REVIEW` and reference resolved comment IDs.
5. Re‑validate. Commit to branch and update PR or open a new one.

1. Locate item by `id` (preferred) or exact `header` match.
2. Apply changes. **Do not** change `id` or `createdDate`.
3. Increment `revision` by 1. Update `updatedDate` and `updatedBy`.
4. Optionally update `status` and `statusReason`.
5. Keep `index` unless reordering is requested.
6. Re‑validate.

## 5) Content Rules

### 5.1 Header
- Clear benefit. Avoid clickbait. One emoji optional.
- Use sentence case. Avoid all caps.

### 5.2 contentShort
- ≤ 120 chars. Imperative or value statement.
- No HTML. No line breaks.

### 5.3 contentLong (HTML)
Allowed tags: `<p> <ul> <ol> <li> <b> <i> <br> <blockquote>`.
Forbidden: `<script> <style> <iframe> <object> <a>`.

**Template (generic):**
```html
<p><b>{Headline}</b></p>
<p>{Intro, 1–2 sentences.}</p>
<ul>
  <li>{Key point 1}</li>
  <li>{Key point 2}</li>
  <li>{Key point 3}</li>
</ul>
<p><i>{Call to action or next step.}</i></p>
```

**Template (medical explainer):**
```html
<p><b>{Condition/Topic}</b></p>
<p>{Definition in 1–2 sentences. Plain language.}</p>
<p><b>Why it matters:</b> {Risk/impact succinctly.}</p>
<ol>
  <li><b>Signs/Symptoms:</b> {bullet list}</li>
  <li><b>Prevention:</b> {bullet list}</li>
  <li><b>When to seek help:</b> {bullet list}</li>
</ol>
<p><i>This content is informational and not a substitute for professional care.</i></p>
```

### 5.4 Keywords
- Semicolon‑separated list. Mix TR and EN terms if audience is mixed.
- Include 6–14 tokens. Example: `LDL;trigliserid;kolesterol;ateroskleroz;cholesterol;LDL‑C;triglycerides;atherosclerosis`.

### 5.5 Label
- Single lowercase token from taxonomy. Examples: `cardiology`, `prevention`, `lifestyle`.

### 5.6 Image
- `imagePath` must be HTTPS and license‑cleared. Prefer neutral medical illustrations.

## 6) Guardrails for Medical Topics
- Use guideline‑consistent phrasing. Avoid therapeutic claims.
- Include disclaimers when suggesting behavior change.
- No diagnosis. No drug dosing. Do not replace clinician advice.
- For statistics, avoid specific figures unless provided in the brief.

## 7) Validation
- Schema: required fields present and types correct.
- Dates: RFC 3339 `YYYY‑MM‑DDThh:mm:ss.sssZ`.
- HTML: allowed tags only; no links; tags closed.
- Keywords: 6–14 tokens; `;` separated; no trailing `;`.
- Status and reason coherent with lifecycle.
- Metrics non‑negative integers.
- If `review` exists, each entry has required fields and `disposition`.

- **Schema**: all required fields present and types correct.
- **Dates**: RFC 3339 `YYYY‑MM‑DDThh:mm:ss.sssZ`.
- **HTML**: allowed tags only. Close all tags. No links.
- **Keywords**: at least 6 tokens; `;` separated; no trailing semicolon.
- **Status**: if `INACTIVE`, provide `statusReason`.
- **Metrics**: integers ≥ 0.

## 8) Topic Library (Input Briefs)
Use these topic labels and minimal briefs during creation. Expand plainly without statistics unless given.

1. **Ateroskleroz nedir?**
   Label: `cardiology`.
   Focus: definition, risk, prevention basics.

2. **Kan yağları nedir ve çeşitleri?**
   Label: `lipids`.
   Focus: LDL, HDL, TG, non‑HDL.

3. **LDL ve kalp hastalığı**
   Label: `lipids`.
   Focus: causal role, lowering risk.

4. **İyi vs kötü kolesterol**
   Label: `lipids`.
   Focus: HDL vs LDL roles.

5. **Türkiye'de KKH durumu**
   Label: `public‑health`.
   Focus: awareness and prevention behaviors.

6. **Kalp krizi nasıl oluşur?**
   Label: `cardiology`.
   Focus: plaque rupture, thrombosis.

7. **İnme nasıl oluşur?**
   Label: `neurology`.
   Focus: ischemic vs hemorrhagic basics.

8. **Kalp krizi önlenebilir mi?**
   Label: `prevention`.
   Focus: lifestyle, risk control.

9. **Genç yaşta kalp krizi nedenleri**
   Label: `cardiology`.
   Focus: FH, smoking, metabolic risk, substances.

10. **Belirti yokken kalp krizi**
    Label: `cardiology`.
    Focus: silent ischemia, screening advice disclaimer.

11. **Günlük hayatta kalp sağlığı**
    Label: `lifestyle`.
    Focus: movement, diet, sleep, stress.

12. **Herkesin riski aynı mı?**
    Label: `risk`.
    Focus: risk factors and calculators conceptually.

13. **LDL ve trigliserid farkı**
    Label: `lipids`.
    Focus: roles and targets differ.

14. **Diyabet ve damar sağlığı**
    Label: `diabetes`.
    Focus: diabetic dyslipidemia and risk.

15. **LDL hedefleri kişisel mi?**
    Label: `lipids`.
    Focus: individual targets by risk.

16. **Lipid düşürücü tedaviler**
    Label: `therapy`.
    Focus: classes overview without dosing.

17. **Ailesel hiperkolesterolemi**
    Label: `genetics`.
    Focus: inheritance, early screening.

18. **Yaşam tarzı ve tedaviye devam**
    Label: `adherence`.
    Focus: adherence, follow‑up.

## 9) Source Handling
Acceptable source list for drafting. Cite internally via PR body or review files. Do **not** embed links in `contentLong`.

## 10) Bilingual Support
- Turkish briefs produce Turkish copy; English briefs produce English copy.
- Keywords can be mixed TR/EN.

- If the brief is Turkish, keep headers in Turkish and expand content in Turkish.
- Populate `keywords` with mixed TR/EN tokens to support retrieval.
- Keep tone neutral, clear, non‑alarmist.

## 11) Ready‑to‑use Creation Prompt (for this agent)
```
You are the Suggestion CMS agent.
Goal: create ONE suggestion item for group {group_key}.
Topic: {topic}. Label: {label}. Audience: general public.
Lifecycle: set status=DRAFT and statusReason=CREATED.
Constraints:
- header 48–80 chars; one emoji optional.
- contentShort ≤120 chars; no HTML.
- contentLong HTML with allowed tags; 160–300 words.
- keywords 6–14 tokens; TR+EN; `;` separated.
- imagePath HTTPS URL.
- UUID v4; revision=1; timestamps now(UTC); createdBy/updatedBy {author}.
Output: JSON object with only the new item fields.
Also emit a `reviews/<id>.review.json` stub with empty arrays for medical, product, context.
```
You are the Suggestion CMS agent. Create ONE suggestion item for group {group_key}. Topic: {topic}. Label: {label}. Audience: general public.
Constraints:
- header 48–80 chars; one emoji optional.
- contentShort ≤ 120 chars; no HTML.
- contentLong HTML using only allowed tags. 160–300 words.
- keywords: 6–14 tokens; TR+EN; semicolon‑separated.
- imagePath: https URL.
- Set status ACTIVE; statusReason CREATED; metrics 0; parameter [].
- Generate UUID v4; revision=1; timestamps now(UTC); set createdBy/updatedBy to {author}.
Output: JSON object with only the new item fields (not the whole file).
```

## 12) Ready‑to‑use Editing Prompt
```
You are the Suggestion CMS agent. Edit the item with id {id}.
Requested changes: {diff_description}.
Rules:
- Do not change id or createdDate.
- Increment revision; set updatedDate now(UTC); updatedBy {author}.
- Keep index unless reordering is specified.
- For each addressed reviewer comment, set `disposition=accepted|rejected` and include a brief reason.
- If all blocking comments are resolved, set status=IN_REVIEW and statusReason=REVIEW_CHANGES.
Output: JSON object with changed fields plus id and revision. Separate list of resolved comment IDs.
```
```
You are the Suggestion CMS agent. Edit the suggestion item with id {id}.
Requested changes: {diff_description}.
Rules:
- Do not change id or createdDate.
- Increment revision by 1; set updatedDate now(UTC); updatedBy {author}.
- Keep index unless reordering is specified.
- Validate HTML and field constraints.
Output: JSON object with only the changed fields plus id and revision.
```

## 13) Example Outputs

### 13.1 Creation (DRAFT)
```json
{
  "id": "1b3f1b6a-8c1b-4a2a-8c39-6a7d2f6a9f11",
  "revision": 1,
  "createdDate": "2025-11-04T10:00:00.000Z",
  "updatedDate": "2025-11-04T10:00:00.000Z",
  "createdBy": "agent",
  "updatedBy": "agent",
  "status": "DRAFT",
  "statusReason": "CREATED",
  "index": 999,
  "keywords": "LDL;LDL-C;kolesterol;ateroskleroz;cholesterol;plaque;statins;trigliserid;kalp krizi;heart attack",
  "label": "lipids",
  "header": "LDL'i Azaltmak Kalp Riskinizi Azaltır 🛡️",
  "contentShort": "LDL'nin kalpteki rolünü ve nasıl düşürüleceğini öğrenin.",
  "contentLong": "<p><b>LDL ve kalp sağlığı</b></p><p>LDL kolesterol, damar duvarında birikip plak oluşturarak kalp krizi riskini artırabilir. Hedef, LDL'yi kişisel riskinize göre düşürmektir.</p><ul><li><b>Ne oluyor?</b> Plaklar zamanla daraltır, koparsa pıhtı oluşabilir.</li><li><b>Ne yapabilirsiniz?</b> Beslenme düzeni, hareket, sigarayı bırakma ve hekiminizin önereceği tedaviler.</li><li><b>Takip önemlidir:</b> Kan yağlarınıza baktırın ve planı sürdürün.</li></ul><p><i>Bu bilgi tıbbi danışmanın yerini tutmaz.</i></p>",
  "imagePath": "https://example.com/images/ldl_shield.png",
  "readingFeatureEnabled": false,
  "parameter": [],
  "readCount": 0,
  "likedCount": 0,
  "bookmarkedCount": 0
}
```

### 13.2 Separate review stub file
`reviews/1b3f1b6a-8c1b-4a2a-8c39-6a7d2f6a9f11.review.json`
```json
{
  "medical": [],
  "product": [],
  "context": []
}
```

### 13.3 Reviewer adds comments
```json
{
  "medical": [
    {"id":"rv-100","author":"Dr X","comment":"HDL mention misleading.","severity":"medium","field":"contentLong","proposed":"Remove HDL claim.","disposition":"open"}
  ],
  "product": [],
  "context": []
}
```

### 13.4 Agent resolves and updates
Edit payload:
```json
{
  "id": "1b3f1b6a-8c1b-4a2a-8c39-6a7d2f6a9f11",
  "revision": 2,
  "updatedDate": "2025-11-04T12:00:00.000Z",
  "updatedBy": "agent",
  "contentLong": "<p><b>LDL ve kalp sağlığı</b></p><p>... HDL iddiası kaldırıldı ...</p>",
  "status": "IN_REVIEW",
  "statusReason": "REVIEW_CHANGES"
}
```
Review file after resolution:
```json
{
  "medical": [
    {"id":"rv-100","author":"Dr X","comment":"HDL mention misleading.","severity":"medium","field":"contentLong","proposed":"Remove HDL claim.","disposition":"accepted"}
  ],
  "product": [],
  "context": []
}
```

## 14) GitHub Workflow
- **Branches**: `main` (protected), feature branches `feat/<topic>`.
- **PRs**: required reviews by CODEOWNERS.
- **Status checks** (CI): schema validation, HTML sanitizer, keyword lint, lifecycle policy.
- **Labels**: `medical`, `product`, `context`, `blocking`, `non‑blocking`.
- **Merging**: squash commit after all blocking comments resolved and CI green.

## 15) .github configuration
**CODEOWNERS**
```
/data/ @medical-reviewers
/reviews/ @medical-reviewers @product-reviewers @content-editors
/agent/ @platform-maintainers
```

**pull_request_template.md**
```
## Summary
- Topic:
- Group key:
- Label:

## Why
Brief rationale and sources (plain text).

## Checklist
- [ ] Validated against schema
- [ ] HTML limited to allowed tags
- [ ] Keywords 6–14; TR+EN
- [ ] Status=DRAFT or IN_REVIEW
- [ ] Review stub added under reviews/<id>.review.json

## Reviewers
- Medical: @
- Product: @
- Context/editor: @
```

**workflows/validate.yml** (outline)
- `ajv` JSON Schema check
- HTML allow‑list check
- Keyword count check
- Lifecycle transitions check

## 16) Comment Resolution Loop
1. Reviewer leaves comments in review file and/or PR.
2. Agent reads open comments, edits item, updates `revision`, and flips dispositions.
3. Repeat until no `severity=high` with `disposition=open`.
4. Reviewer marks `APPROVED`; agent sets item `ACTIVE` on publish commit.

## 17) Roles
- **Agent**: author, editor, resolver.
- **Medical reviewer**: clinical accuracy.
- **Product reviewer**: UX, product fit.
- **Context editor**: tone, localization, SEO/keywords.
