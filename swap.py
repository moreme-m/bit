def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("after swapping: a = ", a, "b = ", b) 

swap(a=15, b=23)