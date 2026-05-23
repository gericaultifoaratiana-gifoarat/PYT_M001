#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._age_days: int = age if age >= 0 else 0

    def get_height(self) -> float:
        return self._height

    def set_height(self, h: float) -> None:
        if h < 0:
            print(f"{self._name}: Error, height can't be negative\nRejected")
        else:
            self._height = h

    def get_age(self) -> int:
        return self._age_days

    def set_age(self, a: int) -> None:
        if a < 0:
            print(f"{self._name}: Error, can't be negative\nRejeted")
        else:
            self._age_days = a

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_days} days")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True
        print(f"[asking the {self.color} {self._name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        shade_length = self.trunk_diameter * 10
        print(f"[asking the {self._name} to produce a shade]")
        print(f"Tree {self._name} now produces a shade of"
              f"{self._height}cm long and {shade_length}cm wide."
              )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, seas: str, nut: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = seas
        self._nutritional_value: int = nut

    def grow(self) -> None:
        self._nutritional_value += 2
        self.set_age(self._age_days + 1)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    to_raise = Tree("To raise", 200.0, 365, 5.0)
    to_raise.show()
    to_raise.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[asking the tomato to grow for 20 days]")
    for _ in range(20):
        tomato.grow()
    tomato.show()
