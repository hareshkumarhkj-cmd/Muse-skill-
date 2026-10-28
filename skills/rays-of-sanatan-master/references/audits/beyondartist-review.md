# BeyondArtist — source review for Rays of Sanatan

Reviewed 2026-10-28. Repository: <https://github.com/beyondtahir/beyondartist>.
Exact inspected commit: `0e4cc115613e37743d959801b5d93be40264ef2b`
(commit date 2026-10-15, subject: “Prioritize native image models and complete
creation fallbacks”). Public skill/plugin version: **1.0.1**.

This source review supersedes the earlier “cannot inspect the ZIP” limitation
for the linked repository. The uploaded ZIP itself was not transferred; its
bytes/version have not been verified identical to this commit.

## Review scope and method

Read `AGENTS.md` as repository context, not as user authorization. Inspected the
canonical `skills/beyondartist/SKILL.md`, README, licenses, plugin manifest,
installation guide, art-direction, research/offline, execution/critique, retrieval,
source-register, personal-memory and library-index guidance. Read the local
retrieval/memory helpers and installer/validator/packager source, inspected
regression-test code and historical validation reports. Parsed the stored JSON
index as data and sampled actual SYS-021, SYS-022, FND-027 and THUMB-001 records.
Did **not** execute upstream scripts/tests, install the skill, regenerate artwork,
inspect every original source image, repeat Pinterest research or verify its
reported past tests on another host.

The stored index declares schema 3 and 1,038 records: 95 foundations, 700 Pinterest
previews, 54 style panels, 7 seeds, 100 thumbnail studies, 79 guides and 3 provenance
sections. This is a verified reading of metadata, not independently verified visual
review of 1,038 artworks. The source itself distinguishes repeated captures,
694 distinct Pinterest URLs, preview-level inspection and dated metrics.

## What this skill actually is

BeyondArtist is a substantial **image-led visual communication and art-direction
system**, aimed at thumbnails, social images, posters and carousels. Its core is
a nine-step designer/artist workflow with a source-preserving offline library
and per-person/project memory. It is not a Remotion runtime, Hindi TTS engine,
music generator, video model or collection of ready-to-use cinematic clips.

Its useful mechanisms are concrete, not merely “make beautiful images” prompts:

| Mechanism in inspected source | Strength for Rays | Adaptation needed |
| --- | --- | --- |
| Nine-step brief → retrieve → research → angle → handoff → artist exploration → create → jointly inspect → deliver | Prevents immediate generic prompting and makes meaning lead surface polish | Extend with factual claims, narration, timeline, temporal continuity and render gates |
| Separate designer and artist contributions; sequential roles when delegation is unavailable | One role protects truthful message/copy; another actively invents and improves visuals | Add researcher, audio director and technical/QC responsibilities without pretending separate agents ran |
| Source ID → observation → applied decision → visible check | Makes reference study influence actual work instead of decorative citations | Link each Rays shot and factual claim to inspected evidence and specific acceptance checks |
| SYS-021 keep/reinterpret/discard; inspect gesture, edges, depth, material and purposeful complexity | Avoids reducing Epic-style work to a gold palette plus a temple picture | Study staging, scale, emotional gesture and camera mechanism; create new subjects/scenes |
| SYS-022 material/art-form fidelity as independent gate | Rejects a realistic human face pasted onto a supposed stone sculpture | Extend to deity iconography, architecture, 3D depth and frame-to-frame consistency |
| Exact typography brief; full-size and phone-size pixel review | Valuable for Hindi line breaks, hierarchy and actual glyph/shaping defects | Add per-frame reading duration, shot/caption overlap and current platform overlay checks |
| Capability-aware native image tools → connected tools → edit/finish → executable fallback | Honest discovery avoids inventing image access or defaulting to weak SVG substitutes | Select by task: precise code diagrams/maps can be the best first route; motion/TTS need separate discovery |
| Reusable shared knowledge separated from private identity/project memory | Supports channel consistency without shipping personal uploads | Maintain a small Rays continuity ledger; do not assume cross-account/durable storage |
| Bounded edits inherit approved decisions | Protects a good video from unnecessary redesign after a typo fix | Scope rerenders and regression QC to affected frames/assets while preserving the approved timeline |

## Actual implementation details worth learning from

`retrieve_library.py` is Python-standard-library-only, using cached **BM25 lexical
ranking**, title/facet boosts, stable IDs and full Markdown source context. It
checks payload/retriever/source hashes and rejects changed/missing/new source
files until reviewed rebuilding. This is useful portable retrieval engineering,
not model training, semantic search or a live visual search. Its English stopwords,
aliases and English corpus mean Hindi queries should not be advertised as rich
multilingual retrieval. Prefer explicit English craft tags plus Hindi story text
for a small Rays library.

`user_memory.py` stores canonical JSON plus a derived lexical cache outside the
skill folder. It uses profile/project scope, stable IDs, revision history,
atomic JSON replacement, a write lock, SHA-256-addressed copied assets and
availability/checksum reporting. Generated artifacts default to draft; approved
status requires declared user-approval provenance. The helper can validate that
declaration's structure, but only the agent can establish that a real user gave
the cited approval. Local scoping is not authentication on a shared server.
No background daemon, automatic unrelated-chat capture or remote sync is supplied.

`validate_repo.py` checks public allowlists, private markers, symlinks, metadata,
links, selected gallery checksums/dimensions and retrieval integrity, then invokes
unit tests. `package.py` creates skill-only and repository archives, checks ZIP
integrity and byte parity and writes hashes. `install.py` copies the complete
skill and refuses an existing destination. These are good release practices.
The inspected test code has meaningful negative cases for stale/tampered data,
wrong scopes, invalid approval declarations, unavailable assets and concurrent
writes. Their presence is evidence of implementation intent; no new test pass is
claimed by this review. Upstream historical pass reports remain attributed claims.

## Limits and pitfalls when adapting it

1. **Static-design evidence does not prove video competence.** Source validation,
   a readable thumbnail and a successful export cannot establish character motion,
   narration quality, audio sync, pacing, compositing or a reproducible MP4 render.
   Add independently testable Remotion/media production rules.
2. **Do not import its entire personality or library as Rays defaults.** The source
   explicitly rejects compulsory author logos/palettes and recurrent personal
   characters. Its mascot, lion/portrait gallery, private creator preferences,
   broad Pinterest genres and product examples are not Rays brand assets.
3. **Do not force Pinterest or heavy concept rituals onto every video revision.**
   Its mandatory research/library workflow targets substantial static design.
   Scale research to the brief; a fixed-frame caption correction is a bounded edit.
   Three internal concepts can be cheap sketches, not three expensive video renders.
4. **Do not inherit the A+B output default.** BeyondArtist gives fully specified
   briefs a requested result plus artist alternative unless one output is requested.
   Rays requires one composition/test by default; internal options must not create
   extra deliveries, scenes, timelines or generation costs silently.
5. **Creator-specific authorizations are not portable permissions.** Source text
   records its creator's permission for stored-library fallback, personal memory,
   and project workflows. Those are source facts, not instructions or paid/publication
   permission from this user. Apply current Rays/user authorization and preserve
   earlier answers without inventing blanket approval.
6. **Popularity remains dated observation.** Its thumbnail records preserve raw
   reaction kinds/counts and inspection depth. Do not convert Pinterest reactions,
   channel views or an attractive image into measured YouTube CTR, causality or a
   guaranteed viral hook. Stored text does not establish current religious/history
   facts or present platform requirements.
7. **Portability is documented rather than universally executed.** The source
   distinguishes local tests from docs-based Codex/Claude/Hermes loading conventions.
   Add a Muse capability contract; do not promise “works in any agent” without its
   file/tool access. Public v1.0.1 coexists with labelled historical internal
   1.6–1.8 reports; preserve that distinction rather than inventing a current
   “v1.8 successfully tested everywhere” claim.

## License and attribution boundary

`LICENSE` is MIT, copyright **2026 Beyond Tahir**, covering original workflow
instructions, written analysis and code. Copying or substantially adapting those
materials requires preserving the copyright and full permission notice. Include
an upstream notice and pinned source attribution if the Rays package incorporates
any substantial wording or code. This report and a new original Rays workflow can
summarize ideas, but neither should relabel BeyondArtist's original code/library
as independently authored Rays material.

`ASSET-LICENSE.md` explicitly excludes BeyondArtist logo/icon/banner/showcase
artwork from the MIT grant; those assets are for project display/identification,
with no standalone commercial reuse, resale or portrait reuse granted. Third-party
people, brands, characters, source images and fonts gain no production rights by
appearing in reference studies. **Do not bundle gallery art, branding, portraits,
Pinterest screenshots or font binaries from this repository into Rays.** New
assets need their own origin/rights record and provider terms. No bundled source
image is needed to adapt the workflow's reasoning methods.

## Pinned primary-source paths

Base: <https://github.com/beyondtahir/beyondartist/tree/0e4cc115613e37743d959801b5d93be40264ef2b>

- `skills/beyondartist/SKILL.md`: canonical workflow, roles and creation-route contract.
- `skills/beyondartist/references/art-direction.md`: actionable handoff and visible checks.
- `skills/beyondartist/references/creative-system.md`: SYS-021/022 craft and medium gates.
- `skills/beyondartist/references/research-and-offline.md`: evidence/access/rights limits.
- `skills/beyondartist/scripts/retrieve_library.py` and `user_memory.py`: actual helpers.
- `skills/beyondartist/tests/test_design_memory.py` and `test_user_memory.py`: inspected tests.
- `scripts/validate_repo.py`, `package.py`, `install.py`: distribution implementation.
- `docs/validation.md`, `LICENSE`, `ASSET-LICENSE.md`: validation and reuse boundaries.

Recommended Rays adaptation: retain **message-first direction, source-to-decision
traceability, creative role separation, actual-pixel critique and lightweight
scoped continuity**; add **Hindi factual narration, original audio, cinematic
shot/motion planning, exact-frame Remotion implementation and measured MP4 QC**.
