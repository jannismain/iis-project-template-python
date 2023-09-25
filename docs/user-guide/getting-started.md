{{ includex('README.md', start_match='Prerequisites', end_match='<!-- usage-end -->')}}

??? note "Using [pipx]"

    ```{.sh .copy}
    pipx run init-python-project
    ```

[pipx]: https://pypa.github.io/pipx/

??? note "Using [copier]"

    The underlying template is built using [copier]. This means you can also use the copier template directly like this:

    ```{.sh .copy}
    copier copy --trust https://gitlab.cc-asp.fraunhofer.de/mkj/project-template.git my_new_project
    ```

    *Note: `--trust` is required because the template uses [tasks] to setup your git repository for you.*

[tasks]: https://git01.iis.fhg.de/mkj/project-template/-/blob/main/copier.yaml
[copier]: https://github.com/copier-org/copier
