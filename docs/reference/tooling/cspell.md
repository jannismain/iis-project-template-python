---
tags: [Linter]
---

# CSpell

[:octicons-mark-github-16: Repository][cspell] :octicons-dash-24: [:octicons-book-16: Documentation][cspell-docs]

## Configuration

CSpell is configured via a `cspell.json` configuration file at the project root, where it is automatically picked up by the [CLI](#command-line-interface) and [pre-commit hook](#pre-commit-hook).

??? example "`cspell.json`"
    {{ includex("docs/examples/default/cspell.json", code="json", indent=4) }}

### Project Dictionary

Sooner or later your project will contain terms not found in any dictionary (like names or acronyms). Those can be added to a custom dictionary so that CSpell only warns on actual issues.

This templates adds a custom dictionary at the root of the project named `project-terms.txt`. If you prefer another filename or location, simply move or rename the file and update `cspell.json#dictionaryDefinitions` to point to the new location.

{{ includex("docs/examples/default/cspell.json", start_match="dictionaryDefinitions", end_match="],", end_offset=1, code="json")}}

## Command Line Interface

### Installation

The optional `cspell` command line interface can be installed via the `cspell-install` Makefile target:

{{ includex("docs/examples/default/Makefile", start_match="cspell-install:", end_match="\t@cspell", include_end_match=True, code="Makefile") }}

After installation, the following Makefile targets are available:

{{ includex("docs/examples/default/Makefile", start_match="cspell:", end_match="cspell-dump:", end_offset=2, code="Makefile") }}

### `make cspell`

`make cspell` allows you to run `cspell` manually to check for any spelling mistakes or unknown terms:

```console
{{ run("$ make cspell", cwd="docs/examples/default") }}
```

### `make cspell-dump`

If you are sure that all remaining spelling issues are project terms, you can quickly dump them into the [project dictionary](#project-dictionary) using `make cspell-dump`.

### Dictionary Lookup

You can also lookup words to find out, which dictionary (if any) includes them:

```console
{{ run("$ cspell trace foo") }}
```

## pre-commit hook

{{ includex("docs/examples/default/.pre-commit-config.yaml", start_match="cspell-cli", lines=5, code="yaml") }}

## CI job

=== "GitLab"

    {{ includex("docs/examples/gitlab/.gitlab-ci.yml", start_match="spellcheck:", end_match="make spellcheck", include_end_match=True, code="yaml", indent=4) }}

=== "GitHub"

    {{ includex("docs/examples/default/.github/workflows/spellcheck.yaml", code="yaml", indent=4) }}

[cspell]: https://github.com/streetsidesoftware/cspell
[cspell-docs]: https://cspell.org
