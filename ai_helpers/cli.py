import os
import sys

import click
from dotenv import find_dotenv, load_dotenv

from ai_helpers.flows import run_anki, run_coverletter

load_dotenv(find_dotenv(usecwd=True))
load_dotenv(os.path.expanduser("~/.env"))


@click.group()
def main() -> None:
    """ai — run predefined LLM prompt flows."""


@main.command("anki")
@click.argument("word", required=False)
def anki_cmd(word: str | None) -> None:
    """Generate a Japanese Anki flashcard entry for WORD."""
    if not word:
        word = click.prompt("Word", type=str)
    try:
        click.echo(run_anki(word))
    except RuntimeError as exc:
        raise click.ClickException(str(exc)) from exc


@main.command("coverletter")
@click.option("--company", default=None, help="Target company name. Prompted for if omitted.")
@click.option("--interest", default=None, help="Why you're interested. Prompted for if omitted (may be left blank).")
def coverletter_cmd(company: str | None, interest: str | None) -> None:
    """Generate 5 company-specific sentence options for a cover letter.

    Interactive: prompts for company and interest, then opens $EDITOR for the job description.
    Piped: reads the job description from stdin; pass --company and --interest as flags.
    """
    interactive = sys.stdin.isatty()
    if not company:
        if not interactive:
            raise click.ClickException("Pass --company when piping the job description.")
        company = click.prompt("Company", type=str).strip()
    if interest is None:
        interest = click.prompt("Why interested (optional)", default="", show_default=False) if interactive else ""
    if interactive:
        click.echo("Opening your editor — paste the job description, save, and close.", err=True)
        jd = click.edit(text="", extension=".txt", require_save=True) or ""
    else:
        jd = sys.stdin.read()
    jd = jd.strip()
    if not jd:
        raise click.ClickException("Job description is empty.")
    try:
        click.echo(run_coverletter(company=company, jd=jd, interest=interest))
    except RuntimeError as exc:
        raise click.ClickException(str(exc)) from exc
