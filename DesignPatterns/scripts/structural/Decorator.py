# Reference: https://github.com/faif/python-patterns/blob/master/patterns/structural/decorator.py


class TextTag:
    """Represents a base text tag"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"


def main():
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())  # before: hello, world!
    print("after:",
          special_hello.render())  # after: <i><b>hello, world!</b></i>
