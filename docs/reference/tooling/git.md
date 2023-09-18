---
tags: [Version Control]
---

# git

[Website][git] :octicons-dash-24: [:octicons-book-16: Documentation][git-docs]

[git]: https://git-scm.com/
[git-docs]: https://git-scm.com/doc


## [git hooks]

Git provides hooks to run custom code when specific git actions occur. One such action would be a commit, for which git provides the following hooks:

| Hook                 | When                                   | Common use cases               |
| -------------------- | -------------------------------------- | ------------------------------ |
| `pre-commit`         | before commit process is started       | linting, style checks, etc.    |
| `prepare-commit-msg` | before commit message editor is opened | provide default commit message |
| `commit-msg`         | after commit message is entered        | validate commit message        |
| `post-commit`        | after commit process is completed      | send notifications             |

These *hooks* are basically just scripts inside the `.git/hooks` directory that are called by git. However, there is also a framework called [pre-commit](../pre-commit), that allows for easy reuse of existing git hooks.

[git hooks]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
