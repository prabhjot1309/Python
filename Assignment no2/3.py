#to find first even no. in list using loop and break
list = [2, 3, 6, 5, 7, 8, 12, 34, 57, 89, 75, 67, 45]
for l in list:
    if l % 2 == 0:
        print("First Even number found:", l)
        break
