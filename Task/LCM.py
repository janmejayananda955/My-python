#LCM of two number (LEASt COMMON MULTIPLE)
num1 =int(input("Enter 1st Number: "))
num2 =int(input("Enter 2st Number: "))
# Using GCD
temp1=num1
temp2=num2
# (here i take temp1 and temp2 to find 
# lcm because at the time of lcm calculation value got changed)
# while(num1!=num2):
#     if(num1>num2):
#         num1-=num2
#     if(num2>num1):
#         num2-=num1
# gcd=num1
# lcm=(temp1*temp2)//gcd
# print("GCD of two number is: ",num1,num2) # to check after gcd 2 numbers are
# print("LCM of two number is: ",lcm)

# Whithout taking GCD value
# great =(num1>num2)? num1 : num2 in java
great =num1 if num1>num2 else num2 # in python
while(True):
    if(great%num1==0 and great%num2==0):
        lcm=great
        break
    great+=1
print("LCM of two number is: ",lcm)