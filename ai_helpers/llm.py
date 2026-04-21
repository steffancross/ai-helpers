import os

import anthropic

DEFAULT_MODEL = "claude-sonnet-4-6"
OPUS = "claude-opus-4-7"
SONNET = "claude-sonnet-4-6"
HAIKU = "claude-haiku-4-5"
DEFAULT_MAX_TOKENS = 2048


def call_llm(
    system: str,
    user: str,
    model: str = HAIKU,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key."
        )

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(
        block.text for block in response.content if getattr(block, "type", None) == "text"
    ).strip()
