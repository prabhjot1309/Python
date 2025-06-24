#keep adding number onwards until total sum exceeds 35 print last sum nd digit
A = [7,5,4,6,2,10,1,9,15,18]
total = 0

for a in A:
    total = total + a
    if total > 25:
        print("Total sum:", total)
        print("Last number added:", a)
        break

    