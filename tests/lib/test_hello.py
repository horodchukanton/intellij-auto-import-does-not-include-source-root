from pytest import fixture

from app.lib.hello import HelloWorldPrinter


class MockOutput:
    def __init__(self):
        self.output = ""

    def write(self, string):
        self.output += string

    def get_output(self):
        return self.output


class TestHelloWorldPrinter:

    @fixture
    def output(self):
        return MockOutput()

    @fixture
    def printer(self, output):
        return HelloWorldPrinter(output)

    @fixture
    def string_input(self):
        return "Hello World"

    def test_sanity(self, printer, string_input, output):
        printer.print_hello_world()

        assert output.get_output() == string_input
        assert printer.get_counter() == 1
