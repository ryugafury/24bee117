print("Pulkit mantri\n24BEE117")

import math
angle = int(input("Enter the value of angle in degrees"))
rad = angle*(3.14//180)
result=0
n = int(input("Enter the range of the series"))
for i in range (0,n+1):
    power = 2*i+1
    term = (((-1)**i)*(rad**power))/math.factorial(power)
    result+=term
    print(result)
