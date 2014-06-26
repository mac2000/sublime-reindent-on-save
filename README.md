Sublime Text - reindent on save
===============================

![screenshot](https://github.com/mac2000/sublime-reindent-on-save/raw/master/screenshot.gif)

This is simple plugin to call *reindent* each time you save your file.

What you should be aware is that sublime's *reindent* is not perfect.

You can specify file types which you want to be reindented on save:

    "reindent_on_save": ["css", "SCSS", "html", "Js"]


Installation
------------

The recommended installation method is via Package Control. Learn more here: https://sublime.wbond.net/.


How to add configuration option
-------------------------------

In your Sublime navigate to **Preferences** \ **Settings - User**

Your settings file will be opened.

In fresh installation of Sublime it probably will be something like this:

    {
        "ignored_packages": ["Vintage"]
    }

Or if you have made some changes, they will be saved here, in my case I had something like this:

    {
        "color_scheme": "Packages/Color Scheme - Default/Monokai.tmTheme",
        "convert_tabspaces_on_save": true,
        "default_line_ending": "unix",
        "draw_white_space": "all",
        "ensure_newline_at_eof_on_save": true,
        "font_size": 14,
        "highlight_line": true,
        "highlight_modified_tabs": true,
        "ignored_packages": ["Vintage"],
        "rulers": [80, 120],
        "show_encoding": true,
        "show_line_endings": true,
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true,
        "word_wrap": false
    }
    
To add new options, just place comma after last option and add new one, here is what it will look like in fresh installation:

    {
        "ignored_packages": ["Vintage"],
        "reindent_on_save": ["php", "sublime-settings", "json", "html", "css"]
    }

That is important to not forget add comma, or sublime will fail saving changes, and show you error message "Error trying to parse settings: Unexpected character, expected a comma"
