from Python_file_access import PythonFileAccess
from python_enum import PythonCode


class TxtImport(PythonFileAccess):

    __path = PythonCode.LOCATION
    __name = PythonCode.FILENAME
    __python = PythonCode.CODE

    def __init__(self, file_path):
        self.__path = file_path
        paths = str(file_path).split("/")
        if len(paths) > 1:
            self.__file_path = "/".join(paths[0:-1])
        self.__name = paths[-1]

    def python_read(self):
        with open(self.__path, "r") as file:
            self.__python = file.read()
            file.close()

    def python_save(self):
        with open(self.__path, "w") as file:
            file.write(str(PythonCode))
            file.close()



