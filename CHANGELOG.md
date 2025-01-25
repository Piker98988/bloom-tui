# Changelog

This changelog will keep track of all major changes from version [0.1.4] onwards.

## [0.1.4] **Enhanced Inputs and Outputs** — 21-01-2025

This version introduces improvements to the `colourup` library, enhancing the flexibility and style of terminal applications. It also updates the project configuration for better dependency management and compatibility.

### Added

- This changelog.
- More and better tests.
- Added a new `lfbefore` argument to `pinput` and `title` functions for controlling if a line feed precedes output.
- Introduced `prefixstyle` argument in `pinput` for customizable prefix styling via `colourup.style`.
- Implemented `autoquestion` in `pinput` to automatically update the prompt prefix based on the presence of a question mark at the end of the prompt.
- Enhanced `title` function with new arguments:
    - `stylebefore` and `styleafter` for applying styles to text and borders.
    - `spacesbetween` to control the spaces between the title and its border.
- Added `license` and `project authors` to `pyproject.toml`.
- Provided HomePage and Issue Tracker URLs in `pyproject.toml`.

### Changed

- Updated `tests/test_main.py` to reflect the argument changes in `pinput`:
    - Modified test cases for the new argument options.
- Refactored `pinput` defaults to ensure effective prefix enhancement and style application.
- Improved `title` defaults for more customized output scenarios.
- Updated Python version requirement in documentation to `3.12+` (from `3.6+`).
- Enhanced compatibility with the addition of new dependencies in `requirements.txt`:
    - `twine`
    - `setuptools`
    - `build`

### Fixes

- Fixed issues in default prompts for `pinput` when custom prefix was improperly applied.
- Corrected the reset behavior for styles in `title` to ensure execution stability during rapid print calls.

### Next versions

- Plan to add localization support for input prompts and titles.
- Upcoming features will allow dynamic attribute injection for more customizable outputs.
- Highlighting system in development for console outputs, including warnings and errors.

## [0.2.0] **Selector and Improved Documentation** — 25-01-2025

This version introduces the new `Selector` feature in the base `colourup` library for terminal-based selection menus and significant improvements to documentation for enhanced clarity and usability.

### Added

- Introduced the `Selector` class to build text-based interactive menus with navigation capabilities. Key features include:
  - Menu navigation using arrow keys and `Enter` for selection.
  - Customizable prompts and multi-option handling.
- Added a new `cursor` helper module in the `utils` package for cursor control in terminal applications. Includes:
  - Cursor movement constants like `MOVE_UP`, `MOVE_DOWN`, `ERASE_LINE`, and more.
  - Visibility control using `HIDE` and `SHOW`.
- Expanded `README.md` with an example showcasing the new `Selector` feature, demonstrating its integration and use cases in TUI applications.

### Changed

- Branding: from ColourUp to Bloom
- Enhanced inline function documentation and type annotations across the entire library for better clarity and standardization:
  - Updated docstrings in the `title` and `pinput` functions to reflect standard formats for arguments, return types, and descriptions.
  - Added detailed docstrings for color (`fg`, `bg`) and style (`style`) modules, covering all available constants and their purposes.
  - Provided guidance on module auto-initialization behavior (e.g., `colorama` initialization setup for terminal styling).
- Adjusted `colorama.init()` by setting `autoreset=False` in the `styles/__init__.py` file to give developers more manual control over ANSI style resets.
- Renamed constants:
  - From `FLIPPED` to `INVERTED` in `style.py` for better readability and alignment with terminal color terminology.
- Updated `requirements.txt`:
  - Added new dependency `getch` for keyboard event handling.

### Fixes

- Resolved minor typos in the `README.md`, improving presentation consistency.
- Corrected behavior in `pinput` and `title` functions:
  - Polished formatting for multi-line output handling in custom styles and borders.

### Next versions

- A focus on enhancing the `Selector`'s styling options