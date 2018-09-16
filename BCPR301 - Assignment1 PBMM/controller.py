from cmd import Cmd
from console_view import ConsoleView as View
from python_data import PythonInfo
from Pep8Validator import AutomatePep8


class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)

        self.prompt = "==>"
        self.intro = "Simple Python parsing. This Program validates and parses python code into a graph. \nFor help please enter \"help\"."
        self._pc = PythonInfo()
        self._valid = AutomatePep8()

    def do_type(self, line):
        """

        :param line:
        :return:
        """
        types = "-py", "-txt"
        args = list(arg.lower() for arg in str(line).split())

        try:
            if args[0] != types:
                raise ValueError("That is not a valid option")
            else:
                if args[0] == "-py":
                    try:
                        if len(args) == 1:
                            self._pc.type(args[0][1:], "test_code.py")
                            View.text_show("No file selected using text_code by default")
                        elif len(args) == 2:
                            self._pc.type(args[0][1], args[1])
                    except Exception as e:
                        (print(e))
                    else:
                        View.text_show("Python file selected")

                elif args[0] == "-txt":
                    try:
                        if len(args) == 1:
                            self._pc.type(args[0][1:], "test_code.txt")
                            View.text_show("No file selected using text_code by default")
                        elif len(args) == 2:
                            self._pc.type(args[0][1], args[1])
                    except Exception as e:
                        (print(e))
                    else:
                        View.text_show("Text file selected")

                else:
                    pass

        except ValueError as e:
            View.error_show(str(e) + "\n")
            View.help_select()
        except Exception as e:
            print(e)



    def do_read(self, line):
        """
        Add a new entry of data
        :param line:
        :return:
        """




    def do_save(self, arg):

        """
        :param arg:
        :return:
        """
        self._pc.save_data()

    def do_display(self, line):
        """
        :param line:
        :return:
        """

    def do_quit(self, exit):
        return True


    @staticmethod
    def help_show():
        View.help_show()

    @staticmethod
    def help_quit():
        View.help_quit()

    def help_type():
        View.help_type()
