gdb.execute("tui new-layout ide {-horizontal src 5 local_variable 1} 5 cmd 1")

gdb.execute("define hook-stop\nlayout ide\nend")
