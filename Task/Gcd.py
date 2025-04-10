# GCD Of two number

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

gcd=1
for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print("GCD of ",num1," and ",num2," is: ",gcd)

# GCD using while loop

while(num1 !=num2):
    if(num1>num2):
        num1-=num2
    if(num2>num1):
        num2-=num1
print("GCD of two number is: ",num1)

# above code explanation
# 1. Take two numbers from user
# 2. check if both numbers are not equal
# 3. check which number is greater
# 4. subtract smaller number from greater number
# 5. repeat step 2 to 4 until both numbers are equal

