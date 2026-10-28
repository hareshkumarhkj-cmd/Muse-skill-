# Actual validation — 2026-10-28

## Source research

- BeyondArtist and Beyondsumi source workflows/code/relevant tests/licenses
  reviewed read-only at exact commits listed in REVIEW-STATUS.md.
- Official pinned Remotion docs and listed audio/tool source docs fetched/read.
- No upstream installer, tests, TTS API, voice/model downloads or demos executed.
  Reviewing source code is not runtime validation of those tools.

## Newly authored helper code

Command from skill root:

```sh
python3 -m unittest discover -s tests -v
```

**42 distinct tests passed.** Includes valid/malformed contracts; gaps/overlaps;
paths/traversal/symlinks; asset hashes; narration/sound-only requirements;
source-row shape; composition ID restrictions; mandatory lockfile; ZIP exclusion
and integrity; missing ffprobe/file/error/malformed metadata; wrong stream count,
size/fps/frame count/duration/audio expectations. Metadata unit tests mock ffprobe;
real output decoding was tested separately below. Full log: validation/helpers.log.

Independent code review caught two issues in an earlier iteration: underscore
composition IDs accepted by the checker despite the pinned runtime rejecting
them, and packaging without the required lockfile. Both were fixed with
regression tests. A test-module Path import was corrected during assembly.
These fixes do not imply proof of every possible input or host environment.

## Included example, fresh root retest

The copied example was improved to derive Composition/Sequence durations from
the actual production-contract.json. Executed in examples/remotion-test:

| Command/check | Actual result |
| --- | --- |
| npm install | Pass, exit 0; pinned dependency install |
| npm run typecheck | Pass, exit 0 |
| npx remotion compositions | Pass; exactly RaysShort01, 1080x1920, 30fps, 450 frames |
| npx remotion render | Pass, exit 0; rendered/encoded 450/450 |
| Contract/asset/hash helper | Pass on real bundled assets |
| verify_render.py against actual new MP4 | Pass; 450 decoded frames, 15s, correct size/fps, no audio stream |
| package_handoff.py | Pass; ZIP CRC, local file inclusion and exclusions |

The render used runtime-PATH Chromium outside the command sandbox because
that sandbox blocks browser sockets. No personal browser path is bundled.
This verifies the prepared Linux/Node 24.19.0 host, not every OS or Muse itself.

Visually inspected actual output frames 1,45,89,90,91,180,239,240,241,330,
389,390,391,435,449: starts, interiors, all boundary neighborhoods, final hold.
No missing images or Hindi glyph boxes observed. Intended fade/entrance frames
are not extra scenes. This is sampled visual QC, not a complete perceptual
audit of every frame. No listening claim: the example intentionally has no audio.

Detailed example logs are under its validation/. Earlier preparation-host
browser-download/sandbox failures and fixes remain recorded, not hidden.

## What remains untested

Actual Muse loading/execution; live LLM compliance with every instruction;
Hindi TTS synthesis/audition/forced alignment; new full-motion character
generation; measured mix loudness; exact reference-audio style; every future
OS/tool/model. Behavior cases in tests/ are a proposed evaluation suite, not
passed Muse tests. No “perfect” or cross-model-equivalent quality is promised.

The source ZIP contains instructions, scripts/tests, notices and the complete
example with original assets, but no node_modules, .git, out/dist, caches, keys,
reference clips, provider voice assets or external sound bank.
