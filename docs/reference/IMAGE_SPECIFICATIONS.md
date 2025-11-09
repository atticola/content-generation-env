# Image Specifications for Health Content

**Guidelines for generating images for health education content**

---

## 📐 Technical Specifications

### Aspect Ratio & Dimensions
- **Aspect Ratio**: 16:9 (horizontal)
- **Recommended Size**: 1280 x 720px
- **Minimum Size**: 1024 x 576px
- **Maximum Size**: 1920 x 1080px

### Safe Zone (Critical!)
- **Total Canvas**: 16:9 (full image)
- **Core/Safe Zone**: 9:9 (center square)
- **Why**: Core content area where main visual focus must be
- **Margins**: 3.5 units on left/right (in 16-unit width)

```
┌─────────────────────────────────┐
│    │                    │       │  ← 16:9 Full Canvas
│ L  │    CORE 9:9       │   R   │
│ E  │    SAFE ZONE      │   I   │
│ F  │   (Main Focus)    │   G   │
│ T  │                   │   H   │
│    │                   │   T   │
└─────────────────────────────────┘
  3.5      9 units        3.5
```

**Critical Rule**: Main subject/focus MUST be centered in the 9:9 core zone.

---

## 🎨 Visual Style Guidelines

### General Style
- **Type**: Modern medical illustration, editorial illustration, or gradient art
- **Mood**: Professional yet approachable, calm, trustworthy, engaging
- **Complexity**: Clean and elegant, not cluttered but not too minimal
- **Visual Appeal**: Eye-catching, clickable, polished
- **Color Palette**: Rich yet soft, health-related colors with depth
  - Blues (trust, calm) - use gradients, not flat
  - Greens (health, nature) - vibrant but not neon
  - Warm neutrals (approachable) - with subtle color accents
  - Gold/copper tones for highlights
  - Depth through layering and gradients
- **Avoid**: Harsh reds, alarming imagery, overly clinical, flat colors, boring stock photos

### Composition
- ✅ **Main subject centered** (in 9:9 core)
- ✅ **Layered depth** - foreground, midground, background elements
- ✅ **Dynamic angles** - subtle perspective, not just flat
- ✅ **Negative space** - breathing room but purposeful
- ✅ **Visual interest** - gradients, lighting effects, subtle details
- ✅ **Symmetrical or balanced** composition
- ✅ **Polished finish** - professional quality that stands out
- ❌ **NO text** or typography
- ❌ **NO detailed charts/graphs**
- ❌ **NO faces** (privacy/universality)
- ❌ **NO overly simple shapes** (boring circles/squares alone)

---

## ✨ Visual Appeal Enhancement

### Key Elements for Clickability
1. **Depth & Dimension**
   - Use gradients (2-3 colors blending)
   - Add subtle shadows or glows
   - Layer elements (foreground/background)
   - Suggest 3D without being too literal

2. **Color Richness**
   - Avoid single flat colors
   - Use color transitions
   - Add complementary accent colors
   - Create visual warmth through color harmony

3. **Professional Polish**
   - Smooth rendering (no pixelation)
   - Refined edges and shapes
   - Balanced saturation (not too dull, not too bright)
   - Editorial illustration quality

4. **Visual Interest Points**
   - Add subtle details that reward closer look
   - Use lighting effects (soft glows, highlights)
   - Include organic shapes mixed with geometric
   - Create movement suggestion (flow, direction)

5. **Emotional Connection**
   - Warm, inviting color temperature
   - Hopeful and positive visual language
   - Approachable yet professional
   - Suggests health improvement journey

### Style Keywords for AI Prompts
Use these to enhance visual appeal:
- "editorial illustration style"
- "gradient art with depth"
- "modern medical aesthetic"
- "polished and refined"
- "soft lighting with highlights"
- "layered composition"
- "rich color palette"
- "professional health publication quality"
- "engaging and inviting"
- "subtle 3D depth"

---

## 📦 File Format & Optimization

### Format
- **Primary**: WebP (best compression)
- **Fallback**: JPEG (high compatibility)
- **Avoid**: PNG (too large for photos)

### Quality Settings
- **WebP Quality**: 80-85%
- **JPEG Quality**: 85-90%
- **Target File Size**: 50-150 KB
- **Maximum File Size**: 200 KB

### Optimization
- Use modern compression
- Remove metadata
- Optimize for web delivery
- Consider lazy loading compatibility

---

## 🏥 Content-Specific Guidelines

### Cardiology Topics (Heart Health)
**Visual Themes**:
- Abstract heart representation (geometric, artistic)
- Blood flow visualization (smooth, flowing)
- Cardiovascular system (simplified, diagram-like)
- Healthy lifestyle symbols (subtle)

**Examples**:
- Stylized heart with flowing lines
- Geometric heart shape with gradient
- Abstract arterial network
- Heart icon with health symbols

**Colors**: Blues, reds (soft), teals

---

### Lipids & Cholesterol Topics
**Visual Themes**:
- Abstract molecular structures (simple)
- Balance/scale metaphors
- Flowing liquids (smooth gradients)
- Shield/protection symbols

**Examples**:
- Geometric shapes representing molecules
- Balance scales (good vs bad cholesterol)
- Flowing gradient representing blood
- Shield with health symbols

**Colors**: Blues, greens, gold tones

---

### Prevention & Lifestyle Topics
**Visual Themes**:
- Lifestyle symbols (exercise, food, health)
- Positive health metaphors
- Growth/vitality symbols
- Action/movement (subtle)

**Examples**:
- Stylized healthy food elements
- Abstract exercise/movement
- Nature/wellness symbols
- Upward progression visuals

**Colors**: Greens, blues, warm oranges

---

### Risk & Assessment Topics
**Visual Themes**:
- Target/bullseye metaphors
- Assessment/measurement (abstract)
- Risk factors (non-alarming)
- Balance/stability

**Examples**:
- Concentric circles (target)
- Abstract measurement symbols
- Balanced elements
- Risk spectrum (calm visualization)

**Colors**: Blues, neutrals, subtle warnings

---

### Treatment & Adherence Topics
**Visual Themes**:
- Medical care (gentle representation)
- Consistency/routine symbols
- Treatment journey (abstract)
- Support/care metaphors

**Examples**:
- Abstract medication symbols
- Calendar/routine visualization
- Journey/path representation
- Support symbols

**Colors**: Blues, greens, trustworthy tones

---

## 🤖 AI Image Generation Prompts

### Prompt Structure Template

```
[Subject/Main Element], [Style], [Composition], [Color Palette], [Technical Specs]

Example:
"Abstract geometric heart shape, medical illustration style, centered composition with breathing room, soft blue and teal gradients, clean minimalist design, horizontal 16:9 format, safe zone centered"
```

### Prompt Components

**1. Subject** (What to show)
- Main visual element
- Related to health topic
- Simple, recognizable

**2. Style** (How to render)
- Medical illustration
- Clean photography
- Geometric abstract
- Gradient art
- Minimalist design

**3. Composition** (Layout)
- Centered in safe zone
- Symmetrical
- Balanced
- Negative space
- Horizontal orientation

**4. Color Palette**
- Specific colors
- Mood descriptors
- Gradient directions
- Tone (warm/cool)

**5. Technical Details**
- 16:9 horizontal
- Centered focus
- No text
- Clean/simple
- Web-optimized

---

## 📝 Example Prompts by Topic

### Topic: Atherosclerosis (Ateroskleroz)
```
Prompt: "Abstract arterial cross-section showing smooth vessel walls, medical
illustration style, centered composition, soft blue and light red gradients,
clean minimalist design showing health and flow, horizontal 16:9 format,
main subject centered in safe zone, no text, professional medical aesthetic"
```

### Topic: Blood Lipids (Kan Yağları)
```
Prompt: "Geometric abstract representation of lipid molecules, floating spheres
in various sizes, medical illustration style, centered balanced composition,
soft blue teal and gold color palette, clean minimalist design, horizontal
16:9 format, main elements centered, no text, modern health aesthetic"
```

### Topic: LDL & Heart Disease
```
Prompt: "Stylized shield protecting a geometric heart, medical illustration
style, centered composition with clear focus, blue and teal gradients with
subtle red accents, minimalist clean design, horizontal 16:9 format, shield
and heart centered in safe zone, no text, protective health concept"
```

### Topic: Good vs Bad Cholesterol
```
Prompt: "Abstract balance scale with geometric shapes, medical illustration
style, perfectly centered composition, blue and green gradients representing
balance, clean minimalist design, horizontal 16:9 format, scale centered in
safe zone, no text, equilibrium concept"
```

### Topic: Heart Attack Prevention
```
Prompt: "Stylized heart surrounded by protective circular elements, medical
illustration style, centered composition, warm blue and green gradients,
minimalist clean design suggesting protection, horizontal 16:9 format, heart
centered in safe zone, no text, preventive care aesthetic"
```

### Topic: Daily Heart Health (Lifestyle)
```
Prompt: "Abstract representation of healthy habits, flowing organic shapes
suggesting movement and vitality, medical illustration style, centered balanced
composition, fresh green and blue gradients, clean minimalist design, horizontal
16:9 format, main elements centered, no text, wellness aesthetic"
```

### Topic: Familial Hypercholesterolemia
```
Prompt: "Abstract DNA helix merged with heart symbol, medical illustration
style, centered composition, blue and teal gradients with gold accents, clean
minimalist genetic health concept, horizontal 16:9 format, main symbol centered
in safe zone, no text, genetic health aesthetic"
```

---

## ✅ Prompt Checklist

Before finalizing an image prompt, verify:

- [ ] **16:9 horizontal** orientation specified
- [ ] **Centered composition** in safe zone
- [ ] **No text** explicitly stated
- [ ] **Color palette** defined
- [ ] **Style** clearly described
- [ ] **Subject** related to health topic
- [ ] **Simplicity** emphasized
- [ ] **Professional medical** aesthetic
- [ ] **Web-optimized** implied or stated
- [ ] **Safe for all audiences** (no graphic medical imagery)

---

## 🎨 AI Image Generators Recommended

### Best Options:
1. **Midjourney** - Best quality for medical illustrations
2. **DALL-E 3** - Good balance, accurate to prompts
3. **Stable Diffusion** - Most customizable
4. **Adobe Firefly** - Commercial-safe, clean style

### Settings for Web:
- Resolution: 1280x720 or 1920x1080
- Quality: High
- Style: Clean, minimalist, professional

---

## 🔄 Image Generation Workflow

### Step 1: Generate Prompt
Use AI to generate image prompt based on content topic:
```
"Generate a Midjourney image prompt for [TOPIC] following these specs:
- 16:9 horizontal format
- Centered composition (9:9 safe zone)
- Medical illustration style
- No text
- Related to: [BRIEF TOPIC DESCRIPTION]"
```

### Step 2: Generate Image
- Paste prompt into image AI
- Generate image
- Review composition (check 9:9 center)

### Step 3: Optimize
- Resize to 1280x720 if needed
- Convert to WebP
- Compress to <150KB
- Test on dark and light backgrounds

### Step 4: Validate
- Check safe zone (crop to 9:9 - does it still work?)
- Verify no text
- Confirm file size
- Test loading speed

---

## 📊 Quality Metrics

### Visual Quality
- ✅ Sharp and clear
- ✅ Professional appearance
- ✅ Appropriate colors
- ✅ Good contrast
- ✅ No artifacts

### Technical Quality
- ✅ Correct dimensions (16:9)
- ✅ Optimized file size (<150KB)
- ✅ Web-friendly format
- ✅ Fast loading
- ✅ Responsive-ready

### Content Quality
- ✅ Topic-relevant
- ✅ Culturally appropriate
- ✅ Safe for all audiences
- ✅ Timeless (not trendy)
- ✅ Brand-consistent

---

## 🚫 What to Avoid

### Visual Elements
- ❌ Text, numbers, labels
- ❌ Real people's faces
- ❌ Graphic medical procedures
- ❌ Blood/gore
- ❌ Needles (can cause anxiety)
- ❌ Complex charts/graphs
- ❌ Stock photo clichés

### Technical Issues
- ❌ Wrong aspect ratio
- ❌ Off-center composition
- ❌ Too large file size
- ❌ Poor compression
- ❌ Pixelation/artifacts

### Style Issues
- ❌ Too abstract (unrecognizable)
- ❌ Too clinical (intimidating)
- ❌ Too colorful (distracting)
- ❌ Inconsistent style across items

---

## 💡 Tips for Success

### For Best Results:
1. **Be Specific**: Detailed prompts = better images
2. **Iterate**: Generate 3-4 options, pick best
3. **Test Center Crop**: Verify safe zone works
4. **Consistent Style**: Keep similar aesthetic across all images
5. **User Feedback**: Test with actual users

### Common Improvements:
- Add "professional medical" to prompts
- Specify "soft lighting" for welcoming feel
- Use "minimalist" to avoid clutter
- Add "editorial illustration" for clean style
- Specify "centered composition" explicitly

---

## 📁 File Naming Convention

```
[topic-key]-[language]-[size].webp

Examples:
ateroskleroz-tr-1280x720.webp
ldl-cholesterol-tr-1280x720.webp
heart-attack-prevention-tr-1280x720.webp
```

---

## 🔄 Update Process

When content is updated:
1. Review if image still relevant
2. Check if style is consistent with newer images
3. Verify file size is optimized
4. Update if topic changed significantly

---

**Remember**: Images support content, not replace it. Keep them simple, professional, and focused on the core 9:9 safe zone!

---

**Last Updated**: 2025-11-07
**Version**: 1.0.0
