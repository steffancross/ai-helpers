from importlib import resources


SEPARATOR = "\n---\n"


def load_prompt(name: str) -> str:
    return resources.files(__package__).joinpath(f"{name}.md").read_text(encoding="utf-8")


def split_template(template: str) -> tuple[str, str]:
    if SEPARATOR in template:
        system, user = template.split(SEPARATOR, 1)
        return system.strip(), user.strip()
    return "", template.strip()


def render(template: str, **vars) -> str:
    return template.format(**vars)
