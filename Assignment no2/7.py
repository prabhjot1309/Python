#give a no. print each digit until a zero is found
number=input("enter the number:")
for digit in number:
    if digit=="0":
        break
    print(digit) 