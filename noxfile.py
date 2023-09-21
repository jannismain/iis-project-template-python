import pathlib
import shutil

import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.stop_on_first_error
nox.options.sessions = ["build", "test"]

source_directories = "src"

supported_python_versions = ["3.11"]

root = pathlib.Path(__file__).parent
build_dir = root / "build" / "dist"


@nox.session
def build(session: nox.Session):
    if build_dir.is_dir():
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True, exist_ok=False)

    session.run("make", "build", external=True, env={"BUILDDIR": str(build_dir)})


@nox.session(python=supported_python_versions)
def test(session: nox.Session):
    """Run all tests against dev and target environment."""
    wheel_files = sorted(build_dir.glob("*.whl"))
    print(wheel_files)
    assert len(wheel_files) == 1, "a single wheel should have been built"
    wheel_file = wheel_files[0]
    session.install(f"{wheel_file}[test]")
    session.run(
        "pytest", "-k", "test_package", *session.posargs, env={"BIN_PATH": str(session.bin)}
    )
