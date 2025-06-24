#7. Given a nested dictionary of students and their subject-wise marks, calculate and print the average marks for each student. 
students={ "student1":{'phy':78, 'chem':65,'maths':89,'english': 85},
         "student2":{'phy':79, 'chem':67,'maths':76,'english': 66},
         "student3":{'phy':74, 'chem':55,'maths':84,'english': 98},
         "student4":{'phy':81, 'chem':45,'maths':88,'english': 75},
         "student5":{'phy':38, 'chem':35,'maths':69,'english': 95},
}

for name, subject in students.items():
    avg= sum(subject.values())/len(subject)
    print(name ," average is",avg)
   
