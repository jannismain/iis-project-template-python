A calculated variable is a variable that is deduced from a user-provided value.

They do not appear in the template questionaire and therefore cannot be modified by the user.

Calculated template variables are managed in the `context` file within the template:

{{ includex('template/context', code='jinja', caption=True, raise_errors=True) }}

This context can then be imported using the [jinja import](https://jinja.palletsprojects.com/templates/#import) command.

As an example, this was used in the README template to reuse the `remote_url_pages` and `remote_url_https` URLs, which are calculated from the `remote_url` provided by the user:

{{ includex('template/README.md.jinja', lines=8, code='jinja', caption=True) }}
