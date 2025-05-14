# gurush

<p align="center">
  <img src="https://raw.githubusercontent.com/antrax2024/gurush/refs/heads/main/src/gurush/assets/mascot.png" alt="gurush Mascot" />
</p>

<div align="center">
  <span>
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gurush">
    <img alt="AUR Version" src="https://img.shields.io/aur/version/gurush">
    <img alt="Python Version from PEP 621 TOML" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fantrax2024%2Fgurush%2Frefs%2Fheads%2Fmain%2Fpyproject.toml">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/antrax2024/gurush">
    <img alt="GitHub License" src="https://img.shields.io/github/license/antrax2024/gurush">
  </span>
</div>

A command-line AI assistant powered by LangChain and OpenAI's language models.

## Overview

gurush is a terminal application that allows you to interact with AI language models through a simple command-line interface. Ask questions and receive answers formatted with rich markdown.

## Features

- 🧠 AI-powered responses using OpenAI's language models
- 💻 Clean terminal interface with rich formatting
- 🎨 Customizable code highlighting themes
- ⚙️ Simple configuration via YAML
- 📝 Markdown rendering for responses
- 📝 Markdown rendering for responses
- ⚙️ Configurable system prompts

## Installation

### Using pip

```bash
pip install gurush
```

### Using uv

```bash
uv install gurush
```

### Using AUR (Arch Linux)

```bash
yay -S gurush
# or
paru -S gurush
```

## Configuration

gurush uses a YAML configuration file to manage its settings. The default configuration is located at `~/.config/gurush/config.yaml`.

### Configuration Parameters

| Parameter         | Description                                          |
| ----------------- | ---------------------------------------------------- |
| `base_url`        | Base URL for API requests                            |
| `api_key`         | Authentication key for accessing the AI service      |
| `model`           | LLM model to use for generating responses            |
| `code_theme`      | Theme for syntax highlighting in code blocks         |
| `system_template` | Instructions that define the AI assistant's behavior |

Example configuration:

```yaml
base_url: "https://api-base-url.org"
api_key: "your-apikey-here"
model: "llm_model"
code_theme: "github-dark"
system_template: |
  You are a senior technical expert who masters everything about Linux.
  Answer questions following these rules:
  - Be brief and concise
  - Format responses in markdown with proper highlighting
```

## Usage

Using gurush is simple:

1. Open your terminal
2. Type `gurush` and press Enter to start the application
3. Ask any technology-related question
4. Press `ESC+Enter` to submit and get your AI-powered response
5. Review the formatted markdown output with syntax highlighting

Example:

```bash
$ gurush
> How do I check disk usage in Linux?
```

After pressing `ESC+Enter`, you'll receive a nicely formatted response with the requested information.
