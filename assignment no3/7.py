# 7. Gven a string containing only '(',').','{','}','[',']', check if the sequence is valid (properly nested and closed). Example: "[{()}]" → "Valid", "(]" → "Invalid".

x=input("Enter a string: ")
s=[]
dict={')':'(', ']':'[','}':'{' }
valid=True

for i in x:
  if i in '([{':
    s.append(i)
  elif i in ')]}':
    if not s or s[-1] != dict[i]:
      valid= False
      break
    s.pop()

if s:
  valid =False

print("Valid" if valid else "Invalid")