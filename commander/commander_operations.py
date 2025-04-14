from abc import ABC, abstractmethod


class CommanderOperations(ABC):
    """
    interface for commander manager.
    a commander manager must implement all of the below methods.
    implementation is handled by concrete class.
    """

    @abstractmethod
    def init_commander(self) -> None:
        """ initialises the commander data members """
        pass

    @abstractmethod
    def parse_command_args(self) -> None:
        """ parse the command arguments """
        pass

    @abstractmethod
    def get_parsed_args(self) -> dict:
        """ returns the dictionary of parsed command arguments """
        pass
