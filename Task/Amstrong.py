# amstrong or not
# number is amstrong when sum of cube of digit is equal to number
# 153=1^3+5^3+3^3
num =int(input("Enter a number: "))
sum=0
temp=num
while(num>0):
    digit=num%10
    sum+=digit*digit*digit
    num//=10
if(sum==temp):
    print(temp,"is amstrong")
else:
    print(temp,"is not amstrong")