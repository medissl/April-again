# April, again

A point-and-click school romance visual novel set at Seiran High School in Fukuoka. Five classmates, fifteen encounters each, choices with consequences, and fifteen illustrated endings.

Download the [Windows installer or portable ZIP](https://github.com/medissl/April-again/releases/latest). The installer sets up the game for your Windows account. For the ZIP, extract the entire folder and run `AprilAgain.exe`; keep its data and runtime folders beside it.

For development, open `Assets/Scenes/AprilAgain.unity` in Unity 6000.3.7f1 and press Play. The checked-in project includes the screenplay, imported assets, prepared scene and catalog. Build instructions are in `Documentation/Implementation.md`.

Click room exits or use the campus map to move. Travel and inspection are free. Small white focus marks identify inspectable targets. On the first day, observe all five classmates before going home. Later days have two three-hour activity blocks; Saturdays have three. Each classmate has one story encounter per day. The journal lists their next appointments.

Click or press Space to reveal or advance a line. Escape opens or closes menus; H hides the interface; F5 and F9 quick-save and quick-load. The labeled quick menu provides log, auto, skip, saves and settings. Skipping stops at unread dialogue and choices. The fifteenth encounter with a classmate ends the playthrough; a separate pre-finale save lets you revisit that decision. CG unlocks survive new games.

The spring-letter UI follows the user-approved classroom reference: a translucent rose reading window, centered ribbon names, an enlarged date ticket and compact controls. Nunito ExtraBold is the default font throughout the game, including system menus. The title uses the school gate without characters. Font and audio notices accompany the Windows release.

The runtime is under `Assets/AprilAgain/Scripts`. Authored screenplay sources are under `Narrative/Screenplay` and `Assets/AprilAgain/Narrative`. Generated art, audio and bindings remain separate from runtime code. Build/setup commands and verification records are documented in `Documentation/Implementation.md` and `Documentation/Testing`.

Audio source and license notes: `Documentation/AudioSources/README.md`. The game includes music, ambience and effects; it does not claim a five-person voice cast.
