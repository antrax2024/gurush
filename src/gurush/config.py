import os
import shutil
from typing import Any
import importlib.resources
from confz import BaseConfig, FileSource
from gurush.constants import APP_NAME, APP_VERSION, CONFIG_FILE
from gurush.kernel import answerGuru
from term_image.image import BaseImage, from_file
from rich.console import Console
from pydantic import HttpUrl

console = Console()
DEBUG = False


def print_message(preamble: str, variable: Any) -> None:
    """Print formatted key-value pair to console.

    Args:
        preamble: Display label (left-aligned)
        variable: Value to display
    """
    console.print(f"[bold yellow]{preamble:<15}[/bold yellow]: {variable}")


def print_mascot() -> None:
    """Display application mascot using terminal image rendering."""
    mascot_path = importlib.resources.files(APP_NAME).joinpath("assets/mascot.png")
    image: BaseImage = from_file(str(mascot_path), width=60, height=25)
    print(image)


def cli() -> None:
    """Main CLI entry point handling configuration and execution flow."""
    print_mascot()
    console.print(f"[bold yellow]{APP_NAME} v{APP_VERSION}[/bold yellow]")
    console.print("[cyan]=[/cyan]" * 80)

    check_config_file(CONFIG_FILE)

    try:
        app_config = AppConfig()
        if DEBUG:
            print_message("Base URL", app_config.base_url)
            print_message("Model", app_config.model)
            print_message("Code Theme", app_config.code_theme)
            console.print("[cyan]=[/cyan]" * 80)

        answerGuru(
            base_url=app_config.base_url,
            api_key=app_config.api_key,
            model=app_config.model,
            system_template=app_config.system_template,
            code_theme=app_config.code_theme,
        )
    except Exception as e:
        console.print(f"[bold red]ERROR:[/bold red] Invalid configuration: {e}")
        return


def check_config_file(config_path: str) -> None:
    """Ensure configuration file exists, creating it if necessary.

    Args:
        config_path: Full path to configuration file
    """
    try:
        if not os.path.exists(config_path):
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            copy_config_file(config_path)
    except OSError as e:
        console.print(f"File system error: {e}")


def copy_config_file(destination: str) -> None:
    """Copy default config file from package assets.

    Args:
        destination: Target path for config file
    """
    filename = os.path.basename(destination)
    source = importlib.resources.files(APP_NAME).joinpath(f"assets/{filename}")
    shutil.copy2(str(source), destination)


class AppConfig(BaseConfig):
    """Main application configuration powered by confz.

    Attributes:
        base_url: API endpoint URL
        api_key: Authentication credential
        model: LLM model identifier
        code_theme: Syntax highlighting theme
        system_template: Base prompt template
    """

    CONFIG_SOURCES = FileSource(file=CONFIG_FILE)

    base_url: HttpUrl
    api_key: str
    model: str
    code_theme: str
    system_template: str


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
