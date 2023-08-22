---
tags: [Documentation]
---

# Sphinx

[Sphinx] is a popular documentation tool for Python projects.

=== "Light Mode"

    ![](https://cln.sh/Fxw2BrHM+)
    *Preview of Documentation built with Sphinx using the Furo theme in light mode*{.caption}


=== "Dark Mode"

    ![](https://cln.sh/vmXwr1mX+)
    *Preview of Documentation built with Sphinx using the Furo theme in dark mode*{.caption}

{{ includex("README.md", start_match="<!-- refs -->") }}

## Configuration

Sphinx is configured via a `conf.py` file.

??? quote "`docs/conf.py`"

    {{ includex('docs/examples/sphinx/docs/conf.py', indent=4, lang='py')}}

See [Sphinx Configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html) for a list of supported options.

## Extensions

### myst_parser
