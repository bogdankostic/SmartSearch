from abc import ABC, abstractmethod


class BaseMatcher(ABC):
    """
    Base class that all matcher classes should inherit from in order
    to ensure uniformity.
    """
    case_sensitive: bool

    @abstractmethod
    def search(self, pattern: str, text: str) -> list[int]:
        """
        Should return a list containing all indices where an instance
        of pattern starts in text.

        :param pattern: The search pattern.
        :param text: The text string to search in.
        :return: List with indices where occurrences of the search
            pattern start in the text.
        """
        raise NotImplementedError()
