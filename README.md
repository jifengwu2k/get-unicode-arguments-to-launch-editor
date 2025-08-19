# `get-unicode-arguments-to-launch-editor`

A cross-platform Python utility that gets Unicode arguments to launch an EDITOR, using user input, environment
variables, and platform-specific fallbacks.

## Features

- Gets arguments to launch an EDITOR using (in order of precedence):
    1. User-supplied command (`editor` parameter)
    2. `$VISUAL` environment variable
    3. `$EDITOR` environment variable
    4. Platform-specific fallbacks:
        - NT: `notepad`
        - POSIX: `nano`, `vi`
- Verifies that the editor executable exists on the system.
- Canonicalizes the returned command as a list suitable for `os.execvp()` or `subprocess` calls.
- Command-line splitting and executable resolution is platform-aware.

## Installation

```commandline
pip install get-unicode-arguments-to-launch-editor
```

## Usage

```python
# coding=utf-8
from __future__ import print_function
from get_unicode_arguments_to_launch_editor import get_unicode_arguments_to_launch_editor

# Example output on Linux:
# [u'/usr/bin/nano']
print(get_unicode_arguments_to_launch_editor())

# Example output on Linux:
# [u'/usr/bin/vim.basic', u'-R']
print(get_unicode_arguments_to_launch_editor(u'vim -R'))
```

## Contributing

Contributions welcome! Please open issues or pull requests on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).