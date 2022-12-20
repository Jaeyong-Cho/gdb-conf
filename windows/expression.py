import source_hl as hl

class expression_window:
    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Expression'
        gdb.events.before_prompt.connect(self.update)
        self.m_x = 0
        self.m_y = 0
        self.m_button = 1
        self.m_view_y = 0
        self.m_window_data = ""
        self.m_win_line = "" 
        self.m_win_len = 0
        self.m_last_value = [""] * 20

    def render(self):
        self.m_window_data = ""
        self.m_window_data += "display:\n"
        self.m_window_data += gdb.execute("info display", False, True)

        self.m_win_line = self.m_window_data.splitlines()
        self.m_win_len = self.m_win_line.__len__()

        for i in range(self.m_view_y, self.m_win_len):
            if i >= 5:
                win_split = self.m_win_line[i].split()
                try:
                    value = gdb.parse_and_eval(''.join(win_split[2:]))
                except gdb.error:
                    self.m_win_line[i] += " = " + str(self.m_last_value[i - 5])
                else:
                    self.m_last_value[i - 5] = (str(value))
                    self.m_win_line[i] += " = " + str(self.m_last_value[i - 5])

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
                gdb.execute("focus expression")
        else:
            gdb.execute("focus expression")

    def vscroll(self, num):
        self.m_view_y += num
        if self.m_view_y < 0:
            self.m_view_y = 0
        elif self.m_view_y > self.m_win_len:
            self.m_view_y = self.m_win_len

        self.print_win()

    def print_win(self):
        win_temp = "Focus:    |Source|Console|Windows|\n\n"

        for i in range(self.m_view_y, self.m_win_len -1):
            win_temp += self.m_win_line[i] + "\n";

        win_temp = hl._tui_text_highlight(win_temp)
        self._tui_window.write(win_temp, True)

    def update(self):
        self.render()

gdb.register_window_type('expression', expression_window)
