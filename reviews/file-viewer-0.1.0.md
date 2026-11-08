# File Viewer 0.1.0 (recipe)

Checked 2026-11-04 by Claude for the maintainer; automatic check (`Scripts/check-submission.py`) passed: hashes, size, schema, api 2, base digest, permissions, icon.

Base `ghcr.io/v2macapp/v2mac-base@sha256:fbe31f55…` (V2Mac Sandbox 1.2.0, Debian trixie with `trixie-security`).

1. **Source**: v2macapp/v2mac-file-viewer @ `76ad717` (tag v0.1.0).
2. **Containerfile**: `FROM ${BASE}`, copies `v2mac-lockdown.xcd` and `start.sh`. No downloads.
3. **Build**: release CI run 41390574975 (success, `76ad717`); release by github-actions[bot].
4. **Permissions**: `shared` only, how files get in; the read-write risk is spelled out in `description` and `securityNotes`. Recipe: evince, libreoffice-gtk3/-writer/-calc/-impress, fonts-noto-core; the layer holds only the `.xcd` and `start.sh`, both identical to the repo. Debian test: not recorded in this repo; `start.sh` warns when LibreOffice isn't 25.2.
5. **Launch**: `zenity` picker in Shared, then `evince` or `soffice --view` with the profile under `/tmp`. Nothing fetched.
6. **No network or VM setup.**
7. **Name and icon**: "File Viewer", a generic document icon. Not called "Safe".
8. **Changelog**: first release.

**Finding (not blocking):** the lockdown sets `Calc/Content/Update/Link` = 2, which in LibreOffice 25.2's `Calc.xcs` means *update on request*. Calc's *never* is 1; Writer's *never* is 2, which is set correctly. So "link updates locked off" holds for Writer but not for Calc. `DisableActiveContent` (finalized, true) still blocks external links, DDE and OLE in Calc, so this needs no revocation. Fix it in 0.1.1 with Calc `Link` = 1.

**Accepted**, with the 0.1.1 fix above.
