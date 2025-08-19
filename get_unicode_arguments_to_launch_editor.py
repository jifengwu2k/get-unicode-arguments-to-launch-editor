# coding=utf-8
# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
from find_unicode_executable import find_unicode_executable
from posix_or_nt import posix_or_nt
from read_unicode_environment_variables_dictionary import read_unicode_environment_variables_dictionary
from typing import List, Optional, Text

if posix_or_nt() == 'nt':
    from split_command_line import split_command_line_nt as iterate_command_line_arguments

    FALLBACKS = [u'notepad']

else:
    from split_command_line import split_command_line_posix as iterate_command_line_arguments

    FALLBACKS = [u'nano', u'vi']


def command_to_arguments(command):
    # type: (Text) -> Optional[List[Text]]
    rough_command_line_arguments = list(iterate_command_line_arguments(command))

    if rough_command_line_arguments:
        executable_or_none = next(find_unicode_executable(rough_command_line_arguments[0]), None)

        if executable_or_none is not None:
            rough_command_line_arguments[0] = executable_or_none
            return rough_command_line_arguments

    return None


def get_unicode_arguments_to_launch_editor(editor=None):
    # type: (Optional[Text]) -> List[Text]
    # Check if `editor` is set and valid.
    if editor is not None:
        arguments_or_none = command_to_arguments(editor)
    else:
        # Read environment variables.
        unicode_environment_variables_dictionary = read_unicode_environment_variables_dictionary()

        # Check if the `VISUAL` environment variable is set and valid.
        if u'VISUAL' in unicode_environment_variables_dictionary:
            arguments_or_none = command_to_arguments(unicode_environment_variables_dictionary[u'VISUAL'])
        # Check if the `EDITOR` environment variable is set and valid.
        elif u'EDITOR' in unicode_environment_variables_dictionary:
            arguments_or_none = command_to_arguments(unicode_environment_variables_dictionary[u'EDITOR'])
        else:
            arguments_or_none = None

            # Check if the fallbacks are set and valid.
            for fallback in FALLBACKS:
                new_arguments_or_none = command_to_arguments(fallback)
                if new_arguments_or_none is not None:
                    arguments_or_none = new_arguments_or_none
                    break

    if arguments_or_none is not None:
        return arguments_or_none
    else:
        # If nothing works, throw an exception.
        raise EnvironmentError(
            'Cannot get arguments to launch an EDITOR. '
            'Please pass a valid command to the `editor` parameter, '
            'or set the VISUAL or EDITOR environment variables.'
        )
