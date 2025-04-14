from abc import ABC, abstractmethod


class SyntaxCounterFactoryOperations(ABC):
    """
    interface for counter counter factory.
    a code counter factory must implement all of the below methods.
    implementation is handled by concrete class.
    """

    @abstractmethod
    def get_counter(self, kind: str):
        """ returns an instance of code counter of the desired kind (counter_type) """
        pass
