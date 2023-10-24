import pytest
from init_python_project.extensions import context


@pytest.mark.parametrize(
    "given, expected",
    [
        (
            dict(
                remote="github",
                remote_url="git@github.com:jannismain/python-project-template-example.git",
                default_branch="main",
            ),
            dict(
                platform="github",
                remote_url_https="https://github.com/jannismain/python-project-template-example",
                remote_url_pages="https://jannismain.github.io/python-project-template-example",
                remote_url_pipeline="https://github.com/jannismain/python-project-template-example/actions?query=branch%3Amain",
                remote_url_coverage_badge="https://jannismain.github.io/python-project-template-example/badges/coverage.svg",
                remote_url_pipeline_badge="https://github.com/jannismain/python-project-template-example/actions/workflows/ci.yaml/badge.svg",
            ),
        )
    ],
)
def test_infer_urls_from_remote(given: dict[str, str], expected: dict[str, str]):
    result = dict(given)
    context.infer_urls_from_remote(result)

    for key, value in expected.items():
        assert result[key] == value
