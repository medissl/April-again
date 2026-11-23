# April, again — production art pack

This directory contains the illustration and interface library for the authored game. The original manifest records 106 selected illustration masters and 395 exported bindings, including crops and native UI graphics. The current compiled catalog source adds 41 conversation-expression exports and 43 Spring UI/icon records for 479 bindings total. These counts do not mean 479 separately generated illustrations. Original masters and unused studies remain preserved.

Use `asset-manifest.json` for file identities, dimensions and hashes; `scene-bindings.json` for all 75 encounters and first-day observations; `Map/map-layout.json` for the campus; `Rooms/room-hotspots.json` for the clickable character regions. All 15 ending CGs are named by character and ending. Expression aliases consolidate the screenplay's acting directions without changing identity.

Character sprites and props use transparent PNG. Room illustrations already contain their character; do not stack multiple full-room images. Additional occupants use transparent exploration poses. Background labels, dialogue and controls remain live text.

Original generation prompts, provenance catalogs, review contact sheets and screen proofs are preserved under `Documentation/Art`. The game runtime uses `GameData/GameCatalog.asset`; rebuild its content with `Tools/Game/build_content.py` and the Unity menu `April Again/Prepare game`.

Nunito ExtraBold is the default across the game and TMP settings. Its official variable source, static-instance process and SIL Open Font License are in Fonts/Nunito. Earlier Source Sans 3, Source Serif 4 and Zen Maru comparisons remain archived with their notices. The user's visual references are direction only and are not shipped as sprites. The generated cast-title study was removed from Assets because the user requested a girl-free main menu.
