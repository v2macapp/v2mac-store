# Chromium 0.3.0 (recipe)

Checked 2026-11-04 by Claude for the maintainer; automatic check (`Scripts/check-submission.py`) passed: hashes, size, schema, api 2, base digest, permissions, icon.

Base `ghcr.io/v2macapp/v2mac-base@sha256:fbe31f55…` (V2Mac Sandbox 1.2.0, Debian trixie with `trixie-security`).

1. **Source**: v2macapp/v2mac-chromium @ `d27bb01` (tag v0.3.0), read at that commit.
2. **Containerfile**: `FROM ${BASE}`, copies `start.sh`, `chmod`. No downloads.
3. **Build**: release CI run 41390565081 (success, push of v0.3.0 at `d27bb01`); release made by github-actions[bot].
4. **Permissions**: clipboard, shared, sound, microphone, each explained in `securityNotes`. Recipe: `chromium`, `fonts-noto-color-emoji`; the layer holds only `/usr/local/bin/start.sh`, byte-identical to the repo. Debian test: S1.3 (0.2.0 → 0.3.0 upgrade in a VM).
5. **Launch**: `start.sh` turns off sway fullscreen, takes a `flock` on the profile, runs `chromium --no-sandbox` (stated in `securityNotes`). Nothing fetched at runtime.
6. **No network or VM setup.**
7. **Name and icon**: "Chromium", an abstract circle icon, not Google's logo.
8. **Changelog** matches the diff since 0.2.0: apt step moved to `packages`, api 1 → 2, new base. `start.sh` unchanged.

**Accepted.**
