from abc import ABC, abstractmethod

from counter_orchestrator.counter_orchestrator_operations import CounterOrchestratorOperations


class CounterOrchestratorFactoryOperations(ABC):
    """
    interface for counter orchestrator factory.
    a counter orchestrator factory must implement all of the below methods.
    implementation is handled by concrete class.
    """

    @abstractmethod
    def get_counter_orchestrator(self) -> CounterOrchestratorOperations:
        """ returns an instance of orchestrator for code counter """
        pass
