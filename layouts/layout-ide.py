gdb.execute("tui new-layout ide -horizontal {src 5 cmd 1} 3 {thread 1 backtrace 1 breakpoint 1 local 1 member 1} 2")        
gdb.execute("tui new-layout ide1 -horizontal {src 5 cmd 1} 3 {breakpoint 1 local 1 member 1} 2")        
gdb.execute("tui new-layout ide2 -horizontal {src 5 cmd 1} 3 {local 1 member 1} 2")        

gdb.execute("tui new-layout ide-bt -horizontal {src 5 cmd 1} 3 {multi 1} 2")
