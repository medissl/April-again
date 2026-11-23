# April, again 1.0.1 — release verification

Verified on 23 November 2026. The final Windows export uses Unity **6000.3.21f1**, Direct3D 11, uGUI, TextMesh Pro and Input System 1.20.0. It preserves the approved Nunito, rose and ivory presentation.

The release fixes missing/obscured room exits, the lobby classroom label, Mari's interaction bounds, first-day poses, small wardrobe sprites, fullscreen scaling and the requested credit lines. It adds names, scene-wide dialogue clicks, reading preferences and display options. Five individual 1024×1536 sprites replace small atlas tiles; imports preserve source resolution without block compression.

## Final checks

- 2,104 rule assertions: 75 encounters, 225 choices, appointments, duplicate commitment, saves and 15 outcomes.
- 134 reported-bug checks, zero failures: actual UI raycasts, five introductions, naming, outside-textbox clicks, HD dimensions, settings and legacy saves. Unread tests use a unique identity to avoid old test progress.
- 48 world scenes and 149 pointer/navigation checks, zero failures: room exits, wayfinding links, every map destination and free travel.
- 15 complete controller playthroughs, 225 commits: every good/neutral/bad CG, ending, credits and return to title.
- 22 smoke assertions and 11 reading/legacy-save checks: opening, home/sleep, encounters, mid-response saves, corruption recovery, audio routing and skip behavior.
- 2,351 rendered layout checks at 1920×1080 and 1280×720, zero issues. Includes world art, map/door hovers, system panels and credits. Populated history also passes.
- All 1,625 dialogue lines fit the 112px reading area at 40px; maximum height 109.12px.
- Asset validation passes: 395 records, 106 original illustrations, 150 prop references, 225 choices and 22 audio assets.
- Final build succeeds: 416,465,066 bytes. Final Editor console: zero errors and warnings. Custom icon assigned; Unity splash disabled.

## Native export and packages

Detailed native mouse checks on the earlier candidate covered naming, fullscreen/windowed display, outside-textbox advance, introductions and infirmary/library/Class A navigation. Its completed log exposed Unity's shutdown crash after UI Automation inspection. The final patch fixes [UUM-146676](https://unity.com/releases/editor/whats-new/6000.3.21f1).

The rebuilt 6.3.21 executable was inspected through Windows UI Automation and quit normally: **exit code 0**, no crash marker or managed exception in the completed log. The user then confirmed the candidate was fine and requested publication; further visual automation was stopped.

The final installer results are in `installer-101-results.json`; that record supersedes the historical 1.0.0 installer check. The portable ZIP passes a complete CRC read. Final sizes/hashes are in `artifact-hashes.json` and the release checksum file. QA saves are isolated and excluded; the normal player profile is preserved.

## Visual review

Palette discipline: 4/5 — approved rose, ivory and dark ink.

Style uniformity: 3/5 — coherent anime direction; illustrations still vary in detail.

Outline discipline: 4/5 — controlled character linework and UI borders.

Silhouette: 4/5 — distinct characters in world and dialogue views.

UI intentionality: 4/5 — inset headings/close controls and measured text.

Feedback visibility: 3/5 — restrained hover and selection feedback.

Source, saves, input ordering, navigation and packaging were reviewed using EngineeringSuite diagnosing-bugs/code-review-and-quality and Unity craft-game-floors/game-shell, visual-scorecard and CLI verification references. Private documents, profiles, diagnostic logs, caches and local tools are excluded from Git.

The binaries are unsigned. No voice acting is included. Audio routing and decoding were checked; subjective listening was unavailable. Injected Escape did not establish physical keyboard-shortcut behavior. These checks cover the exercised paths, not every possible input sequence.