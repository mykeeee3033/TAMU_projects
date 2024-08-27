# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Micheal Tidwell
# Section:      102 536
# Assignment:   1.13 (e.g. Lab 1b-2)
# Date:         22/08/2024

from math import * 

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is 2")

# equation
x = 1
for i in range(8):
    equation = (1-cos(x))/(x**2)
    x = float("."+"0"*i+"1")
    print(equation)

print()


print("My guess wasn't right")