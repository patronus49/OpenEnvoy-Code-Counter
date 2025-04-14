from commander.commander_operations import CommanderOperations
from counter.syntax_counter_operations import SyntaxCounterOperations
from counter_orchestrator.counter_orchestrator_operations import CounterOrchestratorOperations
from commander.commander_factory_manager import CommanderFactoryManager
from counter.counter_factory_manager import CounterFactoryManager
from counter_orchestrator.constants import PARSED_ARG_COUNTERS, PARSED_ARG_COMMENTS, PARSED_ARG_SYNTAX, \
    PARSED_ARG_INPUT, PARSED_ARG_PATH


class CounterOrchestratorManager(CounterOrchestratorOperations):
    """ a concrete class implementing CounterOrchestratorOperations """

    __commander_manager__: CommanderOperations = None
    __counter_manager__: SyntaxCounterOperations = None
    __parsed_args__: dict = None

    def __init__(self):
        pass

    def init_orchestrator(self) -> None:
        """ initialises the orchestrator data members """
        self.__set_commander_manager__()

    def __get_commander_manager__(self) -> CommanderOperations:
        return self.__commander_manager__

    def __set_commander_manager__(self) -> None:
        self.__commander_manager__ = CommanderFactoryManager().get_commander()

    def __get_counter_manager__(self) -> SyntaxCounterOperations:
        return self.__counter_manager__

    def __set_counter_manager__(self) -> None:
        self.__counter_manager__ = CounterFactoryManager().get_counter(
            self.__get_parsed_arg__().get(PARSED_ARG_SYNTAX),
            self.__get_parsed_arg__().get(PARSED_ARG_COMMENTS),
            self.__get_parsed_arg__().get(PARSED_ARG_COUNTERS),
            self.__get_parsed_arg__().get(PARSED_ARG_INPUT),
            self.__get_parsed_arg__().get(PARSED_ARG_PATH))

    def __get_parsed_arg__(self) -> dict:
        return self.__parsed_args__

    def __set_parsed_args__(self, parsed_args: dict) -> None:
        self.__parsed_args__ = parsed_args

    def run(self) -> None:
        """ executes the commands and prints desired code counts """

        self.__get_commander_manager__().init_commander()
        self.__get_commander_manager__().parse_command_args()
        self.__set_parsed_args__(self.__commander_manager__.get_parsed_args())
        print("Arguments = ", self.__get_parsed_arg__())

        self.__set_counter_manager__()
        self.__get_counter_manager__().count()
        print("Counter Response = ", self.__get_counter_manager__().get_count())
