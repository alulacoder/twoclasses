# Define the Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_details(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    def is_passing(self):
        return self.grade >= 50

# Define the Rectangle class
class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Create instances of the classes
student1 = Student("Alice", 20, 75)
rectangle1 = Rectangle(10, 5, "blue")

# Print details of the student
print(student1.get_details())
print(f"Is the student passing? {'Yes' if student1.is_passing() else 'No'}")

# Print details of the rectangle
print(f"Rectangle Color: {rectangle1.color}")
print(f"Area: {rectangle1.area()}")
print(f"Perimeter: {rectangle1.perimeter()}")
