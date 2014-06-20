import sublime, sublime_plugin, os

class ReindentOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    # Save current selections for restore
    sels = []
    for sel in view.sel(): sels.append(sel)

    # Select All
    view.sel().clear()
    view.sel().add(sublime.Region(0, view.size()))

    # Reindent
    view.window().run_command('reindent')

    # Restore saved selections
    view.sel().clear()
    view.sel().add_all(sels)
