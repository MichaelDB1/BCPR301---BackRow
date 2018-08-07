from the_view import View


class ConsoleView(View):
    @staticmethod
    def text_show(text):
        print(text)

    @staticmethod
    def error_show(text):
        print(text)

    @staticmethod
    def data_show(data, ind=False):
        print(data)

    @staticmethod
    def help_show():
        print("Will write up some help commands here")
