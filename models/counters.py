from counter.syntax_counter_operations import SyntaxCounterOperations


class Counters:
    """
    internal model class to hold counter values while execution.
    :param
        counter_type = type of counter (blank, code, comment, total etc)
        counter = an instance of a counter class of counter_type
        count = holds value for counter's result
    """

    counter_type: str = None
    counter: SyntaxCounterOperations = None
    count: int = None

    def __init__(self, counter_type, counter, count) -> None:
        self.counter_type = counter_type
        self.counter = counter
        self.count = count

    def get_counter_type(self) -> str:
        return self.counter_type

    def get_counter(self) -> SyntaxCounterOperations:
        return self.counter

    def get_count(self) -> int:
        return self.count

    def set_count(self, count: int) -> None:
        self.count = count
