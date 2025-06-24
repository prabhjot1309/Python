# 3. Check if two strings are anagrams (same characters, same frequency, ignoring case). Example: "Listen", "Silent" → "Anagram", "Hello" "world" → "Not Anagram".

x=input("Enter first string: ")
y=input("Enter second string: ")

s1=x.replace(" ","").upper()
s2=y.replace(" ","").upper()

if sorted(s1) == sorted(s2):
  print("Anagram")
else:
  print("Not Anagram")
  