

if __name__ == '__main__':
    # Mark the 'app' directory as Sources Root
    # Try to auto-import the class HelloWorldPrinter.
    #   You will get 'lib.hello.HelloWorldPrinter' instead of
    #       'app.lib.hello.HelloWorldPrinter'
    printer = HelloWorldPrinter()
    printer.print_hello_world()
