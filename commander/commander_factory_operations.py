from abc import ABC, abstractmethod

from commander.commander_operations import CommanderOperations


class CommanderFactoryOperations(ABC):
    """
    interface for commander factory.
    a commander factory must implement all of the below methods.
    implementation is handled by concrete class.
    """

    @abstractmethod
    def get_commander(self) -> CommanderOperations:
        """ returns a commander instance """
        pass
