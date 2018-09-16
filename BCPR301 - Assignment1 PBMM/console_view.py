from the_view import View
import os


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

    @staticmethod
    def help_quit():
        print("Command:")
        print("\tquit : Allows user to leave the application")
        print("\nExample:")
        print("\t quit : Exits the user from the application")

    @staticmethod
    def help_type():
        print("Command:")
        print("\ttype: Pick the file type you wish to import")
        print("\tOptions:")
        print("\t-py : Import a python file")
        print("\t-txt : Import a text file")
        print("\t-py : Import a python file")
        print("\t-txt : Import a text file")

    @staticmethod
    def draw_python(pyCode):
        os.system("{pyreverse_file} {flags} {input_data_file}".format(
            pyreverse_file="D:\\Mikescode\\Anaconda3\\Scripts\\pyreverse.exe",
            flags="-f ALL -m y -S",
            input_data_file=pyCode))
            #".\\test_code.py"))

        os.system("{dot_file} {flags} {input_dot_file}".format(dot_file=".\\graphviz-2.38\\release\\bin\\dot.exe",
                                                               flags="-v -O -Tjpeg",
                                                               input_dot_file=".\\classes.dot"))
