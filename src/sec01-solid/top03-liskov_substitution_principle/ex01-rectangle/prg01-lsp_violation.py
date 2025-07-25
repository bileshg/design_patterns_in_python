class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rectangle: Rectangle):
    w = rectangle.width
    rectangle.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rectangle.area}')

# Violates LSP by defining a Square as a specific type of Rectangle,
# while the properties are handled differently

def driver():
    r = Rectangle(5, 10)
    use_it(r)

    s = Square(5)
    use_it(s)  # This will not behave as expected due to the overridden setters

if __name__ == "__main__":
    driver()
    