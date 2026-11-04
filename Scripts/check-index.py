"""Fail when an accepted submission is missing from the signed index (security plan S1.4).

Usage: check-index.py [--selftest]
Every submissions/<id>.json on the branch is an accepted plugin: index.json must list a plugin from that
repo whose layers are assets of that tag's release, and index.json.sig must exist. Offline: it reads
only this repo. Whether the signature is valid is the helper's check (it pins key.pub).
"""
import glob, json, os, sys

ROOT = os.path.join(os.path.dirname(__file__), "..")

def missing(submissions, index):
    """The submissions (path -> {repo, tag}) that no plugin in the index comes from."""
    out = []
    for path, sub in sorted(submissions.items()):
        repo, release = sub["repo"].rstrip("/"), f"{sub['repo'].rstrip('/')}/releases/download/{sub['tag']}/"
        if not any((p.get("source") or {}).get("repo") == repo and p.get("layers") and
                   all(str(l.get("url", "")).startswith(release) for l in p["layers"]) for p in index["plugins"]):
            out.append(f"{path}: {repo} @ {sub['tag']} is not in index.json")
    return out

def selftest():
    p = {"source": {"repo": "https://github.com/a/b"}, "layers": [{"url": "https://github.com/a/b/releases/download/v2/x.tar.gz"}]}
    assert missing({"s.json": {"repo": "https://github.com/a/b", "tag": "v2"}}, {"plugins": [p]}) == []
    for sub in [{"repo": "https://github.com/a/b", "tag": "v1"}, {"repo": "https://github.com/c/b", "tag": "v2"}]:
        assert missing({"s.json": sub}, {"plugins": [p]}), sub
    assert missing({"s.json": {"repo": "https://github.com/a/b", "tag": "v2"}}, {"plugins": [{**p, "layers": []}]})
    print("selftest ok")

if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]: selftest(); sys.exit(0)
    subs = {os.path.relpath(f, ROOT): json.load(open(f)) for f in glob.glob(os.path.join(ROOT, "submissions", "*.json"))}
    found = missing(subs, json.load(open(os.path.join(ROOT, "index.json"))))
    if not os.path.exists(os.path.join(ROOT, "index.json.sig")): found.append("index.json.sig is missing: sign the index")
    print("\n".join(found) or f"all {len(subs)} submissions are in the signed index")
    sys.exit(1 if found else 0)
