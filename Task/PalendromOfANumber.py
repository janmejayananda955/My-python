# check palendrom or not
num = int(input("Enter a Number: "))
# A number says palendrom when given number is equal or same to reverse of that number
temp=num
rev=0
while(num>0):
    rev=rev*10+(num%10)
    num//=10
if(rev==temp):
    print(temp," is palendrom")
else:
    print(temp," is not palendrom")