class multi_window:
    m_x = 0
    m_y = 0
    m_button = 1

    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Locals'
        gdb.events.stop.connect(self.update)

    def click(self, x, y, button):
        m_x = y
        m_y = x
        m_button = button
        if button == 1:
            if y == 0:
                if x >= 0 and x <= 2:
                    self._tui_window.title = 'Locals'
                    self.print_local()
                elif x >= 3 and x <= 5:
                    self._tui_window.title = 'Threads'
                    self.print_thread()
                elif x >= 6 and x <= 8:
                    self._tui_window.title = 'Backtrace'
                    self.print_backtrace()
                elif x >= 9 and x <= 11:
                    self._tui_window.title = 'Breakpoint'
                    self.print_breakpoint()

    def render(self):
        self._tui_window.erase()
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        if self.m_button == 1:
            if self.m_y == 0:
                if self.m_x >= 0 and self.m_x <= 2:
                    self.print_local()
                elif self.m_x >= 3 and self.m_x <= 5:
                    self.print_thread()
                elif self.m_x >= 6 and self.m_x <= 8:
                    self.print_backtrace()
                elif self.m_x >= 9 and self.m_x <= 11:
                    self.print_breakpoint()

    def update(self, event):
        self.render()

    def print_local(self):
        self._tui_window.erase()
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        locals = gdb.execute("info locals", False, True)
        args = gdb.execute("info args", False, True)
        self._tui_window.write("args:\n")
        self._tui_window.write(args)
        self._tui_window.write("locals:\n")
        self._tui_window.write(locals)

    def print_thread(self):
        self._tui_window.erase()
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        thread = gdb.execute("info thread", False, True)
        self._tui_window.write("threads:\n")
        self._tui_window.write(thread)

    def print_backtrace(self):
        self._tui_window.erase()
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        backtrace = gdb.execute("backtrace", False, True)
        self._tui_window.write("backtrace:\n")
        self._tui_window.write(backtrace)
        frame = gdb.execute("frame", False, True)
        self._tui_window.write("frame:\n")
        self._tui_window.write(frame)

    def print_breakpoint(self):
        self._tui_window.erase()
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        breakpoint = gdb.execute("info breakpoint", False, True)
        self._tui_window.write("breakpoint:\n")
        self._tui_window.write(breakpoint)

gdb.register_window_type('multi', multi_window)
