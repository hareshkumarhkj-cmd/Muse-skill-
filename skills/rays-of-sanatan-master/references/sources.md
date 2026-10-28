# Technical sources and actual access

Research date: 2026-10-28. These support engineering, not temple-history claims
or identification of Epic Yug's production software.

## Remotion: official source docs fetched at v4.0.529

The listed paths were fetched/read under:
https://raw.githubusercontent.com/remotion-dev/remotion/v4.0.529/packages/docs/docs/

| Files | Evidence | Public docs |
| --- | --- | --- |
| animating-properties.mdx | Frame-driven animation; CSS transition warning | https://www.remotion.dev/docs/animating-properties |
| use-current-frame.mdx | Zero-index and Sequence-local frames | https://www.remotion.dev/docs/use-current-frame |
| interpolate.mdx; spring.mdx | Extrapolation/overshoot controls | https://www.remotion.dev/docs/interpolate |
| random.mdx | Stable seeds vs nondeterminism | https://www.remotion.dev/docs/random |
| staticfile.mdx; img.mdx | Local public assets, awaited loading | https://www.remotion.dev/docs/staticfile |
| fonts.mdx | Local loading/readiness | https://www.remotion.dev/docs/fonts |
| google-fonts/load-font.mdx | Explicit weights/subsets, network requests | https://www.remotion.dev/docs/google-fonts/load-font |
| delay-render.mdx | Stable handles, continue/cancel, timeout | https://www.remotion.dev/docs/delay-render |
| transitions/transitionseries.mdx | Overlaps subtract duration | https://www.remotion.dev/docs/transitions/transitionseries |
| audio/volume.mdx; media/audio.mdx | Clip-local volume callback | https://www.remotion.dev/docs/audio/volume |
| captions/caption.mdx; captions/create-tiktok-style-captions.mdx | Timed data/grouping, not alignment proof | https://www.remotion.dev/docs/captions/caption |
| cli/render.mdx; cli/compositions.mdx; cli/versions.mdx; config.mdx | CLI/configuration/version gates | https://www.remotion.dev/docs/cli/render |

General CLI can prompt if composition is omitted; the example's bare render
command is actually tested, not assumed from syntax.

## Audio/voice: fetched project/official sources

- FFmpeg filters source:
  https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/doc/filters.texi
  Inspected loudnorm, amix, sidechaincompress, atempo. Moving source: match
  installed-version options. Public docs: https://ffmpeg.org/ffmpeg-filters.html
- WhisperX:
  https://raw.githubusercontent.com/m-bain/whisperX/main/README.md and
  https://raw.githubusercontent.com/m-bain/whisperX/main/whisperx/alignment.py
  ASR/alignment distinction, Hindi mapping. No model installed/aligned here.
- Whisper: https://raw.githubusercontent.com/openai/whisper/main/README.md
  ASR is not TTS; no transcription run here.
- Piper: https://raw.githubusercontent.com/OHF-Voice/piper1-gpl/main/README.md
  Local engine with separate voices/models. No Hindi voice auditioned here;
  engine/model rights and actual availability require task-specific checks.
- W3C SSML https://www.w3.org/TR/speech-synthesis11/ returned HTTP 403.
  Not marked read; arbitrary provider SSML support is not assumed.

## Skill sources

See [comparison](source-review.md) for exact commits, scope, licenses and audits.

## Recommendation is not evidence

Palette, caption sizes, 15s scene grammar, voice direction, rough word count and
-16 LUFS/-1.5 dBTP starting target are Rays design proposals, not platform rules,
verified reference traits or guarantees. Docs access does not prove synthesis.
