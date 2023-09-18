---
tags: [Documentation]
---

# MkDocs

## Material for MkDocs

[Material for MkDocs] is a theme for [MkDocs] that adds many features to build beautiful documentation on the web.

![](https://cln.sh/MtfFQRS1+)
*Documentation of example project built with Material for MkDocs*{.caption}

Actually, this documentation happens to be built with Material for MkDocs too, so yours will likely look similar.

## Configuration

MkDocs is configured in the `mkdocs.yml` file in the root of your project.

??? quote "`mkdocs.yml`"

    {{ includex("docs/examples/mkdocs/mkdocs.yml", indent=4, code=True) }}

## Extensions

### `mkdocstrings`

[:octicons-mark-github-16: Repository][mkdocstrings] :octicons-dash-24: [:octicons-book-16: Documentation][mkdocstrings-docs]

### `mkdocs-macros`

[:octicons-mark-github-16: Repository][mkdocs-macros-github] :octicons-dash-24: [:octicons-book-16: Documentation][mkdocs-macros-docs]

Use [Jinja][] template expressions in your markdown documentation.

### `mkdocs-macros-includex`

[:octicons-mark-github-16: Repository][includex-github] :octicons-dash-24: [:octicons-book-16: Documentation][includex-docs]

Include content from any file in your repository for documentation purposes.

[material for mkdocs]: https://squidfunk.github.io/mkdocs-material/
[mkdocs]: https://www.mkdocs.org/
[jinja]: https://jinja.palletsprojects.com/templates/
[includex-github]: https://github.com/jannismain/mkdocs-macros-includex
[includex-docs]: https://jannismain.github.io/mkdocs-macros-includex
[mkdocs-macros-includex]: https://pypi.org/project/mkdocs-macros-includex/
[mkdocs-macros-github]: https://github.com/fralau/mkdocs_macros_plugin
[mkdocs-macros-docs]: https://mkdocs-macros-plugin.readthedocs.io/
[mkdocstrings]: https://github.com/mkdocstrings/mkdocstrings
[mkdocstrings-docs]: https://mkdocstrings.github.io/
