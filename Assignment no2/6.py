#to print multiples of 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

#method 2
n=7
while n>=100:
    print(n)
    n+=7

#method3
n=7
for i in range (8):
	j=1
	print ("Table to ", i, "is as follows")
	while j <15:
		print (i, "*", j, "=", i*j)
		j=j+1
		print()