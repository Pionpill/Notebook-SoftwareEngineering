# Reference: https://github.com/faif/python-patterns/blob/master/patterns/behavioral/iterator_alt.py

from __future__ import annotations


class NumberWords:

    _WORD_MAP = ("one", "two", "three", "four", "five")

    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> NumberWords:  # this makes the class an Iterable
        return self

    def __next__(self) -> str:  # this makes the class an Iterator
        if self.start > self.stop or self.start > len(self._WORD_MAP):
            raise StopIteration
        current = self.start
        self.start += 1
        return self._WORD_MAP[current - 1]


# Test the iterator

if __name__ == "__main__":
    # Counting to two...
    for number in NumberWords(start=1, stop=2):
        print(number)
    # Counting to five...
    for number in NumberWords(start=1, stop=5):
        print(number)
