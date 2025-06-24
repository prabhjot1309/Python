#5. Write a Python program to merge the contents of two files into a third file.
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    data1 = f1.read()
    data2 = f2.read()

# Open the third file in write mode and write both contents
with open('merged_file.txt', 'w') as f3:
    f3.write(data1 + '\n' + data2)

print("Files merged successfully into 'merged_file.txt'")
