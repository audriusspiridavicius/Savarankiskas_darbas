from Rectangle import Rectangle
from Triangle import Triangle

t = Triangle(5,6)
rec = Rectangle(10,5)

print(f"triangle perimeter {t.perimeter()}")
print(f"triangle area {t.area()}")

print(f"rectangle perimeter {rec.perimeter()}")
print(f"rectangle area {rec.area()}")