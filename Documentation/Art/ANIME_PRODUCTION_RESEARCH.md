# Anime production research and revised art standard

Researched 22 November 2026 after the user rejected the initial rendering. This is a concrete production specification, not a claim that a prompt guarantees professional results.

## What the original pass got wrong

The first cast sheet accumulated fine strands, diffuse face modeling, numerous small hair highlights and blanket grey-brown softness. Several girls shared nearly the same eye, nose and jaw construction. The expression atlases inherited these problems. The exploration test also produced an unwanted translucent glow behind a sprite. None of these are accepted final assets. Stop propagating that sheet.

## Primary-source findings

### Design, drawing, paint and compositing are separate decisions

[Toei Animation's production overview](https://corp.toei-anim.co.jp/en/company/animation_production.html) separates storyboard/layout, key animation, color designation, backgrounds, digital coloring, effects and compositing. For this project the useful principle is to fix the character design and paint rules before adding atmosphere. More effects cannot repair a weak model. This application is our production inference, not a statement that all anime uses one aesthetic.

### Drawing should communicate acting

[Kyoto Animation's job descriptions](https://www.kyotoanimation.co.jp/recruit/job/) describe key animation in terms of acting through drawings, distinguish clean-up and digital painting, and explain color designation as communicating materials, time and emotion. Its background and compositing roles remain distinct. Apply that here by making each expression change the brows, lids, mouth and gaze in a purposeful way. Different hair colors alone do not establish five personalities.

The official site's production-color photograph was inspected in the browser. It illustrates the separation of clean linework and controlled filled-color regions; it is process evidence, not a visual style to copy.

### Cel shading is built from deliberate shadow shapes

[Animator Nicca's tutorial published by CLIP STUDIO](https://www.clipstudio.net/how-to-draw/archives/162911) describes cel shading as simple unblended shading, demonstrates defining shadow edges, and recommends restraint with airbrush additions. Its optional diffusion/glow section is not a requirement. For our sprites: choose a clear base, a main shadow and a small secondary accent when necessary; keep hair and cloth edges legible. Add soft transitions only where they help form, not across every surface. These color-count limits are project choices, not universal anime rules.

### Identity needs silhouette and specific features

[CLIP STUDIO's character-design guide](https://www.clipstudio.net/en/characterart/beginners-guide/) discusses silhouette, consistent color themes and distinctive characteristics. For our cast, lock each hairstyle's outer contour, eye shape, brows and facial proportions before expression variants. Use the profile's glasses, mole, ponytail, posture and clothes as secondary identifiers.

### Contemporary school-romance comparison

The [official Tsuki ga Kirei character page](https://tsukigakirei.jp/charactor/) was inspected visually in the browser, including its student character selector and a female full-body model. Our observations: readable hair silhouettes, economical internal detail, bounded shadow regions and ordinary school clothing. Use these as evidence that visual clarity survives simplification. Do not copy its cast, uniforms, palette or exact line style. Its restrained production models are a process comparison; the user's later illustration requests a more finished, high-definition illustration treatment.

## The user's new rendering reference

Local source: `C:/Users/media/AppData/Local/Temp/codex-clipboard-00256f03-7efb-40e6-8250-a5222ad32bcd.jpg`.

Observed qualities: hair organized into broad flowing locks; only a few lines describing each plane; confident facial contours; clearly separated upper lashes, iris and pupil; skin largely clean with controlled warm blush; sharp shadow shapes with a few localized soft transitions. Light accents follow form. The strong rim light and sparkle effects are not needed on neutral dialogue sprites. Do not transfer its face, hairstyle, bow, eye color or costume onto our original characters.

## Rendering contract for replacements

| Area | Use | Reject |
|---|---|---|
| Hair | Large and medium designed locks, a few small silhouette accents; coherent part and hairline | Hundreds of fine strands, spaghetti curls, evenly spaced etched highlight lines |
| Hair paint | One clear main shadow shape; one broad restrained highlight family; localized light transitions | Metallic reflections, silver thread texture, every strand lit separately, grey airbrush haze |
| Face | Clear lid/iris/pupil separation; small nose mark; intentional jaw and cheek shapes | Doll-like identical faces, oily skin, sculpted plastic noses/lips, photographic pores |
| Eyes | Distinct contours per girl; limited crisp catchlights; legible pupils | Gemstone irises packed with random glitter and concentric detail |
| Skin | Calm base, economical shadow under bangs/chin, light expression-specific blush | A blush mask on every expression, glossy lips, broad airbrush modeling |
| Cloth | Folds at actual tension/compression points; matte uniform fabric | Satin-like blazer highlights, dozens of arbitrary micro-creases |
| Light | Neutral consistent sprite light; illustrated room light supplies context | Baked sunset rim light on every asset, glowing halos, bloom over linework |
| Backgrounds | Believable scale, useful objects, clear foreground/midground, consistent room materials | Overdecorated academy interiors, repetitive copy-pasted windows, unnecessary particles |
| Expression | Actual acting through eye/brow/mouth relationships, preserve identity | Repeating one smile with slightly different blush intensity |

## Face differentiation

- Katya: longer face, straighter sharp upper lids, slightly narrower ice-blue eyes, precise brows, controlled mouth. Long silver hair uses broad quiet planes rather than wispy strands.
- Akira: shorter rounded face, energetic arched brows, rounder brown eyes behind thin glasses, mobile mouth. Short pink bob has a clear rounded silhouette.
- Seo-yun: oval face, gently tapered brown eyes, softer brows, small mole under her left eye. Long dark hair remains organized rather than tousled into dozens of flyaways.
- Mari: softly elongated face, gentle lower-lid rhythm, calm cyan eyes, relaxed mouth. Salmon low ponytail is drawn as a few feathered locks, not a mass of fine curls.
- Svea: youthful feminine face, soft jaw rather than a broad angular male jaw, calm narrow blue-grey eyes, understated lashes, blunt expression. Tomboy identity stays in haircut, posture, clothes and behavior.

## Quality gate before resuming the pack

1. Generate a single high-resolution replacement portrait from the new rendering reference and the written profile, without using the rejected cast image.
2. Inspect eyes, hair shapes, face clarity, uniform materials and unwanted gloss at normal size and close range.
3. If those pass, establish replacement individual models and a coherent five-girl sheet.
4. Only then generate expression variants, exploration poses and CGs. Review every output; do not mistake a grid of nearly identical faces for finished acting.
5. Record prompts and source paths, keep raw masters, and distinguish final deliverables from rejected studies. Do not call a partial or unreviewed pack complete.

Current state: research complete; corrected Svea rendering proof saved as `Documentation/Art/svea-rendering-master-v2.png`. The user then redirected work to finish the screenplay first. The full writing milestone is now in `Narrative/Screenplay`; no runtime game or final complete art pack has been delivered yet.
