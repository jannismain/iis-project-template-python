---
tags: [Documentation]
---

# Sphinx

[Sphinx] is a popular documentation tool for Python projects.

=== "Light Mode"

    ![](https://cln.sh/Fxw2BrHM+)
    *Preview of Documentation built with Sphinx using the [Furo] theme in light mode*{.caption}

=== "Dark Mode"

    ![](https://cln.sh/vmXwr1mX+)
    *Preview of Documentation built with Sphinx using the [Furo] theme in dark mode*{.caption}

## Configuration

Sphinx is configured via a `conf.py` file.

??? quote "`docs/conf.py`"

    {{ includex('docs/examples/sphinx/docs/conf.py', indent=4, code=True)}}

See [Sphinx Configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html) for a list of supported options.

## Extensions

### myst_parser

[:octicons-book-16: Documentation][myst-parser]

> MyST - Markedly Structured Text - Parser
>
> A Sphinx and Docutils extension to parse MyST, a rich and extensible flavour of Markdown for authoring technical and scientific documentation.

This extension of CommonMark allows for integration of markup previously only available when using reStructuredText.

[sphinx]: https://www.sphinx-doc.org
[furo]: https://github.com/pradyunsg/furo
[myst]: https://myst-parser.readthedocs.io/
[automodule]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[myst-parser]: https://myst-parser.readthedocs.io
