# V2Mac Store

The signed plugin index for [V2Mac's Secure Sandbox](https://v2macapp.github.io/sandbox/): the apps you can install from the Sandbox window, each running in its own mini VM.

- `index.json` lists every plugin with its pinned commit and layer hashes. `index.json.sig` is its Ed25519 signature, checked against `key.pub`.
- `bases.json` lists the released base images a plugin may build on.

## Submit a plugin

Build one from [v2mac-plugin-template](https://github.com/v2macapp/v2mac-plugin-template), then open a pull request adding `submissions/<id>.json`:

```json
{"repo": "https://github.com/<you>/<repo>", "tag": "<tag>"}
```

CI checks the release and comments a report. A maintainer then reviews it against [REVIEW.md](REVIEW.md) before merging and signing the index.
