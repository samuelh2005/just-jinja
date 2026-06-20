from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from yaml import safe_load

env = Environment(loader=FileSystemLoader(["pages", "templates"]))
pages_dir = Path("pages")

config_path = Path("site.yaml")
with open(config_path, "r") as f:
    config = safe_load(f)

Path("dist").mkdir(exist_ok=True)

def render_template(template_path: Path, name: str):
    template = env.get_template(template_path.name)

    html = template.render(
        config=config
    )
    Path(f"dist/{name}.html").write_text(html, encoding="utf-8")

for page in pages_dir.glob("*.html"):
    render_template(page, page.stem)
