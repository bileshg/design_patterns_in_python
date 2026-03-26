from abc import ABC

from hot_drinks import Coffee, Tea


class HotDrinkFactory(ABC):
    """Interface for HotDrink factories"""

    def prepare(self, amount):
        raise NotImplementedError()


class TeaFactory(HotDrinkFactory):
    """Tea factory"""

    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    """Coffee factory"""

    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()
