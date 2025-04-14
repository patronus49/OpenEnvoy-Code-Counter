from abc import ABC, abstractmethod
from typing import Union


class SyntaxCounterOperations(ABC):
    """
    interface for syntax counter.
    a syntax counter must implement all of the below methods.
    implementation is handled by concrete class.
    """

    @abstractmethod
    def set_path(self, path: str) -> None:
        """
        set the code file path in counter.
        parent syntax counter need not implement this
        """
        pass

    @abstractmethod
    def count(self) -> None:
        """ counts all the desired code count type in input """
        pass

    @abstractmethod
    def get_count(self) -> Union[int, str]:
        """ returns all the desired code count type in input """
        pass
