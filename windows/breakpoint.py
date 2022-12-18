class breakpoint_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Breakpoint'

    def render(self):
        self._tui_window.erase()
        breakpoint = gdb.execute("info breakpoint", False, True)
        self._tui_window.write("breakpoint\n")
        self._tui_window.write(breakpoint)

gdb.register_window_type('breakpoint', breakpoint_window)
