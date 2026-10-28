# Goal
Render an original cinematic temple-engineering visual proof for Rays of Sanatan using three bundled AI stills, restrained camera moves, structural highlights and Hindi captions.

Composition: `RaysShort01` (one composition only).
Duration: 15 seconds / 450 frames. Resolution: 1080x1920. Frame rate: 30 fps.

## Exact scene table

| Scene | Time | Frames, inclusive | Caption |
| --- | --- | --- | --- |
| Hook | 0–3s | 0–89 | ये पत्थर / टिके कैसे हैं? |
| Reveal | 3–8s | 90–239 | हर जोड़ में / छिपा है संतुलन। |
| Climax | 8–13s | 240–389 | छोटे जोड़। / विराट रचना। |
| End card | 13–15s | 390–449 | कला या इंजीनियरिंग? / दोनों। |

Scene boundaries are fixed. Each scene animates within its assigned interval.
The end card reuses the hero image; it is not a fifth image or scene.

## Run exactly

From the extracted `rays-stone-test` directory:

```sh
npm install
npx remotion render
```

Expected file: `out/rays-stone-test.mp4` (H.264, 4:2:0, silent).
Entry: `src/index.ts`, registering `RemotionRoot` and `RaysShort01`.
The configuration sets the entry, codec and output path, so no prompt or
composition selection is needed. A Chrome/Chromium browser on PATH is detected
automatically; otherwise Remotion automatically downloads its rendering browser.
Installation and a first browser download need Internet access.
All media and font files used by the video are bundled locally.
No API keys, personal files, paid assets or environment configuration are required.

Optional type check: `npm run typecheck`.
Optional stills:

```sh
npx remotion still src/index.ts RaysShort01 out/start.png --frame=45
npx remotion still src/index.ts RaysShort01 out/middle.png --frame=180
npx remotion still src/index.ts RaysShort01 out/end.png --frame=435
```

## Scope and accuracy

The user explicitly authorized new AI images for this original 15-second test.
The temple is fictional. The technical overlay is an illustrative graphic,
not an engineering simulation or an archaeological reconstruction. All frames
carry a Hindi fictional/AI-image disclosure. No historical or supernatural
claims are made. The supplied reference video, its logos, voice, music and
sound effects are not included or reused.

This tests cinematic still-image editing, Hindi readability, composition and
render portability. It does not demonstrate newly generated walking workers,
moving elephants, changing character gestures, simulated ropes or liquid, or
continuous camera motion revealing new 3D geometry as in parts of the reference.
Those require original motion footage or a separate 3D/video-generation pipeline.
Matching the reference perfectly is not promised. Audio: no audio.

Hindi uses a bundled copy of the Noto Sans Devanagari system sans-serif font;
its redistribution license is in `public/fonts/LICENSE.txt`.
Use this existing project directory; do not create an additional Git worktree.
See TEST-NOTE.txt for actual validation evidence and any limitations.
