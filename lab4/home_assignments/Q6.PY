import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Initialize the radius

    def area(self):
        # Calculate area of the circle: A = π * r^2
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Calculate perimeter (circumference) of the circle: P = 2 * π * r
        return 2 * math.pi * self.radius

# Example usage
if __name__ == "__main__":
    # Take user input for the radius of the circle
    radius = float(input("Enter the radius of the circle: "))
    
    # Create an instance of the Circle class
    circle = Circle(radius)
    
    # Calculate and print the area and perimeter
    print(f"The area of the circle is: {circle.area():.2f}")
    print(f"The perimeter (circumference) of the circle is: {circle.perimeter():.2f}")

"""Enter the radius of the circle: 2
The area of the circle is: 12.57
The perimeter (circumference) of the circle is: 12.57"""