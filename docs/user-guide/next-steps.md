# Next Steps

## Enable CI

=== "GitLab"

    On GitLab remotes, CI Pipelines might need to be enabled by assigning a CI Runner to your project. Do this now so your CI pipeline doesn't get stuck when you push your repository for the first time.

=== "GitHub"

    On GitHub remotes, pages need to be configured for your project to be published from a GitHub Action under `Settings/Pages`:

    ![](https://cln.sh/SFzK7Hzh+)

## First commit and push

During project creation, you entered the URL to your remote project (e.g. on GitHub or GitLab). After project creation, the template configured this remote with your local repository, so you are now ready to make your first commit and push it to the remote repository.

??? question "Want to change the remote URL manually?"

    ```sh
    git config remote.origin.url <remote_url>
    ```

    If your are specifying a remote at a different location, you likely also need to update URLs in the following files:

    - `README.md`
    - `CHANGELOG.md`
    - documentation configuration (either `mkdocs.yml` or `docs/conf.py`)

Let's start with an empty commit so we can verify everything is set up correctly without actually committing any files yet:

``` {.sh .copy}
git commit --allow-empty -m "initial commit"
git push
```

If everything went smoothly, your remote project should be aware of your first commit now.

## Install Project

The new project is installable right away. Create a virtual environment using any method you like, for example using the builtin `venv` module:

``` {.sh .copy}
python -m venv .venv
source .venv/bin/activate
```

Then use `install-dev` to install your Python project in-place with all optional dev requirements:

``` {.sh .copy}
make install-dev
```

You can verify your installation by running the [example cli][cli] included with the Python package by default. The command is the [package name][package-name] you have set, only with dashes instead of underscores. The CLI of `sample_project` would therefore be called like this:

```console
(.venv) $ sample-project
{{ run(".venv/bin/sample-project", cwd="docs/examples/default", show_command=False) }}
```

#### Start Implementing

Now you are ready to start your implementation. As a quick reference, Python packages and modules go into `./src/`, documentation into `./docs/` and tests into `./tests/`.
