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