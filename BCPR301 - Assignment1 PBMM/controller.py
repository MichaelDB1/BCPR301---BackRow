from cmd import Cmd
from console_view import ConsoleView as View


class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)

    def source_select(self, line):

        """
        Data source selection
        :param line:
        :return:
        """

    def data_add(self, line):
        """
        Add a new entry of data
        :param line:
        :return:
        """

    def data_save(self, arg):
        """

        :param arg:
        :return:
        """

    def data_display(self, line):
        """
        :param line:
        :return:
        """

    @staticmethod
    def help_show():
        View.help_show()


if __name__ == "__main__":
    ctl = Controller()
    ctl.cmdloop()
