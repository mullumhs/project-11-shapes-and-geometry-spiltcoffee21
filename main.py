from shapes import Shape, Rectangle, Circle, Triangle

rectangle = Rectangle(10, 3)
print(f"area is {rectangle.area()} perimeter is {rectangle.perimeter()}")


circle = Circle(5)
print(f"area is {circle.area()} perimeter is {circle.perimeter()}")

triangle = Triangle(4,4)
print(f"area is {triangle.area()} perimeter is {triangle.perimeter()}")