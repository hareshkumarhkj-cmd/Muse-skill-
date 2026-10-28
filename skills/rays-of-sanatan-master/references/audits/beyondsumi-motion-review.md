# Beyondsumi — visual, story, motion and code review

## Source and scope

Read-only inspection; no bundled scripts, installers, tests or code were run.
Repository: https://github.com/beyondtahir/beyondsumi
Exact inspected commit: `43bf2094a5874d315a6148f64c6f10b4d9651777`.
The repository's plugin.json and main SKILL.md identify **1.0.1**, while the user's
uploaded filename says **beyondsumi-v1.0.0.zip**. The ZIP remains inaccessible
under the 32 MiB transfer limit. This report reviews that public source commit,
not a proven byte-for-byte match to the uploaded archive. Do not conceal this
version/evidence distinction.

The root license is MIT (copyright 2026 Beyondsumi contributors), with adjacent
notices for bundled original audio/third-party materials. Preserve its license
and copyright if copying substantial code/text; do not assume provider outputs
or third-party audio receive the repository's license. The recommended master
skill should mostly use independently written instructions and a fresh schema.

## What is valuable for Rays

### 1. Scene-first direction rather than assembling random pictures

`skills/sumi/references/scene-first-workflow.md` is the strongest reusable idea.
It plans what the viewer must understand before finished artwork: causal story,
preliminary geography/camera, actual narration timing, storyboard, rough timed
animatic, layout, then integrated masters and motion sources. A scene table alone
does not prove the sequence works.

Adopt for Rays: every shot names its purpose, source-grounded claim or folklore
status, opening/closing visual state, audio phrase, exact frame interval, supported
camera view, dominant motion, caption clearance and transition. Establish whether
a shot is an actual source view, fictional reconstruction, diagram or metaphor.
Use the temple's plausible structural geometry and authentic iconography only
when supported; a beautiful AI frame is not archaeological evidence.

### 2. Compose complete shots, derive layers second

The source explicitly says unrelated generated people/backgrounds do not become
integrated simply by compositing. It requires a common shot master with shared
perspective, scale, light, grounded support, shadows and occlusion. Derivatives
retain parent source/hash/registration and clean plates for exposed areas.

Adopt for Rays: generate a coherent temple/workers/rope/stones master before
cutouts. Extract foregrounds and masks only when needed for the planned move.
Keep original sources and a crop/registration map. Do not mistake a zoomed crop
for a new camera angle; a real orbit or reveal needs a 3D scene or matching motion
footage/new coherent views. Code must not promise unseen side/back geometry from
one flat image.

### 3. Make continuity explicit

`production-continuity.md` tracks incoming state, visible action/contact and
outgoing state. It covers hand/side, object ownership/orientation, clothing,
knowledge, route, consequences and eyelines. It rejects repeated or reset events
just to reuse artwork.

Adopt a lightweight Rays continuity ledger: stone/rope positions, number and
orientation of workers, deity attributes, jewelry, crown, costume, temple geometry,
light direction, camera axis, transition into next shot and narrative fact state.
A boulder cannot teleport to a new load-bearing position without a readable cut
or movement; an object cannot remain in both hands and on the floor.

### 4. Plan the hardest motion before bulk generation

`action-pose-sheets.md`, `physics-and-review.md` and `motion-detail.md` correctly
separate real source drawings, derived states, reused exposures and output frames.
They require connected anticipation/action/contact/reaction/settling, matching
whole poses, registration and normal-speed playback. A single standing figure
translated sideways is not a walk; camera/weather cannot replace body action.

Adopt for Rays: if the requested scene includes workers pulling ropes or a stone
swinging, prove a bounded 3–6 second representative action with genuine motion
assets or a real 3D implementation before calling a full batch. For a gesture,
use matched source poses only when identity/contact continuity is actually good.
Do not expose the user to arbitrary frame-state counts as a quality promise.
No quantity of repeated stills establishes high-end motion.

### 5. One deterministic event ledger

The source coordinates visible contact, prop state, reaction, particles, narration,
SFX and cuts through an output-frame event ledger. Its code guidance discourages
independently typed approximate timestamps and history-dependent simulation.

Adopt: a single scene/event data module derives Sequences, captions, cue onsets
and duration. World/camera/text spaces stay separate. Absolute frame evaluation
must return the same state when seeking forward or backward. Cache any simulated
trajectories from fixed initial conditions. Keep attached ropes/props/shadows
under the same transform hierarchy.

### 6. Local living environment, tied to actual sources

`living-environments.md` requires animate/still with a story reason per shot,
source-space masks, rigid holdouts and matching clean plates for moving clouds.
A common seeded driver links a flame to its light/reflection; effects respect
world wind, depth and occlusion. It explicitly rejects full-picture pulsing,
warping architecture and palette cycling. It also requires environmental change
to be visible at actual display size and normal speed, not merely a pixel diff.

Adopt for Rays: coherent temple dust/light shafts, restrained fog, source-linked
lamp glow and bounded particles where appropriate. Protect faces, text, rigid
stone and rope anchors. Do not add global wobble to suggest motion or inflate
quality through constant effects. A deliberate locked shot can be valid.

### 7. Review actual movement and encoded output

`production-standard.md` and `physics-and-review.md` distinguish metadata/validators
from visual approval. They call for normal-speed playback and adjacent frames
around contacts rather than only seconds-apart contact sheets. They retain
reviewed file hashes and invalidate affected review after timing/source changes.

Adopt: inspect beginning/middle/end, every cut, and action/event windows around
n−6, n−3, n−1, n, n+1, n+3, n+6 when relevant. Check rigid architecture, identity,
hand/rope contact, generated extra limbs, scale, captions and audio clarity.
Record listening unavailable if it was unavailable; meters cannot certify a
Hindi voice's pronunciation, acting or mix. User acceptance and agent review
must remain different statuses. Avoid 'perfect' or 'zero errors' claims.

## What should NOT become the Rays default

1. **Japanese ink identity.** All three source styles are explicitly Sumi-e or
   wet-brush/ink. Original is painted Sumi Anime, Light has luminous paper/mineral
   washes, Dark has broad splash masses and selective red. Rays needs cinematic
   photoreal stone, realistic humans/deities and golden temple light. This is not
   a palette edit of Sumi. Copy its production logic, not its art recipes.

2. **Sumi motion clocks.** Original 30fps/20 designed character states and
   Light/Dark 24fps/on-twos are specific style policies. The user's Rays contract
   is 30fps, 1080x1920. Do not impose 24fps, 20Hz acting, or a mandatory 24-drawing
   setting on photoreal footage. A video model's coherent motion and real source
   cadence matter more than a metadata target. Source counts are not call counts.

3. **Compulsory three-edition dashboard.** Source delivery asks for all three
   edition cards and a branded watch/download page. Rays handoff is one selected
   composition, source ZIP, MP4/QC when rendered, and four concise handoff fields.
   A dashboard is optional and must not replace actual downloadable files.

4. **Provider/paid-call coupling.** The source can route to ElevenLabs, Voicebox,
   recording or no narration; neither service nor account entitlement is part of
   a generic skill. A name in a manifest is not a callable provider. For Rays,
   discover actual TTS/image/video/listening/alignment capabilities separately.
   Do not call provider code, use credits, install a model or upload work merely
   because a reference document shows a command. Existing user authorization
   governs the scope; do not copy its repeated approval prompts mechanically.

5. **No-AI-label instruction.** The Sumi SKILL says not to add visible AI labels.
   The current Rays brief uses fictional/AI reconstruction disclosures. Preserve
   the actual user's disclosure decision and relevant platform requirements;
   do not inherit Sumi's branding/disclosure policy as a higher-priority rule.

6. **Default music despite silent-proof contract.** Source sound rules treat
   missing music/SFX as unfinished except explicit silence. The Rays user has
   approved silent visual proofs and restricted unsupplied audio. Keep these
   modes separate from a final narrated Short; do not silently synthesize music
   or claim a voice exists because Sumi can route to a speech provider.

## Actual code and dependence checks

### Bundled Remotion starter

Inspected `skills/sumi/assets/remotion-starter/package.json`, `src/index.tsx`,
`src/Film.tsx`, `src/components.tsx`, and the initializer script.

- Remotion and CLI are pinned to **4.0.516**, React/DOM **19.2.3**, TypeScript
  **5.9.3**. Rays currently requests around **4.0.529**. Upgrade all Remotion
  packages together only with actual validation; do not copy an older lockfile
  and claim it was validated at the newer version.
- Entry is `src/index.tsx`, composition is **Film**, and the initializer creates
  a generic **engine check**, not a story. The user requires `src/index.ts` /
  RemotionRoot and a clearly named single Rays composition. Write a matching
  fresh starter or adapt/test all commands consistently.
- `npm run render` invokes a **Python** preflight before CLI rendering. A
  Node-only host cannot run that script without Python. The requested bare
  `npx remotion render` may bypass that npm preflight. Integrate required checks
  into the actual documented workflow, and disclose Python/FFmpeg prerequisites
  separately from the generated project's Node rendering requirements.
- Initializer copies several validators, motion assets and recursively linked
  references. Partial copying can break imports (`sumi_catalog`, style/profile,
  plan provenance, physics, environment, motion detail). Do not ship a single
  borrowed validator without its dependency closure.
- Initializer explicitly refuses existing destination, a good protection against
  accidental overwrite. Preserve user files and reuse valid assets.
- It writes `sound-tools/library-location.json` with a runtime absolute path to
  the installed skill's bundled sound bank, then excludes that bank from the
  copied project. This may be valid in its local studio, but a fresh handoff to
  another host must remove that path dependency and bundle permitted used audio
  under public/ or use explicit silence. Do not assume copying the initializer
  output alone is a self-contained final film.
- `AssetLayer` computes pure frame-derived transforms with clamped smooth
  interpolation and groups children under the same parent. This is a good
  attachment mechanism, but it is a planar layer transform, not character acting
  or 3D view synthesis. It holds outside its motion window unless a Sequence
  bounds its lifetime.
- CaptionTrack selects whole-string cues on [start,end), supports RTL and
  user-supplied fonts, and avoids per-letter shaping damage. Its default font
  alone does not establish Hindi support on a different host. Load a permitted,
  licensed Devanagari-capable font and inspect final glyphs.
- `useLocalFont` uses the browser FontFace API plus render delay/error handling.
  This is reasonable source logic; this review did not run its typecheck or
  Strict Mode behavior, so no test pass is asserted here.

### Motion/environment implementation

Inspected `assets/motion-core/motion-core.mjs`, `environment-canvas.mjs`,
`living-frame-canvas.mjs` and relevant validator portions.

- motion-core provides deterministic numerical helpers: gait foot anchors,
  two-link IK with reach failure, hierarchy transforms, ballistic/release and
  sampled contacts. Its own header explicitly says it is **not a human body,
  cloth, fluid or rigid-body physics engine**. It is not a turnkey cinematic
  photoreal 3D asset system.
- living-frame-canvas supports authored **hair/cloth/breath** patch deformation.
  It explicitly rejects other behaviors and calls for checked expression art
  or rigs for faces. It does not recognize anatomy or segment images.
- Environment adapter is a Canvas compositor over authored bounds/masks/layers,
  plus particles, gradients and bounded resampling. It does not infer hidden
  surfaces, discover automatic light geometry, reconstruct 3D temples, or
  generate coherent new camera perspective. Clean plates and masks must exist.
- Validators check declared schema, file presence/sha256, timing, bounds,
  provenance and supplied review records. They cannot determine whether the
  visual looks cinematic or whether a self-reported true flag is honest. A
  validation pass must not be presented as independent artistic certification.
- `validate_shot_plan.py` enforces identity `japanese-sumi` and its style catalogue;
  environment validation enforces Sumi-specific fps and palette. These cannot be
  reused unmodified as a generic Rays gate.

## Recommended original Rays architecture

Use one compact `SKILL.md` routing to independently written references:
capability gate → channel DNA/fact rules → script and final-voice alignment →
shot bible/continuity → tool-specific artwork and actual-motion branch →
Remotion implementation → audio/caption QC → delivery.

Asset routes must be honestly labeled:

- **Cinematic still-motion:** images + restrained camera/parallax/local effects.
- **Generated/supplied motion footage:** genuine moving scene clips, assembled
  and timed in Remotion, with action/identity/geometry checks.
- **3D/code scene:** authored 3D assets, lighting, camera, rigging and animation;
  more technical and computational scope, not a promise hidden in a skill.

For high-end Rays, default to coherent shot direction and correct technical
handoff, never claim the still-motion fallback equals the reference's generated
motion. Prove the selected route's hardest representative shot before scaling.
Use a fresh light scene/event manifest and portable validator focused on the
user's 30fps/9:16/one-composition/local-asset contract, rather than inheriting
Sumi's entire versioned engine/catalogue.
