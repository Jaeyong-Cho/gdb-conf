class local_variable_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Locals'

    def render(self):
        self._tui_window.erase()
        locals = gdb.execute("info locals", False, True)
        args = gdb.execute("info args", False, True)
        self._tui_window.write(args)
        self._tui_window.write(locals)

gdb.register_window_type('local_variable', local_variable_window)
