class backtrace_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Backtrace'
        gdb.events.stop.connect(self.update)

    def render(self):
        self._tui_window.erase()
        backtrace = gdb.execute("backtrace", False, True)
        self._tui_window.write("backtrace\n")
        self._tui_window.write(backtrace)

    def update(self, event):
        self.render()

gdb.register_window_type('backtrace', backtrace_window)
