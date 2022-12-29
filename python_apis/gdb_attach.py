import gdb
import psutil

def attach_with_process_name(name):
    processes = psutil.process_iter()
    for proc in processes:
        if proc.name() == name:
            gdb.execute("attach " + str(proc.pid))
            print("Attach to pid: " + str(proc.pid))
            return

    print("Process not found with name " + name)

