# 🌸🎨 Bloom 🎨🌸

[![PyPI version](https://badge.fury.io/py/bloom-tui.svg)](https://badge.fury.io/py/bloom-tui)
[![Static Badge](https://img.shields.io/badge/python-%2B3.12-blue?logo=python&logoColor=blue)](https://www.python.org/downloads/)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/piker98988/bloom-tui/python-package.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/piker98988/bloom-tui)

Make your terminal output beautiful with simple, intuitive styling functions.

## ✨ Features

- 🎯 Simple API for common terminal styling needs
- 🌈 16 Foreground & Background colors
- 💫 Text effects (bold, italic, underline, inverse)
- 📏 Centered titles with custom borders
- 🔤 Styled input prompts
- 💻 Windows support via Colorama

## 📦 Installation

```bash
pip install bloom-tui
```

## 🚀 Quick Start

```python
from bloom import title, pinput, selector
from bloom.styles import fg, bg, style

# Create beautiful titles
title(text="Welcome to Bloom!", borderchar="=", borderlen=6)  # ====== Welcome to Bloom! ======

# Styled input prompts (spaces at the end included)
name = pinput("What's your name?", customprefix="→")
# What's your name?
# → 

# Easy selection menus
mySelector = selector.Selector("How are you feeling?", ["good", "bad", "normal"])
mySelector.invoke()
"""
How are you feeling?
 > good
 - bad
 - normal
"""

# Colorful output
print(f"{fg.GREEN}{style.BOLD}Success!{style.RESET}")
print(f"{bg.BLUE}{fg.WHITE}Info message{style.RESET}")
```

## 🎨 Available Styles

### Colors (fg/bg)
Standard: `BLACK` `RED` `GREEN` `YELLOW` `BLUE` `MAGENTA` `CYAN` `WHITE`

Bright: `BBLACK` `BRED` `BGREEN` `BYELLOW` `BBLUE` `BMAGENTA` `BCYAN` `BWHITE`

### Text Effects
- `BOLD` -- **Bold text**
- `ITALIC` -- *Italic text*
- `UNDERLINE` -- Underlined text
- `INVERTED` -- The foreground and background colours are inverted
- `RESET` -- Reset all styles, leave it like default 

> [!TIP]
> Use `style.RESET` at the end of each print to prevent bleeding the style to the next lines

## 🛠️ Development
```bash
# Clone the repository
git clone https://github.com/piker98988/bloom-tui.git
cd bloom-tui

# Install bloom
pip install poetry
poetry install
```

## 💡 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

- Fork the repository
- Create your feature branch (`git checkout -b feature/AmazingFeature`)
- Commit your changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request

## 📄 License

This project is licensed under the GNU General Public License v3.0 — see the [LICENSE](LICENSE) file for details.

Copyright (C) 2024 Piker

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
