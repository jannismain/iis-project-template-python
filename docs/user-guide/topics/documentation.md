# Documentation

Documentation is anything about your project that is not executed or used by your application or development environment.

While code is written for both humans and machines, documentation is purely written for other humans.

Each project starts with a [README](#readme) and [CHANGELOG](#changelog) file. Additional documentation, such as a user guide or reference documentation is usually written in Markdown and published using one of the [documentation tools](#documentation-tools) included with the template.

## README

The `README` included with the template only covers the bare minimum (installation, basic usage).

??? quote "`README.md`"

    {{ includex('docs/examples/default/README.md', indent=4, code=True, replace=[("```", "'''")])}}

For additional sections often found in READMEs, see [Make a README], this [README Generator] or explore [READMEs of popular GitHub projects].

[make a readme]: https://www.makeareadme.com/
[readme generator]: https://readme.so/de/editor
[readmes of popular github projects]: https://github.com/search?q=stars%3A%3E10000+path%3AREADME.md

## CHANGELOG

The `CHANGELOG` included with the template follows the [keep a changelog][] format.

??? quote "`CHANGELOG.md`"

    {{ includex('docs/examples/default/CHANGELOG.md', indent=4, code=True, replace=[("```", "'''")])}}

[keep a changelog]: https://keepachangelog.com/en/1.1.0

## API Documentation

Part of the reference documentation is a section on the API[^1] provided by your Python package or module.
While this can be hand-written, it would be hard to keep in sync with the actual implementation. Therefore, it is
usually included as [docstrings][] with the code and extracted by a third-party tool.

[^1]: For Python projects, the API includes classes and methods meant to be used by users or programs interacting with your code.
[docstrings]: https://peps.python.org/pep-0257/

## Documentation Tools

### Material for MkDocs

Projects generated with this option start with [MkDocs][] as a documentation system right out of the box, which is configured via the `./mkdocs.yaml` file to use the excellent [Material for MkDocs][] theme. Python docstrings are extracted and added as reference documentation using the [`mkdocstrings`][mkdocstrings] extension.

See the [MkDocs reference](../../reference/tooling/mkdocs.md) for more information about the MkDocs configuration provided by the template.

[material for mkdocs]: https://squidfunk.github.io/mkdocs-material/
[mkdocs]: https://www.mkdocs.org/
[mkdocstrings]: https://mkdocstrings.github.io/

### Sphinx

Projects generated with this option start with [Sphinx] as a documentation system right out of the box, which is configured via the `./conf.py` file to use the excellent [Furo] theme. [`myst`][myst] is included to add support for Markdown. Python docstrings are extracted and added as reference documentation using the [`.. automodule`][automodule] directive.

See the [Sphinx reference](../../reference/tooling/sphinx.md) for more information about the Sphinx configuration provided by the template.

[sphinx]: https://www.sphinx-doc.org
[furo]: https://github.com/pradyunsg/furo
[myst]: https://myst-parser.readthedocs.io/
[automodule]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
