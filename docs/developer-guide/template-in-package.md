# Template in Package

## Summary

- use `make copy-template` before building a package.
- use `make link-template` during development with an in-place installation.

## Explanation

Copier templates require a `copier.yaml` in the root of the git project in order to be discovered during `copier copy gh:jannismain/python-project-template`.

However, for distribution of the template as a Python package, the template files need to be part of the Python package in `src/init_python_project/`.
So when building a package using `make build`, the template files are copied into the package using `make copy-template`.

During development, a copy is impractical, as changes to the template are not picked up by `init-python-project`, which still uses the (now out-of-date) copy inside the package. For this reason, it is useful to *link* the template into the package using `make link-template`. Those symbolic links are not supported when building a Python package, so they are replaced the next time a package is created.
