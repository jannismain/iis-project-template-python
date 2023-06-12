example: example-clean
	copier -d "project_name=Sample Project" -d "package_name=sample_project" -d user_name=mkj --defaults . ./example
	$(MAKE) example-setup

.PHONY: example-setup
example-setup:
	cd example &&\
		git add . &&\
		git commit -m "Initial commit" &&\
		pyenv local project-template-example &&\
		$(MAKE) install-dev &&\
		code --new-window .

.PHONY: example-push
example-push:
	cd example &&\
		git push -f -u origin main

.PHONY: example-clean
example-clean:
	rm -rf example && mkdir example
