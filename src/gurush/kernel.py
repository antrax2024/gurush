import sys
import time
from InquirerPy import inquirer
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.prompts import HumanMessagePromptTemplate
from rich.console import Console
from rich.markdown import Markdown
from pydantic import HttpUrl
from typing import List, Optional

cl = Console()


def printWithDelay(
    content: str, delay: float = 0.2, code_theme: str = "monokai"
) -> None:
    """
    Print the markdown content with a delay, preserving code blocks.

    Args:
        content: The markdown text content to print
        delay: The delay in seconds between each print operation
        code_theme: The theme to use for code blocks
    """
    import re

    # Split content into chunks: normal text and code blocks
    segments = []
    code_block_pattern = r"(```[\s\S]*?```)"
    parts = re.split(code_block_pattern, content)

    for i, part in enumerate(parts):
        # If this is a code block (starts with ```)
        if part.startswith("```"):
            segments.append({"type": "code", "content": part})
        # If it's regular text
        elif part.strip():
            # Split by paragraphs (double newlines)
            paragraphs = re.split(r"\n\s*\n", part)
            for para in paragraphs:
                if para.strip():
                    segments.append({"type": "text", "content": para.strip()})

    # Print each segment with appropriate formatting
    for segment in segments:
        if segment["type"] == "code":
            # Print code blocks as a whole
            markdown = Markdown(segment["content"], code_theme=code_theme)
            cl.print(markdown)
            time.sleep(delay * 2)  # Slightly longer pause after code blocks
        else:
            # Print text segments line by line for typing effect
            lines = segment["content"].split("\n")
            for line in lines:
                if line.strip():
                    markdown = Markdown(line, code_theme=code_theme)
                    cl.print(markdown)
                    time.sleep(delay)

            # Add a small pause between paragraphs
            cl.print()
            time.sleep(delay)


def answerGuru(
    base_url: HttpUrl, api_key: str, model: str, system_template: str, code_theme: str
) -> None:
    try:
        answer = inquirer.text(message="What is your question?", multiline=True).execute()  # type: ignore
    except KeyboardInterrupt:
        cl.print("\n[bold red]Exiting program.[/bold red]")
        sys.exit(0)

    # Configuração do modelo de chat
    chat_model = ChatOpenAI(
        base_url=str(base_url),
        openai_api_key=api_key,
        model=model,
        temperature=0.9,
    )

    system_template = system_template

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template("{inputText}"),
        ]
    )

    try:
        with cl.status("[bold green]Wait, the Guru is thinking...[/bold green]"):
            chain = prompt | chat_model
            response = chain.invoke({"inputText": answer})
            # Split the response into lines and print with delay
            printWithDelay(response.content, code_theme=code_theme)
    except Exception as e:
        cl.print(f"\n[bold red]Error: {e}[/bold red]")
