class Shape:
    def calculate_area(self, **kwargs):
        pass
        
class Circle(Shape):
    def calculate_area(self, **kwargs):
        radius = kwargs.get('radius')
        return 3.14 * radius * radius

class Square(Shape):
    def calculate_area(self, **kwargs):
        side = kwargs.get('side')
        return side * side

class Triangle(Shape):
    def calculate_area(self, **kwargs):
        base = kwargs.get('base')
        height = kwargs.get('height')
        return 0.5 * base * height
    
class Rectangle(Shape):
    def calculate_area(self, **kwargs):
        base = kwargs.get('length')
        height = kwargs.get('width')
        return  base * height
