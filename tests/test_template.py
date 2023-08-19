import os
from pathlib import Path
from subprocess import check_output
from tabnanny import check

import pytest
import yaml
from copier import run_copy
from pytest_venv import VirtualEnvironment

template = yaml.safe_load(Path(__file__).parent.with_name("copier.yaml").read_text())
SUPPORTED_REMOTES = template["remote"]["choices"].values()
SUPPORTED_DOCS = template["docs"]["choices"].values()

fp_template = Path(__file__).parent.parent

required_static_data = dict(
    project_name="Sample Project",
    user_name="mkj",
)


@pytest.fixture
def venv(tmp_path):
    """Create virtual environment in subdirectory of tmp_path."""
    venv = VirtualEnvironment(tmp_path / ".venv")
    venv.create()
    (venv.path / ".gitignore").unlink()
    yield venv


@pytest.mark.slow
@pytest.mark.parametrize("use_precommit", [True, False], ids=["pre-commit", "no pre-commit"])
@pytest.mark.parametrize("use_bumpversion", [True, False], ids=["bumpversion", "no bumpversion"])
@pytest.mark.parametrize("docs", SUPPORTED_DOCS)
@pytest.mark.parametrize("remote", SUPPORTED_REMOTES)
def test_template_generation(
    venv: VirtualEnvironment,
    tmp_path: Path,
    use_precommit: bool,
    use_bumpversion: bool,
    docs: str,
    remote: str,
    project_name: str = "Sample Project",
):
    run_copy(
        str(fp_template),
        str(tmp_path),
        data=dict(
            **required_static_data,
            use_precommit=use_precommit,
            use_bumpversion=use_bumpversion,
            docs=docs,
            remote=remote,
        ),
        defaults=True,
    )

    fp_readme = tmp_path / "README.md"
    assert fp_readme.is_file(), "new projects should have a README file"
    readme_content = fp_readme.read_text()
    assert readme_content.startswith(
        f"# {project_name}"
    ), "README should start with the project name"
    assert "## Installation" in readme_content, "README should have a getting started section"

    fp_changelog = tmp_path / "CHANGELOG.md"
    assert fp_changelog.is_file(), "new projects should have a CHANGELOG file"

    fp_precommit_config = tmp_path / ".pre-commit-config.yaml"
    assert fp_precommit_config.is_file() == use_precommit

    fp_bumpversion_config = tmp_path / ".bumpversion.cfg"
    assert fp_bumpversion_config.is_file() == use_bumpversion

    os.chdir(tmp_path)
    check_output(["make", "init"])

    fp_git = tmp_path / ".git"
    assert fp_git.is_dir(), "new projects should be git repositories"

    fp_docs = tmp_path / "docs"
    if docs == "mkdocs":
        fp_mkdocs_cfg = tmp_path / "mkdocs.yml"
        assert fp_mkdocs_cfg.is_file(), "mkdocs configuration file should exist"
    elif docs == "sphinx":
        fp_sphinx_cfg = fp_docs / "conf.py"
        assert fp_sphinx_cfg.is_file(), "sphinx configuration file should exist"

    use_docs = docs != "none"
    assert fp_docs.is_dir() == use_docs, "docs directory should exist if configured"

    fp_git_config = fp_git / "config"
    git_config = fp_git_config.read_text()
    assert (
        '[remote "origin"]' in git_config
    ), "new projects should have a remote repository configured"

    check_output(["git", "add", "."])
    check_output(["git", "commit", "-m", "initial commit"])

    # verify that example can be installed
    venv.install(".[doc,dev,test]", editable=True)
    venv_bin = Path(venv.bin)

    # verify that pytest works and all tests pass
    check_output([venv_bin / "pytest", "-q"])

    # verify docs can be built
    if use_docs:
        fp_docs_built = tmp_path / "build" / "docs" / "html"
        assert not fp_docs_built.is_dir()
        check_output(
            ["make", "docs"],
            env={
                "SPHINXBUILD": str(venv_bin / "sphinx-build"),
                "MKDOCS_BIN": str(venv_bin / "mkdocs"),
            },
        )
        assert fp_docs_built.is_dir(), "docs should have been built into build directory"
        assert (fp_docs_built / "index.html").is_file(), "index should exist"

    # TODO: Test template update


def test_default_branch_option(tmp_path: Path):
    default_branch = "custom"
    run_copy(
        str(fp_template),
        str(tmp_path),
        data=dict(
            project_name="Sample Project",
            user_name="mkj",
        ),
        defaults=True,
        user_defaults={"default_branch": default_branch},
    )
    check_output(["make", "init"], cwd=str(tmp_path))
    assert (
        check_output(["git", "status", "--branch", "--porcelain"], cwd=str(tmp_path))
        .decode()
        .split("\n")[0]  # first line -> branch info
        .split()[-1]  # last word -> branch
        == default_branch
    )


@pytest.mark.parametrize("remote", SUPPORTED_REMOTES)
def test_remote_option(tmp_path: Path, remote: str):
    user_name = "foo"
    project_name = "Wonderful Project"

    run_copy(
        str(fp_template),
        str(tmp_path),
        data=dict(
            project_name=project_name,
            remote=remote,
            user_name=user_name,
        ),
        defaults=True,
    )
    check_output(["make", "init"], cwd=str(tmp_path))

    git_remote_output = check_output(["git", "remote", "-v"], cwd=str(tmp_path)).decode()
    branch, remote_url, _ = git_remote_output.split("\n")[0].split()

    readme_template_url = (tmp_path / "README.md").open().readlines()[-1].strip()

    if remote == "gitlab":
        assert remote_url == f"git@github.com:{user_name}/wonderful-project.git"
        assert (tmp_path / ".github").is_dir()
        assert "github.com" in readme_template_url
    if remote.startswith("gitlab"):
        assert (tmp_path / ".gitlab-ci.yml").is_file()
    if remote.endswith("iis"):
        assert remote_url == f"git@git01.iis.fhg.de:{user_name}/wonderful-project.git"
        assert "git01.iis.fhg.de" in readme_template_url
    if remote.endswith("fhg"):
        assert remote_url == f"git@gitlab.cc-asp.fraunhofer.de:{user_name}/wonderful-project.git"
        assert "gitlab.cc-asp.fraunhofer.de" in readme_template_url


@pytest.mark.parametrize("docs", SUPPORTED_DOCS)
def test_docs_option(venv: VirtualEnvironment, tmp_path: Path, docs: str):
    root = tmp_path

    run_copy(
        str(fp_template),
        str(root),
        data=dict(
            **required_static_data,
            docs=docs,
        ),
        defaults=True,
    )

    if docs == "mkdocs":
        fp_mkdocs_cfg = root / "mkdocs.yml"
        assert fp_mkdocs_cfg.is_file(), "mkdocs configuration file should exist"
    elif docs == "sphinx":
        fp_sphinx_cfg = root / "docs" / "conf.py"
        assert fp_sphinx_cfg.is_file(), "sphinx configuration file should exist"

    if docs != "none":
        assert (root / "docs").is_dir(), "docs directory should exist"

        # install example including its doc requirements
        venv.install(f"{root}[doc]", editable=True)
        venv_bin = Path(venv.bin)

        # verify docs can be built
        fp_docs_built = tmp_path / "build" / "docs" / "html"
        assert not fp_docs_built.is_dir()
        check_output(
            ["make", "docs"],
            env={
                "SPHINXBUILD": str(venv_bin / "sphinx-build"),
                "MKDOCS_BIN": str(venv_bin / "mkdocs"),
            },
            cwd=tmp_path,
        )
        assert fp_docs_built.is_dir(), "docs should have been built into build directory"
        assert (fp_docs_built / "index.html").is_file(), "index should exist"


@pytest.mark.parametrize("docs", SUPPORTED_DOCS)
@pytest.mark.parametrize("remote", SUPPORTED_REMOTES)
def test_publish_docs_ci(venv: VirtualEnvironment, tmp_path: Path, docs: str, remote: str):
    root = tmp_path

    run_copy(
        str(fp_template),
        str(root),
        data=dict(
            **required_static_data,
            docs=docs,
            remote=remote,
        ),
        defaults=True,
    )

    ci_platform = "gitlab" if remote.startswith("gitlab") else remote

    if ci_platform == "gitlab":
        gitlab_ci_config = yaml.safe_load((root / ".gitlab-ci.yml").read_text())

    match (docs, ci_platform):
        case ("none", "github"):
            assert not (root / ".github" / "docs.yaml").is_file()
        case ("none", "gitlab"):
            assert "pages" not in gitlab_ci_config
