string= "hello world"
freq={}

for char in string:
    if char!= " ":
        freq[char]= freq.get(char,0)+1
print(freq)