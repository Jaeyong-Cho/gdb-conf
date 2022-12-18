class multi_window:
    m_x = 0
    m_y = 0
    m_button = 1
    m_current_window = 0 # 0: local, 1: threads 2: backtrace 3: breakpoint

    def __init__(self, tui_window):
        self._tui_window = tui_window
        self._tui_window.title = 'Locals'
        gdb.events.stop.connect(self.update)

    def click(self, x, y, button):
        m_x = y
        m_y = x
        m_button = button
        if y == 0:
            if x >= 0 and x <= 3:
                gdb.execute("run")
            elif x >= 4 and x <= 8:
                gdb.execute("next")
            elif x >= 9 and x <= 13:
                gdb.execute("step")
            elif x >= 14 and x <= 18:
                gdb.execute("continue")
            elif x >= 19 and x <= 23:
                gdb.execute("C-c")
            elif x >= 24 and x <= 28:
                gdb.execute("finish")
        elif y == 1:
            if x >= 0 and x <= 2:
                self._tui_window.title = 'Locals'
                self.m_current_window = 0
                self.print_local()
            elif x >= 3 and x <= 5:
                self._tui_window.title = 'Threads'
                self.m_current_window = 1
                self.print_thread()
            elif x >= 6 and x <= 8:
                self._tui_window.title = 'Backtrace'
                self.m_current_window = 2
                self.print_backtrace()
            elif x >= 9 and x <= 11:
                self._tui_window.title = 'Breakpoint'
                self.m_current_window = 3
                self.print_breakpoint()
        elif y == 2:
            if self.m_current_window == 1:
                current_thread_str = gdb.execute("thread", False, True)
                current_thread_split = current_thread_str.split()
                current_thread_id = current_thread_split[3]

                if x >= 0 and x <= 4:
                    id = str(int(current_thread_id) + 1)
                    gdb.execute("thread " + id)
                    self.print_thread()
                elif x >= 5 and x <= 9:
                    id = str(int(current_thread_id) - 1)
                    gdb.execute("thread " + id)
                    self.print_thread()
            elif self.m_current_window == 2:
                if x >= 0 and x <= 2:
                    gdb.execute("up")
                    self.print_backtrace()
                elif x >= 3 and x <= 7:
                    gdb.execute("down")
                    self.print_backtrace()
            else:
                gdb.execute("focus multi")
        else:
            gdb.execute("focus multi")

    def render(self):
        self._tui_window.erase()
        self._tui_window.write("|Run|Next|Step|Cont|Stop|Fini|\n")
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")

        if self.m_current_window == 0:
            self.print_local()
        elif self.m_current_window == 1:
            self.print_thread()
        elif self.m_current_window == 2:
            self.print_backtrace()
        elif self.m_current_window == 3:
            self.print_breakpoint()

    def update(self, event):
        self.render()

    def print_local(self):
        self._tui_window.erase()
        self._tui_window.write("|Run|Next|Step|Cont|Stop|Fini|\n")
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        locals = gdb.execute("info locals", False, True)
        args = gdb.execute("info args", False, True)
        self._tui_window.write("args:\n")
        self._tui_window.write(args)
        self._tui_window.write("locals:\n")
        self._tui_window.write(locals)

    def print_thread(self):
        self._tui_window.erase()
        self._tui_window.write("|Run|Next|Step|Cont|Stop|Fini|\n")
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        self._tui_window.write("|next|prev|\n")
        thread = gdb.execute("info thread", False, True)
        self._tui_window.write("threads:\n")
        self._tui_window.write(thread)

    def print_backtrace(self):
        self._tui_window.erase()
        self._tui_window.write("|Run|Next|Step|Cont|Stop|Fini|\n")
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        self._tui_window.write("|up|down|\n")
        backtrace = gdb.execute("backtrace", False, True)
        self._tui_window.write("backtrace:\n")
        self._tui_window.write(backtrace)
        frame = gdb.execute("frame", False, True)
        self._tui_window.write("frame:\n")
        self._tui_window.write(frame)

    def print_breakpoint(self):
        self._tui_window.erase()
        self._tui_window.write("|Run|Next|Step|Cont|Stop|Fini|\n")
        self._tui_window.write("|Lo|Th|Bt|Bp|\n")
        breakpoint = gdb.execute("info breakpoint", False, True)
        self._tui_window.write("breakpoint:\n")
        self._tui_window.write(breakpoint)

gdb.register_window_type('multi', multi_window)
