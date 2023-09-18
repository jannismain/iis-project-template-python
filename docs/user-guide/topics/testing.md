# Testing

## Tooling

- [pytest][]: testing framework
- [coverage.py][]: collect test coverage and create report

## Configuration

Both pytest and coverage.py support configuration via the `pyproject.toml` file. Learn more at their respective reference documentation.

- [pytest configuration reference](https://docs.pytest.org/en/7.4.x/reference/customize.html)
- [coverage configuration reference](https://coverage.readthedocs.io/en/latest/config.html)

## Writing Tests

Python tests are implemented using [pytest][] in the `tests` subdirectory.

```
{{ run("tree --noreport docs/examples/default/tests") }}
```

Each test module starts with `test_` so it is automatically discovered when running `pytest`.

In addition, pytest also collects data from a `conftest.py` file. This would be where [global fixtures](https://docs.pytest.org/en/7.4.x/how-to/fixtures.html) are defined that can be reused across multiple test modules.

## Executing tests

### ...during development

Tests can be executed like this

```console
$ pytest -q
{{ run(".venv/bin/pytest --config-file pyproject.toml -q", cwd="docs/examples/default") }}
```

If you have never used pytest before, check out their [pytest documentation](https://docs.pytest.org/en/7.4.x/contents.html). The more you know about pytest, the better your test suite is going to be. 😉

### ...as CI job

If a remote has been configured, your tests are also automatically run as part of the project's [continuous integration pipeline][continuous-integration].

??? quote "Run tests in GitLab CI"

    {{ includex('docs/examples/gitlab/.gitlab-ci.yml', code=True, start_match='test:\n', end_match='pages:') | indent(4) }}

A coverage report is created and linked in the README file.

## IDE Integration

Most Python IDE's integrate with test suites written for pytest and allow you to run them easily during development. Here is an example of VSCode's Testing UI:

![](https://cln.sh/Krfmprql+)
*VSCode automatically loads your test suite in the "Testing" sidebar and makes it easy to (1) run or debug all your tests or (2) run or debug individual tests. It understands parametrized tests and breaks them out as separate test cases.*{.caption}

[pytest]: https://pytest.org/
[coverage.py]: https://coverage.readthedocs.io/
