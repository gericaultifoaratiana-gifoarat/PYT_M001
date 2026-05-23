#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.names = name
        self.heights = height
        self.ages = age

    def show(self) -> None:
        print(f"{self.names}: {round(self.heights, 1)}cm,"
              f"{self.ages} days old")

    def grow(self) -> None:
        self.heights += 0.8

    def age(self) -> None:
        self.ages += 1


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25, 30)
    initial_heights = rose.heights

    rose.show()

    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()

    growth = rose.heights - initial_heights
    print(f"Growth this week: {round(growth, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
