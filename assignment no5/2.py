#Generate a pattern like:
'''
*
* *
* * * 
* * * *
'''
def pattern(n, current=1):
    if(current>n):
     return
    print("*"* current)
    pattern(n, current+1)
n= int(input("Enter No.:"))
print(pattern(n))