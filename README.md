SublimeLinter-contrib-stylint
================================

This linter plugin for [SublimeLinter][docs] provides an interface to [stylint](https://github.com/rossPatton/stylint). It will be used with files that have the “stylus” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `stylint` is installed on your system. To install `stylint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `stylint` by typing the following in a terminal:
   ```
   npm install -g stylint
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

1. If you are using `zsh` and `oh-my-zsh`, do not load the `nvm` plugin for `oh-my-zsh`.


**Note:** This plugin requires `stylint` 0.9.3 or later.

### Linter configuration
In order for `stylint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `stylint`, you can proceed to install the SublimeLinter-contrib-stylint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `stylint`. Among the entries you should see `SublimeLinter-contrib-stylint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You can configure stylint options in the way you would from the command line, with `.stylintrc` files. For more information, see the stylint docs. The linter plugin does this by searching for a `.stylintrc` file in your stylus file’s current directory tree. If you are an OSX / Linux user, you can also set a global `.stylintrc` in your User (`~`) directory.

You may provide a custom config file by setting the linter’s `"args"` setting to `["--config", "/path/to/file"]`. On Windows, be sure to double the backslashes in the path, for example `["--config", "C:\\Users\\Name\\stylint.conf"]`.

The path to the `.stylintrc` file is cached, meaning if you create a new .stylintrc that should have precedence over the previous one (meaning it is closer to the .styl file) you need to clear the cache for the linter to use the new `.stylintrc` You can clear the cache by going to: Tools > SublimeLinter > Clear Caches.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
