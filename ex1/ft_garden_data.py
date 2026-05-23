#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 150, 45)
    cactus = Plant("Cactus", 10, 60)
    rose.show()
    sunflower.show()
    cactus.show()
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
