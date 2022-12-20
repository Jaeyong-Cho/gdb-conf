gdb.execute("define hookpost-layout\nset logging enable off\nset logging enable on\nend")

gdb.execute("tui new-layout ide -horizontal {src 2 cmd 1} 1 {thread 1 backtrace 1 breakpoint 1 local 1 member 1} 1")        
gdb.execute("tui new-layout ide1 -horizontal {src 2 cmd 1} 1 {backtrace 1  local 1 member 1 expression 1} 1 output 1") 
gdb.execute("tui new-layout ide2 -horizontal {src 2 cmd 1} 1 {backtrace 1  local 1 member 1 expression 1} 1") 
gdb.execute("tui new-layout ide3 -horizontal {src 2 cmd 1} 1 {local 1 member 1} 1")        
gdb.execute("tui new-layout ide-bt -horizontal {src 5 cmd 1} 3 {multi 1} 2")
