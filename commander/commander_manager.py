import argparse

from commander.commander_operations import CommanderOperations
from commander.constants import COMMAND_ARG_SYNTAX, COMMAND_ARG_COMMENTS, COMMAND_ARG_COUNTERS, COMMAND_ARG_INPUT, \
    COMMAND_ARG_PATH


class CommanderManager(CommanderOperations):
    """ a concrete class implementing CommanderOperations """

    __arg_parser__: argparse.ArgumentParser = None
    __parsed_args__: dict = None

    def __init__(self) -> None:
        pass

    def init_commander(self) -> None:
        """ initialises the commander data members """
        self.__set_arg_parser__()

    def __get_arg_parser__(self) -> argparse.ArgumentParser:
        return self.__arg_parser__

    def __set_arg_parser__(self) -> None:
        self.__arg_parser__ = argparse.ArgumentParser()

    def get_parsed_args(self) -> dict:
        """ returns the dictionary of parsed command arguments """
        return self.__parsed_args__

    def __set_parsed_args__(self, parsed_args: dict) -> None:
        self.__parsed_args__ = parsed_args

    def parse_command_args(self) -> None:
        """ parse the command arguments """
        self.__parse_syntax_arg__()
        self.__parse_comments_arg__()
        self.__parse_counters_arg__()
        self.__parse_input_arg__()
        self.__parse_path_arg__()

        self.__set_parsed_args__(self.__get_arg_parser__().parse_args().__dict__)

    def __parse_syntax_arg__(self) -> None:
        self.__get_arg_parser__().add_argument(COMMAND_ARG_SYNTAX)

    def __parse_comments_arg__(self) -> None:
        self.__get_arg_parser__().add_argument(COMMAND_ARG_COMMENTS)

    def __parse_counters_arg__(self) -> None:
        self.__get_arg_parser__().add_argument(COMMAND_ARG_COUNTERS)

    def __parse_input_arg__(self) -> None:
        self.__get_arg_parser__().add_argument(COMMAND_ARG_INPUT)

    def __parse_path_arg__(self) -> None:
        self.__get_arg_parser__().add_argument(COMMAND_ARG_PATH)
