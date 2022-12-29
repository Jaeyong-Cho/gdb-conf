import gdb_attach as ga
import psutil

class AttachWithProcessName(gdb.Command):
    """gdb attach with process name"""
    def __init__(self):
        super(AttachWithProcessName, self).__init__("attach-with-name", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        name = gdb.string_to_argv(arg)[0]
        ga.attach_with_process_name(name)

AttachWithProcessName()
