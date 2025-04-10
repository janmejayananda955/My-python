# print name 5 times
# for i in range(0,6):
#     print("NAME")

# decrement order 5number
# for i in range(6,0,-1):
#     print(i)

# sum of natural number in given range
# n=int(input("Enter a range "))
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)

# Print even number
# n=int(input("ENter a range "))
# for i in range(1,n):
#     if(i%2==0):
#         print(i)

# prime number
# n=int(input("Enter a number "))
# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count=count+1
# if(count==2):
#     print("Prime")
# else:
#     print("Non Prime")

# prime number in range
n=int(input("Enter a number:"))
for i in range(1,n+1):
    count=0
    for j in  range(2,i):
        if(i % j == 0):
            count=count+1
            break
    if(count==0):
        print(i)   

# break and continue  
# continue
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)

# break
# for i in range(1,11):
#     if(i==5):
#         break
#     print(i)