# Final presentation pass — 23 November 2026

The approved direction is rose and ivory stationery with Nunito ExtraBold, natural anime environments, centered speaker ribbons and a translucent reading window. The main menu shows the school gate without characters. Reference artwork was used for direction and is not redistributed as game art.

The final pass replaced malformed generated buttons, choice plates and hover tags with original editable SVG/PNG geometry in Art/UI/Final. The reading window, wordmark, ribbon and floral frame retain the approved illustrated components. The enlarged calendar holds date, weekday and location within its border.

Door targets have one hit region, a small resting marker and one hover caption. The map uses permanent room labels and a border hover state. Duplicate destination captions and white rectangle washes were removed. Physical door targets follow the visible artwork; other wings are available through the map. Class C's noticeboard target and the corridor's window targets were fixed. Classmates take input priority over exits. Choice screens use full-height sprites so portrait crops do not end visibly above the floor.

System panels hide the underlying HUD. Save and gallery previews preserve illustration aspect ratio. Populated history uses measured text heights. Sliders start flush with the track. Ending credits return to a visible title screen.

The user's final screenshot review caught headings and close buttons sitting on the illustrated border. The first layout checks measured text fit but did not enforce space from the artwork. The corrected shared header starts at y104, close controls sit inside the paper clear of the fold, and body content begins at y208 or later. The map reserves a separate header and a 1280×720 illustration. All system pages now have explicit interior side/bottom bounds. Message height follows actual text measurement; inspection and classmate thumbnails are centered within their rectangles. World interaction markers are hidden behind modal pages. These constraints are checked separately from text fitting and visually reviewed at both output sizes.

Dialogue reveal and advance are silent. Existing accepted menu cues remain. Quiet door and rain recordings have explicit CC0 provenance and release notices.

Real camera captures and layout checks cover all 48 world illustrations, menus, 75 encounter/choice screens and 15 ending/credits branches at 1080p and 720p. Curated public evidence is in Documentation/ReleaseReview.

The Windows source path contains a comma. A clean, normal, comma-free staging copy fixes the Unity linker issue. The earlier 8.3 short-path experiment caused broken script serialization and was abandoned. Build with the provided staging scripts.
