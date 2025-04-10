number1 = int(input("Enter number1 number: "))
number2 = int(input("Enter number2 number: "))
number3 = int(input("Enter number3 number: "))
if number1>number2 and number1>number3:
    print("Greatest Number is: ",number1)
elif number2>number1 and number2>number3:
    print("Greatest Number is: ",number2)
else:
    print("Greatest Number is: ",number3)

# neasted if else

if number1>number2:
    if number1>number3:
        print("Greatest Number is: ",number1)
    else:
        print("Greatest Number is: ",number3)
else:
    if number2>number3:
        print("Greatest Number is: ",number2)
    else:
        print("Greatest Number is: ",number3)