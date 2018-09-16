from python_enum import PythonCode
from text_import import TxtImport
from python_import import PythonImport


class PythonInfo:

    def __init__(self):
        self.pythonCode = []
        self._type = None

    def type(self, source):
        if type == "-txt":
            self._type = TxtImport()
            self.my_data()
        if source == "-py":
            self._type = PythonImport()
            self.my_data()

    def my_data(self):

        self.pythonCode = self._type.read()

    def save_data(self):

        self._source.save(self.pythonCode)

