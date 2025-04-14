from counter.counter_factory_operations import CounterFactoryOperations
from counter.syntax_counter_operations import SyntaxCounterOperations
from counter_orchestrator.constants import ARG_SYNTAX_JAVA
from counter.java_counter.java_counter_manager import JavaCounterManager


class CounterFactoryManager(CounterFactoryOperations):
    """ a concrete class implementing CounterFactoryOperations """

    __counter_manager__: SyntaxCounterOperations = None

    def __init__(self) -> None:
        pass

    def __get_counter_manager__(self) -> SyntaxCounterOperations:
        return self.__counter_manager__

    def __set_counter_manager__(
            self,
            arg_syntax: str,
            arg_comments: str,
            arg_counters: str,
            arg_input: str,
            arg_path: str) -> None:
        if arg_syntax == ARG_SYNTAX_JAVA:
            self.__counter_manager__ = JavaCounterManager().get_counter(
                arg_syntax,
                arg_comments,
                arg_counters,
                arg_input,
                arg_path)
        else:
            raise Exception('invalid syntax value in command')

    def get_counter(
            self,
            arg_syntax: str,
            arg_comments: str,
            arg_counters: str,
            arg_input: str,
            arg_path: str) -> SyntaxCounterOperations:
        """ returns an instance of syntax code counter """
        self.__set_counter_manager__(arg_syntax, arg_comments, arg_counters, arg_input, arg_path)
        return self.__get_counter_manager__()
