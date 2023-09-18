# Task Execution

Recurring tasks, such as running the test suite, generating a coverage report or previewing the documentation locally should be easy to do for any developer.

Therefore, a unified way of running those tasks is preferable over remembering the command for each of those tasks. Especially when these commands  differ across projects, a common way of calling them without remembering their exact syntax reduces the mental overhead of everyday development tasks significantly.

This project template relies on [GNU make][make intro] as a task runner. While it was designed as a build tool, it is available across many systems already, which helps with bootstrapping a project environment without any additional dependencies.

[make intro]: https://www.gnu.org/software/make/manual/make.html#Introduction

## Makefile

An overview of the included Makefile targets and what they do can be obtained using `make help`:

```console
{{ run('make help', cwd='docs/examples/default') | replace('[36m', '') | replace('[0m', '')}}
```

### Installation

{{ includex('docs/examples/default/Makefile', start_match='install-dev:', end_match='.PHONY', code=True) }}

The project is being installed in place (using pip's `-e` option) including all optional requirements (given in square brackets).

The project template keeps development requirements as optional requirements of the Python package in the [pyproject.toml][], so these can be installed alongside the project.

{{ includex('docs/examples/default/pyproject.toml', code=True, start_match='[project.optional-dependencies]', end_match='# ') }}

The advantage of this is that development dependencies are handled exactly the same as other dependencies. A possible downside of this approach is that these optional dependencies are also included in the package built for users. If this is undesirable, an alternative approach would be to keep development requirements in a separate file (e.g. `dev-requirements.txt`) or use tooling that manages development requirements (e.g. [pipenv][]).

[pipenv]: https://pipenv.pypa.io/
[pyproject.toml]: {{URL_EXAMPLE_FILE}}/pyproject.toml

### Static Analysis

#### Maintainability

A key aspect of maintainability is reducing accidental complexity[^1]. This means not allowing complexity to accumulate that is not inherent to the problem to be solved. During development, accidental complexity arises in many forms, some of which may be caught by the right tooling.

##### Radon

[:octicons-book-16: Documentation][radon-docs]

[radon-docs]: https://beta.ruff.rs/docs/https://radon.readthedocs.io/

{{ includex('docs/examples/default/Makefile', start_match='maintainability:', end_match='.PHONY', code=True) }}

One such tool to estimate complexity is [radon][], which can be used to calculate the average cyclomatic complexity (cc) for your project:

```console
{{ run('make maintainability', cwd='docs/examples/default', should_exit_with_error=True) }}
```

[^1]: sometimes also called incidental complexity
[radon]: https://pypi.org/project/radon/

#### Code Linters

Another type of static analysis is code linting i.e. analyzing source code for potential errors, code style violations, and programming best practice adherence.

{{ includex('docs/examples/default/Makefile', start_match='lint:', end_match='.PHONY', code=True) }}

##### ruff

[:octicons-book-16: Documentation][ruff-docs]

[ruff-docs]: https://beta.ruff.rs/docs/

### Testing

{{ includex('docs/examples/default/Makefile', start_match='coverage:', end_match='.PHONY', code=True) }}

### Documentation

??? quote "Makefile - Documentation Targets"

    {{ includex('docs/examples/default/Makefile', start_match='.PHONY: docs', end_match='.PHONY', start_offset=1, code=True, indent=4) }}

---

??? quote "Example Makefile"

    ```Makefile
    --8<-- "docs/examples/default/Makefile"
    ```

## pre-commit

??? quote "Example `.pre-commit-config.yaml`"

    ```Makefile
    --8<-- "docs/examples/default/.pre-commit-config.yaml"
    ```

While [pre-commit][] is primarily designed to run checks against your repository including changes you are about to commit, it can also be used to run those checks manually

<!-- TODO: Add pre-commit hooks -->

[pre-commit]: https://pre-commit.com/
