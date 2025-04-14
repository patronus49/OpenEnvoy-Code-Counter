from abc import ABC, abstractmethod


class CounterOrchestratorOperations(ABC):
    """
    interface for counter orchestrator.
    a counter orchestrator must implement all of the below methods.
    implementation is handled by concrete class.
    """

    @abstractmethod
    def init_orchestrator(self) -> None:
        """ initialises the orchestrator data members """
        pass

    @abstractmethod
    def run(self) -> None:
        """ executes the commands and prints desired code counts """
        pass
