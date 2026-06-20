from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from yaml import safe_load

PAGES_DIR = Path("pages")
TEMPLATES_DIR = Path("templates")
DIST_DIR = Path("dist")
CONFIG_PATH = Path("site.yaml")

env = Environment(
    loader=FileSystemLoader([
        str(PAGES_DIR),
        str(TEMPLATES_DIR)
    ])
)

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = safe_load(f)

DIST_DIR.mkdir(exist_ok=True)


def page_url(path: Path) -> str:
    """
    Convert pages/foo/bar.html -> /foo/bar/
    Convert pages/index.html -> /
    """
    rel = path.relative_to(PAGES_DIR)
    url = "/" + str(rel).replace("\\", "/")

    if url.endswith("/index.html"):
        url = url[:-10]
        if url == "":
            url = "/"

    return url


def output_path_for(page_path: Path) -> Path:
    """
    Preserve folder structure in dist/
    """
    rel = page_path.relative_to(PAGES_DIR)
    return DIST_DIR / rel


def template_name(page_path: Path) -> str:
    """
    Resolve template relative to loader roots.
    Pages are rendered as templates directly.
    """
    return str(page_path.relative_to(PAGES_DIR)).replace("\\", "/")


def render_page(page_path: Path):
    template = env.get_template(template_name(page_path))

    current_url = page_url(page_path)

    html = template.render(
        config=config,
        current_url=current_url
    )

    out_path = output_path_for(page_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_path.write_text(html, encoding="utf-8")


def build():
    for page in PAGES_DIR.rglob("*.html"):
        render_page(page)


if __name__ == "__main__":
    build()
