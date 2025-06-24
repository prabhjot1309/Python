# 5. Compress a string by replacing repeated characters with the character and count. Example: "aaabbcc" → "a3b2c2", If compressed string isn't shorter return orignal.

x = input("Enter a string: ")

if not x:
    print("")
else:
    compress = ""
    count = 1
    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            count += 1
        else:
            compress += x[i - 1] + str(count)
            count = 1

    compress += x[-1] + str(count)

    if len(compress) < len(x):
        print("compressed string:", compress)
    else:
        print("no need to compress:", x)
