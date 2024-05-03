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
# Solution .
n = int(input('enter the number of students you want to provid: '))
student_marks = {}
for i in range(n):
    name, *line = input("enter name and scores (separated by space): ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
    
student_name = input(
    'enter the name of student whose percentage you want to print:')
list_1 = list(student_marks[student_name])

sum_marks = sum(list_1)
average = sum_marks/len(list_1)
print("The average score for ", student_name,  " is: ", '%.2f' % average)
