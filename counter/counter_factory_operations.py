from abc import ABC, abstractmethod
from typing import Union

from counter.syntax_counter_operations import SyntaxCounterOperations


class CounterFactoryOperations(ABC):
    """
    interface for counter factory.
    a counter factory must implement all of the below methods.
    implementation is handled by concrete class.
    """

    @abstractmethod
    def get_counter(
            self,
            arg_syntax,
            arg_comments,
            arg_counters,
            arg_input,
            arg_path) -> Union[SyntaxCounterOperations, "CounterFactoryOperations"]:
        """ returns an instance of syntax code counter """
        pass
