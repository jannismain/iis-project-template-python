---
tags: [Tutorial]
---

# Your First Project

If you followed the steps outlined in [Getting Started][getting-started], you are now presented with a couple of questions about your new project.

Let's go through them together.

{% for key, item in read_yaml('copier.yaml').items() %}
{% if not key.startswith("_") and "explanation" in item %}
## {{key.replace("_", " ").title().replace("Precommit", "pre-commit")}}

{{ item.explanation }}
{% endif %}
{% endfor %}
