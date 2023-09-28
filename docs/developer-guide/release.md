# Releasing a new version

As this repository is hosted on three different remotes to reach different target audiences ([Fraunhofer IIS internal](https://git01.iis.fhg.de), [FHG internal](https://gitlab.cc-asp.fraunhofer.de) and [public](https://github.com/jannismain/python-project-template)), it is convenient to have their respective main branches all available under different names in your local repository:

```
git remote add origin git@git01.iis.fhg.de:mkj/project-template.git
git checkout main
git remote add fhg git@gitlab.cc-asp.fraunhofer.de:mkj/project-template.git
git remote add github git@github.com:jannismain/python-project-template.git
git branch --set-upstream-to=fhg/main main-fhg
git branch --set-upstream-to=github/main main-github
```

Each of those remotes host a version of the project template with links updated to point to that remote. Therefore, updates cannot be simply pushed to those remotes but need to be merged into their main branches, so that the platform-specific changes remain intact.

With those preparations in place, a new release can be created like this:

1. Commit everything that should be part of the release to be `main` branch of the IIS-internal version of the repository. That includes updating the CHANGELOG and bumping the version number.
2. Merge those changes into the `main` branches of the fhg and public remotes.

    ```
    git co main-fhg
    git merge main --ff-only --ff
    git co main-github
    git merge main --ff-only --ff
    ```

3. Trigger the release process on the public `main` branch

    ```
    make release
    ```
