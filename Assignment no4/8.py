#8. Write a program to group words by their length from a list using a dictionary.
list=['red', 'blue','black','pink','green']
group={}
for word in list:
    l=len(word)
    group.setdefault(l,[]).append(word)
    
    
print(group)

