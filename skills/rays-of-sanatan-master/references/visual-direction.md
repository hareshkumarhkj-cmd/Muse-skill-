# Cinematic visual direction and motion

## Art bible before prompts

Define subject, era/fictional status, architectural vocabulary, character
descriptors, wardrobe, materials, palette, lighting direction, camera grammar
and excluded elements. Reference boards must use authorized materials; never
strip another channel's watermark or present its art as newly created.

Use these as variables, not magic words repeated without inspection:

```text
Purpose: [what this shot communicates]
Originality / status: [fictional reconstruction or sourced setting]
Subject lock: [character identity or architectural motif]
Action: [one specific action, or still pose]
Composition: [shot size, angle, focal point, scale, caption negative space]
Materials / light: [coherent palette, textures, light direction]
Motion: [camera path and/or actor action; identify still vs motion output]
Continuity: [reference asset IDs and supported conditioning]
Exclusions: text/logos/watermarks, duplicate limbs, implausible anatomy,
incompatible ornaments, unrequested modern objects
```

Resolve every bracket before generation. Keep the actual prompts alongside
the chosen output IDs and model/version when known; never invent a seed/model.
Ask the image tool for captions separately in editing, not text baked into art.

## Shot grammar

- Hook: an instantly legible scale, expression, object or puzzle. Large subject,
  no busy collage, question answerable by the next shots.
- Reveal: a meaningful new view/detail. If showing an interlock, the seam must
  be visible. Technical overlays should follow the object and explain something.
- Climax: a wide contextual/emotional payoff, not an unrelated brighter image.
- End: preserve visual continuity, leave enough reading time, retain disclosure.

Use low angle for scale, close detail for mechanism, wide view for context.
Avoid four almost identical hero images or arbitrary cuts every half second.

## Generate, compare, repair

Check each actual asset at useful resolution before coding: faces/hands,
ornaments, perspective, surfaces, readable silhouette, light continuity,
unwanted text/logo, cropped head/feet, contradictory geometry and resemblance
to a real monument where the claim is fictional. Reject or repair bad shots.
Reference conditioning and approved keyframes help consistency where available;
identical prompt wording alone does not lock a face.

## Declare the motion mode

| Mode | Appropriate use | Cannot be claimed |
| --- | --- | --- |
| Still-motion | Camera crop, slow push/pan, modest graphic highlight | New body motion, real orbit, moving cloth/liquid |
| Layered parallax | Separate licensed/original layers with limited displacement | Hidden geometry that was never created |
| Motion clips | Walking, ropes, gestures, pouring, camera viewpoint change | Perfect temporal identity/physics without reviewing frames |
| True 3D | Deliberate geometry, lights, rigs and simulations | Historical accuracy merely because the render is realistic |

For stills start around 1.02–1.12 scale over 3–5 seconds. It is a design range,
not a requirement: inspect crop loss. No fake mouth movement or wobbling faces.
For full motion inspect intermediate frames for morphing, impossible contact,
flicker, identity drift and camera discontinuities; a beautiful first frame is
not enough. Never label an image-to-video model's output a physical simulation.

## Mobile design

Design on the actual 1080x1920 canvas. Start with about 72px side margins,
130px top clearance and 240–300px bottom clearance for important copy, then
inspect the intended player UI; platform overlays vary, so no universal safe
area guarantee. Keep captions away from faces/important joins and no more than
two short lines. At final resolution start around 64–82px for primary Hindi
captions and tune by reading at phone scale. Preserve Devanagari marks with
adequate line-height (about 1.35–1.5) and font ascent space.

Use consistent contrast and a controlled dark gradient/outline as needed.
Do not cover 40% of a key image with decoration. Add dust, glow and sound cues
only when they serve scale, atmosphere or the reveal; restraint is part of polish.
