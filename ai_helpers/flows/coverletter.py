from ai_helpers.llm import call_llm
from ai_helpers.prompts import load_prompt, render, split_template


def run_coverletter(company: str, jd: str, interest: str = "") -> str:
    system, user_template = split_template(load_prompt("coverletter"))
    user = render(user_template, company=company, jd=jd, interest=interest or "(none provided)")
    return call_llm(system, user)
