# gdb-conf
## Introduction
- Simple configuration for gdb

1. New gdb tui layout 'ide'

## Installation
### gdb configure compile
```
./configure --enable-targets=all --with-curses --with-python
```

### ~/.gdbinit
```
source .../gdb-conf/source_py.py

set history save
set verbose off
set print pretty on
set print array off
set print array-indexes on
set python print-stack full
```

## Usage
- run gdb
- type `layout ide` in gdb

### 

## Screenshot
1. Arguments and Locals **(click 'Lo')**
![plot](./doc/gdb1.png)
2. Threads **(click 'Th')**
![plot](./doc/gdb2.png)
3. Backtrace and Frame **(click 'Bt')**
![plot](./doc/gdb3.png)
4. Breakpoint **(click 'Bp')**
![plot](./doc/gdb4.png)
