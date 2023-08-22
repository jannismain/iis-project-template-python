---
tags: [Best Practice, Documentation]
---

# Documentation

Documentation is anything about your project that is not executed or used by your application or development environment.

While code is written for both humans and machines, documentation is purely written for other humans.

With this template you can choose one of the following documentation tools:

{% for name, value in read_yaml("copier.yaml").docs.choices.items() %}
{% if value != 'none' %}
- [{{name}}][{{value}}]
{% endif %}
{% endfor %}
