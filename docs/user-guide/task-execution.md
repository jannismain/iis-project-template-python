# Task Execution

Recurring tasks, such as running the test suite, generating a coverage report or previewing the documentation locally should be easy to do for any developer.

Therefore, a unified way of running those tasks is preferable over remembering the command for each of those tasks. Especially when these commands  differ across projects, a common way of calling them without remembering their exact syntax reduces the mental overhead of everyday development tasks significantly.

This project template relies on [GNU make][make intro] as a task runner. While it was designed as a build tool, it is available across many systems already, which helps with bootstrapping a project environment without any additional dependencies.

[make intro]: https://www.gnu.org/software/make/manual/make.html#Introduction

## Makefile

??? example "Example Makefile"

    ```Makefile
    --8<-- "docs/examples/default/Makefile"
    ```

```console
{{ run('make', 'help', cwd='example') | replace('[36m', '') | replace('[0m', '')}}
```
