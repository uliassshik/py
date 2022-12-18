import math

def isPrime(a):
    x = int(math.sqrt(a))
    y=a
    for i in range (2,x+1):
        if y%i==0:
            return False
        else:
            continue
    if y<=1:
        return False
    return True
print(isPrime(0))  #False   
print(isPrime(1))  #False   
print(isPrime(144))  #False     
print(isPrime(1103))    #True    