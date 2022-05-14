"""Prints 'Hello, World' to the provided writer"""
import sys


class HelloWorldPrinter:
    """Prints 'Hello, World' to the provided writer"""

    def __init__(self, out=sys.stdout):
        self.out = out
        self.counter = 0

    def print_hello_world(self):
        """Prints 'Hello, World' to the writer"""
        self.counter += 1
        return self.out.write('Hello World')

    def get_counter(self):
        """Returns the number of times the hello world has been printed"""
        return self.counter
