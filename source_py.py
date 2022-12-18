import glob

python_dir = "/home/jaeyong/gdb-python/commands"

py_files = glob.glob("%s/*.py" % python_dir)
for py_file in py_files:
    gdb.execute('source %s' % py_file)

python_dir = "/home/jaeyong/gdb-python/windows"

py_files = glob.glob("%s/*.py" % python_dir)
for py_file in py_files:
    gdb.execute('source %s' % py_file)

python_dir = "/home/jaeyong/gdb-python/layouts"

py_files = glob.glob("%s/*.py" % python_dir)
for py_file in py_files:
    gdb.execute('source %s' % py_file)
