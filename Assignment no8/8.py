#8. Write a Python program to create a log file and append timestamps whenever the program is run.
import time

file = open("log.txt", "a")
file.write("Program run at: " + time.ctime() + "\n")
file.close()

print("Logged.")
