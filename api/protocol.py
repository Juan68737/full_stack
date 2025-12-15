from typing import Protocol


# 1) Define the Protocol (the rule)
class Greeter(Protocol):
    def greet(self, name: str) -> str:
        ...


# 2) First class that follows the rule
class FriendlyGreeter:
    def greet(self, name: str) -> str:
        return f"Hey {name}!"


# 3) Second class that follows the rule
class FormalGreeter:
    def greet(self, name: str) -> str:
        return f"Hello, {name}."


# 4) Function that uses the Protocol
def say_hello(greeter: Greeter, name: str) -> None:
    print(greeter.greet(name))


# 5) Run it
if __name__ == "__main__":
    friendly = FriendlyGreeter()
    formal = FormalGreeter()

    say_hello(friendly, "Jhonathan")
    say_hello(formal, "Jhonathan")

#Will add protocol + Fast API example soon
