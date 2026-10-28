# Beyondsumi source review for the Rays of Sanatan master skill

Reviewed read-only on 2026-10-28. Source repository:
https://github.com/beyondtahir/beyondsumi

Exact inspected commit: `43bf2094a5874d315a6148f64c6f10b4d9651777`.
Local checkout: `/workspace/skill-review-sources/beyondsumi`.

The uploaded `beyondsumi-v1.0.0.zip` could not be opened because it exceeds the
32 MiB transfer limit. This review concerns the GitHub source above, whose core
`SKILL.md` identifies itself as **Version 1.0.1**. It does not establish that this
checkout is byte-identical to the uploaded release. No repository code, tests,
installer, app, speech model or paid provider call was executed.

## Scope actually read

- Root `LICENSE`, `THIRD-PARTY.md`, `COMPATIBILITY.md`.
- `skills/sumi/SKILL.md`.
- Core references `narration.md`, `supplied-narration.md`, `script-duration.md`,
  `sound-routing.md`, `hooks-endings-sound.md`, `image-capabilities.md`, and the
  relevant production-standard material.
- `skills/sumi-voicebox/SKILL.md`, `references/setup.md`, `scripts/probe.py`.
- `skills/sumi-elevenlabs/SKILL.md`, `references/setup.md`, and relevant portions
  of `scripts/elevenlabs_voice.py` including credential routing, network calls,
  model restrictions, timing conversion, receipts and error handling.
- `skills/sumi/assets/sound-library/route_sound.py`, relevant `library.py`
  functions, original-audio notice, procedural-audio license/material generator.
- Test source in `tests/test_first_run_companions.py`,
  `tests/test_sound_routing.py`, `skills/sumi/scripts/test_material_audio.py`,
  and `skills/sumi/scripts/test_sound_library.py`.

Links below use the exact inspected commit rather than a moving main branch.

## The useful system behind the documentation

This is a **Japanese Sumi film-production suite**, not a generic prompt that
magically supplies image, video and speech models. Its core separates story,
direction, artwork preparation, real narration timing, animation, sound and
review. Four authored skill folders provide core Sumi, SVG, ElevenLabs and
Voicebox routes. The portable Rays skill should take the production discipline,
not inherit the Japanese artistic identity or provider assumptions.

### 1. Preserve the real script and recording

The [duration contract](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi/references/script-duration.md)
separates approved spoken wording, required visible text and causal visual
beats. A requested runtime does not authorize silently deleting any of these.
It estimates the complete cut before expensive media, distinguishes estimates
from real duration, then checks the actual generated/recorded take.

The [supplied-recording workflow](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi/references/supplied-narration.md)
distinguishes a complete narration recording from a voice sample. It keeps
original bytes and the actual words/performance; a narration upload does not
automatically authorize voice cloning or sending the recording to a provider.
It explicitly discloses missing listening/transcription capabilities.

**Adopt:** real-take timing, untouched originals, content preservation and an
explicit scope decision only for a material unresolved runtime conflict.
**Adapt:** Rays already has a 10–15-second first-test requirement and a fixed
scene table; do not ask duration/style again when those choices are known.

### 2. Narration, music and effects are independent capabilities

The [narration router](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi/references/narration.md)
offers ElevenLabs, local Voicebox, supplied recording or none. It states that
assistant writing-language ability and the speech engine's language support
are separate. Voicebox is not automatically a music or foley generator.

**Adopt:** independent capability records and independent route selection.
**Adapt:** do not force users to pick the same menu in every future job; reuse
their actual authorized choices. An original Rays voice should be selected
for Hindi pronunciation and audition quality, not because a model name is
popular. Missing narration cannot be called a completed narrated final.

### 3. Local Voicebox route is an optional app with real prerequisites

The [Voicebox companion](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi-voicebox/SKILL.md)
and its setup guide point to `jamiepine/voicebox`. They distinguish desktop
releases from source builds and the app license from each chosen model's terms.
They discuss OS, CPU/GPU, RAM, free storage, cached models and language support.
The guide source-reports Hindi for Chatterbox Multilingual, while noting that
the listed Qwen languages do not include Hindi/Urdu. Those specific versions,
sizes and language claims need fresh upstream verification at use time.

The [read-only probe](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi-voicebox/scripts/probe.py)
only GETs `/models/status` and `/openapi.json` on a validated loopback port,
default 17493. It blocks redirects, caps metadata size, filters returned model
fields, sets a short timeout, and reports that it started no generation or
download. It is not a synthesis endpoint implementation or a working voice test.

**Adopt:** read-only status/schema probes, language checks and a two-line actual
pronunciation audition before long generation.
**Avoid:** claiming “free voiceover works anywhere without a key” merely because
the companion exists. Local compute/model downloads and appropriate licensing
still matter. Do not expose a local speech backend publicly.

### 4. ElevenLabs adapter is careful but deliberately limited

The [Python helper](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi-elevenlabs/scripts/elevenlabs_voice.py)
is a stdlib HTTP/MCP adapter, not a hosted service. It reads a configured
`ELEVENLABS_API_KEY` or macOS Keychain; secure persistent storage on other OSes
is left to the host. It prevents credential forwarding on redirects, verifies
available model/voice IDs through read-only calls, retains pagination, filters
response fields and bounds response size.

Before a take it creates a fresh job directory and atomically writes a receipt.
After a request it saves audio, original/normalized alignment, script and
provider IDs. An interrupted paid POST can be marked `outcome_unknown`; no
automatic retry is performed. Last timed text is expressly not equated with
full decoded MP3 duration.

Important concrete limitations:

- It generates via `/v1/text-to-speech/{voice}/with-timestamps` with
  `mp3_44100_128`, not a universal TTS endpoint.
- `generate_narration` expressly rejects `eleven_v4` and `eleven_v4_turbo`
  because those need a separately verified Text-to-Dialogue adapter. The setup
  guide's discussion of models is broader than the bundled helper's support.
- Approval/cost scope for TTS is largely a host/instruction responsibility;
  the helper does not make possession of a key equivalent to permission.
- Model/voice quality and account permission are not established by installing
  this adapter. It does not include a provider account or free credits.
- Its subtitle punctuation expression recognizes `. ! ? 。 ！ ？`, but omits
  Hindi danda `।`/`॥` and Urdu `؟`. Reusing that segmenter unchanged for Rays
  would lose some natural Hindi sentence boundaries. Its 72-character/6-second
  caption rules also need adjustment for vertical Hindi text and real font widths.
- It validates alignment array lengths, finite nonnegative times and monotonic
  starts, but actual decoded-audio bounds and perceptual alignment still need
  an independent check. It does not manufacture cues when alignment is absent.

**Adopt:** receipts, actual IDs, no uncertain paid retries, private source takes,
alignment provenance and no fabricated subtitles.
**Adapt:** native Hindi-aware segmentation, pronunciation lexicon, actual-audio
bounds and engine-neutral capability routing. Keep credentials and private
receipts out of a public reusable skill/project.

### 5. Sound routing and review bind to actual files

The [sound router](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi/assets/sound-library/route_sound.py)
uses library-first or Python-only. It checks safe cue IDs and source hashes,
preserves prior outputs, deep-copies the plan and records each selected route.
With an attested paid-SFX capability and missing cue, it can write
`NEXT-ACTIONS.json` and exit without making a provider call. Python-only does
not inspect the private/provider bank. Unknown materials fail rather than
becoming a random generic whoosh. Synthesized effects retain seeds/design hashes.

The [mixer/library](https://github.com/beyondtahir/beyondsumi/blob/43bf2094a5874d315a6148f64c6f10b4d9651777/skills/sumi/assets/sound-library/library.py)
uses 48 kHz stereo and fixed output-frame clocks. It keeps music, ambience and
SFX buses, contact anchors, preroll and full tails. It rejects out-of-film cue
tails or negative preroll, gates pending listening/contact/loop review unless
making an explicitly labelled review draft, and uses duck envelopes that recover
without multiplying overlapping reductions. Stem balance is preserved with
shared attenuation. Its report explicitly says `listening_reviewed: false` and
`loudness_true_peak_measured: false`.

**Adopt:** event-ledger synchronization, source hashes, stems, actual contact
anchors/tails and honest distinction between meters and sensory review.
**Adapt:** final LUFS/true-peak analysis on the final encoded mix, and all selected
delivery audio copied into `public/` with relative paths. The source library's
peak/RMS statistics and default sample ceiling are not integrated LUFS/dBTP.

Portability caveats: the source explicitly keeps a roughly 224 MB shared original
music bank outside each film, with `library-location.json`/selected cache paths
or regeneration on a new machine. That may suit a local studio but **cannot be
an unresolved dependency in the user's self-contained Muse ZIP**. Do not copy
the whole bank unnecessarily; bundle only actual selected legally usable assets
or a tested dependency-free rebuild step. The mixer also has an explicit
180-second section-duration limit; do not assume unlimited long-form support.

### 6. Test source shows specific contracts, not artistic certification

The inspected tests cover read-only first use, capability evidence, nonsecret
preferences, loopback-only metadata, backup-preserving installation, safe SVG,
hash-bound reuse, no provider calls in Python-only mode, pending-audition
gates, exact sample counts, safe paths, no overwrite, seed reproducibility,
duck recovery, sound-contact timing and paid-generation uncertainty handling.

These are meaningful software contracts. They do not demonstrate high-end
Hindi pronunciation, realistic foley, a moving cinematic character, or a new
complete film on every assistant platform. `COMPATIBILITY.md` appropriately
distinguishes folder/first-use checks from native discovery and full-film tests;
it source-reports 39 setup/memory/routing tests passed while leaving many
platform/native-generation rows pending. This review did not rerun those tests.

## Do not carry these Sumi-specific rules into Rays unchanged

1. Japanese ink/anime artwork, Original/Light/Dark style menus and source
   16:9/24 fps defaults. Rays defaults are cinematic Indian subject matter,
   1080x1920, 30 fps, exact approved scene table.
2. 12/20/24 designed-state/drawing-rate targets as a blanket badge of quality.
   They need real prepared poses and review. Camera movement or a crop is not
   a new camera angle/character action; keep that excellent distinction.
3. Requiring a non-silent soundtrack even for an explicitly silent proof. The
   current user's direct audio restrictions take precedence over source defaults.
4. The blanket instruction to exclude visible AI-generated labels. Rays needs
   honest documentary/reconstruction attribution; follow the actual approved
   brief/platform requirements, not a borrowed prohibition on disclosure.
5. Beyondsumi branding/dashboard, three film editions or repeated technical
   choices. These are source product UX, not portable Rays requirements.
6. Asking again for every setting/budget already selected. Preserve concrete
   existing authorization; ask only for genuine missing external prerequisites
   or materially changed content/cost scope.
7. A supplied reference recording as a free reusable stock voice/music pack.
   Study production qualities without redistributing its artwork or audio.

## Licensing and attribution

Root code/docs are MIT, copyright 2026 Beyondsumi contributors, requiring the
notice with copies/substantial portions. The procedural-audio kit has an
adjacent MIT notice crediting whaleyxbt. Original Sumi Python music/audio has a
separate permissive notice requiring retention for source/library redistribution
and expressly excludes provider outputs, voice recordings and imported assets.

`THIRD-PARTY.md` says demo films are examples, not stock voice/effect licenses;
no provider voice/effect output is relicensed by the repository. Voicebox/model,
Remotion/React/TypeScript and browser/FFmpeg licenses remain separate.

For the Rays skill, prefer original implementation of these general production
principles. If substantial source text/code or audio is copied, preserve the
correct adjacent notices and document exactly what was reused. Do not bundle
the reference films, private bank, models or provider helper merely for branding.

## Bottom line for the original master skill

Adopt the **separation of capabilities, measured-take timing, receipts,
event-ledger continuity, hash-bound assets and honest sensory QC**. Add a
Rays-specific research/claim ledger, Hindi pronunciation and punctuation checks,
cinematic image/shot bible, portrait-safe caption layouts, frozen local media,
explicit still-motion versus true-action evidence, and a no-manual-step verified
Remotion handoff. None of these instructions alone creates an image/TTS engine
or guarantees identical performance across hosts.
