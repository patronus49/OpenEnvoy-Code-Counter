from counter.syntax_counter_operations import SyntaxCounterOperations


class JavaCounterCode(SyntaxCounterOperations):
    """ a concrete class implementing SyntaxCounterOperations """

    __path__: str = None
    __count__: int = None

    def __init__(self) -> None:
        pass

    def __get_path__(self) -> str:
        return self.__path__

    def set_path(self, path: str) -> None:
        self.__path__ = path

    def get_count(self) -> int:
        """ returns the code lines code count in input """
        return self.__count__

    def __set_count__(self, count: int) -> None:
        self.__count__ = count

    def count(self) -> None:
        """ counts all the code lines code type in input """
        count = 0

        with open(self.__get_path__(), 'r') as file:
            for line in file:
                stripped = line.strip()

                # Skip blank lines
                if not stripped:
                    continue

                # Skip single-line comments
                if stripped.startswith("//"):
                    continue

                # Count as code
                count += 1

            file.close()

        self.__set_count__(count)
