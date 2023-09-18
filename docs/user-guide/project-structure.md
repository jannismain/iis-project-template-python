# Project Structure

Depending on which options you selected, your project initially consists of the following files and folders:

=== "minimal"

    ```
    {{ run("tree -a -I .git -I *.egg-info -I .venv -I __pycache__ docs/examples/minimal/") | indent(4) }}
    ```

=== "default"

    ```
    {{ run("tree -a -I .git -I *.egg-info -I .venv -I __pycache__ docs/examples/default/") | indent(4) }}
    ```

=== "full"

    ```
    {{ run("tree -a -I .git -I *.egg-info -I .venv -I __pycache__ docs/examples/full/") | indent(4) }}
    ```

## Python-specific files

The Python project structure consists of the following elements

```
{{ run("tree -L 3 -P *.py -I docs -P pyproject.toml --gitfile .gitignore --noreport docs/examples/default/") }}
```

* `pyproject.toml`: The main responsibility of this file is to declare the [build system][] needed to build your Python package (`[build-system]`) as well as package metadata (in the `[project]` section). However, many Python tools support reading their configuration from this file. These sections are prefixed by `[tool.*]`
* `src`: folder that contains Python packages (folders that contain at least an `__init__.py` file) and modules (files ending in `.py`)
* `tests`: folder that contains tests of your Python code

While other structures are possible, this one has proven itself (and it also the one suggested by the [Python Packaging Authority][pypa] in their [Python Packaging User Guide][] and corresponding [sample project][pypa sample project]). Modern Python packaging tools, like setuptools, will recognize this convention and require no further configuration.

[build system]: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
[pypa]: https://www.pypa.io/en/latest/
[pypa sample project]: https://github.com/pypa/sampleproject
[Python Packaging User Guide]: https://packaging.python.org/en/latest/tutorials/packaging-projects/
