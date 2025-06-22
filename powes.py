def is_power_of_2(n):
    return(n & (n -1)) == 0

print(is_power_of_2(16))
print(is_power_of_2(37))
print(is_power_of_2(20))

def is_power_of_4(n):
    if (n & (n -1)) !=0:
        return False #Not a power of 4
    count = 0
    while n > 1:
        n >>= 1
        count += 1
    return count % 2 == 0 #check if position is even    

print(is_power_of_4(16))
print(is_power_of_4(37))
print(is_power_of_4(64))
