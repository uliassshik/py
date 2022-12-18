a = int(input())
b = int(input())

def egcd (a, b) :
    if (b == 0) :
        y = 0
        x = 1
        return a,x,y
    else:
        d, x, y = egcd(b, a % b)
        return d, y, x - y * (a // b)
        
print(egcd(a,b))