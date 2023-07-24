#SWITCH A VALUE A TO B VALUE
a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)

import random

print('Random number with seed 30')
for i in range(3):
    # Random number with seed 30
    random.seed(30)
    print(random.randint(25, 50))