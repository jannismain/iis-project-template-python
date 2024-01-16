# Creating your first project

If you followed the steps outlined in [Getting Started][getting-started], you are now presented with a couple of questions about your new project:

{% include 'docs/user-guide/questions.html.jinja' %}

Let's look at them one by one and figure out, what you should choose or how to find the information the template asks for.

{% for key, item in read_yaml('copier.yaml').items() %}
{% if not key.startswith("_") and "explanation" in item %}
{% if item.explanation.startswith("##") %}
{{item.explanation.splitlines()[0]}}
{% set description = "\n".join(item.explanation.splitlines()[1:]) %}
{% else %}
## {{key.replace("_", " ").title()}}
{% set description = item.explanation %}
{% endif %}

{{ description }}
{% endif %}
{% endfor %}

---

Congrats 🎉 You just created your first project!

Head over to [Next Steps][next-steps] to find out what you should do now.

🤓 *Pro tip: Simply press ++"."++ to continue to the next page...*
