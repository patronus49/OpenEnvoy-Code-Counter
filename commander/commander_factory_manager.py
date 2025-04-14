from commander.commander_factory_operations import CommanderFactoryOperations
from commander.commander_manager import CommanderManager
from commander.commander_operations import CommanderOperations


class CommanderFactoryManager(CommanderFactoryOperations):
    """ a concrete class implementing CommanderFactoryOperations """

    __commander_manager__: CommanderOperations = None

    def __init__(self) -> None:
        pass

    def __get_commander_manager__(self) -> CommanderOperations:
        return self.__commander_manager__

    def __set_commander_manager__(self) -> None:
        self.__commander_manager__ = CommanderManager()

    def get_commander(self) -> CommanderOperations:
        """ returns a commander instance """
        self.__set_commander_manager__()
        return self.__get_commander_manager__()
