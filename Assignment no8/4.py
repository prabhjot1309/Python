# 4. Write a Python program to read a file and print only those lines which start with the letter 'A'.
with open('example.txt','r')as f:
	for line in f:
            if line.startswith('A'):
                 print(line)
		


'''with open('example.txt', 'r') as f:
    for line in f:
        if line.startswith('A'):
            print(line.strip())'''
