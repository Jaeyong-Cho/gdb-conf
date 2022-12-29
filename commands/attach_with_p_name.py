import psutil

class AttachWithProcessName(gdb.Command):
    """gdb attach with process name"""
    def __init__(self):
        super(AttachWithProcessName, self).__init__("attach-with-name", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        name = gdb.string_to_argv(arg)[0]
        processes = psutil.process_iter()
        for proc in processes:
            if proc.name() == name:
                gdb.execute("attach " + str(proc.pid))
                print("Attach to pid: " + str(proc.pid))
                return

        print("Process not found with name " + name)

AttachWithProcessName()
