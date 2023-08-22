PUBLISHED_EXAMPLES = build/examples/github build/examples/gitlab_fhg build/examples/gitlab_iis build/examples/gitlab_iis_sphinx
DOC_EXAMPLES = docs/examples/mkdocs docs/examples/sphinx docs/examples/default
COPIER_ARGS?=--trust
COPIER_DEFAULT_VALUES=-d "project_name=Sample Project" -d "package_name=sample_project"

.PHONY: examples $(PUBLISHED_EXAMPLES) $(DOC_EXAMPLES) example-setup example-setup-commit example-setup-local example examples-clean

examples: ## build all published examples
examples: $(PUBLISHED_EXAMPLES)

build/examples/%: COPIER_DEFAULT_VALUES += --defaults
build/examples/%: EXAMPLE_DIR:=$@
build/examples/github: COPIER_DEFAULT_VALUES+=-d user_name=jannismain -d remote=github -d remote_url=git@github.com:jannismain/python-project-template-example.git
build/examples/gitlab%: COPIER_DEFAULT_VALUES+=-d user_name=mkj
build/examples/gitlab_fhg: COPIER_DEFAULT_VALUES+= -d remote=gitlab-fhg -d remote_url=git@gitlab.cc-asp.fraunhofer.de:mkj/sample-project.git
build/examples/gitlab_iis: COPIER_DEFAULT_VALUES+= -d remote=gitlab-iis -d remote_url=git@git01.iis.fhg.de:mkj/sample-project.git
build/examples/gitlab_iis_sphinx: COPIER_DEFAULT_VALUES+= -d remote=gitlab-iis -d remote_url=git@git01.iis.fhg.de:mkj/sample-project-sphinx.git -d docs=sphinx

$(PUBLISHED_EXAMPLES):
	@echo "Recreating '$@'..."
	@rm -rf "$@" && mkdir -p "$@"
	@copier copy ${COPIER_ARGS} ${COPIER_DEFAULT_VALUES} . "$@"
	$(MAKE) example-setup EXAMPLE_DIR="$@"

docs/examples/mkdocs: COPIER_DEFAULT_VALUES+=-d docs=mkdocs
docs/examples/sphinx: COPIER_DEFAULT_VALUES+=-d docs=sphinx

$(DOC_EXAMPLES):
	@echo "Recreating '$@'..."
	@rm -rf "$@" && mkdir -p "$@"
	@copier copy ${COPIER_ARGS} --defaults -d user_name=mkj ${COPIER_DEFAULT_VALUES} . "$@"

example-setup: example-setup-commit example-setup-local
example-setup-commit:
	-cd ${EXAMPLE_DIR} &&\
		rm -rf .copier-answers.yml &&\
		git add . &&\
		git commit -m "automatic update" &&\
		git fetch &&\
		git branch --set-upstream-to=origin/main &&\
		git pull --rebase=True -X theirs
example-setup-local:
ifndef CI
	cd ${EXAMPLE_DIR} &&\
		pyenv local project-template-example || echo "Couldn't set example env via pyenv" &&\
		pip install --upgrade pip &&\
		$(MAKE) install-dev || echo "Couldn't install dev environment for example" &&\
		code --new-window .
endif

examples-clean: ## remove all published examples
	rm -rf $(PUBLISHED_EXAMPLES)

example:  ## build individual example for manual testing (will prompt for values!)
	rm -rf "$@"
	copier copy ${COPIER_ARGS} ${COPIER_DEFAULT_VALUES} . "$@"
	$(MAKE) example-setup EXAMPLE_DIR="$@"


.PHONY: docs docs-live docs-clean docs-clean-cache
MKDOCS_CMD?=build
MKDOCS_ARGS?=
docs: ## build documentation
docs: $(DOC_EXAMPLES)
	mkdocs $(MKDOCS_CMD) $(MKDOCS_ARGS)
docs-live: ## serve documentation locally
docs-live:
	$(MAKE) docs MKDOCS_CMD=serve
docs-clean:
	rm -rf docs/examples public
docs-clean-cache:
	rm -rf build/.docs_cache




.PHONY: cspell cspell-ci
CSPELL_ARGS=--show-suggestions --show-context --config ".vscode/cspell.json" --unique
CSPELL_FILES="**/*.*"
DICT_FILE=.vscode/terms.txt
spellcheck: ## check spelling using cspell
	cspell ${CSPELL_ARGS} ${CSPELL_FILES}
spellcheck-ci:
	cspell --no-cache ${CSPELL_ARGS} ${CSPELL_FILES}
spellcheck-dump: ## save all flagged words to project terms dictionary
	cspell ${CSPELL_ARGS} ${CSPELL_FILES} --words-only >> ${DICT_FILE}
	sort --ignore-case -s --output=${DICT_FILE} ${DICT_FILE}

.PHONY: test
PYTEST_ARGS=-n auto
test: ## run tests quickly
	pytest ${PYTEST_ARGS} -m "not slow"
test-all: ## run all tests
	pytest ${PYTEST_ARGS}


.PHONY: help
# a nice way to document Makefiles, found here: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
