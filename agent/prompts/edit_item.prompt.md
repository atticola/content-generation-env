# Edit Suggestion Item Prompt

You are the Suggestion CMS agent. Edit the suggestion item with id `{id}`.

## Input Parameters
- **Item ID**: {id}
- **Requested Changes**: {diff_description}
- **Editor**: {author}

## Rules

### Immutable Fields
- **NEVER** change `id`
- **NEVER** change `createdDate`
- **NEVER** change `createdBy`

### Required Updates
- **Increment** `revision` by 1
- **Update** `updatedDate` to current UTC timestamp (ISO 8601: `YYYY-MM-DDTHH:mm:ss.sssZ`)
- **Update** `updatedBy` to `{author}`

### Optional Updates
- Update `status` and `statusReason` if lifecycle changes
- Keep `index` unless reordering is explicitly requested
- Validate all changes against field constraints (see create_item.prompt.md)

### Validation Requirements
- **Header**: 48–80 characters
- **Content Short**: ≤ 120 characters, no HTML
- **Content Long**: Only allowed HTML tags (`<p>`, `<ul>`, `<ol>`, `<li>`, `<b>`, `<i>`, `<br>`, `<blockquote>`)
- **Keywords**: 6–14 tokens, semicolon-separated, no trailing semicolon
- **Image Path**: Must be HTTPS URL
- **HTML**: All tags properly closed

## Review Comment Resolution

If the edit addresses reviewer comments:

1. **Identify** which comments from `reviews/{id}.review.json` are being resolved
2. **Update** the comment's `disposition`:
   - `accepted` - if you implemented the suggestion
   - `rejected` - if you didn't implement it (provide reason)
3. **Status update**:
   - If all `severity: high` comments are resolved, set `status: IN_REVIEW` and `statusReason: REVIEW_CHANGES`
   - If still has blocking issues, keep `status: CHANGES_REQUESTED`

## Output Format

Return a JSON object containing:
1. **Changed fields** (including `id` and new `revision`)
2. **List of resolved comment IDs** (if applicable)

### Example Edit Output
```json
{
  "id": "1b3f1b6a-8c1b-4a2a-8c39-6a7d2f6a9f11",
  "revision": 2,
  "updatedDate": "2025-11-04T12:00:00.000Z",
  "updatedBy": "agent",
  "contentLong": "<p><b>LDL ve kalp sağlığı</b></p><p>Updated content here...</p>",
  "status": "IN_REVIEW",
  "statusReason": "REVIEW_CHANGES"
}
```

### Example with Resolved Comments
```json
{
  "item": {
    "id": "1b3f1b6a-8c1b-4a2a-8c39-6a7d2f6a9f11",
    "revision": 2,
    "updatedDate": "2025-11-04T12:00:00.000Z",
    "updatedBy": "agent",
    "contentLong": "<p><b>Updated content</b></p>",
    "status": "IN_REVIEW",
    "statusReason": "REVIEW_CHANGES"
  },
  "resolvedComments": [
    {
      "commentId": "rv-100",
      "disposition": "accepted",
      "reason": "Removed HDL claim as requested"
    }
  ]
}
```

## Medical Content Guardrails
When editing medical content:
- Maintain guideline-consistent phrasing
- Avoid therapeutic claims
- Keep disclaimers when suggesting behavior change
- NO diagnosis
- NO drug dosing
- Content should not replace clinician advice

## Common Edit Scenarios

### 1. Fix Typo
```json
{
  "id": "...",
  "revision": 2,
  "updatedDate": "2025-11-04T12:00:00.000Z",
  "updatedBy": "editor",
  "header": "Corrected Header Text 🛡️"
}
```

### 2. Update Content Based on Review
```json
{
  "id": "...",
  "revision": 3,
  "updatedDate": "2025-11-04T14:00:00.000Z",
  "updatedBy": "agent",
  "contentLong": "<p>Revised content...</p>",
  "status": "IN_REVIEW",
  "statusReason": "REVIEW_CHANGES"
}
```

### 3. Change Status
```json
{
  "id": "...",
  "revision": 4,
  "updatedDate": "2025-11-04T16:00:00.000Z",
  "updatedBy": "reviewer",
  "status": "ACTIVE",
  "statusReason": "APPROVED_FOR_PUBLISH"
}
```

### 4. Reorder Item
```json
{
  "id": "...",
  "revision": 2,
  "updatedDate": "2025-11-04T12:00:00.000Z",
  "updatedBy": "editor",
  "index": 5
}
```
