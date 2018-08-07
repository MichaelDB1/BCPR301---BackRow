from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    """
    View interface for output
    """
    @staticmethod
    @abstractmethod
    def text_show(text):
        """

        :param text:
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def error_show(text):
        """

        :param text:
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def data_show(data, ind=False):
        """

        :param data:
        :param ind:
        :return:
        """
        pass

