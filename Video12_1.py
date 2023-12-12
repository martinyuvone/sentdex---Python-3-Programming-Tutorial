#!python3
import time

#Funcionts parameters defaults
def simple_addition(num1 = 1, num2 =1):
    answer = num1 + num2
    print('num1 is', num1)
    print('num2 is', num2)
    print('sum is ', answer)

print("Default call")
simple_addition()

print("Custom call")
simple_addition(10,2)