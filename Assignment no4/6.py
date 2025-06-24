#6. Write a program that inverts a dictionary (i.e., swaps keys and values). Assume all values are unique. 
dict={'a':1,'b':6,'c':10,'d':4,'e':9}
inverted_dict={value: keys for keys, value in dict.items() }
print(inverted_dict)