# Python Project Template

A customizable template for new Python projects to get you up and running with current best practices faster.

## Features

- Each project has a [README][] and [CHANGELOG][] file and includes further documentation based on [Material for MkDocs][] or [Sphinx][].
- [Testing][kb_testing] and [continuous integration][ci] tooling are included from the very beginning
    - Test coverage is collected and displayed as a badge
    - Coverage report is integrated with [Gitlab's coverage report artifact][gitlab coverage report]
- Projects use [pre-commit][] for sanity checks on each commit or push
- Projects use bumpversion to increase their version according to [semantic versioning guidelines][semver]
- Python projects are installable by default and provide a simple command-line interface

[readme]: https://intern.iis.fhg.de/x/I5DPFQ
[changelog]: https://intern.iis.fhg.de/display/DOCS/Changelog
[material for mkdocs]: https://squidfunk.github.io/mkdocs-material
[sphinx]: https://www.sphinx-doc.org
[ci]: https://intern.iis.fhg.de/x/DK6qG
[kb_testing]: https://intern.iis.fhg.de/x/DS9SFw
[gitlab coverage report]: https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscoverage_report
[pre-commit]: https://pre-commit.com/
[semver]: https://semver.org/

Everything comes pre-configured with sensible defaults so you can focus on your implementation and let the template handle the rest.

See this [sample project][] to see how projects generated from this template using default values look like.

[sample project]: https://gitlab.cc-asp.fraunhofer.de/mkj/sample-project

## Getting Started

### Prerequisites

* [copier][]

*Note: If you have [pipx][] installed (you should, it is good), you can simply use `pipx run copier` out of the box.*

[copier]: https://github.com/copier-org/copier
[pipx]: https://pypa.github.io/pipx/

### Usage

```console
copier copy --trust https://gitlab.cc-asp.fraunhofer.de/mkj/project-template.git my_new_project
```

*Note: `--trust` is required because the template uses [tasks][] to setup your git repository for you.*

[tasks]: https://gitlab.cc-asp.fraunhofer.de/mkj/project-template/-/blob/main/copier.yaml

<!-- usage-end -->

## User Guide

The first part of the [user guide][] consists of tutorials on how to answer the template questions for [Your First Project][], what [Next Steps][] there are after your project is created and why the [Project Structure][] looks like it does.

[user guide]: https://mkj.pages.fraunhofer.de/project-template/user-guide/
[your first project]: https://mkj.pages.fraunhofer.de/project-template/user-guide/first-project
[next steps]: https://mkj.pages.fraunhofer.de/project-template/user-guide/first-project
[project structure]: https://mkj.pages.fraunhofer.de/project-template/user-guide/project-structure

The second part of the user guide explains how best practices, like [testing][], [documentation][], and [continuous integration][], are implemented in this template.

[testing]: https://mkj.pages.fraunhofer.de/project-template/user-guide/topics/testing
[documentation]: https://mkj.pages.fraunhofer.de/project-template/user-guide/topics/documentation
[continuous integration]: https://mkj.pages.fraunhofer.de/project-template/user-guide/topics/ci

## Known Issues

* Do not name your project `test`. It will mess with [`pytest`'s automatic test discovery mechanism](https://docs.pytest.org/explanation/goodpractices.html#conventions-for-python-test-discovery).
