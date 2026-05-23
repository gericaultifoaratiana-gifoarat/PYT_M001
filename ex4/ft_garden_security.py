#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._age_days = age if age >= 0 else 0

    def get_height(self) -> float:
        return self._height

    def set_height(self, h: float) -> None:
        if h < 0:
            print(f"{self._name}: Error, height can't be negative\nRejected\n")
        else:
            self._height = h

    def get_age(self) -> int:
        return self._age_days

    def set_age(self, a: int) -> None:
        if a < 0:
            print(f"{self._name}: Error, can't be negative\nRejeted\n")
        else:
            self._age_days = a

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_days} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("orange", 11.0, 10)
    print(f"Plant created: {rose._name}: {rose.get_height()}cm, "
          f"{rose.get_age()} day old\n")

    rose.set_height(25)
    rose.set_age(-10)

    rose.set_height(-25)
    rose.set_age(-10)

    print("Curent state: ", end="")
    rose.show()
