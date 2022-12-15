from typeguard import typechecked

a: int = int(input())
b: int = int(input())

@typechecked
def egcd (a: int, b: int) -> tuple [int, int, int]:
    if (b == 0) :
        y = 0
        x = 1
        return a,x,y
    else:
        d, x, y = egcd(b, a % b)
        return d, y, x - y * (a // b)
print(egcd(a,b))