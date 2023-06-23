# IIS Project Template for Python

An opinionated project template for Python projects.

## Features

* Each project has a [README][] and [CHANGELOG][] file
* [Testing][] and [continuous integration][ci] tooling are included from the very beginning
  * Test coverage is collected and displayed as a badge
  * Coverage report is integrated with [Gitlab's coverage report artifact][gitlab coverage report]
* Projects are documented using [MkDocs][] with the [Material for MkDocs][] theme
* Projects use [pre-commit][] to ensure adherence to a [coding style][] on the client side
* Projects use bumpversion to increase their version according to [semantic versioning guidelines][semver]
* Python projects are installable

See this [sample project](https://git01.iis.fhg.de/mkj/sample-project) to see how projects generated from this template look like.

## Getting Started

### Prerequisites

* [copier](https://github.com/copier-org/copier)

*Note: If you have [`pipx`][pipx] installed (you should, it is good), you can simply use `pipx run copier` out of the box.*

### Usage

```console
mkdir my_new_project
copier copy --UNSAFE https://git01.iis.fhg.de/mkj/iis-project-template.git my_new_project
```

*Note: the `--UNSAFE` flag is required because the template uses [tasks][] to setup your git repository for you.*

[tasks]: https://git01.iis.fhg.de/mkj/iis-project-template/-/blob/main/copier.yaml#L32

### Next Steps

#### Configure Remote Repository

During the project creation, you will be asked about the Gitlab remote url where your project will be pushed to. You can take that moment to create a new project in Gitlab and copy its link into the questionnaire. You can also change this value later by modifying the git remote associated with your project

```sh
git config remote.origin.url <url_to_project>
```

If your remote repository is created and configured, you can create an initial commit and push it to your remote

```sh
git add .
git commit -m "initial commit"
git push -u origin main
```

#### Install Project

The new project is installable right away. Create a virtual environment using any method you like, for example using the builtin `venv` module:

```sh
python -m venv env
source env/bin/activate
```

Now you can use `make install-dev`, to install your Python project in-place with all optional dev requirements.

#### Start Implementing

Now you are ready to start your implementation. As a quick reference, Python packages and modules go into `./src/`, documentation into `./docs/` and tests into `./tests/`.

## Template Features

### Python Project Layout

The Python project structure consists of the following elements

* [`./pyproject.toml`][pyproject.toml]: Python package configuration
* `./src/`: folder that contains the Python packages and modules you want to develop
* `./test/`: folder that contains tests of your Python code

While other structures are possible, this one has proven itself (and it also the one suggested by the [Python Packaging Authority][pypa] in their [Python Packaging User Guide][] and corresponding [sample project][pypa sample project]). Modern Python packaging tools, like setuptools, will recognize this project structure without further need for configuration.

### Command Line Interface

An example command line interface is included in the `./src/cli.py` module.

### Testing and CI

Python tests are implemented using [pytest][] in the `./test/` subdirectory. Each test module starts with `test_` so it is automatically discovered when running `pytest`.

These tests are also executed as part of a [Gitlab continuous integration][gitlab ci] pipeline, which is configured via the [`.gitlab-ci.yml`][.gitlab-ci.yml] file.

### Documentation

Projects generated from this template start with [MkDocs][] as a documentation system right out of the box, which is configured via the `./mkdocs.yaml` file to use the excellent [Material for MkDocs][] theme. Python docstrings are extracted and added as reference documentation using the [`mkdocstrings`][mkdocstrings] extension.

In addition, projects start with a [README][] and [CHANGELOG][] file.

Learn more about [good documentation practices][documentation].

[pre-commit]: https://pre-commit.com/
[semver]: https://semver.org/
[mkdocs]: https://www.mkdocs.org/
[material for mkdocs]: https://squidfunk.github.io/mkdocs-material/
[mkdocstrings]: https://mkdocstrings.github.io/
[pytest]: https://pytest.org/
[gitlab ci]: https://docs.gitlab.com/ee/ci/
[.gitlab-ci.yml]: https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html
[gitlab coverage report]: https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscoverage_report
[mypy]: https://mypy.readthedocs.io/
[pipx]: https://pypa.github.io/pipx/

[readme]: https://intern.iis.fhg.de/x/I5DPFQ
[changelog]: https://intern.iis.fhg.de/x/7jCzFQ
[testing]: https://intern.iis.fhg.de/x/DS9SFw
[ci]: https://intern.iis.fhg.de/x/DK6qG
[coding style]: https://intern.iis.fhg.de/x/ig6QFg
[documentation]: https://intern.iis.fhg.de/x/YoplGQ

[pyproject.toml]: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
[pypa]: https://www.pypa.io/en/latest/
[pypa sample project]: https://github.com/pypa/sampleproject
[Python Packaging User Guide]: https://packaging.python.org/en/latest/tutorials/packaging-projects/
