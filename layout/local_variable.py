class local_variable_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Locals'

    def render(self):
        self._tui_window.erase()
        local_variables = gdb.execute("info locals", False, True)
        self._tui_window.write(local_variables)

gdb.register_window_type('local_variable', local_variable_window)
