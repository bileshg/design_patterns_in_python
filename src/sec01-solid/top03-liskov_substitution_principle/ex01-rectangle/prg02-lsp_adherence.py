from abc import ABC, abstractmethod


class Shape(ABC):
    """Interface for shapes"""

    @abstractmethod
    def area(self):
        """Calculate the area of a shape"""
        pass


class Rectangle(Shape):
    """Provides the structure for a rectangle"""
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def __str__(self) -> str:
        """Custom string representation to show the dimensions of the rectangle"""
        return f'Width: {self._width}, Height: {self._height}'

    def area(self) -> float:
        """Calculates the area of the rectangle"""
        return self._width * self._height

    @property
    def width(self) -> float:
        """Getter of the width property"""
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """Setter of the width property"""
        self._width = value

    @property
    def height(self) -> float:
        """Getter of the height property"""
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """Setter of the height property"""
        self._height = value


class Square(Shape):
    """Provides the structure for a square"""
    def __init__(self, side: float):
        self._side = side

    def __str__(self) -> str:
        """Custom string representation to show the dimensions of the square"""
        return f'side: {self._side}'

    def area(self) -> float:
        """Calculates the area of the square"""
        return self._side ** 2

    @property
    def side(self) -> float:
        """Getter of the side property"""
        return self._side

    @side.setter
    def side(self, value: float) -> None:
        """Setter of the side property"""
        self._side = value

    @property
    def width(self) -> float:
        """Getter of the width property"""
        return self._side

    @width.setter
    def width(self, value: float) -> None:
        """Setter of the width property"""
        self._side = value

    @property
    def height(self) -> float:
        """Getter of the height property"""
        return self._side

    @height.setter
    def height(self, value: float) -> None:
        """Setter of the height property"""
        self._side = value


def driver():
    width, height = 2, 3
    rectangle = Rectangle(width=width, height=height)
    print(f'Expected an area of {width * height}, got {rectangle.area()}')

    rectangle.width = 6
    print(f'Expected an area of {rectangle.width * height}, got {rectangle.area()}')

    side = 5
    square = Square(side=side)
    print(f'Expected an area of {side**2}, got {square.area()}')
    square.side = 11
    print(f'Expected an area of {square.side**2}, got {square.area()}')


if __name__ == "__main__":
    driver()
