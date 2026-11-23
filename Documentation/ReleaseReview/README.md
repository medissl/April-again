# Release verification — 23 November 2026

The game uses Unity 6000.3.7f1, uGUI, TextMesh Pro and the Input System. The tests below exercised the real runtime/controller in a clean staging project; they are not a claim that every possible player input sequence is bug-free.

- Rules: 2,102 assertions, 15 route outcome runs, all 75 encounters and 225 choices, appointment reachability, duplicate-commit rejection, save-state validation and all 136 possible final score combinations.
- Controller: 15 complete good/neutral/bad playthroughs, 225 committed encounters, all 15 CG/ending/credits branches. The actual credits Return to title button is clicked and visible title controls are verified.
- Smoke: 21 assertions covering the opening, all five observations, home/sleep/day two, real choice commitment, mid-response save/load, busy interaction, menus, sliders, music mute and recovery from a corrupt primary save.
- Layout: 1,757 checks across all 48 world illustrations, system screens and door/map hover states. Captures at 1920×1080 and 1280×720. No reported overflow or mixed-font failures.
- Dialogue: all 1,625 spoken/narration lines measured at 40px; maximum height 109.12px inside the 112px reading area. All 225 choice labels are covered by encounter screen checks.
- Shared rooms: four actual paired-classmate arrangements from the initial schedules over days 2–28; no overlapping classmate hit regions. Images reviewed after correcting placement, scale and floor alignment.
- History: 100 populated entries, measured wrapping, both ends of the scroll area checked.
- Presentation review: all 48 world compositions and all 15 CGs inspected, along with system screens and representative dialogue, choice and hover frames. Selected real captures accompany this report.
- Source review: runtime rules, saves, dialogue, navigation and modal transitions reviewed. Removed unused date formatting and color code. No replacement framework or speculative architecture was introduced.
- Hygiene: staged text files scanned for credential patterns; private source documents, player profiles, caches and local tooling excluded from Git.
- Branding: Unity splash disabled; custom application icon assigned to all eight Windows icon sizes.

Dialogue advance/reveal is silent. Accepted menu cues are retained; quiet door and rain recordings have explicit CC0 notices. Audio playback routing is tested, but this environment cannot provide a subjective listening review. There is no voice acting.

The Windows build succeeded (375,179,556 bytes) with one Unity services warning: native debug symbols could not be uploaded. The extracted executable icon matches the custom monogram. Native mouse input was checked on title, settings, slider minimum/restore, Done, credits Return and close. Injected Escape did not confirm standalone keyboard shortcuts; hardware keyboard verification remains a limitation.

Installer verification matched all 183 installed files by hash. Uninstall succeeded and preserved the existing player saves. The portable ZIP passed a full CRC read. Artifact sizes and SHA-256 hashes are in release-package.json and the release downloads. The binaries are unsigned.
