from ai_helpers.providers import anthropic as _anthropic
from ai_helpers.providers import openai as _openai

OPUS = "claude-opus-4-7"
SONNET = "claude-sonnet-4-6"
HAIKU = "claude-haiku-4-5"
GPT5_4 = "gpt-5.4"
GPT5_4_MINI = "gpt-5.4-mini"

DEFAULT_MODEL = GPT5_4
DEFAULT_MAX_TOKENS = 2048


def call_llm(
    system: str,
    user: str,
    model: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> str:
    if model.startswith("claude-"):
        return _anthropic.call(system, user, model, max_tokens)
    return _openai.call(system, user, model, max_tokens)
