# Hindi voiceover, music, sound and measured sync

## Capability adapters, not imaginary APIs

Use a built-in authorized Hindi voice when available, a supplied recording,
or an already installed/configured local TTS route with suitable voice rights.
Existing keys/bindings stay in the host's secure configuration, never in code,
ZIPs or chat. Generation may use that environment's authorized tools; the final
render consumes local files and never needs the generation key.

API-free narration is possible with some local engines/models, but requires
model files, hardware and license compatibility. This package does not install
or audition such a model. Piper is one possible route, not a promise of a
natural installed Hindi voice. Whisper transcribes; it does not synthesize.
Do not download large models or subscribe to a service without checking the
task scope/resources. A tool-neutral skill cannot create missing tool access.

The current request for good narration authorizes work toward original voiceover;
it does not authorize cloning Epic Yug's narrator or a real person's voice.
Use an original non-cloned voice by default. If the user explicitly requires
silent/no-generated-audio output, that instruction controls instead.

## Pronunciation first

1. Separate editorial delivery notes, clean narration text and engine-specific
   synthesis input. Strip literal [pause], [emphasis] and XML from plain-text
   input unless the selected engine documents support.
2. Make a short lexicon of actual episode names, compounds and numbers. Check
   difficult Sanskrit/Hindi pronunciations using a credible source/speaker;
   do not invent phonetic certainty. Spell numbers/units as intended speech.
3. Generate a two-line sample containing the hardest name, one number and a
   question. Actually listen where the host can. Check matras, syllable endings,
   repeated words, emphasis, robotic gaps and breath/noise artifacts.
4. If no listening interface exists, state “generated, not auditioned”; waveform,
   ASR and a transcript cannot certify naturalness or correct pronunciation.
5. Generate the complete narration only after correcting the audition where
   possible. Save voice ID/model/version and settings only when actually known.

Proposed performance: warm conversational Hindi storyteller, precise consonants,
curiosity without shouting, respectful emotion, pauses before the payoff.
This is Rays direction, not a verified description of the reference speaker.

## Duration and captions

Probe actual duration/sample rate. For a fixed timeline, generate sentence clips
inside assigned slots; rewrite/re-synthesize overlong lines rather than silently
extending scenes, truncating endings or aggressively speeding the speaker.
Time estimates guide drafting only. A slight tempo adjustment needs an audition.

Use actual engine word timestamps or tested forced alignment against FINAL
audio plus the corrected transcript. WhisperX has a Hindi alignment mapping in
its source, but model availability, licensing and Sanskrit-name accuracy remain
separate checks. Validate monotonicity/bounds and spot-listen names and beginnings,
middles and endings. Do not label uniform word spacing “forced alignment”.
If alignment is absent, use measured sentence-clip times and label caption
precision sentence-level/approximate. Never split Devanagari grapheme clusters.

## Sound design and mix

Keep voice, music and SFX stems separate. Use supplied/original/licensed local
files with rights notes. No scraped “royalty-free” track without an actual
license. When explicitly authorized, original procedural effects can be generated
locally; do not describe a synthesized tone as natural speech or a recorded bell.

Choose events in the frame table: a quiet airy reveal, a single soft bell for
an earned devotional beat, a controlled low impact for scale. Do not add a whoosh
to every cut. Protect the first consonant and last syllable. Give tails space.
Duck music under narration and listen for pumping and masked consonants.

A useful HOUSE starting target is around -16 LUFS integrated and <= -1.5 dBTP
on the final encoded mix, adjusted deliberately for the brief. These are not
YouTube requirements or a naturalness guarantee. Measure the actual final mix
and encoded file; do not confuse dBFS sample peak with true peak or LUFS.

Select sound-only when an unvoiced music/SFX video is actually requested;
do not call that silent or require an invented narrator. In Hindi segmentation,
recognize danda “।”/“॥” and actual punctuation rather than splitting only on
English full stops. Review boundaries around abbreviations and proper names.

Before an authorized potentially billed generation, record the intended take
privately and retain returned IDs/status. A timeout may leave the result unknown:
check the provider's documented receipt/status before retrying. Never assume
“failed response” means no charge, or that a connected key authorizes new spend.

Analysis command when FFmpeg exists (change filename to the actual output):

```sh
ffmpeg -hide_banner -i final-mix.wav -af loudnorm=I=-16:TP=-1.5:LRA=7:print_format=json -f null -
```

Read real measurements. Two-pass normalization must use CURRENT input_I,
input_LRA, input_TP, input_thresh and target_offset statistics with documented
option mappings; do not paste invented values. Explicitly set output sample
rate (typically 48kHz), verify linear/dynamic behavior and remeasure. Check
installed FFmpeg options; master-branch documentation can evolve.

Final voiced gate: expected content, auditioned diction if possible, measured
duration/sync, intelligibility, correct audio streams and measured level/peak.
An audio file's existence passes none of the subjective checks by itself.

When required narration is unavailable: finish the script/visual/code work,
state the missing capability precisely, and deliver only a clearly labelled
visual proof if appropriate. Never mark a silent version a completed voiced final.
