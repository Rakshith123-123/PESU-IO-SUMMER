n = input("enter a number")
n = int(n)
sum = 0
while (n != 0): 
    sum = sum + int(n % 10) 
    n = int(n/10) 
print("sum is",sum) 