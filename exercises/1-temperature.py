#Temperature degrees conversions Celsius to Fahrenheit
'''
    1- take input temperature(in celsius) from user
    2- create conversion equation/formula to calculte temperature in fahrenheit
    3- F = 9/5 * C +32
    4- print the result {temperature from fahrenheit to celsius}
    5- take input temperature(in fahrenheit) from user
    6- create conversion equation/formula to calculte temperature in celsius
    7- C = 5/9 * F -32
    8- print the result {temperature from celsius to fahrenheit}
'''

# convert celsius to fahrenheit
input_temprature_celsius = input("please enter the temperature in celsius  :")
temprature_fahrenheit = (9/5 * float(input_temprature_celsius)) + 32
print('the temprature  ', input_temprature_celsius,
      ' C' + ' is ', temprature_fahrenheit, ' F')

# convert fahrenheit to celsius
input_temprature_fahrenheit = input(
    "plz enter the temperature in fahrenheit  :")
temprature_celsius = 5/9 * (float(input_temprature_fahrenheit) - 32)
print('the temprature  ', input_temprature_fahrenheit,
      ' F' ' is ', temprature_celsius, ' C')
