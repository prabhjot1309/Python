#Create a dictionary with names as keys and ages as values. Print the name(s) of the oldest person(s). 
dict= {"ram":56, "Sohan":67,"Shalu":60,"raman":53}
max_age=max(dict.values())
for k,v in dict.items():
    if v==max_age:
        print("oldest person is ", k)