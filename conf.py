project = "Linee guida di design per i servizi web della PA"
docs_italia_theme = __import__("docs-italia-theme")

html_theme = "docs_italia_theme"
html_theme_path = [docs_italia_theme.get_html_theme_path()]
html_title = project

master_doc = "index"

exclude_patterns = [
    ".venv*",
    ".tox",
]