import json
from typing import List

from models.counters import Counters


class CounterResponse:
    """
    data class for counter program output
    :param
        blank: blank lines count
        comments: comments line count
        code: code lines count
        total: total lines count
    """

    __blank__: int = None
    __comments__: int = None
    __code__: int = None
    __total__: int = None

    def __init__(self, blank: int, comment: int, code: int, total: int) -> None:
        self.__blank__ = blank
        self.__comments__ = comment
        self.__code__ = code
        self.__total__ = total

    def __get_blank__(self):
        return self.__blank__

    def __set_blank__(self, blank: int) -> None:
        self.__blank__ = blank

    def __get_comments__(self):
        return self.__comments__

    def __set_comments__(self, comments: int) -> None:
        self.__comments__ = comments

    def __get_code__(self):
        return self.__code__

    def __set_code__(self, code: int) -> None:
        self.__code__ = code

    def __get_total__(self):
        return self.__total__

    def __set_total__(self, total: int) -> None:
        self.__total__ = total

    @staticmethod
    def from_counters(counters: List[Counters]) -> "CounterResponse":
        counter_response = CounterResponse(-1, -1, -1, -1)

        for counter in counters:
            if counter.get_counter_type() == 'blank':
                counter_response.__set_blank__(counter.get_count())
            elif counter.get_counter_type() == 'comments':
                counter_response.__set_comments__(counter.get_count())
            elif counter.get_counter_type() == 'code':
                counter_response.__set_code__(counter.get_count())
            elif counter.get_counter_type() == 'total':
                counter_response.__set_total__(counter.get_count())
            else:
                raise Exception('Invalid counter type in counters list')

        return counter_response

    def __to_dict__(self) -> dict:
        return {
            "blank": self.__get_blank__(),
            "comments": self.__get_comments__(),
            "code": self.__get_code__(),
            "total": self.__get_total__()
        }

    def to_json(self):
        return json.dumps(self.__to_dict__(), indent=2)




