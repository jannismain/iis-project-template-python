from pathlib import Path

import pytest
import yaml
from copier import run_auto

template_variables = {var for var in yaml.safe_load(Path(__file__).parent.with_name('copier.yaml').read_text()) if not var.startswith('_')}
print(template_variables)

fp_template = Path(__file__).parent.parent/"template"


@pytest.mark.parametrize("project_name", ["My Project"])
@pytest.mark.parametrize("use_precommit", [True, False])
@pytest.mark.parametrize("use_bumpversion", [True, False])
def test_template_generation(tmp_path: Path, project_name: str, use_precommit: bool, use_bumpversion: bool):
    run_auto(
        str(fp_template),
        str(tmp_path),
        data=dict(project_name=project_name, use_precommit=use_precommit, use_bumpversion=use_bumpversion),
    )
    fp_readme = tmp_path / 'README.md'
    assert fp_readme.is_file(), "all new projects should have a README"
    readme_content = fp_readme.read_text()
    assert readme_content.startswith(f'# {project_name}'), "README should start with the project name"
    assert "## Installation" in readme_content, "README should have a getting started section"
    # assert (tmp_path / 'CHANGELOG.md').is_file(), "all new projects should have a CHANGELOG"

    fp_precommit_config = tmp_path / '.pre-commit-config.yaml'
    assert fp_precommit_config.is_file() == use_precommit

    fp_bumpversion_config = tmp_path / '.bumpversion.cfg'
    assert fp_bumpversion_config.is_file() == use_bumpversion
