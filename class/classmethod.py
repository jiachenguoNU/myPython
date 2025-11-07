class Circle:
    pi = 3.14159 # Class-level attribute

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    @classmethod
    def from_diameter(cls, diameter): # Class method for alternative constructor
        radius = diameter / 2
        return cls(radius) # Calls the __init__ of the class (cls): constructor

print(Circle.pi) # Accessing a class attribute directly

circle1 = Circle(5)
print(f"Area of circle1: {circle1.area()}")

circle2 = Circle.from_diameter(10) # Using the class method as an alternative constructor
print(f"Area of circle2 (from diameter): {circle2.area()}")