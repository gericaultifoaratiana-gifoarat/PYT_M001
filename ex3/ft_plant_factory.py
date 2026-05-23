#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.ages = age

    def grow(self) -> None:
        self.height += 0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.ages} day old")


if __name__ == "__main__":
    rose = Plant("rose", 10, 10)
    rose1 = Plant("rose1", 1.4, 100)
    rose2 = Plant("rose2", 10, 10)
    rose3 = Plant("rose3", 10, 10)
    rose4 = Plant("rose4", 1.4, 100)
    print("=== Plant Factory Output ===")
    for r in [rose, rose1, rose2, rose3, rose4]:
        print("Created: ", end="")
        r.grow()
        r.show()
