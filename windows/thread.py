class thread_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Threads'

    def render(self):
        self._tui_window.erase()
        thread = gdb.execute("info thread", False, True)
        self._tui_window.write("thread\n")
        self._tui_window.write(thread)

gdb.register_window_type('thread', thread_window)
