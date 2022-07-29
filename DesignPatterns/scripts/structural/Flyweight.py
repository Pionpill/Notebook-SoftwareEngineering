# Reference: https://github.com/faif/python-patterns/blob/master/patterns/structural/flyweight.py

import weakref


class Card:
    """The Flyweight"""
    _pool: weakref.WeakValueDictionary = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        obj = cls._pool.get(value + suit)
        if obj is None:
            obj = object.__new__(Card)
            cls._pool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return f"<Card: {self.value}{self.suit}>"


if __name__ == "__main__":
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    c1, c2  # (<Card: 9h>, <Card: 9h>)
    c1 == c2  # True
    c1 is c2  # True
    c1.new_attr = 'temp'
    c3 = Card('9', 'h')
    hasattr(c3, 'new_attr')  # True
    Card._pool.clear()
    c4 = Card('9', 'h')
    hasattr(c4, 'new_attr')  # False
