"""Refresh the 'Recently updated' section of the profile README.

Lists the most recently pushed public, non-archived, non-fork repos with
their latest commit subject. Runs daily from .github/workflows/refresh-profile.yml.
"""
import json
import os
import re
import urllib.request
from datetime import datetime

USER = "abdihakim-said"
SKIP = {"abdihakim-said", "abdihakim-said.github.io"}
LIMIT = 5
START, END = "<!-- RECENT:START -->", "<!-- RECENT:END -->"


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    repos = [
        r for r in api(f"/users/{USER}/repos?per_page=100&type=owner&sort=pushed")
        if not r["archived"] and not r["fork"] and r["name"].lower() not in SKIP
    ]
    repos.sort(key=lambda r: r["pushed_at"], reverse=True)

    lines = []
    for r in repos[:LIMIT]:
        commits = api(f"/repos/{USER}/{r['name']}/commits?per_page=1")
        subject = commits[0]["commit"]["message"].splitlines()[0] if commits else ""
        subject = re.sub(r"\s*\[skip ci\]\s*", " ", subject).strip()
        if len(subject) > 90:
            subject = subject[:87].rstrip() + "..."
        date = datetime.strptime(r["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y")
        lines.append(f"- **[{r['name']}]({r['html_url']})** · {date}<br><sub>{subject}</sub>")

    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    path = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
    readme = open(path).read()
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), block, readme, flags=re.S)
    if new != readme:
        open(path, "w").write(new)
        print("README updated")
    else:
        print("No change")


if __name__ == "__main__":
    main()
