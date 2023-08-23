USER_NAME?=jannismain
REMOTE?=github
REMOTE_URL?=git@github.com:jannismain/python-project-template-example.git

examples: example-github example-gitlab-fhg example-gitlab-iis
example-github: example-clean-github example example-setup
example-gitlab-fhg: example-clean-gitlab-fhg
	$(MAKE) example USER_NAME=mkj REMOTE=gitlab-fhg REMOTE_URL=git@gitlab.cc-asp.fraunhofer.de:mkj/sample-project.git
	$(MAKE) example-setup REMOTE=gitlab-fhg
example-gitlab-iis: example-clean-gitlab-iis
	$(MAKE) example USER_NAME=mkj REMOTE=gitlab-iis REMOTE_URL=git@git01.iis.fhg.de:mkj/sample-project.git
	$(MAKE) example-setup REMOTE=gitlab-iis

example-manual: example-clean
	copier copy ${COPIER_ARGS} -d "project_name=Sample Project" -d "package_name=sample_project" . ./example
	$(MAKE) example-setup

COPIER_ARGS?=--trust
COPIER_DEFAULT_VALUES?=-d "project_name=Sample Project" -d "package_name=sample_project" --defaults
EXAMPLE_DIR=./build/example_$(subst -,_,$(REMOTE))
example:
	copier copy ${COPIER_ARGS} ${COPIER_DEFAULT_VALUES} -d "user_name=${USER_NAME}" -d "remote=${REMOTE}" -d "remote_url=${REMOTE_URL}" . ${EXAMPLE_DIR}

example-setup:
	-cd ${EXAMPLE_DIR} &&\
		rm -rf .copier-answers.yml &&\
		git add . &&\
		git commit -m "automatic update" &&\
		git fetch &&\
		git branch --set-upstream-to=origin/main &&\
		git pull --rebase=True -X theirs
	$(MAKE) example-setup-local REMOTE=${REMOTE}
example-setup-local:
ifndef CI
	cd ${EXAMPLE_DIR} &&\
		pyenv local project-template-example || echo "Couldn't set example env via pyenv" &&\
		pip install --upgrade pip &&\
		$(MAKE) install-dev || echo "Couldn't install dev environment for example" &&\
		code --new-window .
endif

examples-clean: example-clean-github example-clean-gitlab-fhg example-clean-gitlab-iis
example-clean-github:
	rm -rf build/example_github && mkdir -p build/example_github
example-clean-gitlab-fhg:
	rm -rf build/example_gitlab_fhg && mkdir -p build/example_gitlab_fhg
example-clean-gitlab-iis:
	rm -rf build/example_gitlab_iis && mkdir -p build/example_gitlab_iis

MKDOCS_CMD?=build
MKDOCS_ARGS?=
docs: docs/examples/mkdocs docs/examples/sphinx docs/examples/default
	mkdocs $(MKDOCS_CMD) $(MKDOCS_ARGS)
docs-live:
	$(MAKE) docs MKDOCS_CMD=serve
docs/examples/mkdocs:
	copier copy ${COPIER_ARGS} ${COPIER_DEFAULT_VALUES} -d "user_name=mkj" -d "docs=mkdocs" . docs/examples/mkdocs
docs/examples/sphinx:
	copier copy ${COPIER_ARGS} ${COPIER_DEFAULT_VALUES} -d "user_name=mkj" -d "docs=sphinx" . docs/examples/sphinx
docs/examples/default:
	copier copy ${COPIER_ARGS} ${COPIER_DEFAULT_VALUES} -d "user_name=mkj" . docs/examples/default
docs-clean:
	rm -rf docs/examples public
docs-clean-cache:
	rm -rf build/.docs_cache

.PHONY: test
PYTEST_ARGS=-n auto
test:
	pytest ${PYTEST_ARGS} -m "not slow"
test-all:
	pytest ${PYTEST_ARGS}
