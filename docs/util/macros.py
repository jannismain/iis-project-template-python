"""Documentation macros.

See the [`mkdocs-macros-plugin` Documentation](https://mkdocs-macros-plugin.readthedocs.io/) for more information.
"""

import hashlib
import json
import logging
import os
import pathlib
import re
import subprocess
import unicodedata
from typing import List, Tuple, Union

import pymdownx.magiclink
from mkdocs_macros.plugin import MacrosPlugin

# patch for private gitlab instance
base_url = "https://git01.iis.fhg.de"
pymdownx.magiclink.PROVIDER_INFO["gitlab"].update(
    {
        "url": base_url,
        "issue": "%s/{}/{}/issues/{}" % base_url,
        "pull": "%s/{}/{}/merge_requests/{}" % base_url,
        "commit": "%s/{}/{}/commit/{}" % base_url,
        "compare": "%s/{}/{}/compare/{}...{}" % base_url,
    }
)

root = pathlib.Path(__file__).parent.parent.parent

log = logging.getLogger("mkdocs.mkdocs_macros")


def define_env(env: MacrosPlugin):
    """Define variables, macros and filters for mkdocs-macros."""

    @env.filter
    def pretty_json(s, indent=2, **kwargs):
        return json.dumps(s, indent=indent, **kwargs)

    @env.filter
    def pretty_json_obj(s, indent=2, indent_char=" "):
        r = ""
        indentation = ""
        prev = ""
        for c in s:
            if c == "{":
                indentation += indent * indent_char
                r += c + "\n" + indentation
            elif c == "}":
                indentation = indentation[:-indent]
                r += "\n" + indentation + c
            elif c == ",":
                r += c + "\n" + indentation
            elif c == " " and prev != ":":
                pass
            else:
                r += c
            prev = c
        return r

    env.macro(get_files)
    env.macro(list_directory)
    env.macro(run)


def get_files(directory: str | pathlib.Path, match: str = "", ignore: str = "") -> List[str]:
    """Return list of files in *directory* that match the provided substring.

    Args:
        directory: path to directory
        match: only files that contain this string will be included

    Returns:
        List of files in *directory*
    """
    rv = []
    try:
        directory = pathlib.Path(directory)
        assert directory.is_dir()
        for file in sorted(os.listdir(directory)):
            if match and match not in file:
                continue
            if ignore and ignore in file:
                continue
            rv.append(file)
    except Exception as e:
        rv.append(f"Error: {e}")
    return rv


def list_directory(directory: str | pathlib.Path, hide_extension: bool = False, join: str = "\n", **kwargs) -> str:
    """List files in given *directory* that match the provided substring.

    Uses [`get_files`][macros.get_files] to retrieve list of files

    Args:
        directory: path to directory
        hide_extension: strip extension from filename
        join: string to join filenames together with

    Returns:
        files in directory
    """
    files = get_files(directory=directory, **kwargs)
    if hide_extension:
        files = [pathlib.Path(file).stem for file in files]
    return join.join(files)


fp_cli_command_output_cache = root / "build" / ".docs_cache"
fp_cli_command_output_cache.mkdir(parents=True, exist_ok=True)


def run(
    *command,
    setup: list = None,
    skip_lines=0,
    show_command=True,
    skip_cache=False,
    should_exit_with_error=False,
):
    if setup is None:
        setup = []
    # ensure arguments are all strings
    setup = [str(x) for x in setup]
    command = [str(x) for x in command]

    filename = _get_filename(command, setup)
    fp_cached_command = fp_cli_command_output_cache / filename

    if skip_cache or not fp_cached_command.is_file():
        log.info("Generating output for: %s", " ".join(setup) + " " + " ".join(command))
        result = subprocess.run(
            [*setup, *command],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=not should_exit_with_error,  # use to catch issues with any cli command
        )
        rv = result.stdout
        if result.returncode != 0 and not should_exit_with_error:  # We check ourselves, in order to log the output
            log.error(f"{' '.join(setup)} {' '.join(command)} failed with return code {result.returncode}")
            log.error(rv.decode())
        fp_cached_command.open("wb").write(rv)

    output = fp_cached_command.open().read()

    if skip_lines:
        output = "\n".join(output.split("\n")[skip_lines:])

    if show_command:
        command_str = f"$ {' '.join(command)}"
        output = command_str + "\n" + output

    return output


def _get_filename(args: list[str], setup: list[str] = None) -> str:
    """Create filename with human-readable prefix and unique suffix for given args and setup.

    Filenames include ascii-characters only and strip other characters problematic for certain filesystems.

    Human-readable prefix will be generated from args alone.
    Unique suffix (i.e. hash) will be generated from both args and setup.

    Args:
        args: list of cli arguments
        setup: list of cli setup commands. Defaults to [].

    Returns:
        filename of the format: {args}_{hash}
    """
    sha_hash = hashlib.sha1(("".join([*setup, *args])).encode()).hexdigest()
    filename = f"{'_'.join(args)}_{sha_hash}"
    filename = unicodedata.normalize("NFKD", filename).encode("ascii", "ignore").decode("ascii")
    filename = re.sub(r"[^\w\s-]", "", filename)
    return filename
