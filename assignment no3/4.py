# 4. Find the first character in a string that appears only once (case-sensitive). Example: "Swiss" → "w" "Programming → "r".

x=input("Enter a string: ")

s1=x.replace(" ","").upper()

for i in s1:
  if s1.count(i)==1:
    print(i)
    break
else:
    print("None")
