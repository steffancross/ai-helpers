import os

from openai import OpenAI


def call(system: str, user: str, model: str, max_tokens: int) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Copy .env.example to .env and add your key."
        )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        instructions=system,
        input=user,
        max_output_tokens=max_tokens,
    )
    return response.output_text.strip()
