import math

from antra.Shape import Shape


class Triangle(Shape):
    def __init__(self, base, leg):
        super().__init__(base, leg)
        self.base = self.length
        self.leg = self.width

    def area(self):
        return self.base * self.leg / 2

    def perimeter(self):
        return self.base + self.leg + math.sqrt(self.base**2 + self.leg**2)

