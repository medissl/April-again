# April, again — complete screenplay

The full writing milestone is complete: all five routes, all choices and epilogues, the shared opening, home transitions, and a second pass for performed character voices. The screenplay was reread for branch and prop continuity. The resulting asset plan now provides the basis for further CG, room illustration and placement-sprite production. Existing artwork is a study or UI material, not a locked story asset.

Read the generated `Screenplay/00_Common.md`, then any of the five complete route files. `Screenplay/06_Production_Notes.md` records continuity, timing, character voices and the asset list. JSON exports under `Assets/AprilAgain/Narrative` carry the same content for later Unity implementation; these are content files, not a running game.

Each route has 15 complete encounters with three written choice responses, plus good, neutral and bad epilogues. The first encounter is after the five observation-only introductions on day one. The first completed route ends a playthrough. There is no combined harem finale.

Dialogue is contemporary, readable English aimed at B2–C1 readers. Character voices come from the five supplied profiles; personal struggles are not cured by the protagonist or reduced to romance points. Japanese school life supplies the setting without requiring honorific knowledge or untranslated exposition.

Authoring sources are in `Tools/Narrative/`. Run `build_story.py` using Python to export and validate. `Narrative/validation-report.json` records content checks and the limits of verification. No Unity runtime behavior is claimed by these exports.
