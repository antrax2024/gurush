# - This is a Python 3.13 application
# - Enforce static typing (type hints) in all functions
# - Enable rich terminal output using `rich`
# - Manage Python dependencies and builds with `uv`
# - Adhere to PEP8 code style standards
# - Maintain English-only documentation and code comments
# - Apply camelCase convention for variables, methods and functions
# **Note**: While camelCase conflicts with PEP8's snake_case recommendation for Python,
# this requirement takes precedence per project specifications

import os
import shutil
from typing import Any
from confz import BaseConfig, FileSource
from .constants import APP_NAME, APP_VERSION, CONFIG_FILE
import importlib.resources
from rich.console import Console
from gurush.kernel import answerGuru
from pydantic import HttpUrl
from term_image.image import from_file

cl = Console()

# control debug mode
DEBUG = True


def printMessage(preamble: str, variable: Any) -> None:
    """
    Print a message to the console with fixed width preamble.
    """
    cl.print(f"[bold yellow]{preamble:<15}[/bold yellow]: {variable}")


def printMascot() -> None:
    mascotFile = importlib.resources.files(anchor=f"{APP_NAME}").joinpath(
        "assets/mascot.png"
    )
    image = from_file(mascotFile, width=40)  # pyright: ignore
    print(image)


def cli() -> None:
    printMascot()
    cl.print(f"[bold yellow]{APP_NAME} v{APP_VERSION}[/bold yellow]\n")
    cl.print("[cyan]=[/cyan]" * 80)
    # Check config file
    checkFile(file=CONFIG_FILE)

    try:
        appConfig = AppConfig()
    except Exception as e:
        cl.print(f"[bold red]ERROR:[/bold red] Invalid configuration: {e}")
        return

    if DEBUG:
        printMessage(preamble="Base URL", variable=appConfig.base_url)
        printMessage(preamble="Model", variable=appConfig.model)
        printMessage(preamble="Code Theme", variable=appConfig.code_theme)
        cl.print("[cyan]=[/cyan]" * 80)

    answerGuru(
        base_url=appConfig.base_url,
        api_key=appConfig.api_key,
        model=appConfig.model,
        system_template=appConfig.system_template,
        code_theme=appConfig.code_theme,
    )


def checkFile(file: str) -> None:
    try:
        if not os.path.exists(path=file):
            os.makedirs(name=os.path.dirname(p=file), exist_ok=True)
            copyFile(destination=file)
    except FileNotFoundError as e:
        cl.print(f"Error: {e}")


def copyFile(destination) -> None:
    # Extract only the filename from destination variable
    filename = os.path.basename(destination)

    source = importlib.resources.files(anchor=f"{APP_NAME}").joinpath(
        f"assets/{filename}"
    )
    # Convert Traversable to string path and copy the file
    shutil.copy2(
        src=str(object=source),
        dst=destination,
    )


# Main configuration class
class AppConfig(BaseConfig):
    CONFIG_SOURCES = FileSource(
        file=os.path.join(
            os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
        )
    )
    base_url: HttpUrl
    api_key: str  # API key for authentication
    model: str
    code_theme: str
    system_template: str


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
