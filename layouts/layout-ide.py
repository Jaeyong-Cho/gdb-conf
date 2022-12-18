gdb.execute("tui new-layout ide -horizontal {src 9 cmd 1} 3 {thread 1 breakpoint 1 local_variable 1} 2")

gdb.execute("define hook-stop\nlayout ide\nend")
