# Chromium 0.3.1 (recipe)

Checked 2026-11-08 by Claude for the maintainer; automatic check (`Scripts/check-submission.py`) passed: hashes, size, schema, api 2, base digest, permissions, icon.

Base `ghcr.io/v2macapp/v2mac-base@sha256:fbe31f55…` (V2Mac Sandbox 1.2.0, unchanged since 0.3.0).

1. **Source**: v2macapp/v2mac-chromium @ `8a6f75f` (tag v0.3.1). Diff since 0.3.0: `securityNotes`, `changelog`, a comment in `start.sh`, README.
2. **Containerfile**: unchanged; `FROM ${BASE}`, copies `start.sh`. No downloads.
3. **Build**: release CI run 42429932131 (success, push of v0.3.1 at `8a6f75f`); release made by github-actions[bot].
4. **Permissions**: unchanged (clipboard, shared, sound, microphone). Recipe unchanged: `chromium`, `fonts-noto-color-emoji`; the layer holds only `/usr/local/bin/start.sh`, byte-identical to the repo.
5. **Launch**: unchanged; `chromium --no-sandbox`, now explained first in `securityNotes`.
6. **No network or VM setup.**
7. **Name and icon**: unchanged.
8. **Changelog**: describes this version (Security Notes wording only).

**Accepted.**
