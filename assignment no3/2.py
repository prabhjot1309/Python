# 2. Given a string of consonants (non-vowels, ignoring case). Example "Hello World" → 7(H,l,l,W,r,l,d).

x=input("Enter a string: ")
vowels='aeiouAEIOU'
consonants=[ i for i in x if i.isalpha() and i not in vowels ]
count=len(consonants)
print(f"{count}({','.join(consonants)})")