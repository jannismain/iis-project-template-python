# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Started this template by forking [pypa/sampleproject] and converting it to a copier template.

An example project (comparable to [pypa/sampleproject]) can be found at [jannismain/python-project-template-example].

### Added

- CHANGELOG proposal from [jimustafa](https://github.com/jimustafa) in [!185](https://github.com/pypa/sampleproject/pull/185)
- added `__main__` and `cli` modules (based on discussion of [!67](https://github.com/pypa/sampleproject/pull/67))
  - the project script can now be executed additionally via `python -m sample`
- Tooling
    - add option to use `bumpversion`
    - add option to use `pre-commit`
    - add option to choose between MkDocs and Sphinx documentation
    - `remote` option ('github' (default), 'gitlab-fhg', 'gitlab-iis')
        - if `gitlab-*` is selected, Gitlab CI configuration is added
        - if `github` is selected, GitHub actions are added
    - add Gitlab CI configuration to
        - run tests
        - collect test coverage and publish it as [Gitlab report artefact](https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscoverage_report)
        - calculate maintainability metric
        - generate badges that are shown in the README
        - generate documentation and publish via [Gitlab Pages](https://docs.gitlab.com/ee/user/project/pages/)
    - add Github Actions configuration to
        - generate documentation and publish via [Github Pages](https://pages.github.com/)
    - default branch option (default: main)

### Changed

- convert to a copier template
- tests are executed using pytest (was unittest)

### Removed

- trove classifiers (only relevant when publishing to PyPI)

<!-- [unreleased]: https://github.com/jannismain/python-project-template/compare/v0.0.2...HEAD -->
<!-- [0.0.2]: https://github.com/jannismain/python-project-template/compare/v0.0.1...v0.0.2 -->
<!-- [0.0.1]: https://github.com/jannismain/python-project-template/releases/tag/v0.0.1 -->

[pypa/sampleproject]: https://github.com/pypa/sampleproject
[jannismain/python-project-template-example]: https://github.com/jannismain/python-project-template-example
