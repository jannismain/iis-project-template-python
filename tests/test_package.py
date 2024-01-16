from pathlib import Path

import pexpect
import pytest


@pytest.fixture
def bin():
    import os

    yield Path(os.getenv("BIN_PATH", "."))


KEY_UP = "\x1b[A"
KEY_DOWN = "\x1b[B"


@pytest.mark.slow
@pytest.mark.parametrize("mode", ["default", "minimal", "custom"])
def test_template_generation_via_cli(bin: Path, tmp_path: Path, mode: str):
    child = pexpect.spawn(str(bin / "init-python-project"), ["my-project"], cwd=tmp_path, timeout=3)
    child.expect(".* project.*")
    child.sendline("My Project")
    child.expect(".* package.*")
    child.sendline("")  # accept default

    child.expect(".* kind of project.*")
    if mode == "default":
        child.sendline("")  # accept default
    if mode == "minimal":
        child.sendline(f"{KEY_UP}\n")  # select minimal
    if mode == "custom":
        child.sendline(f"{KEY_DOWN}\n")  # select custom

    if mode == "custom":
        child.expect(".* pre-commit.*")
        child.sendline("")  # accept default
        child.expect(".* bumpversion.*")
        child.sendline("")  # accept default
        child.expect(".* cspell.*")
        child.sendline("")  # accept default
        child.expect(".* documentation.*")
        child.sendline("")  # accept default
        child.expect(".* documentation template.*")

    child.expect(".* platform.*")
    child.sendline("")  # accept default
    child.expect(".* name.*")
    child.sendline("cool-user")
    child.expect(".* remote.*")
    child.sendline("")  # accept default
