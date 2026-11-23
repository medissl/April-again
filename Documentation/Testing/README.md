# Verification records

The current public results and selected rendered captures are in `Documentation/ReleaseReview`.

Full local captures and historical diagnostics live here but are excluded from version control. Editor QA saves are isolated under `Library/AprilAgainPlaytest`; real player saves remain outside the game installation. No QA unlocks or profiles are packaged.

Run `April Again/Validate rules` in the Unity Editor. `RuntimeChecks` and `PresentationChecks` provide controller, ending, text-fit, crowded-room and real camera review helpers while in Play mode. Stop Play before preparing a scene or building.

Use a clean normal Windows path for the staging build. The historical short-path alias experiment is not a valid release. See `Documentation/Implementation.md` for build and packaging tools.
