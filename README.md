# Just Jinja

Just Jinja is a simple static site generator built on top of Jinja2.

## Requirements

- Python 3.7 or higher
- Jinja2 `pip install jinja2`
- PyYAML `pip install pyyaml`

## Usage

To use Just Jinja, create a directory structure like this:

```
.
├── templates/
|   ├── base.html
│   └── ... more templates
├── pages/
|   ├── index.html
|   ├── page.html
│   └── ... more pages
└── site.yaml
```

Its entirely up to you where you do inheritance and how you want to structure your templates and pages, Just Jinja will find them all.

Then run the following command:

```
python justjj.py
```

This will generate a `dist/` directory with the rendered HTML files, which you may serve with any static file server, such as Python's built-in HTTP server, Nginx, or anything else.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
