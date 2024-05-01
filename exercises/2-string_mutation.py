# You are given an immutable string, and you want to make changes to it.
# Read a given string, change the character at a given index and then print the modified string.
'''
    1- take input a string: string (the string to change) 
    2- take input an integer: position (the index to insert the character at)
    3- take input a string: character (the character to insert) 
    4- print string: the altered string
'''

# Solution 1 is to slice the string and join it back.
string =string2 = input(" enter the string to change  :")
position = int(input(" enter the index to insert the character at  :"))
character = input(" enter the character to insert  :")
string = string[:position] + character + string[position+1:]
#if you like to insert the charachter not to changed it 
#string = string[:position] + character + string[position:]
print('the modified string:   ', string)

# Solution 2 is to convert the string to a list and then change the value.
l = list(string2)
l[position] = character
string2 = ''.join(l)
print('the before  modified string:   ', string2)

