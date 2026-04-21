from ai_helpers.llm import call_llm
from ai_helpers.prompts import load_prompt, render, split_template


def run_anki(word: str) -> str:
    system, user_template = split_template(load_prompt("anki"))
    return call_llm(system, render(user_template, word=word))
