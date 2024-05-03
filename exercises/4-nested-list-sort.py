# 
# Print 
'''
    1- take input an integer: n int (the number of students' records)     
    2- take input a string: string name (the name of a student ) 
    3- take input a float: float score (the grade of a student )
    4- print list: The second lowest students debends on grades ordered alphabetically by name .
'''
# Solution
alist = []
for i in range(int(input("enter the number of students you want to provid: "))):
    name = input("enter the name of the student ")
    score = float(input("enter the grade of the student "))
    alist.append([name, score])

second_highest = sorted(set([score for name, score in alist]))[1]
print(
    '\n'.join(sorted([name for name, score in alist if score == second_highest])))
