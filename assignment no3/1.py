#Take a sentence and reverse the order of its words. Example: "I love Python" → "Python love I"
x= input("Enter a sentence: ")
list1= x.split()
list2 =list1[::-1]
x = ' '.join(list2)

print("Reversed sentence:",x)
