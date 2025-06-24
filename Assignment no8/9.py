# 9. Write a Python program to store and read student records (name and marks) from a file.
# Store student records
with open("students.txt", "w") as file:
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        file.write(name + "," + marks + "\n")

print("\nRecords saved successfully!\n")

# Read and display student records
with open("students.txt", "r") as file:
    print("Student Records:")
    for line in file:
        name, marks = line.strip().split(",")
        print(f"Name: {name}, Marks: {marks}")



#method 2
# Write records to file
file = open("students.txt", "w")
file.write("Alice,85\n")
file.write("Bob,90\n")
file.write("Charlie,78\n")
file.close()

# Read and display records
file = open("students.txt", "r")
for line in file:
    name, marks = line.strip().split(",")
    print("Name:", name, "Marks:", marks)
file.close()



