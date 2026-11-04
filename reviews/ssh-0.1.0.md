# SSH 0.1.0 (recipe)

Checked 2026-11-04 by Claude for the maintainer; automatic check (`Scripts/check-submission.py`) passed: hashes, size, schema, api 2, base digest, permissions, icon.

Base `ghcr.io/v2macapp/v2mac-base@sha256:fbe31f55…` (V2Mac Sandbox 1.2.0, Debian trixie with `trixie-security`).

1. **Source**: v2macapp/v2mac-ssh @ `6977cea` (tag v0.1.0).
2. **Containerfile**: `FROM ${BASE}`, copies `start.sh`. No downloads.
3. **Build**: release CI run 41390573369 (success, `6977cea`); release by github-actions[bot].
4. **Permissions**: `ssh-agent` only, the point of the app. Recipe: `openssh-client`; the layer holds only `start.sh`, identical to the repo. Debian test: not recorded in this repo.
5. **Launch**: prompt loop. A target starting with `-` is refused, and `ssh -o ForwardAgent=no -- "$target"` keeps the Mac's keys off the server. An empty answer opens `bash -l` inside the container.
6. **No network or VM setup.**
7. **Name and icon**: "SSH", a generic terminal-prompt icon.
8. **Changelog**: first release, matches.

**Accepted.**
