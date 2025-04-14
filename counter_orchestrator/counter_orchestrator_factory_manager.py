from counter_orchestrator.counter_orchestrator_factory_operations import CounterOrchestratorFactoryOperations
from counter_orchestrator.counter_orchestrator_manager import CounterOrchestratorManager
from counter_orchestrator.counter_orchestrator_operations import CounterOrchestratorOperations


class CounterOrchestratorFactoryManager(CounterOrchestratorFactoryOperations):
    """ a concrete class implementing CounterOrchestratorFactoryOperations """

    __counter_orchestrator_manager__: CounterOrchestratorOperations = None

    def __init__(self) -> None:
        pass

    def __get_counter_orchestrator_manager__(self) -> CounterOrchestratorOperations:
        return self.__counter_orchestrator_manager__

    def __set_counter_orchestrator_manager__(self) -> None:
        self.__counter_orchestrator_manager__ = CounterOrchestratorManager()

    def get_counter_orchestrator(self) -> CounterOrchestratorOperations:
        """ returns an instance of orchestrator for code counter """
        self.__set_counter_orchestrator_manager__()
        return self.__get_counter_orchestrator_manager__()


