import sys
from pathlib import Path
from typing import Annotated, Optional

from copier import run_copy
from typer import Argument, Option, Typer, colors, confirm, style

app = Typer()

__version__ = "0.0.2"


def version_callback(value: bool) -> None:
    if value:
        print(__version__)
        sys.exit(0)


@app.command(name="init-python-project")
def cli(
    target_path: Path = Argument("new-project"),
    version: Annotated[
        Optional[bool], Option("--version", callback=version_callback, is_eager=True)
    ] = None,
) -> None:
    """Executes the CLI command to create a new project."""
    target_path.mkdir(exist_ok=True)
    if (
        target_path.is_dir()
        and any(target_path.iterdir())
        and not confirm(
            style(
                f"Target directory '{target_path}' is not empty! Continue?",
                fg=colors.YELLOW,
            )
        )
    ):
        sys.exit(1)

    run_copy(
        src_path=str(Path(__file__).parent.absolute()),
        dst_path=target_path,
        unsafe=True,
    )


if __name__ == "__main__":
    app()
