# Visual novel interaction research

Ren'Py's production documentation supplies useful, engine-independent conventions: explicit save/load screens, backlog/history, text speed and auto-forward preferences, separate sound/music levels, and skipping read text while stopping at choices. April, again follows those reading conventions while keeping its navigation, calendar and scoring in Unity.

Primary references:

- https://www.renpy.org/doc/html/gui.html — dialogue, choices, navigation and game menus.
- https://www.renpy.org/doc/html/preferences.html — text speed, auto-forward and skipping preferences.
- https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-CanvasScaler.html — resolution-independent UI scale.
- Installed uGUI/TMP documentation under `Library/PackageCache/com.unity.ugui@11343a6274f3/Documentation~` — canvas, event system and text rendering.
- https://kenney.nl/assets/interface-sounds — small readable interface cues, CC0.

The user's example informs the rose/white palette and reading hierarchy; its exact graphics are not copied. Inspectable room targets receive a soft white hover/focus wash and a clear label. The journal exposes appointments and the map exposes current locations, avoiding blind searching or hidden travel penalties.
