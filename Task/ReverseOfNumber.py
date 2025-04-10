# reverse of a number
num = int(input("Enter a number: "))
rev=0
while(num>0):
    rev=rev*10+(num%10) #due to time complexity
    num=num//10 # // floor division
print("Reverse of number is: ",rev)