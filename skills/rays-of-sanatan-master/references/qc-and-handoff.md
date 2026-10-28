# Production gates and handoff

## Measurable gates

1. **Brief parity:** correct topic, language, original/source permission,
   duration, aspect, fps, motion mode and audio state. One exact scene table.
2. **Truth:** material claims have inspected sources or clearly attributed
   tradition/fiction. Unsupported real-world claims are removed or qualified.
3. **Design:** intentional focal subject and depth; consistent characters,
   costumes, lighting and geometry; no unwanted text/logos, malformed hands,
   morphing faces or contradictory shot geography. Read Hindi at phone scale.
4. **Timing:** scenes contiguous with no accidental overlaps/gaps; actual
   narration fits; speech is not truncated; changes occur for a story reason.
5. **Audio:** required voice actually exists and decodes; content/pronunciation
   reviewed as capability allows; measured sync and output levels; no unsupported
   claims that a waveform or successful render proves naturalness.
6. **Implementation:** install and typecheck pass; runtime lists exactly one
   correctly named composition; the advertised render fully completes.
7. **Output:** fresh MP4 metadata matches; decode and inspect frames at start,
   middle, end and before/at/after EVERY scene boundary, plus motion intermediates.
   Listen to the FULL final mix when possible. Record unrun checks honestly.
8. **Packaging/delivery:** assets and licenses local; contract hashes match;
   clean ZIP integrity; no dependencies/outputs/credentials; working download
   route or explicitly unverified delivery, with no invented artifact ID.

For a first proof aim for a coherent design rather than an overflowing effects
stack. Do not expand to a series until the short test passes its agreed gates.
If a required gate fails, fix what is fixable and name the precise remaining
blocker. Never “pass” a narrated final by silently changing it to a silent proof.

## Actual output inspection

Use ffprobe/FFmpeg if present. The bundled verify_render.py runs a bounded
metadata/frame-count check against the contract; it is not perceptual inspection.
Fail on a missing audio stream in a voiced job or a mismatch in frames/fps/size.
Metadata duration tolerances are bounded by one frame; large drift is a failure.

Baseline phone QC: no clipped Devanagari marks, safe reading holds, no captions
over faces/mechanisms, no platform UI collisions at intended viewing size,
no unexpected black/flash frames at cuts. Don't certify all frames after only
three stills; report the actual sampling coverage.

## Required project content

- package.json + lockfile, remotion.config.ts, src/index.ts and scene code;
- public/ with ACTUAL used media/fonts and licenses;
- production-contract.json, TASK.md, README.txt, TEST-NOTE.txt;
- relevant claims/asset provenance and real test evidence, including full errors.

TASK.md: one-line goal; composition; duration/size/fps; exact run commands;
expected output. README.txt: short specs and actual audio yes/no/state.
TEST-NOTE.txt: commands, environment versions, actual pass/fail/unrun evidence,
error logs/fixes and material limits. No promise of a Muse test that didn't occur.

ZIP excludes node_modules, .git, out, dist, build caches, .env files, private
keys, unrelated source/client files and unreviewed nested archives. Human review
remains necessary: basic secret-pattern scans are not comprehensive. Keep MP4
preview and QC stills separate so the source ZIP remains small.

## Reliable handoff

Never manufacture sandbox: links to files the host cannot expose. Use the
actual host's artifact facility and test it when possible. If GitHub is the
authorized route, use a dedicated package path, preserve unrelated repo content,
commit/push the artifact and verify the remote SHA. A push is not a download test;
private repository access may still block Muse. Do not leak local logs/secrets.

Give four short handoff facts: topic; duration/size/fps; composition; audio state.
Explain any material limitation, such as still-motion rather than full-motion,
briefly. Include reliable links, not guarantees of another agent's execution.
