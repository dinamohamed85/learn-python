# The code will read in a dictionary containing key/value pairs of name:[marks] for a list of students
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''
    1- take input an integer: n int (the number of students' records) 
    2- take input a dictionary: name, *line (The next lines contain the names and marks obtained 
    by a student, each value separated by a space)
    3- take input a string: string student_name (the name of a student to query.) 
    4- print float: The average of the marks obtained by the particular 
    student correct to 2 decimal places.
'''
# Solution 1 is to slice the string and join it back.
n = int(input('enter the number students: '))
student_marks = {}
for i in range(n):
    name, *line = input("enter name and scroe (spared by space): ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
student_name = input('enter the name of student:')
list_1 = list(student_marks[student_name])

sum_marks = sum(list_1)
average = sum_marks/len(list_1)
print("The average score " ,'%.2f' % average)
