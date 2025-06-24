# 6. Find the longest substring in a string thai is a palindrome (case-sensitive). Example: "babad" → "bab" (or"aba"), "cbbd" → "bb".

s=input("Enter a string: ")
x=s.replace(" ","").upper()
n=len(x)

longest=""

for i in range(n):
  for j in range(1,n):
    substr=x[i:j+1]
    if substr == substr[::-1]:
      if len(substr) > len(longest):
        longest = substr
print("Longest palindrome: ",longest)