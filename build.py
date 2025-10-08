#!/usr/bin/env python3

from pathlib import Path
from ryland import Ryland
from ryland.tubes import load, markdown


VAULT_NAME = "Example Ryland Vault"

ryland = Ryland(__file__)

ryland.clear_output()

ryland.global_context["vault_name"] = VAULT_NAME

PANTRY_DIR = Path(__file__).parent / "pantry"

ryland.copy_to_output(PANTRY_DIR / "style.css")
ryland.add_hash("style.css")

ryland.render_template("404.html", "404.html")

VAULT_DIR = Path(__file__).parent / "vault" / VAULT_NAME


for page_file in VAULT_DIR.glob("*.md"):
    ryland.render(
        load(page_file),
        markdown(frontmatter=True),
        {"page_title": page_file.stem},
        {"url": f"/{page_file.stem}/"},
        {"template_name": "page.html"},
    )
