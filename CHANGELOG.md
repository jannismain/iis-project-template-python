# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Started this template by forking [pypa/sampleproject](https://github.com/pypa/sampleproject) and converting it to a copier template.

### Added

- CHANGELOG [jimustafa](https://github.com/jimustafa)[!185](https://github.com/pypa/sampleproject/pull/185)
- added `__main__` and `cli` modules (based on discussion of [!67](https://github.com/pypa/sampleproject/pull/67))
  - the project script can now be executed additionally via `python -m sample`
- add option to use `bumpversion`
- add option to use `pre-commit`

### Changed

- convert to a copier template
- tests are executed using pytest (was unittest)

### Removed

- trove classifiers (only relevant when publishing to PyPI)

<!-- [unreleased]: https://github.com/jannismain/pypa-sampleproject/compare/v0.0.2...HEAD -->
<!-- [0.0.2]: https://github.com/jannismain/pypa-sampleproject/compare/v0.0.1...v0.0.2 -->
<!-- [0.0.1]: https://github.com/jannismain/pypa-sampleproject/releases/tag/v0.0.1 -->
