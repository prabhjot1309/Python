# 10. Create a function that takes a temperature in Celsius and returns it in Fahrenheit
def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(0))

#method2
#formulaa: c/5=(f-32)/9
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("Enter tempreature:"))
c=f_to_c(f)
print(f"{round(c,3)}, degree celsisus")