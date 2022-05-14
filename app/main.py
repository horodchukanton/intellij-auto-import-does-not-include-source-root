"""Simplest possible import from same package"""

import sys

from app.lib.hello import HelloWorldPrinter

# from lib.hello import HelloWorldPrinter

if __name__ == '__main__':
    # Mark the 'app' directory as Sources Root
    # Try to auto-import the class HelloWorldPrinter.
    #   You will get 'lib.hello.HelloWorldPrinter' instead of
    #       'app.lib.hello.HelloWorldPrinter'
    printer = HelloWorldPrinter(sys.stdout)
    printer.print_hello_world()
