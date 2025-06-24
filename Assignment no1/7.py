# Logical operator challenge
is_raining = True 
have_umbrella = False

print(is_raining & have_umbrella)

print(is_raining | have_umbrella)

if not is_raining or (is_raining and have_umbrella): #not is_raining= false 
    print("You can go outside.")                     # is_raining and have_umbrella= false then it gives output false 
else:                                                #false or false gives false 
    print("You cannot go outside.")