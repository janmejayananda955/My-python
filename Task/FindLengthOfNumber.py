# find length of number
num = int(input("Enter a number: "))
count = 0
while(num>0):
    count+=1
    num=num//10
print("Length of number is: ",count)