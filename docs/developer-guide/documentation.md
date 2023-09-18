# Documentation

This project uses MkDocs with the Material for MkDocs theme.

## Configuration

??? quote "`mkdocs.yaml` Configuration File"

    {{ includex('mkdocs.yaml', indent=4, code=True) }}

## Navigation

The navigation is setup using [:octicons-cpu-24:`mkdocs-literate-nav`](https://github.com/oprypin/mkdocs-literate-nav) and managed in the `_nav.md` file:

{{ includex('docs/_nav.md', code=True) }}

## Macros

[Jinja macros][jinja] are provided by [:octicons-cpu-24:`mkdocs-macros`](https://github.com/fralau/mkdocs_macros_plugin) and can be configured via the `macros.py` file:

??? quote "`docs/util/macros.py`"

    {{ includex('docs/util/macros.py', indent=4, code=True) }}

[jinja]: https://jinja.palletsprojects.com/
