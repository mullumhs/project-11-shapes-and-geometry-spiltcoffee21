
# defining perimitor in shape class
class Shape():
    def __init__(self):
        pass
    
    def area(self):
        pass
    
    def perimeter(self):
        pass



#calculating rectangles area and perimitor 
class Rectangle(Shape):
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight
    
    def area(self):
        return self.width * self.hight
    
    def perimeter(self):
        return 2 * (self.width + self.hight)


#calculating circle radius
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 *  self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius



#calculating triangles area and perimitor
class Triangle(Shape):
    def __init__(self, base, hight):
        self.base = base
        self.hight = hight
    
    def area(self):
        return (self.base * self.hight / 2)
    
    def perimeter(self):
        return 3 * self.base
    
        
    
    
    