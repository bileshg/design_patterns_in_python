from enum import Enum
from abc import ABCMeta, abstractmethod
from typing import Any


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    """Defines a product"""
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Specification(metaclass=ABCMeta):
    """Interface for specifications that must be satisfied"""
    @abstractmethod
    def is_satisfied(self, item: Any) -> bool:
        """Contains logic to validate the item"""
        pass

    def __and__(self, other):
        """Allows for combining the '&' (ampersand) operator to combine specification requirements"""
        return AndSpecification(self, other)


class AndSpecification(Specification):
    """"Specification implementation that allows to bind multiple specifications together that must all be satisfied"""
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item) -> bool:
        """Validates whether all specifications are validated by the given item"""
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class ColorSpecification(Specification):
    """Color specification"""
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item) -> bool:
        """Validate if the defined color matches the color of the item"""
        return item.color == self.color


class SizeSpecification(Specification):
    """Size specification"""
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item) -> bool:
        """Validate if the defined size matches the size of the item"""
        return item.size == self.size

class FilterInterface(metaclass=ABCMeta):
    """Interface for filters"""

    @staticmethod
    @abstractmethod
    def filter(items: list[Any], spec: Specification) -> Any:
        pass


class FilterSpec(FilterInterface):
    @staticmethod
    def filter(items: list[Any], spec: Specification) -> Any:
        """Filter items on provided specification"""
        for item in items:
            if spec.is_satisfied(item):
                yield item


def driver():
    pear = Product('Pear', Color.GREEN, Size.SMALL)
    ball = Product('Ball', Color.GREEN, Size.MEDIUM)
    palace = Product('Palace', Color.BLUE, Size.LARGE)
    products = [pear, ball, palace]

    green = ColorSpecification(Color.GREEN)
    small = SizeSpecification(Size.SMALL)
    small_blue = small & ColorSpecification(Color.BLUE)

    print('Green products (new):')
    for p in FilterSpec.filter(items=products, spec=green):
        print(f' - {p.name} is green')

    print('Small products:')
    for p in FilterSpec.filter(items=products, spec=small):
        print(f' - {p.name} is small')

    print('Small blue items:')
    for p in FilterSpec.filter(items=products, spec=small_blue):
        print(f' - {p.name} is small and blue')

if __name__ == "__main__":
    driver()
