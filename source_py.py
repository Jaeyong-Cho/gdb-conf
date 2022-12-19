import glob
import sys

# gdb pretty printing of c++ STL
sys.path.insert(0, '/usr/share/gcc/python')
from libstdcxx.v6.printers import register_libstdcxx_printers
register_libstdcxx_printers (None)

python_dir = "/home/jaeyong/gdb-conf/commands"

py_files = glob.glob("%s/*.py" % python_dir)
for py_file in py_files:
    gdb.execute('source %s' % py_file)

python_dir = "/home/jaeyong/gdb-conf/windows"

py_files = glob.glob("%s/*.py" % python_dir)
for py_file in py_files:
    gdb.execute('source %s' % py_file)

python_dir = "/home/jaeyong/gdb-conf/layouts"

py_files = glob.glob("%s/*.py" % python_dir)
for py_file in py_files:
    gdb.execute('source %s' % py_file)
