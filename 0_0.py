from math, cmath import *

# variable_name = Value (saved in Ram memory)
id = 5
print(5)
print("hello")
''' 
this an integer variable
to use in a calculator
'''
x = 10  # interger int variable
print(x)

y = 2.5  # float variable
print(y)

i = -10  # interger int variable
print(i)

j = -2.5  # float variable
print(j)

text = "dina"  # string variable
print(text)

ch = 'd'  # cahr variable
print(ch)

value = True  # boolean bool variable true or false
print(value)

# sum
input_1 = 5  # int
input_2 = 6  # int
result = input_1 + input_2  # int
print(result)

input_3 = 1.1  # float
input_4 = 3  # int
result2 = input_4 - input_3  # float

input_5 = "summtion= "
# to concatenation use casting or conversion variable type to another type
convert_result_to_string = str(result2)
print(input_5 + convert_result_to_string)

# user_nmae = input("plz enter your name :")
# type , int()  , float()
# + - * / % abs pow 3**2 min max ciel floor round sqrt sqrt
phrase = ' enter your \' '
phrase2 = ''' hallo ,
            how are you'''
# len()
print(phrase[0])    # -1 -2 -3 -4 -5 hello
print(phrase.index('e'))
# slicing
print(phrase[1:4])
print(phrase[-1:-4])
# print(phrase[:-1])
print(phrase[-1:])
print(phrase[0:])
print(phrase[-3:-8:-1])
# upper() lower() find count('A') replace('Ali','saad')
# string concatenation
# 3 methods
# first_name + second_name
# formated string format(first_name,second_name)
# {first_name} , {second_name}
# print(dir(phrase))
# ----------------------------------------------------------
num_int, num_float, var_str = 1, .5, "dina"
num = 10 * 2   # 10 pow 6
round(num, 3)
new_num = format(num, 3)
new_num = f"the number {num:.3f}"
# int , float,  string,  bool , complex  , list , tuble , dictionry , set
# complex numbers
num1 = 2+5j  # imaganary
str = "   \t fdfdff "
str.strip()
str.split(',')  # tokenazation maxsplit
# row string escape the spicail charachter
str_m = r"i will \tgo \n"
# printable Ascii table
ord('A')
chr(65)
# non Ascii table
ascii('')  # \x32
# double divion //  to get only int
#
# elif
# -------------------------------------
