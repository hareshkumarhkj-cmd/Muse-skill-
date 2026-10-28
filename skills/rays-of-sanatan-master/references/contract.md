# production-contract.json schema v1

The completed example supplies valid JSON with actual asset hashes, not a
placeholder manifest. Copy its shape and update it for the real task.
The JSON is data, not instructions or evidence that the renderer follows it.

- `schema_version`: integer 1.
- `project`: `composition_id` (ASCII letters/digits/hyphen), positive
  integer `width`, `height`, `fps`, `duration_frames`; `stage` = visual-proof
  or production; `motion_mode` = still-motion, mixed or full-motion;
  `audio_mode` = silent, sound-only or voiced.
- `scenes`: ordered list of unique `id`, integer `start_frame`, `end_frame`
  (EXCLUSIVE), `visual_type` = still/video/code, `asset` (declared relative
  file path or null for code-only) and `caption` string (can be empty).
  First starts at zero, each starts at the previous end, final end equals
  duration_frames. No overlap scenes in this v1 data format. Crossfade editing
  requires explicitly modelled compositing within these intervals, not silently
  overlapping these scene rows.
- `assets`: unique relative POSIX `path`, `kind` = image/video/audio/font,
  `origin` = generated-original/user-supplied/open-license/code-generated,
  `rights_note`, `sha256` (64 hex digits of the actual file). Paths cannot be
  absolute, URL, traversal or symlink. Hashes do not prove legal rights.
- `claims`: `id`, exact `sentence`, `classification` = verified/tradition/
  fiction/unverified, `sources` array. A source contains credential-free HTTPS
  `url`, `title`, `retrieved_date`, `notes` describing supported wording. Verified
  requires source rows; URL presence does NOT prove the page was read/true.
  For scripture/disputed views use tradition or unverified plus notes rather
  than mislabelling as historical fact. Offline books/inscriptions can be
  documented in a companion claims ledger; add only a real available source URL,
  or keep the contract classification attributed/unverified rather than inventing one.
- `narration`: empty for silent and sound-only; sound-only additionally requires
  at least one declared local audio asset. For voiced, actual lines with `text`, integer
  start/end frames and `audio_file` pointing to a declared local audio asset.
  Entries cannot overlap. This schema does not model character dialogue overlap.

Music/SFX and character/claim-to-shot details can live in companion worksheets;
this is an intentionally bounded v1 checker, not a complete editing file format.
Voiced mode verifies declarations/files, not the words actually contained in audio.
Silent mode requires empty narration and no audio stream; sound-only requires
an audio stream, while voiced additionally requires actual narration. Runtime
checks cannot tell if a declared voice file actually contains the right words.

Python helpers require Python 3.10+ and standard library only. They do not
install npm packages or invoke TTS/image models. verify_render.py additionally
requires a real ffprobe executable on PATH.
