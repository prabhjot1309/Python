#10. Create a program that takes a list of tuples (name, score) and builds a dictionary 
#where each name is a key, and the value is a list of all their scores. Then calculate and print 
#each person's average score.
list= [('Aditi',78),('Pia',88),('Komal',55),('Prabh',90),('Aditi',74),('Pia',98),('Komal',59),('Prabh',80)]
score_dict={}
for name,score in list:
    if name in  score_dict:
        score_dict[name].append(score)
    else:
        score_dict[name]=[score]
print(score_dict)   
for name, score in score_dict.items():
    avg= sum(score)/len(score)
    print(name,"average is",avg)