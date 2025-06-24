#Draw a sqaure pattern like star.
def square_pattern(n):
    for i in range(n):
        print("* " * n)

size = int(input("Enter the size of the square: "))
square_pattern(size)