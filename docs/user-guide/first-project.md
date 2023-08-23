---
tags: [Tutorial]
---

# Creating your first project

If you followed the steps outlined in [Getting Started][getting-started], you are now presented with a couple of questions about your new project:

{% include 'docs/user-guide/questions.html.jinja' %}

Let's look at them one by one and figure out, what you should choose or how to find the information the template asks for.

{% for key, item in read_yaml('copier.yaml').items() %}
{% if not key.startswith("_") and "explanation" in item %}
## {{key.replace("_", " ").title().replace("Precommit", "pre-commit")}}

{{ item.explanation }}
{% endif %}
{% endfor %}
