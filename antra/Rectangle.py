from Shape import Shape


class Rectangle(Shape):

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.length + self.width) * 2