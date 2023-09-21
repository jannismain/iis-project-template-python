{{ includex('README.md', start_match='Prerequisites', end_match='<!-- usage-end -->')}}

## Using [copier] directly

```console
copier copy --trust https://gitlab.cc-asp-fraunhofer.de/mkj/project-template.git my_new_project
```

*Note: `--trust` is required because the template uses [tasks][] to setup your git repository for you.*

[tasks]: https://gitlab.cc-asp.fraunhofer.de/mkj/project-template/-/blob/main/copier.yaml

*Note: If you have [pipx][] installed (you should, it is good), you can simply use `pipx run copier` out of the box.*

[copier]: https://github.com/copier-org/copier
[pipx]: https://pypa.github.io/pipx/
