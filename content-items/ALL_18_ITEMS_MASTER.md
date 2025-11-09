# Master Content Document: All 18 Health Education Items

**Purpose**: Complete reference for all 18 Turkish health education articles
**Format**: Both Turkish (TR) and English (EN) versions
**Status**: Ready for AI generation and review

---

## Instructions for Use

1. **For AI Generation**: Copy the prompt template below and paste into Claude/ChatGPT
2. **For Manual Review**: Each item includes validation checklist
3. **For Export**: Use `scripts/export_to_markdown.py` after adding to JSON

---

## Content Items Overview

| # | Title (TR) | Category | Group | Label |
|---|-----------|----------|-------|-------|
| 01 | Ateroskleroz (Damar Sertliği/Tıkanıklığı) Nedir? | Cardiology | heart_health | cardiology |
| 02 | Kan Yağları Nedir ve Çeşitleri Nelerdir? | Lipids | heart_health | lipids |
| 03 | LDL Kolesterol ve Kalp Hastalıkları | Lipids/Cardiology | heart_health | lipids |
| 04 | İyi Kolesterol ve Kötü Kolesterol Kavramı | Lipids | heart_health | lipids |
| 05 | Türkiye'de Kalp ve Damar Hastalıkları Durumu | Public Health | popular | public-health |
| 06 | Kalp Krizi Nasıl Oluşur? | Cardiology | heart_health | cardiology |
| 07 | İnme Nasıl Oluşur? | Neurology | heart_health | neurology |
| 08 | Kalp Krizi Önlenebilir Mi? | Prevention | heart_health | prevention |
| 09 | Genç Yaşta Kalp Krizinin Sebepleri | Cardiology/Risk | heart_health | cardiology |
| 10 | Hiçbir Şikâyeti Yokken Kalp Krizi Geçirdi - Bu Gerçekçi Mi? | Cardiology/Awareness | popular | cardiology |
| 11 | Kalp Sağlığı İçin Günlük Hayatta Neler Yapabiliriz? | Lifestyle/Prevention | popular | lifestyle |
| 12 | Kalp Damar Hastalığında Risk Nasıl Hesaplanır? | Risk Assessment | heart_health | risk |
| 13 | LDL ve Trigliserid Farkı | Lipids | heart_health | lipids |
| 14 | Diyabet ve Kalp-Damar Sağlığı (Diyabetik Dislipidemi) | Diabetes/Cardiology | heart_health | diabetes |
| 15 | LDL Hedefleri Kişisel mi? | Lipids/Personalized | heart_health | lipids |
| 16 | Lipid Düşürücü Tedaviler | Therapy | heart_health | therapy |
| 17 | Ailesel Hiperkolesterolemi (FH) | Genetics | heart_health | genetics |
| 18 | Yaşam Tarzı Değişikliği ve Tedaviye Devam Önemi | Adherence/Lifestyle | heart_health | adherence |

---

## AI Generation Prompt

To generate all content, use the file:
```
docs/ai-prompts/batch-generation/GENERATE_ALL_18_ENHANCED.txt
```

This prompt will generate:
- ✅ All 18 items with exact Turkish titles
- ✅ Enhanced image prompts (not simple/flat)
- ✅ Both Turkish content and bilingual keywords
- ✅ Proper field lengths and validation
- ✅ Medical disclaimers
- ✅ JSON format ready for import

---

## Individual Item Templates

### Item 04: İyi Kolesterol ve Kötü Kolesterol Kavramı

**Header**: `İyi ve Kötü Kolesterol: Farkı Nedir? ⚖️`
**Short**: `HDL ve LDL kolesterolün farklarını ve rollerini öğrenin.`

**Turkish Content**: Educational explanation of HDL (good) vs LDL (bad) cholesterol, their roles, balance concept, why both matter. Include disclaimer.

**Keywords**: `HDL;LDL;iyi kolesterol;good cholesterol;kötü kolesterol;bad cholesterol;kolesterol dengesi;lipid balance;kalp sağlığı;heart health`

**Image Prompt**: Abstract balance scale in centered composition, two sides with geometric shapes representing HDL (gold/green tones #4A9B9F) and LDL (blue tones #2C5AA0), perfectly balanced in equilibrium, editorial illustration style with gradient depth and soft lighting, polished modern aesthetic, horizontal 16:9 format with main scale centered in 9:9 safe zone, no text, professional medical publication quality, engaging and visually sophisticated

---

### Item 05: Türkiye'de Kalp ve Damar Hastalıkları Durumu

**Header**: `Türkiye'de Kalp Sağlığı: Farkındalık ve Önleme 🇹🇷❤️`
**Short**: `Ülkemizdeki kalp sağlığı durumu ve alabileceğiniz önlemler.`

**Turkish Content**: Awareness content about cardiovascular health in Turkey, importance of prevention, early detection, positive encouraging tone (not alarmist), emphasize that prevention is possible.

**Keywords**: `Türkiye;Turkey;kalp hastalıkları;heart disease;kardiyovasküler;cardiovascular;farkındalık;awareness;önleme;prevention;sağlık taraması;health screening`

**Image Prompt**: Stylized heart shape with subtle Turkish cultural geometric patterns (çini/tile inspired) integrated tastefully, warm gradient from red (#C41E3A) to pink (#FF9999) center, surrounded by protective circular elements in Turkish flag colors (red accent with soft integration), editorial illustration celebrating health awareness, layered composition with heart centered in 9:9 safe zone, modern medical aesthetic balancing cultural relevance with universal health message, soft lighting creating warmth and hope, horizontal 16:9 at 1280x720px, no text, professional engaging style that resonates with Turkish audience

---

### Item 06: Kalp Krizi Nasıl Oluşur?

**Header**: `Kalp Krizi Nasıl Gerçekleşir? Mekanizmayı Anlayın 🚨`
**Short**: `Kalp krizinin oluşum sürecini ve acil müdahalenin önemini öğrenin.`

**Turkish Content**: Step-by-step explanation of heart attack mechanism (plaque rupture, clot formation, blocked blood flow, heart muscle damage), emphasize it's medical emergency, include when to seek help.

**Keywords**: `kalp krizi;heart attack;miyokard enfarktüsü;myocardial infarction;plak yırtılması;plaque rupture;pıhtı;blood clot;koroner;coronary;acil durum;emergency`

**Image Prompt**: Detailed medical editorial illustration of stylized heart with coronary artery visible, showing dramatic moment of arterial blockage visualized as narrowing vessel with obstruction, rendered in sophisticated gradients from healthy pink (#FF9999) heart tissue to warning red (#C41E3A) at blockage site, flowing blood represented as elegant particle streams interrupted at blockage point, layered composition with clear focus on blocked artery, professional urgency conveyed through color and lighting without being graphic, soft directional lighting creating depth, centered heart within 9:9 safe zone, horizontal 16:9 format at 1280x720px, modern medical aesthetic balancing educational clarity with visual sensitivity, no text, polished illustration suitable for serious health education

---

### Item 07: İnme Nasıl Oluşur?

**Header**: `İnme Nedir ve Nasıl Gerçekleşir? Belirtileri Tanıyın 🧠`
**Short**: `İnme türlerini, belirtilerini ve acil müdahalenin önemini öğrenin.`

**Turkish Content**: Explain stroke (ischemic vs hemorrhagic), symptom recognition (FAST protocol), emphasize medical emergency, basic prevention.

**Keywords**: `inme;stroke;iskemik inme;ischemic stroke;hemorajik inme;hemorrhagic stroke;beyin;brain;felç;paralysis;FAST;acil;emergency`

**Image Prompt**: Sophisticated medical illustration of stylized brain profile in side view with intricate vascular network visible as elegant branching lines, gradient color scheme transitioning from healthy purple-blue (#4A5B92) in main brain tissue to lighter teal (#4A9B9F) in vascular structures, one vessel showing subtle blockage or disruption visualized abstractly, layered composition with brain centered in 9:9 safe zone showing both structure and vulnerable vasculature, editorial illustration style with anatomical accuracy balanced by accessibility, soft ambient lighting suggesting neurological importance, horizontal 16:9 format optimized for 1280x720px, modern medical aesthetic that is educational without being clinical or frightening, no text, polished professional finish inviting viewer engagement with neurological health content

---

### Item 08: Kalp Krizi Önlenebilir Mi?

**Header**: `Kalp Krizi Önlenebilir Mi? Evet! Nasıl Yapılır? 💪`
**Short**: `Kalp krizinin büyük oranda önlenebilir olduğunu ve koruma yollarını öğrenin.`

**Turkish Content**: Empowering content about heart attack prevention (YES it's preventable!), lifestyle changes, risk factor control, regular check-ups, positive motivating tone.

**Keywords**: `kalp krizi;heart attack;önleme;prevention;koruyucu önlemler;preventive measures;risk faktörleri;risk factors;yaşam tarzı;lifestyle;sağlıklı yaşam;healthy living`

**Image Prompt**: Inspiring editorial illustration of stylized heart surrounded by multi-layered protective shield elements forming concentric circles, rendered in confident gradient blues (#2C5AA0) and teals (#4A9B9F) suggesting strength and security, heart in warm healthy pink (#FF9999) at center radiating subtle glow of vitality, shield layers semi-transparent showing depth, positive uplifting composition centered in 9:9 safe zone, soft heroic lighting from above creating optimistic mood, horizontal 16:9 format at 1280x720px, modern medical aesthetic with empowering protective metaphor, visual language of strength and prevention, no text, polished professional style that motivates viewer toward heart health action, engaging and confidence-inspiring

---

### Item 09: Genç Yaşta Kalp Krizinin Sebepleri

**Header**: `Genç Yaşta Kalp Krizi: Nedenleri ve Risk Faktörleri ⚠️`
**Short**: `Genç yaşlarda kalp krizi riskini artıran faktörleri tanıyın.`

**Turkish Content**: Causes of heart attacks in younger people (FH, smoking, metabolic issues, substance use), importance of family history screening, prevention message for young people.

**Keywords**: `genç yaşta kalp krizi;young heart attack;erken kalp krizi;early heart attack;ailesel hiperkolesterolemi;FH;familial hypercholesterolemia;sigara;smoking;genetik;genetic`

**Image Prompt**: Modern editorial illustration showing youthful stylized heart rendered in vibrant healthy gradients (pink #FF9999 to coral) with warning indicator elements tastefully integrated as small geometric shapes in cautionary yellow (#FFB84D) scattered around periphery suggesting risk awareness, layered composition balancing youth vitality with educational caution, centered heart in 9:9 safe zone surrounded by subtle circular risk factor symbols kept abstract and non-alarming, editorial health publication style with sophisticated gradient work, lighting suggesting alertness without fear, horizontal 16:9 at 1280x720px, modern aesthetic appropriate for younger demographic, no text, professional polished finish that engages younger viewers while communicating serious health message, inviting and age-appropriate

---

### Item 10: Hiçbir Şikâyeti Yokken Kalp Krizi Geçirdi - Bu Gerçekçi Mi?

**Header**: `Belirtisiz Kalp Krizi: Ne Kadar Gerçekçi? 🤔`
**Short**: `Kalp krizi belirtisiz olabilir mi? Sessiz iskemi ve önemi hakkında bilgi edinin.`

**Turkish Content**: Explain silent ischemia concept, some people have mild or no symptoms, importance of screening and risk assessment, balanced tone (not panic-inducing).

**Keywords**: `sessiz iskemi;silent ischemia;belirtisiz kalp krizi;silent heart attack;asemptomatik;asymptomatic;kalp krizi;heart attack;tarama;screening;risk değerlendirmesi;risk assessment`

**Image Prompt**: Intriguing editorial medical illustration concept showing two-part composition - visible stylized heart on one side in clear definition with rich gradients (pink #FF9999 to red #C41E3A), and semi-transparent ghosted heart on other side suggesting hidden or subtle aspects, both connected by subtle flowing lines representing silent processes, layered depth with foreground and background elements, centered in 9:9 safe zone showing duality of visible and hidden, professional medical illustration style with sophisticated transparency effects, soft mysterious lighting suggesting things not immediately apparent, horizontal 16:9 format at 1280x720px, modern aesthetic that visually communicates concept of silent ischemia, no text, polished finish that invites viewer curiosity about hidden cardiac risks, thought-provoking and engaging

---

### Item 11: Kalp Sağlığı İçin Günlük Hayatta Neler Yapabiliriz?

**Header**: `Günlük Hayatta Kalp Sağlığı: Basit Ama Etkili Adımlar 💚`
**Short**: `Kalp sağlığınızı korumak için günlük hayatta uygulayabileceğiniz pratik öneriler.`

**Turkish Content**: Practical lifestyle advice for heart health (physical activity, diet, sleep, stress, smoking cessation), achievable recommendations, positive encouraging tone, focus on sustainable changes.

**Keywords**: `kalp sağlığı;heart health;yaşam tarzı;lifestyle;egzersiz;exercise;sağlıklı beslenme;healthy diet;stres yönetimi;stress management;günlük alışkanlıklar;daily habits`

**Image Prompt**: Uplifting editorial illustration showing abstract representation of healthy daily habits through flowing organic shapes suggesting movement and vitality, vibrant fresh color palette with greens (#4A9B9F, #7CB342) representing nutrition and life, blues (#2C5AA0) for wellness, warm oranges (#FFB84D) for energy, elements flowing in harmonious circular motion around central heart symbol in healthy pink (#FF9999), layered composition with depth suggesting life layers, all centered in 9:9 safe zone, soft natural lighting creating positive hopeful mood, horizontal 16:9 format at 1280x720px, modern wellness aesthetic that feels achievable and inviting, professional health publication quality, no text, polished style that motivates lifestyle change through visual optimism, engaging and lifestyle-friendly

---

### Item 12: Kalp Damar Hastalığında Risk Nasıl Hesaplanır?

**Header**: `Kalp Hastalığı Riski Herkeste Aynı mı? Risk Değerlendirmesi 📊`
**Short**: `Kalp hastalığı riskinin kişiden kişiye değiştiğini ve nasıl değerlendirildiğini öğrenin.`

**Turkish Content**: Explain cardiovascular risk assessment concept, risk varies by individual, factors affecting risk (age, gender, cholesterol, BP, diabetes, smoking), emphasize talking to healthcare provider.

**Keywords**: `risk değerlendirmesi;risk assessment;kardiyovasküler risk;cardiovascular risk;risk faktörleri;risk factors;risk calculator;bireysel risk;personalized risk;kalp hastalığı;heart disease`

**Image Prompt**: Sophisticated editorial illustration showing abstract risk spectrum visualization as layered gradient bands flowing from low risk (cool greens #7CB342) through moderate (amber #FFB84D) to higher risk (deeper reds #C41E3A), target or bullseye element at center suggesting personalized focus, geometric shapes representing different risk factors distributed along spectrum, professional data visualization aesthetic adapted for health education, layered composition centered in 9:9 safe zone, soft analytical lighting creating clarity, horizontal 16:9 format at 1280x720px, modern medical assessment aesthetic that communicates individual variability, no text or numbers, polished style balancing scientific accuracy with accessibility, engaging visual that invites personal risk awareness

---

### Item 13: LDL ve Trigliserid Farkı

**Header**: `LDL ve Trigliserit: Farkları ve Etkileri Nedir? 🔬`
**Short**: `LDL ve trigliserit arasındaki farkları ve her ikisinin önemini öğrenin.`

**Turkish Content**: Explain difference between LDL and triglycerides simply, both are lipids but different roles and targets, comparison/contrast format.

**Keywords**: `LDL;trigliserit;triglycerides;fark;difference;kan yağları;blood lipids;kolesterol;cholesterol;lipid paneli;lipid panel`

**Image Prompt**: Clean editorial scientific illustration showing side-by-side comparison of two distinct molecular structures, left side showing LDL particle as spherical geometric form with layered structure in blues (#2C5AA0) suggesting cholesterol carrier, right side showing triglyceride molecules as three-pronged elegant structure in warm greens (#4A9B9F, #7CB342) suggesting energy storage, both rendered with sophisticated gradient depth and polished glass-like finish, subtle connecting element between them showing they're related but different, balanced composition with both structures prominently centered within 9:9 safe zone, educational clarity through visual distinction, soft analytical lighting emphasizing structural differences, horizontal 16:9 at 1280x720px, modern scientific medical aesthetic, no text, professional illustration suitable for lipid education, engaging visual comparison that clarifies difference

---

### Item 14: Diyabet ve Kalp-Damar Sağlığı (Diyabetik Dislipidemi)

**Header**: `Diyabet ve Kalp Sağlığı: Damar Sistemi Üzerine Etkiler 💉❤️`
**Short**: `Diyabetin kalp ve damar sisteminize etkilerini ve diyabetik dislipidemiyi öğrenin.`

**Turkish Content**: Explain relationship between diabetes and CVD, diabetic dyslipidemia concept, diabetes affects more than blood sugar, increased CV risk, comprehensive risk management needed.

**Keywords**: `diyabet;diabetes;diyabetik dislipidemi;diabetic dyslipidemia;kalp hastalığı;heart disease;kardiyovasküler risk;cardiovascular risk;kan şekeri;blood sugar;damar sağlığı;vascular health`

**Image Prompt**: Sophisticated editorial medical illustration showing interconnection between glucose metabolism and cardiovascular health, stylized heart and blood glucose molecule (simple hexagonal structure) connected by flowing gradient pathways suggesting metabolic relationship, heart in healthy pink (#FF9999) with subtle glucose crystals in amber/gold (#D4AF37) tones integrated into surrounding vessels, layered composition showing systemic connection, professional medical publication quality with refined polished finish, soft lighting creating dimensional depth, centered interconnected elements within 9:9 safe zone, color palette combining cardiovascular reds/pinks with metabolic golds and blues, horizontal 16:9 format at 1280x720px, modern medical aesthetic illustrating diabetes-heart connection, no text, engaging visual that communicates complexity accessibly, inviting understanding of metabolic cardiovascular relationship

---

### Item 15: LDL Hedefleri Kişisel mi?

**Header**: `LDL Hedef Değerleri: Herkes İçin Aynı mı? 🎯`
**Short**: `LDL kolesterol hedeflerinin neden kişiden kişiye değiştiğini öğrenin.`

**Turkish Content**: Explain LDL targets are personalized based on individual risk, higher risk patients need lower LDL, determined by healthcare provider, individualized approach.

**Keywords**: `LDL hedefleri;LDL targets;bireysel hedefler;personalized targets;risk bazlı hedefler;risk-based targets;kolesterol tedavisi;cholesterol treatment;kişiselleştirilmiş tıp;personalized medicine`

**Image Prompt**: Modern editorial illustration of target/bullseye concept with multiple concentric rings in gradient blues (#2C5AA0 to #4A9B9F), but with key innovation - multiple different colored markers at various ring levels representing different individuals' personalized targets, sophisticated visualization showing not one-size-fits-all, markers in varied colors (gold #D4AF37, green #7CB342, amber #FFB84D) suggesting diversity of targets, centered target composition within 9:9 safe zone, professional data visualization aesthetic adapted for medical education, soft focused lighting emphasizing center while showing variety, horizontal 16:9 format at 1280x720px, modern personalized medicine aesthetic, no text or numbers, polished style that visually communicates individualization concept, engaging and contemporary

---

### Item 16: Lipid Düşürücü Tedaviler

**Header**: `Lipid Düşürücü Tedaviler: Neden Önemli? 💊`
**Short**: `Lipid düşürücü tedavilerin türleri ve kalp sağlığındaki rolünü öğrenin.`

**Turkish Content**: Overview of lipid-lowering therapies without specific dosing, classes of medications exist (statins most common), importance of treatment when prescribed, NO specific drug names/doses, defer to healthcare provider, focus on adherence importance.

**Keywords**: `lipid tedavisi;lipid therapy;statinler;statins;kolesterol ilacı;cholesterol medication;kalp koruma;cardioprotection;tedaviye uyum;medication adherence`

**Image Prompt**: Clean editorial medical illustration showing abstract treatment pathway concept, stylized medication representation as elegant geometric capsule forms in professional pharmaceutical blue (#2C5AA0) with subtle gradient depth, flowing pathway lines suggesting therapeutic journey from elevated lipids (warm tones) to controlled lipids (cool protective tones #4A9B9F), heart symbol at end of pathway in healthy pink (#FF9999) representing protected outcome, layered composition with clear directional flow centered in 9:9 safe zone, professional pharmaceutical-medical aesthetic with polished finish, soft lighting suggesting hope and efficacy, horizontal 16:9 format at 1280x720px, modern treatment education style that is informative without being promotional, no text or specific drug names, sophisticated illustration suitable for general therapy education, engaging and trustworthy

---

### Item 17: Ailesel Hiperkolesterolemi (FH)

**Header**: `Ailesel Hiperkolesterolemi: Genetik Yüksek Kolesterol 🧬`
**Short**: `Kalıtsal yüksek kolesterol hastalığı FH'yi ve erken tarama önemini öğrenin.`

**Turkish Content**: Explain FH in simple terms (genetic high cholesterol), inherited/runs in families, early high LDL, increased heart attack risk, family screening importance, manageable with treatment, hopeful message.

**Keywords**: `ailesel hiperkolesterolemi;familial hypercholesterolemia;FH;genetik;genetic;kalıtsal;hereditary;yüksek kolesterol;high cholesterol;tarama;screening;aile taraması;family screening`

**Image Prompt**: Elegant editorial medical-genetic illustration showing stylized double helix DNA structure in sophisticated gradient blues and teals (#2C5AA0 to #4A9B9F) merging seamlessly with heart symbol in healthy pink (#FF9999), DNA strand appearing to wrap protectively around or integrate with heart suggesting genetic-cardiac connection, small golden particles (#D4AF37) representing lipids distributed along DNA suggesting familial lipid disorder, layered composition with DNA-heart fusion centered in 9:9 safe zone, professional medical genetics aesthetic with polished molecular detail, soft scientific lighting creating depth and highlighting genetic aspect, horizontal 16:9 format at 1280x720px, modern genetic medicine visualization style, no text, sophisticated illustration communicating hereditary heart condition, engaging visual balancing genetic science with cardiac health, hopeful rather than concerning tone through color and light

---

### Item 18: Yaşam Tarzı Değişikliği ve Tedaviye Devam Önemi

**Header**: `Tedaviye Devam ve Yaşam Tarzı: Neden Bu Kadar Önemli? 🔄`
**Short**: `Tedaviye uyum ve yaşam tarzı değişikliklerinin kalp sağlığınızdaki rolünü öğrenin.`

**Turkish Content**: Emphasize medication adherence and lifestyle changes importance, both needed for long-term heart health, address common concerns (side effects, forgetting doses), encourage communication with provider, regular follow-up importance, positive supportive tone.

**Keywords**: `tedaviye uyum;medication adherence;yaşam tarzı;lifestyle;tedavi devamlılığı;treatment compliance;takip;follow-up;kalp sağlığı;heart health;ilaç uyumu;medication compliance`

**Image Prompt**: Inspiring editorial illustration showing continuous cycle or circular flow concept representing ongoing commitment, smooth circular pathway in gradient greens (#7CB342) and blues (#4A9B9F) suggesting positive sustainable journey, lifestyle elements (abstract activity, nutrition symbols) integrated as elegant geometric forms along path, medication reminder as subtle geometric shape also in cycle, heart at center in vibrant healthy pink (#FF9999) glowing with vitality as destination and source, layered composition with circular flow centered in 9:9 safe zone, professional health commitment aesthetic with polished flowing design, soft encouraging lighting suggesting long-term success, horizontal 16:9 format at 1280x720px, modern wellness-medical hybrid aesthetic, no text, sophisticated illustration communicating sustained effort and positive outcomes, engaging motivational visual about adherence and lifestyle, supportive and empowering tone through design

---

## Validation Standards

Each item must meet:
- ✅ Header: 48-80 characters (exact Turkish title)
- ✅ Content Short: ≤120 characters
- ✅ Content Long: 160-300 words Turkish
- ✅ Keywords: 6-14 bilingual (TR;EN), no trailing semicolon
- ✅ Image Prompt: 100-150 words, enhanced visual language
- ✅ Medical disclaimer included
- ✅ No specific dosing or diagnosis
- ✅ Appropriate label and group
- ✅ Both TR and EN versions

---

## Next Steps

1. **Generate Full Content**: Use `GENERATE_ALL_18_ENHANCED.txt` with AI
2. **Review Generated JSON**: Check all fields present and valid
3. **Import to System**: Use `scripts/add_batch_items.py`
4. **Export to Markdown**: Use `scripts/export_to_markdown.py` for review
5. **Review Process**: Use `templates/CONTENT_REVIEW_TEMPLATE.md`
6. **Generate Images**: Use image prompts with Midjourney/DALL-E
7. **Final Validation**: Run `scripts/validate.py`

---

**Created**: 2025-11-07
**Version**: 1.0
**Status**: Master Reference Document
