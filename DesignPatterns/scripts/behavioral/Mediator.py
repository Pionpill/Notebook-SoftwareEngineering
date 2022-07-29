# Reference: https://github.com/faif/python-patterns/blob/master/patterns/behavioral/mediator.py

from __future__ import annotations


class ChatRoom:
    def display_message(self, user: User, message: str) -> None:
        print(f"[{user} says]: {message}")


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message: str) -> None:
        self.chat_room.display_message(self, message)

    def __str__(self) -> str:
        return self.name


if __name__ == "__main__":
    molly = User('Molly')
    mark = User('Mark')
    ethan = User('Ethan')
    molly.say("Hi Team! Meeting at 3 PM today.")
    # [Molly says]: Hi Team! Meeting at 3 PM today.
    mark.say("Roger that!")
    # [Mark says]: Roger that!
    ethan.say("Alright.")
    # [Ethan says]: Alright.
