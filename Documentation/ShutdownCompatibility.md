# Windows shutdown compatibility

The final native check reproduced a shutdown crash in Unity 6000.3.7f1 after a Windows UI Automation client had inspected the player. Both a full gameplay session and a fresh title-screen-only session reproduced it. The save completed first; no managed exception preceded the native window-message stack.

Unity documents this exact class of failure as UUM-146676 and includes the fix in [6000.3.21f1](https://unity.com/releases/editor/whats-new/6000.3.21f1). The release build therefore uses that stable patch in the same 6.3 LTS line. A fresh native test must exercise the player through UI Automation and then check the process exit code and complete log after quitting. Merely observing that the window disappeared is insufficient.

The Windows build explicitly uses Direct3D 11, matching the graphics API used for the verified 2D presentation. Existing source assets, screenplay and save locations are preserved. No process-kill workaround or accessibility disabling is added to the game.

The final engine version, native exit result and package hashes are recorded under `Documentation/ReleaseReview` after rebuilding. Earlier 6.3.7 shutdown logs remain private diagnostics under `Documentation/Testing`.
