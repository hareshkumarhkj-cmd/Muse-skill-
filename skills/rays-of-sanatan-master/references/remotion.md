# Remotion engineering strategy

## Architecture and versions

Keep composition metadata and scene frame boundaries in one data source.
The included example imports `production-contract.json` through a typed
timeline module. Derive Composition and Sequence durations from it; static
contract validation alone does not verify the React tree follows the data.

Use one composition, one root registration, clear scene components and small
shared design primitives. Avoid a 1000-line component or unnecessary dependencies.
Pin remotion, @remotion/cli and every extra @remotion/* package to the same
exact tested release. Example pin: 4.0.529. Pin React/ReactDOM/types/TypeScript
compatibly and include the generated lockfile. Never ship latest-only versions.

No live API generation at render time. Store original local assets under public/,
use staticFile with relative names and load images through Img. Record provenance
and SHA-256; do not embed credentials or personal/Windows asset paths. Media URLs
from dependencies' lockfile metadata are not runtime media assets.

## Determinism and time

- Every visible animation comes from useCurrentFrame + data and fps. No CSS
  animations/transitions, Date.now, requestAnimationFrame or wall-clock timers.
- Math.random is unsuitable during rendering. Use seeded Remotion random or
  a deterministic formula. Do not use random(null) for reproducible particles.
- Sequence children see LOCAL frames. Global captions/SFX offsets must not be
  mistakenly calculated from local time. Pass global frame when needed.
- Clamp interpolation for opacity/crops. Spring may overshoot; select damping
  or overshootClamping deliberately rather than clipping unintended movement.
- Fixed Sequences with contained fade/dip effects are simplest for the test's
  locked boundaries. TransitionSeries overlaps SUBTRACT duration: 40 + 60 -
  30 = 70 frames. Do not silently add transitions and preserve the old duration
  claim. Show overlap explicitly if the user chooses that editing structure.

## Fonts and loading

Use the user's allowed font route. System sans may vary by host; the example
bundles a licensed Noto Devanagari system font for consistent Hindi. Include
license and glyph coverage, and await FontFace or @remotion/fonts loadFont.
If using Remotion GoogleFonts, specify weight/style/subsets and acknowledge
network loading; do not call that offline. Do not introduce an arbitrary paid font.

Create one stable loading handle per async operation, continue it on success,
cancel with the actual error on failure. A longer timeout does not repair a
missing asset. Test both Hindi matras and mixed numerals before measuring text.

## Actual audio/video components

For a voiced implementation, add the selected supported package (e.g.
@remotion/media at exactly 4.0.529) and use its documented Audio API. The silent
example deliberately has no audio dependency or fake voiceover.
Volume callback frame zero is relative to that clip's start; compute fades and
ducking accordingly. Match footage offsets and frame rates, avoid rounding drift
and inspect actual decoded output. Caption data can use @remotion/captions;
the package format is not an automatic alignment result.

## Browser portability

The example detects a Chrome/Chromium executable on runtime PATH and otherwise
allows Remotion's automatic browser download. No personal executable path is
stored. This does not guarantee every OS/host has compatible browser libraries
or network access. Diagnose a real error; never disable TLS/checksums or require
the user's PC. Record sandbox socket restrictions separately from project bugs.

## Test exactly what Muse will run

From the actual project root, run npm install, npm run typecheck,
npx remotion compositions and **npx remotion render**. With one composition and
configured entry/output the example runs noninteractively; general CLI docs may
prompt when composition is omitted, so never assume the bare command works.

Check all 450 frames encoded for the 15s test, not just bundle success.
Verify actual streams/dimensions/fps/frame count/duration and audio expectation.
Inspect caption holds, every boundary neighborhood and intermediate motion.
Capture the command's real exit code when redirecting/piping logs. Do not call a
stale previous MP4 the current result. Keep complete failed logs and diagnosis.

Use the helpers for static asset/schedule validation and measured ffprobe
metadata, then do visual/audio QC separately. No script certifies taste,
pronunciation, source truth or Muse execution.
