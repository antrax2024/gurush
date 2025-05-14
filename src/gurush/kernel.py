import sys
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

cl = Console()


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
        with cl.status("[bold green]Processing...[/bold green]"):
            chain = prompt | chat_model
            response = chain.invoke({"inputText": answer})
            markdown = Markdown(
                response.content,
                code_theme=code_theme,
            )
            cl.print(markdown)
    except Exception as e:
        cl.print(f"\n[bold red]Error: {e}[/bold red]")
