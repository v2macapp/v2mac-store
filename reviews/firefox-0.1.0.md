# Firefox ESR 0.1.0 (recipe)

Checked 2026-11-04 by Claude for the maintainer; automatic check (`Scripts/check-submission.py`) passed: hashes, size, schema, api 2, base digest, permissions, icon.

Base `ghcr.io/v2macapp/v2mac-base@sha256:fbe31f55…` (V2Mac Sandbox 1.2.0, Debian trixie with `trixie-security`).

1. **Source**: v2macapp/v2mac-firefox @ `69cb5f4` (tag v0.1.0).
2. **Containerfile**: `FROM ${BASE}`, copies `policies.json` and `start.sh`. No downloads.
3. **Build**: release CI run 41390568494 (success, `69cb5f4`); release by github-actions[bot].
4. **Permissions**: clipboard, shared, sound, microphone, explained. Recipe: `firefox-esr`, `fonts-noto-color-emoji`; the layer holds only `policies.json` and `start.sh`, both identical to the repo. Debian test: not recorded in this repo; `start.sh` warns when the ESR major isn't 153.
5. **Launch**: `start.sh` reads only numbers from `exit.json` for the geolocation URL (no injection), writes `user.js`, runs `firefox-esr --no-remote --profile`. Nothing fetched.
6. **No network or VM setup.** Policies: telemetry and studies off; WebRTC `no_host` and `default_address_only` locked; geoclue and gpsd off.
7. **Name and icon**: "Firefox ESR" is Debian's package name, and the icon is a generic globe, not Mozilla's logo.
8. **Changelog**: first release, matches.

**Accepted.**
