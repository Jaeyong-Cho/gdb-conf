gdb.execute("tui new-layout ide -horizontal {src 5 cmd 1} 3 {thread 1 backtrace 1 breakpoint 1 local 1 member 1} 2")        
gdb.execute("define hookpost-up\n layout ide\n end")
gdb.execute("define hookpost-down\n layout ide\n end")

gdb.execute("tui new-layout ide-bt -horizontal {src 5 cmd 1} 3 {multi 1} 2")
