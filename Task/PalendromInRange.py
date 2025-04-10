# check palendrom or not in range
MAX_range =int(input("Enter a range to check palendrom number: "))
print("your range from (1 to ",MAX_range,") are: ")
for num in range(1,MAX_range+1):
    temp=num
    rev=0
    while(num>0):
        rev=rev*10+(num%10)
        num//=10
    if temp==rev:
        print(temp)