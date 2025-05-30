<!-- markdownlint-disable -->

# gurush

<p align="center">
  <img src="https://raw.githubusercontent.com/antrax2024/gurush/refs/heads/main/src/gurush/assets/mascot.png" alt="gurush Mascot" />
</p>

<div align="center">
  <span>
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gurush">
    <img alt="Python Version from PEP 621 TOML" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fantrax2024%2Fgurush%2Frefs%2Fheads%2Fmain%2Fpyproject.toml">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/antrax2024/gurush">
    <img alt="GitHub License" src="https://img.shields.io/github/license/antrax2024/gurush">
  </span>
</div>

_A shell command-line AI assistant powered by LangChain._

## 📋 Overview

**gurush** is a terminal application that allows you to interact with **AI language models** through a simple command-line interface. Ask questions and receive answers formatted with rich markdown.

The name "gurush" combines "guru" (the oracle of wisdom) and "sh" (for shell), creating a digital wisdom oracle right in your terminal! 🧙 It's like having a wise mountain sage who lives in your command line, ready to share knowledge without requiring a trek to a distant peak.

## Demonstration

https://github.com/user-attachments/assets/cb96185d-32c6-4cf8-8316-321646b36bff

## ✨ Features

- 🤖 Compatible with any LLM (Large Language Model) that provides an OpenAI-compatible API
- 💻 Clean terminal interface with rich formatting
- 🎨 Customizable code highlighting themes
- ⚙️ Simple configuration via YAML
- 📝 Markdown rendering for responses
- 🔧 Configurable system prompts

## 📥 Installation

### Using pip

```bash
pip install gurush
```

### Using uv

```bash
uv pip install gurush
```

### Using AUR (Arch Linux)

```bash
yay -S gurush
# or
paru -S gurush
```

### ⚙️ Configuration Parameters

- **base_url**: Base URL for API requests
- **api_key**: Authentication key for accessing the AI service
- **model**: LLM model to use for generating responses
- **code_theme**: Theme for syntax highlighting in code blocks. Available themes include: "monokai", "github-dark", "one-dark", "solarized-dark", "solarized-light", "dracula", "nord", "gruvbox-dark", "zenburn", etc. (Any Pygments style)
- **system_template**: Instructions that define the AI assistant's behavior

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

### 🎨 Available Code Themes

The `code_theme` parameter accepts any Pygments style name. Some popular options include:

- `github-dark` - GitHub's dark theme
- `monokai` - Vibrant dark theme popular in many editors
- `one-dark` - Atom editor's dark theme
- `solarized-dark` and `solarized-light` - Popular color schemes with light/dark variants
- `dracula` - A dark theme with vibrant colors
- `nord` - A blue-tinted minimal theme
- `gruvbox-dark` - Retro theme with warm colors

## 🚀 Usage

It's very simple to use **gurush**. In the terminal, type **gurush** and press Enter. Ask any question and
you will receive a response formatted in markdown.
Example:

```bash
$ gurush
> How do I check disk usage in Linux?
```

## 📄 License

gurush is released under the **MIT License**, which is a permissive open-source license. This means you can use, modify, distribute, and even use the software for commercial purposes, provided you include the original copyright notice and disclaimer in any copies or substantial portions of the software.

For more details, see the [LICENSE](LICENSE) file in the repository.
