#Write a Python program to read the contents of 'example.txt' and display them on the screen.
with open('example.txt','r')as f:
	f_contents = f.read()
	print(f_contents)