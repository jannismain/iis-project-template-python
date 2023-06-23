import os
from pathlib import Path
from subprocess import check_output

import pytest
import yaml
from copier import run_copy
from pytest_venv import VirtualEnvironment

template_variables = {
    var
    for var in yaml.safe_load(
        Path(__file__).parent.with_name("copier.yaml").read_text()
    )
    if not var.startswith("_")
}

fp_template = Path(__file__).parent.parent

static_data = dict(
    user_name="mkj", remote_url="git@git01.iis.fhg.de:mkj/sample-project.git"
)


@pytest.fixture
def venv(tmp_path):
    """Create virtual environment in subdirectory of tmp_path."""
    venv = VirtualEnvironment(tmp_path / ".venv")
    venv.create()
    (venv.path / ".gitignore").unlink()
    yield venv


# @pytest.mark.parametrize("project_name", ["Sample Project"])
@pytest.mark.parametrize("use_precommit",[True, False],ids=["pre-commit", "no pre-commit"])
@pytest.mark.parametrize("use_bumpversion", [True, False], ids=["bumpversion", "no bumpversion"])
def test_template_generation(
    venv: VirtualEnvironment,
    tmp_path: Path,
    use_precommit: bool,
    use_bumpversion: bool,
    project_name: str = "Sample Project",
):
    run_copy(
        str(fp_template),
        str(tmp_path),
        data=dict(
            project_name="Sample Project",
            package_name=project_name.lower().replace(" ", "_"),
            use_precommit=use_precommit,
            use_bumpversion=use_bumpversion,
            **static_data,
        ),
    )

    fp_readme = tmp_path / "README.md"
    assert fp_readme.is_file(), "new projects should have a README file"
    readme_content = fp_readme.read_text()
    assert readme_content.startswith(
        f"# {project_name}"
    ), "README should start with the project name"
    assert (
        "## Installation" in readme_content
    ), "README should have a getting started section"

    fp_changelog = tmp_path / "CHANGELOG.md"
    assert fp_changelog.is_file(), "new projects should have a CHANGELOG file"

    fp_precommit_config = tmp_path / ".pre-commit-config.yaml"
    assert fp_precommit_config.is_file() == use_precommit

    fp_bumpversion_config = tmp_path / ".bumpversion.cfg"
    assert fp_bumpversion_config.is_file() == use_bumpversion

    fp_git = tmp_path / ".git"
    assert fp_git.is_dir(), "new projects should be git repositories"

    fp_git_config = fp_git / "config"
    git_config = fp_git_config.read_text()
    assert (
        '[remote "origin"]' in git_config
    ), "new projects should have a remote repository configured"

    os.chdir(tmp_path)
    check_output(["git", "add", "."])
    check_output(["git", "commit", "-m", "initial commit"])

    # verify that example can be installed
    venv.install(".[doc,dev,test]", editable=True)
    venv_bin = Path(venv.bin)

    # verify that pytest works and all tests pass
    check_output([venv_bin / "pytest", "-q"])

    # TODO: Test template update
