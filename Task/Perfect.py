num = int(input("Enter a number: "))
sum = 0

for i in range(1, num+1):
    if num % i == 0:
        sum += i

if sum == num:
    print(num," is a Perfect Number")
else:
    print(num," is NOT a Perfect Number")
