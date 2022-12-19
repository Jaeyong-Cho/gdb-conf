class thread_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Threads'
        gdb.events.stop.connect(self.update)
        gdb.events.new_thread.connect(self.update)
        self.m_x = 0
        self.m_y = 0
        self.m_button = 1
        self.m_view_y = 0
        self.m_window_data = ""
        self.m_win_len = 0

    def render(self):
        self.m_window_data = "Focus:    |Source|Console|Windows|\n\n"
        self.m_window_data += "thread\n"
        self.m_window_data += gdb.execute("info thread", False, True)

        win_line = self.m_window_data.splitlines()
        self.m_win_len = win_line.__len__()
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
                gdb.execute("focus thread")
        else:
            gdb.execute("focus thread")

    def vscroll(self, num):
        self.m_view_y += num
        if self.m_view_y < 0:
            self.m_view_y = 0
        elif self.m_view_y > self.m_win_len:
            self.m_view_y = self.m_win_len

        self.print_win()

    def print_win(self):
        win_line = self.m_window_data.splitlines()
        win_temp = ""

        for i in range(self.m_view_y, self.m_win_len):
            win_temp += win_line[i] + "\n";

        self._tui_window.erase()
        self._tui_window.write(win_temp)

    def update(self, event):
        self.render()

gdb.register_window_type('thread', thread_window)
