# File Viewer 0.2.0 (recipe)

Checked 2026-11-08 by Claude for the maintainer; automatic check (`Scripts/check-submission.py`) passed: hashes, size, schema, api 2, base digest, permissions, icon.

Base `ghcr.io/v2macapp/v2mac-base@sha256:fbe31f55…` (V2Mac Sandbox 1.2.0, unchanged since 0.1.0).

1. **Source**: v2macapp/v2mac-file-viewer @ `52de12f` (tag v0.2.0). Diff since 0.1.0: `start.sh` opens the file it is given and, without Shared, shows a hint instead of the picker; `description`, `changelog`, `securityNotes`, README.
2. **Containerfile**: unchanged; copies `v2mac-lockdown.xcd` and `start.sh`. No downloads.
3. **Build**: release CI run 42429935079 (success, push of v0.2.0 at `52de12f`); release made by github-actions[bot].
4. **Permissions**: `shared`, now optional: without it the app gets only the opened file, read-only, with no network (V2Mac Sandbox 1.3.0, "Open a file in a sandbox app with only that file and no network"). Both cases are spelled out in `securityNotes`. Recipe unchanged; the layers hold only the `.xcd` and `start.sh`, byte-identical to the repo.
5. **Launch**: `start.sh "$1"` opens the given file with `evince` or `soffice --view`; otherwise the `zenity` picker in Shared. Nothing fetched.
6. **No network or VM setup** in the plugin; the no-network open is the runtime's.
7. **Name and icon**: unchanged.
8. **Changelog**: describes this version.

**Still open from 0.1.0 (not blocking):** Calc `Link` is still 2 (*update on request*); *never* is 1. `DisableActiveContent` still blocks external links, DDE and OLE.

**Note:** Open With and drop need V2Mac Sandbox 1.3.0. An older helper still installs 0.2.0 and offers only the Shared picker, as 0.1.0 did.

**Accepted.**
