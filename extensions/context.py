import subprocess

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        context["author_name"] = call(["git", "config", "user.name"]) or context["user_name"]
        context["author_email"] = call(["git", "config", "--global", "user.email"]) or ""


def call(cmd: list[str]):
    try:
        return subprocess.check_output(cmd, text=True).strip()
    except subprocess.CalledProcessError:
        return None
