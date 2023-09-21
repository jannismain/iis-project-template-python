<div align=center>
<h1>Python Project Template</h1>

[![](https://img.shields.io/badge/Documentation-main-blue)][docs]
[![](https://img.shields.io/badge/Example-Sample_Project-blue)][sample project]
[![PyPI - Version](https://img.shields.io/pypi/v/init-python-project)][pypi]

</div>

[pypi]: https://pypi.org/project/init-python-project/

<!-- start -->

A customizable template for new Python projects to get you up and running with current best practices faster.

## Features

- Each project has a *README* and *CHANGELOG* file and includes further documentation based on [Material for MkDocs][] or [Sphinx][].
- *Testing* and *continuous integration* tooling are included from the very beginning
    - Test coverage is collected and displayed as a badge
    - Coverage report is integrated with [Gitlab's coverage report artifact][gitlab coverage report]
- Projects use [pre-commit][] for sanity checks on each commit or push
- Projects use bumpversion to increase their version according to [semantic versioning guidelines][semver]
- Python projects are installable by default and provide a simple command-line interface

[material for mkdocs]: https://squidfunk.github.io/mkdocs-material
[sphinx]: https://www.sphinx-doc.org
[gitlab coverage report]: https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscoverage_report
[pre-commit]: https://pre-commit.com/
[semver]: https://semver.org/

Everything comes pre-configured with sensible defaults so you can focus on your implementation and let the template handle the rest.

See the [sample project][] to see how projects generated from this template using default values look like.

[sample project]: https://gitlab.cc-asp.fraunhofer.de/mkj/sample-project

## Getting Started

### Prerequisites

* Python3.11 or newer

### Installation

```sh
pip install init-python-project
```

*Note: If you have [pipx][] installed (you should, it is good), you can skip this step and instead run it directly using `pipx run init-python-project`*

[pipx]: https://pypa.github.io/pipx/

### Usage

```console
init-python-project <name of project>
```

<!-- usage-end -->

## User Guide

The first part of the user guide consists of tutorials on how to answer the template questions for [Your First Project][], what [Next Steps][] there are after your project is created and why the [Project Structure][] looks like it does.

[your first project]: https://mkj.pages.fraunhofer.de/project-template/user-guide/first-project
[next steps]: https://mkj.pages.fraunhofer.de/project-template/user-guide/first-project
[project structure]: https://mkj.pages.fraunhofer.de/project-template/user-guide/project-structure
[docs]: https://mkj.pages.fraunhofer.de/project-template/

The second part of the user guide explains how best practices, like [testing][], [documentation][], and [continuous integration][], are implemented in this template.

[testing]: https://mkj.pages.fraunhofer.de/project-template/user-guide/topics/testing
[documentation]: https://mkj.pages.fraunhofer.de/project-template/user-guide/topics/documentation
[continuous integration]: https://mkj.pages.fraunhofer.de/project-template/user-guide/topics/ci

## Known Issues

* Do not name your project `test`. It will mess with [`pytest`'s automatic test discovery mechanism](https://docs.pytest.org/explanation/goodpractices.html#conventions-for-python-test-discovery).
