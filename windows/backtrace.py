class backtrace_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Backtrace'
        gdb.events.before_prompt.connect(self.update)
        self._x = 0
        self.m_y = 0
        self.m_button = 1
        self.m_view_y = 0
        self.m_window_data = ""
        self.m_win_line = "" 
        self.m_win_len = 0

    def render(self):
        self.m_window_data = ""
        self.m_window_data += "backtrace:\n"
        self.m_window_data += gdb.execute("backtrace", False, True)
        self.m_window_data += "\n"
        self.m_window_data += "frame:\n"
        self.m_window_data += gdb.execute("frame", False, True)

        self.m_win_line = self.m_window_data.splitlines()
        self.m_win_len = self.m_win_line.__len__()
        self.print_win()

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

    def vscroll(self, num):
        self.m_view_y += num
        if self.m_view_y < 0:
            self.m_view_y = 0
        elif self.m_view_y > self.m_win_len:
            self.m_view_y = self.m_win_len

        self.print_win()

    def print_win(self):
        win_temp = "Focus:    |Source|Console|Windows|\n\n"

        for i in range(self.m_view_y, self.m_win_len - 1):
            win_temp += self.m_win_line[i] + "\n";

        win_temp = hl._tui_text_highlight(win_temp)
        self._tui_window.write(win_temp, True)

    def update(self):
        self.render()

gdb.register_window_type('backtrace', backtrace_window)
