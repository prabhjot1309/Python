#WAP to make a pyramid.
def pyramid(n, current=1):
    if current > n:
        return
    spaces = ' ' * (n - current)
    stars = '*' * (2 * current - 1)
    print(spaces + stars)
    pyramid(n, current + 1)

#n=int(input("Enter no. of lines: "))
print( pyramid(5))

          