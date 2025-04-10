#sum of digit
num= int(input("ENter a number: "))
sum=0
while(num>0):
    sum+=num%10 #due to time complexity
    num=num//10 # // floor division 
print("Sum of digit is: ",sum)
