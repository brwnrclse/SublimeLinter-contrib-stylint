#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jack Brewer
# Copyright (c) 2015 Jack Brewer
#
# License: MIT

"""Exports the Stylint plugin class."""

from SublimeLinter.lint import NodeLinter, util
from regex import regex


class Stylint(NodeLinter):

    """Provides an interface to stylint."""

    npm_name = 'stylint'
    syntax = ('stylus', 'vue')
    selectors = {'vue': 'source.stylus.embedded.html'}
    cmd = 'stylint @ *'
    executable = 'stylint'
    version_requirement = '>= 1.5.0'
    regex = regex
    multiline = True
    error_stream = util.STREAM_STDOUT
    tempfile_suffix = 'styl'
    config_file = ('--config', '.stylintrc', '~')
