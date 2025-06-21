a = int(input("Enter the first number :"))
b = int(input("Enter the second number"))

if (a ^ b == 0):
    print("numbers are equal")
else:
    print("numbers are not equal")


arr = [5,5,6,6,6,2,2]
result = 0
for num in arr:
    result = result ^ num

print("The number that appears an odd number of times is,", result)     