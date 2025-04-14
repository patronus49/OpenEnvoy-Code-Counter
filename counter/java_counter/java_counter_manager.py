from pathlib import Path
from typing import Union, List

from models.counter_response import CounterResponse
from counter.counter_factory_operations import CounterFactoryOperations
from counter.syntax_counter_operations import SyntaxCounterOperations
from counter.java_counter.java_counter_factory_manager import JavaCounterFactoryManager
from counter.java_counter.constants import COUNTER_SYNTAX_JAVA, COUNTER_INPUT_SINGLE_FILE, \
    SUPPORTED_COMMENTS_JAVA_LIST, SUPPORTED_COUNTERS_JAVA_LIST, ARG_PATH_DEFAULT_VALUE, JAVA_TEST_DIR_PATH, \
    JAVA_TEST_FILE_NAME, JAVA_FILE_SUFFIX
from models.counters import Counters
from utilities.string_utilities import StringUtilities


class JavaCounterManager(SyntaxCounterOperations, CounterFactoryOperations):
    """ a concrete class implementing SyntaxCounterOperations and CounterFactoryOperations """

    __arg_syntax__: str = None
    __arg_comments__: List[str] = None
    __arg_counters__: List[str] = None
    __arg_input__: str = None
    __arg_path__: str = None
    __counters__: List[Counters] = list()
    __counter_response__: CounterResponse = None

    def __init__(self) -> None:
        pass

    def __set_arg_syntax__(self, arg_syntax: str) -> None:
        self.__arg_syntax__ = arg_syntax

    def __set_arg_comments__(self, arg_comments: List[str]) -> None:
        self.__arg_comments__ = arg_comments

    def __get_arg_counters__(self) -> List[str]:
        return self.__arg_counters__

    def __set_arg_counters__(self, arg_counters: List[str]) -> None:
        self.__arg_counters__ = arg_counters

    def __get_counters__(self) -> List[Counters]:
        return self.__counters__

    def __set_counters__(self) -> None:
        for counter_type in self.__get_arg_counters__():
            self.__counters__.append(Counters(counter_type, JavaCounterFactoryManager().get_counter(counter_type), 0))

    def __set_arg_input__(self, arg_input: str) -> None:
        self.__arg_input__ = arg_input

    def __set_arg_path__(self, arg_path: str) -> None:
        self.__arg_path__ = arg_path

    def __get_arg_path__(self) -> str:
        return self.__arg_path__

    def set_path(self, path: str) -> None:
        """
        currently we set path in each syntax counter
        parent syntax counter is exempt to implement this
        """
        pass

    def get_counter(
            self,
            arg_syntax: str,
            arg_comments: str,
            arg_counters: str,
            arg_input: str,
            arg_path: str) -> Union[SyntaxCounterOperations, CounterFactoryOperations]:
        """ returns an instance of syntax code counter and counter factory """
        if not self.validate_arg_syntax(arg_syntax):
            raise Exception('Invalid syntax for java counter')

        if not self.validate_arg_comments(arg_comments):
            raise Exception('Invalid comment-type for java counter')

        if not self.validate_arg_counters(arg_counters):
            raise Exception('Invalid counter-type for java counter')

        if not self.validate_arg_input(arg_input):
            raise Exception('Invalid input for java counter')

        arg_path = self.validate_arg_path(arg_path)

        self.__set_arg_syntax__(arg_syntax)
        self.__set_arg_comments__(StringUtilities.convert_comma_separated_string_to_list(arg_comments))
        self.__set_arg_counters__(StringUtilities.convert_comma_separated_string_to_list(arg_counters))
        self.__set_arg_input__(arg_input)
        self.__set_arg_path__(arg_path)
        self.__set_counters__()

        return self

    @staticmethod
    def validate_arg_comments(arg_comments: str) -> bool:
        if not arg_comments:
            return False

        arg_comments_list: List[str] = StringUtilities.convert_comma_separated_string_to_list(arg_comments)

        for comment in arg_comments_list:
            if comment not in SUPPORTED_COMMENTS_JAVA_LIST:
                return False

        return True

    @staticmethod
    def validate_arg_counters(arg_counters: str) -> bool:
        if not arg_counters:
            return False

        arg_counters_list: List[str] = StringUtilities.convert_comma_separated_string_to_list(arg_counters)

        for counter in arg_counters_list:
            if counter not in SUPPORTED_COUNTERS_JAVA_LIST:
                return False

        return True

    @staticmethod
    def validate_arg_input(arg_input: str) -> bool:
        if not arg_input or arg_input != COUNTER_INPUT_SINGLE_FILE:
            return False

        return True

    @staticmethod
    def validate_arg_syntax(arg_syntax: str) -> bool:
        if not arg_syntax or arg_syntax != COUNTER_SYNTAX_JAVA:
            return False

        return True

    @staticmethod
    def validate_arg_path(arg_path: str) -> str:
        try:
            if arg_path == ARG_PATH_DEFAULT_VALUE:
                base_dir: Path = Path(__file__).resolve().parent.parent.parent
                file_path = base_dir / JAVA_TEST_DIR_PATH / JAVA_TEST_FILE_NAME
            else:
                file_path = Path(arg_path)

            if not file_path.is_file() or file_path.suffix != JAVA_FILE_SUFFIX:
                raise Exception('Invalid file for java counter')

            with open(file_path, 'r') as file:
                file.close()

            return str(file_path)

        except Exception as e:
            raise Exception('Invalid path for java counter')

    def count(self) -> None:
        """ counts all the desired code count type in input """
        for counter in self.__get_counters__():
            local_counter: SyntaxCounterOperations = counter.get_counter()
            local_counter.set_path(self.__get_arg_path__())
            local_counter.count()
            counter.set_count(local_counter.get_count())

    def get_count(self) -> str:
        counter_response: CounterResponse = CounterResponse.from_counters(self.__get_counters__())
        return counter_response.to_json()
