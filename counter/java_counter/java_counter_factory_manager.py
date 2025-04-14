from counter.java_counter.java_counter_code import JavaCounterCode
from counter.java_counter.java_counter_comment import JavaCounterComments
from counter.java_counter.java_counter_total import JavaCounterTotal
from counter.syntax_counter_factory_operations import SyntaxCounterFactoryOperations
from counter.java_counter.java_counter_blank import JavaCounterBlank
from counter.syntax_counter_operations import SyntaxCounterOperations


class JavaCounterFactoryManager(SyntaxCounterFactoryOperations):
    """ a concrete class implementing SyntaxCounterFactoryOperations """

    __java_counter_manager__: SyntaxCounterOperations = None

    def __init__(self) -> None:
        pass

    def __get_java_counter_manager__(self) -> SyntaxCounterOperations:
        return self.__java_counter_manager__

    def __set_java_counter_manager__(self, kind: str) -> None:
        if kind == 'blank':
            self.__java_counter_manager__ = JavaCounterBlank()
        elif kind == 'comments':
            self.__java_counter_manager__ = JavaCounterComments()
        elif kind == 'code':
            self.__java_counter_manager__ = JavaCounterCode()
        elif kind == 'total':
            self.__java_counter_manager__ = JavaCounterTotal()
        else:
            raise Exception('Invalid counter type for java')

    def get_counter(self, kind: str) -> SyntaxCounterOperations:
        """ returns an instance of code counter of the desired kind (counter_type) """
        self.__set_java_counter_manager__(kind)
        return self.__get_java_counter_manager__()


