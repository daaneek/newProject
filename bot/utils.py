import sys
from typing import Iterator, Generator


class IterableAdapter:
    def __init__(self, iterator_factory: Iterator | Generator):
        self.iterator_factory = iterator_factory

    def __iter__(self):
        return self.iterator_factory()

    def __next__(self):
        return next(self.iterator_factory())

    def getsizeof(self):
        return sys.getsizeof(self.iterator_factory)
