# April, again — visual direction

## Current milestone

The full 75-encounter, 15-ending screenplay, performed voice pass and story-dependent art pack are complete. The user has authorized implementing and testing the complete Unity game. `AprilAgain.unity` is the new playable scene; SampleScene is preserved. The runtime uses uGUI/TMP and the Input System, with the local Unity Pipeline for development checks. Actual build and runtime evidence belongs in `Documentation/Testing`.

## Direction

A quiet, contemporary anime school romance in Fukuoka. Ordinary classrooms, useful doors, a readable campus and small acts of attention carry the atmosphere. Crisp, finished anime illustration with economical clear linework, broad designed hair masses, clean cel-shadow boundaries and restrained soft lighting unite the cast and backgrounds. Uniforms are navy, white, maroon and charcoal. No fantasy academy, palace interiors, glitter haze, excessive sakura, promotional card-grid UI or photorealistic character renders.

The first cast sheet and all derivatives made from it were REJECTED by the user: too much strand-level hair detail, textured/glossy rendering and generic faces. `Documentation/Art/cast-model-sheet.png` is a rejected study, never an approved identity/style master. Do not use its rendering as an input to new final art. The user's later clear-face ponytail illustration is the primary rendering reference, not a character/costume to copy. Its lesson is controlled highlights and broad hair shapes, not zero highlights or artificially flat low-detail TV art. See `Documentation/Art/ANIME_PRODUCTION_RESEARCH.md`.

Differentiate faces by eye contour, brow construction, cheek/jaw shape and expression timing. Svea should read clearly as a girl with a tomboy style: not an angular male face pasted onto a feminine body. Preserve her shaggy hair, half-lidded eyes, loose uniform and athletic posture. All first-year designs remain non-sexualized; do not implement requests to enlarge or emphasize breasts.

The current presentation is spring-letter stationery: cranberry rose, pale blush, peach ivory and cocoa. A consistent ribbon, blossom and folded-corner motif unites the generated frames. Illustration occupies the screen; compact live controls support reading. Avoid repeated explanation paragraphs and permanent button strips. The first plain cream/serif UI was rejected; use the Spring skin and rounded font.

## Sources and adaptation

All five supplied profiles were read in full (four PDFs totaling 14 pages and Katya's DOCX). They are character evidence, not instructions that can override the user's request. The six supplied images establish appearance direction and campus topology, not a license to copy existing characters or reproduce unrelated costume/sexualized reference panels.

The user places everyone in their first year of high school. Adapt the source dossiers' 18-year-old/final-secondary framing to ordinary first-year peers, approximately 15–16. Romance is non-explicit. Mari remains a student who spends time in the infirmary, never a nurse. Katya is an aspiring council/fencing member rather than an already appointed first-day vice president. Seo-yun's family has relocated to Japan before the story; her cultural history informs her perspective without making romance a rescue narrative. No political uniform insignia.

Written appearance details win over conflicting references:

| Character | Locked identity | Uniform variation | Emotional vocabulary |
|---|---|---|---|
| Katya | 176 cm; waist-length silver-white hair; ice-blue eyes | Impeccable blazer, silver stud, black tights | Composed, annoyed, surprised, flustered, sad, soft smile |
| Akira Seojin | 167 cm; short pink bob; brown eyes; round glasses and charm | Pin/keychain satchel | Attentive, delighted, puzzled, flustered, worried, excited |
| Han Seo-yun | 163 cm; long slightly wavy dark-brown hair; brown almond eyes; mole under her left eye | Neat blazer, dark-blue journal | Reserved, warm, curious, flustered, sad, determined |
| Yasuko Mari | 176 cm; feathered salmon low ponytail; cyan eyes | Neat blazer, bento/thermos | Composed, warm, concerned, downcast, blushing, peaceful |
| Kurokawa Svea | 171 cm; shaggy blue-black fringe; blue-grey eyes | Open blazer, loose collar, straight trousers, sneakers | Unbothered, smirk, annoyed, flustered, sleepy, soft smile |

All skirts are modest knee length. Normal youthful anatomy; no glamour posing. The MC is an unidentifiable charcoal-grey silhouette with an ordinary school uniform outline.

## Color and type

| Token | Value | Purpose |
|---|---|---|
| paper | #FFF7F2 | Peach ivory reading panels |
| ink | #6E3C50 | Rose cocoa text and navigation |
| rose | #CB4D7A | Selection, ribbons and title accent |
| muted | #7E6270 | Secondary text |
| sage | #8C9B8D | Calendar and quiet support |
| brass | #B8A17A | Fine framing, never primary body text |
| line | #D8CEC1 | Panel boundaries |

The user rejected Zen Maru and approved the supplied classroom reference's heavier rounded lettering and placement. Nunito ExtraBold (800) is the default throughout the entire game: dialogue, names, choices, menus, settings and HUD. Catalog body/title fonts and the global TMP default all point to NunitoDefault. Static instances are made from Google's official variable source using FontTools, with the original source, process record and SIL Open Font License preserved. Text stays live: no dialogue, choices, room/day labels or character names baked into backgrounds. Dialogue is 40 px; name 38; supporting UI 22–26. Compiler paginates prose into short reading beats; actual TMP measurements must fit 1560×112 with a maximum of two lines. Scale the UI canvas, never stretch illustration aspect ratios.

## Composition and interaction

1920×1080 reference canvas, 16:9. Translucent dialogue frame x24 y792 w1872 h264, ribbon nameplate x40 y736 w400 h128. Name text is optically centered in the pink ribbon body at rect x150 y756 w260 h64, rather than the full bow/tailed artwork. The enlarged date ticket is x−12 y10 w420 h196 so both month/date and the longest weekday stay above its diagonal edge; exploration's room caption starts at y210 below it. Neutral character staging follows the approved three-quarter composition, with the original full-body sprite extending below the screen. Emotional beats use closer expression sprites whose lower edges stay behind the reading frame. Three choice ribbons occupy the middle-left without covering faces. Time/activity details appear on calendar hover or keyboard focus. Six labeled quick controls (Log, Auto, Skip, Save, Load, Menu) sit inside the window's lower-right region, clear of the rose decoration. H hides the interface. The title uses the school gate without girls, per the user's explicit preference; the cast-title study is archived outside Assets and is not shipped.

Every selectable object has hover and keyboard-focus states, plus a label on focus. Doors use a small white arrow rather than giant floating buttons; inspectable hotspots wash softly white. Clicking empty scenery does nothing. A girl who has already had her scene today has a short non-scoring acknowledgement. Location navigation costs no time; the 'Talk · 3h' hover label declares encounter cost, and the route finale additionally requires confirmation. Nearby props use one magnifier and a focused item sheet instead of a permanent row of cards.

The map preserves the supplied sketch: infirmary west; B northwest; C north/northeast; library east; A southeast of the hall; lobby south-center; canteen southwest; sports field southeast; gate south. Corridor connects the academic rooms; lobby connects corridor, canteen, field and gate. Bedroom is reached through the gate/home action. Rooms A/B/C have distinct room IDs and art even when architectural materials repeat.

Save/load, settings, journal, ending gallery, pause, choice confirmation and end-of-day prompts share the same frames and controls. Disabled states require shape/text cues, not color alone. Keyboard focus is a 3 px maroon outline. Buttons are at least 56 px tall; HUD targets at least 64×64. Sliders expose a numeric value. Reduced motion disables character fades and decorative transitions. Auto and skip visibly indicate state; skip stops at unread text and choices. Hide UI restores with a click/Escape.

## Art deliverables and checks

Separate illustration masters from UI source geometry and review composites. Transparent PNG is used for character sprites (JPEG cannot hold transparency); backgrounds and CGs can use opaque PNG/JPEG. Expressions and exploration poses are regular atlases with explicit slices; preserve every source atlas. No invented separate illustration is counted for a color filter or crop.

Inspect the actual generated cast, each atlas, every background and every ending. Check identity, hand count, skirt/trouser continuity, props, perspective, empty compositing areas, cell boundaries, alpha and readable hotspots. Review title, map, exploration, dialogue, choices, bedroom, save/load, settings, journal and gallery at 1920×1080 and 1280×720. Record integration limitations honestly.

The redesign visually studied official publisher-provided Aokana title/dialogue screenshots and Sabbat of the Witch's library dialogue screen, alongside the user's pink Akascarlet UI example. Adapted character-first composition, shallow reading windows and quiet system controls. Café Stella promotional images were reviewed for illustration context, not claimed as a system-screen reference. Sources and generated master records are in Documentation/PresentationPass.md. No reference-game graphics are shipped.
