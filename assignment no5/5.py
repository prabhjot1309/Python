#Draw a circular pattern like star.
import math

def circle_pattern(radius):
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            distance = math.sqrt(x**2 + y**2)
            # Adjust threshold to improve circular look
            if radius - 0.5 < distance < radius + 0.5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
r = int(input("Enter the radius of the circle: "))
circle_pattern(r)
