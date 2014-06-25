import sublime, sublime_plugin, os

class ReindentOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    cfg = view.settings().get('reindent_on_save', True)

    if not cfg:
      return

    path = view.file_name()

    if not path:
      return

    if isinstance(cfg, list):
      extension = (path.split('.')[-1]).lower()
      if extension in [ext.lower() for ext in cfg]:
        view.window().run_command('reindent', {"single_line": False})
    else:
      view.window().run_command('reindent', {"single_line": False})
