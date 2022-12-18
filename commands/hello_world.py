class HelloWorld(gdb.Command):
    """Print Hello World"""
    def __init__(self):
        super(HelloWorld, self).__init__("hello-world", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        print("Hello World!")

HelloWorld()
