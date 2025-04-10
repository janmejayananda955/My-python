# Fibonachi series
Max_range = int(input("Enter the range: "))
a,b=0,1
print(a,b)
print("Fibonacci series:")
c=0
for i in range(2, Max_range+1):
        a = b + c
        print(a)
        b = c
        c = a
