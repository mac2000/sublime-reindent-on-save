import sublime, sublime_plugin, os

class ReindentOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    view.window().run_command('reindent', {"single_line": False})
