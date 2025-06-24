#keep asking the user to guess the paassword until they guess
#admin123 use while nd break
right_password="admin123"
while True:
    guessed_password= input("Enter the password")
    if guessed_password == right_password:
        print("password is correct.")
        break
    else:
        print("wrong password") 




#2nd method
while True:
    guessed_password= input("Enter the password:")
    if guessed_password == "admin123":
        print("password is correct:")
        break
    else:
        print("wrong password")    