class history_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Value History'

    def render(self):
        self._tui_window.erase()
        self._tui_window.write('Hello World\n')
        self._tui_window.write('Two\nLines\n')

gdb.register_window_type('history', history_window)
