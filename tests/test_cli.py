import logging as log
import re

import pytest
from init_python_project.cli import app
from typer.testing import CliRunner


@pytest.fixture
def cli():
    runner = CliRunner()
    return lambda *args: runner.invoke(app, args)


def test_default_values(cli):
    result = cli("--help")
    log.debug(result.output)
    assert result.output.strip().startswith("Usage: init-python-project")


def test_version(cli):
    result = cli("--version")
    log.debug(result.output)
    assert re.match(r"^\d\.\d\.\d$", result.output.strip()), "should return semantic version number"
