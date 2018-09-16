from abc import ABCMeta, abstractmethod


class PythonFileAccess(metaclass=ABCMeta):
    """
    Interface for python file interaction
    """

    @abstractmethod
    def python_read(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def python_save(self, data: list):
        """

        :param data:
        :return:
        """
        pass
