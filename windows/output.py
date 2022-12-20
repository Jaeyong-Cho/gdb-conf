class output_window:

    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Output'
        gdb.events.before_prompt.connect(self.update)
        self.m_x = 0
        self.m_y = 0
        self.m_button = 1
        self.m_view_y = 0
        self.m_window_data = ""
        self.m_win_line = "" 
        self.m_win_len = 0
        self.m_outfile = open("./gdb.out", "r")
        self.m_output = ""
        self.m_output_len = 0
        self.m_window_height = self._tui_window.height

    def render(self):
        self.m_window_data = ""

        self.m_window_height = self._tui_window.height

        self.m_outfile.seek(0)
        self.m_output = self.m_outfile.readlines()
        self.m_output_len = self.m_output.__len__()
        
        self.m_window_data += "".join(self.m_output)

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
                gdb.execute("focus output")
        else:
            gdb.execute("focus output")

    def vscroll(self, num):
        self.m_view_y += num
        if self.m_view_y + self.m_win_len < 0:
            self.m_view_y = -self.m_win_len 
        elif self.m_view_y > 0:
            self.m_view_y = 0

        self.render()

    def print_win(self):
        win_temp = "output:\n"

        start_line = self.m_view_y + self.m_win_len - self.m_window_height
        end_line = self.m_view_y + self.m_win_len

        if start_line < 0:
            for i in range(0, -start_line):
                win_temp += "\n"
            start_line = 0

        for i in range(start_line + 1, end_line):
            win_temp += self.m_win_line[i] + "\n"

        win_temp += "\n"

        win_temp = hl._tui_text_highlight(win_temp)
        self._tui_window.write(win_temp, True)

    def update(self):
        self.render()

gdb.register_window_type('output', output_window)
