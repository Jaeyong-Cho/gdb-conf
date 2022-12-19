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
        self.m_x = y
        self.m_y = x
        self.m_button = button
        if y == 0:
            if x >= 10 and x <= 16:
                gdb.execute("focus src")
            elif x >= 17 and x <= 24:
                gdb.execute("focus cmd")
            elif x >= 25 and x <= 32:
                gdb.execute("focus multi")
        elif y == 1:
            if x >= 10 and x <= 13:
                gdb.execute("run")
            elif x >= 14 and x <= 18:
                gdb.execute("next")
            elif x >= 19 and x <= 23:
                gdb.execute("step")
            elif x >= 24 and x <= 28:
                gdb.execute("continue")
            elif x >= 29 and x <= 33:
                gdb.execute("interrupt")
            elif x >= 34 and x <= 38:
                gdb.execute("finish")
        elif y == 2:
            if x >= 10 and x <= 12:
                self._tui_window.title = 'Locals'
                self.m_current_window = 0
                self.print_local()
            elif x >= 13 and x <= 15:
                self._tui_window.title = 'Threads'
                self.m_current_window = 1
                self.print_thread()
            elif x >= 16 and x <= 18:
                self._tui_window.title = 'Backtrace'
                self.m_current_window = 2
                self.print_backtrace()
            elif x >= 19 and x <= 21:
                self._tui_window.title = 'Breakpoint'
                self.m_current_window = 3
                self.print_breakpoint()
        elif y == 3:
            if self.m_current_window == 1:
                current_thread_str = gdb.selected_thread()
                current_thread_split = current_thread_str.split()
                current_thread_id = current_thread_split[3]

                if x >= 10 and x <= 14:
                    id = str(int(current_thread_id) + 1)
                    gdb.execute("thread " + id)
                    self.print_thread()
                elif x >= 15 and x <= 19:
                    id = str(int(current_thread_id) - 1)
                    gdb.execute("thread " + id)
                    self.print_thread()
            elif self.m_current_window == 2:
                if x >= 10 and x <= 12:
                    gdb.execute("up")
                    self.print_backtrace()
                elif x >= 13 and x <= 17:
                    gdb.execute("down")
                    self.print_backtrace()
            else:
                gdb.execute("focus multi")
        else:
            gdb.execute("focus multi")

    def render(self):
        self._tui_window.erase()
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

    def print_button(self):
        self._tui_window.write("Focus:    |Source|Console|Windows|\n")
        self._tui_window.write("Commands: |Run|Next|Step|Cont|Stop|Fini|\n")
        self._tui_window.write("Windows:  |Lo|Th|Bt|Bp|\n")
        if self.m_current_window == 1:
            self._tui_window.write("Thread:   |next|prev|\n")
        elif self.m_current_window == 2:
            self._tui_window.write("Frame:    |up|down|\n")
        self._tui_window.write("\n")

    def print_local(self):
        self._tui_window.erase()
        self.print_button()
        locals = gdb.execute("info locals", False, True)
        args = gdb.execute("info args", False, True)
        self._tui_window.write("args:\n")
        self._tui_window.write(args)
        self._tui_window.write("\n")
        self._tui_window.write("locals:\n")
        self._tui_window.write(locals)

    def print_thread(self):
        self._tui_window.erase()
        self.print_button()
        thread = gdb.execute("info thread", False, True)
        self._tui_window.write("threads:\n")
        self._tui_window.write(thread)

    def print_backtrace(self):
        self._tui_window.erase()
        self.print_button()
        backtrace = gdb.execute("backtrace", False, True)
        self._tui_window.write("backtrace:\n")
        self._tui_window.write(backtrace)
        frame = gdb.execute("frame", False, True)
        self._tui_window.write("\n")
        self._tui_window.write("frame:\n")
        self._tui_window.write(frame)

    def print_breakpoint(self):
        self._tui_window.erase()
        self.print_button()
        breakpoint = gdb.execute("info breakpoint", False, True)
        self._tui_window.write("breakpoint:\n")
        self._tui_window.write(breakpoint)

gdb.register_window_type('multi', multi_window)
