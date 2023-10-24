A calculated variable is a variable that is deduced from a user-provided value.

They do not appear in the template questionnaire and therefore cannot be modified by the user. The reason for this is to not overload the user with too many questions, the answers of which might not be obvious to them (e.g. what is the pages domain of your gitlab instance).

Calculated template variables are managed in `extensions/context.py`:

{{ includex('extensions/context.py', code='jinja', caption=True, raise_errors=True) }}

As the calculated variables are inserted into the context directly, they can be used just like any other user-provided value.

As an example, this was used in the README template to reuse the `remote_url_pages` and `remote_url_https` URLs, which are calculated from the `remote_url` provided by the user:

{{ includex('template/README.md.jinja', lines=8, code='jinja', caption=True) }}


## History

In the past, these calculated variables were managed in a `context` template file, that could be included in other template files. However, transforming those values in `Jinja` was much more limiting than doing it in Python, which is why this approach was replaced by the `ContextUpdater`
