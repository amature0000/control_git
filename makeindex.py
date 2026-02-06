import subprocess
from pathlib import Path

BASE = Path("resource")

def last_modified(path):
    cmd = ["git", "log", "-1", "--format=%ad", "--date=short", "--", str(path)]
    try:
        return subprocess.check_output(cmd).decode().strip()
    except:
        return "-"

sections = []

for topic in sorted(BASE.iterdir()):
    if not topic.is_dir():
        continue

    rows = []

    for file in sorted(topic.glob("*.zip")):
        date = last_modified(file)

        rows.append(f"""
        <li>
            <a href="{file}">{file.name}</a>
            <small>({date})</small>
        </li>
        """)

    if not rows:
        continue

    sections.append(f"""
    <h2>{topic.name}</h2>
    <ul>
        {''.join(rows)}
    </ul>
    """)

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Downloads</title>
<style>
body {{
    font-family: sans-serif;
    max-width: 800px;
    margin: auto;
}}
h2 {{
    margin-top: 40px;
}}
li {{
    margin: 6px 0;
}}
</style>
</head>
<body>
<h1>Download Center</h1>
{''.join(sections)}
</body>
</html>
"""

Path("index.html").write_text(html, encoding="utf-8")
