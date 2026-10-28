# Deep source review and adaptation decisions

Reviewed 2026-10-28, read-only, using the user's source repository links.
The uploaded archives could not be transferred; source-version parity is unknown.

## BeyondArtist

Source: https://github.com/beyondtahir/beyondartist/tree/0e4cc115613e37743d959801b5d93be40264ef2b

It is an image-led art-direction system for thumbnails, posts and carousels.
We inspected canonical skill/README, strategy/intake/handoff/critique/memory
references, retrieval/memory/package implementations, test code and licenses,
with representative library records. It is not a TTS/video engine.

| Actual strength | Rays adaptation |
| --- | --- |
| Designer and artist responsibilities | Separate message/craft critique; agents only if available |
| Source-ID → lesson → decision → visible check | Compact reference-to-decision record |
| Artist interpretation, hierarchy, material fidelity | Original direction; reject generic or wrong-medium art |
| Full/phone-size pixel inspection | Read Hindi and composition at phone scale |
| Scoped memory, draft/approved/rejected distinction | User-controlled channel bible and episode decisions |
| Capability-aware creation | Actual assets, not prompts presented as generated images |

Not imported: its large design corpus, gallery/source art, branding, mandatory
Pinterest route, two-deliverable thumbnail default, private memory or installer.
Detailed evidence: [BeyondArtist audit](audits/beyondartist-review.md).

## Beyondsumi

Source: https://github.com/beyondtahir/beyondsumi/tree/43bf2094a5874d315a6148f64c6f10b4d9651777

It is a guided Japanese ink-animation studio with a Remotion starter, local
sound tooling and optional narration companions. We inspected core workflows,
motion/continuity, narration/supplied-recording/script-duration/sound routing,
provider adapters, implementation/test source and notices. No upstream code ran.

| Actual strength | Rays adaptation |
| --- | --- |
| Scene-first master before layers | Coordinate camera, scale, light and occlusion |
| Hard representative action before batch | Prove actual difficult motion before scaling |
| Prop/knowledge/consequence continuity | Single frame-based contact/event ledger |
| Preserve recording; actual-take timing | Measure final narration before captions |
| Separate voice/music/SFX | Original local stems, contact anchors and ducking |
| Audio hashes/listening state | Bind QC to current files; mark unheard audio unverified |
| Receipts/pending-result handling | Private take IDs; no blind retry of possibly billed calls |

Important mismatches and code-level cautions:

- Original/Light/Dark are ink aesthetics, not a photoreal temple pipeline.
  Style clocks and 16:9/24fps defaults are not our vertical 30fps contract.
- Starter is Remotion 4.0.516, Film, index.tsx; Rays uses tested 4.0.529,
  RaysShort01, src/index.ts. Our contract is not its Sumi-specific validator.
- Patch motion covers bounded hair/cloth/breath, not automatic character
  video/3D generation. Higher fps does not invent action drawings.
- Shared external sound-bank paths are not portable. Bundle only selected
  authorized files; no reliance on the installer's cache.
- The reviewed subtitle sentence regex lacks Hindi danda/Urdu punctuation.
  Our workflow requires language-aware segmentation, not that copied helper.
- RMS/sample peak fields do not certify LUFS/true peak.
- Voicebox metadata probe does not prove synthesis. The inspected ElevenLabs
  adapter rejects v4 endpoints; don't promise support for every provider model.
- Its no-visible-AI-label and always-audible defaults do not override Rays/user
  disclosure or silent-proof requirements.

Not imported: ink templates, demos, audio bank, SVG art, dashboard, provider
scripts, private takes or third-party procedural kit.
Detailed evidence: [audio audit](audits/beyondsumi-audio-review.md) and
[motion audit](audits/beyondsumi-motion-review.md).

## What this master adds

Hindi fact/tradition/fiction discipline; original Rays cinematic art bible;
capability-aware voice gates; still/full-motion distinctions; simple frame
contract; local asset/hash checks; output metadata checks; clean packaging;
actual test evidence and external-delivery boundaries.

Both upstream workflow/code licenses are MIT with separate asset exceptions.
Full notices are retained under third-party/. No upstream art/audio is reused.
See THIRD-PARTY.md. Source reading does not prove Muse performance.
