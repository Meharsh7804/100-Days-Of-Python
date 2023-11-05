# Create a Python module called math_operations with functions for addition, subtraction, multiplication, and division. Import this module and use it to perform these operations. 

import math_operations as mo 

a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))

ans1 = mo.add(a,b)
ans2 = mo.sub(a,b)
ans3 = mo.mul(a,b)
ans4 = mo.div(a,b)
ans5 = mo.mod(a,b)

print("Addition :",ans1)
print("Subtraction :",ans2)
print("Multiplication :",ans3)
print("Quotient :",ans4)
print("Remainder :",ans5)


