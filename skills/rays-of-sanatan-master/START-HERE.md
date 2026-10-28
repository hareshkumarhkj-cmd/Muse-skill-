# Rays of Sanatan master skill — portable v1.0

This package is an original, tool-neutral production workflow for cinematic
Hindi Shorts. It includes production guides, reusable worksheets, static
validation/packaging tools and an actually rendered 15-second Remotion example.
It does not install a TTS/image/video model or supply credentials.

## Use with Muse or another assistant

1. If the host supports folder-based skills, add the complete
   `rays-of-sanatan-master` folder using that host's documented skill mechanism.
   Keep SKILL.md and its relative references/scripts together.
2. If the host accepts ZIP attachments, attach this ZIP and ask it to extract
   and read SKILL.md, then load the referenced modules needed for the task.
3. If it only accepts text, paste SKILL.md and the relevant reference modules.
   That text-only route does not transfer the bundled example/images/scripts.

This is not an executable app and does not auto-register with every assistant.
The host must be able to read instructions and actually use the required tools.

Copy-ready first request:

> Use rays-of-sanatan-master/SKILL.md for Rays of Sanatan. First inspect your
> real tools. Create one original 15-second visual proof, 1080x1920 at 30fps,
> composition RaysShort01. Show the exact scene table, distinguish history,
> tradition and fiction, and deliver a tested self-contained Remotion ZIP.
> Use only assets authorized in this task. Tell me precisely which voice,
> image and motion capabilities are available before promising them.

For a narrated production, add:

> Narration is required. Use an original authorized Hindi voice. Check a short
> pronunciation sample, then measure actual speech and align captions. If you
> cannot generate/listen to voice here, report that limitation; do not call a
> silent sample the completed narrated video. Do not use paid services unless
> I authorize them.

For a fresh AI-image sample add an explicit instruction such as:

> Original AI images are allowed for this 15-second task. Do not reuse the
> reference channel's logo, audio or clips. No paid generation or voice cloning.

## What is already tested

`examples/remotion-test/` is a complete **silent still-motion** example using
three original AI images previously approved by the user. It is not a narrated
or full-motion reference replica. From that directory:

```sh
npm install
npx remotion render
```

Its complete test notes live there. See root `VALIDATION.md` for tests of the
master package itself. Only claim the specific tests recorded, not Muse execution.

## Honest scope of this release

The uploaded ZIPs exceed the transfer limit, but the user supplied GitHub
sources. Both were deeply reviewed read-only at recorded commits; useful
principles were adapted into this original skill. See REVIEW-STATUS.md and
references/source-review.md. The reviewed Beyondsumi source says 1.0.1;
equality with the uploaded v1.0.0 archive is not established. No upstream
galleries, sound banks, demos, installers or provider adapters are bundled.

The supplied Epic Yug video was merged and sampled visually. Its audio decoded,
but no listening/transcription interface was available, so narrator/music/SFX
analysis is not presented as verified. Skill audio standards are proposed Rays
production direction, not a claim about Epic Yug's exact sound.

No skill guarantees identical output across different models, voices or render
hosts. This one makes capability gaps, editorial choices and tests explicit.
