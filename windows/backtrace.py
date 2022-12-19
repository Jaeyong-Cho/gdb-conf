class backtrace_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Backtrace'
        gdb.events.stop.connect(self.update)
        m_x = 0
        m_y = 0
        m_button = 1

    def render(self):
        self._tui_window.erase()
        self._tui_window.write("Focus:    |Source|Console|Windows|\n")
        self._tui_window.write("\n")
        backtrace = gdb.execute("backtrace", False, True)
        frame = gdb.execute("frame", False, True)
        self._tui_window.write("backtrace\n")
        self._tui_window.write(backtrace)
        self._tui_window.write("\n")
        self._tui_window.write("frame\n")
        self._tui_window.write(frame)

    def click(self, x, y, button):
        self.m_x = y
        self.m_y = x
        self.m_button = button

        if y == 0:
            if x >= 10 and x <= 16:
                gdb.execute("focus src")
            elif x >= 17 and x <= 24:
                gdb.execute("focus cmd")
            elif x >= 25 and x <= 32:
                gdb.execute("focus backtrace")
        else:
            gdb.execute("focus backtrace")

    def update(self, event):
        self.render()

gdb.register_window_type('backtrace', backtrace_window)
