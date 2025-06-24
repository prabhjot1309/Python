#Draw a rectangle pattern like star.
#area of rectangle = lXb
def rectangle_pattern(l,b):
    for i in range(b):
        print("* " * l)
l= int(input("Enter the length of rectangle: "))
b= int(input("Enter the breadth of rectangle: "))
print(rectangle_pattern(l,b))


