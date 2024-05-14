from abc import ABC, abstractmethod


class BaseMatcher(ABC):
    """
    Base class that all matcher classes should inherit from in order
    to ensure uniformity.
    """
    case_sensitive: bool

    @abstractmethod
    def search(self, pattern: str, text: str) -> tuple:
        """
        Should return a list containing all indices where an instance
        of pattern starts in text.

        :param pattern: The search pattern.
        :param text: The text string to search in.
        :return: Tuple with indices where occurrences of the search
            pattern start in the text.
        """
        raise NotImplementedError()

    @staticmethod
    def _input_validation(pattern: str, text: str) -> bool:
        """
        Validates the input pattern and text.

        :param pattern: The search pattern.
        :param text: The text string to search in.
        :return: True if the input is valid, False otherwise.
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string.")
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        if pattern == "":
            return False
        if text == "":
            return False
        if len(pattern) > len(text):
            return False
        return True
