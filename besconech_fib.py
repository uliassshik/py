import itertools

class Fib:    

    class _Fib_iter:
        def __init__(self):
            self.i1=1 
            self.i2=1
            
        def __next__(self):
            d = self.i1
            self.i2=self.i1+self.i2
            self.i1=self.i2-self.i1
            return d

    def __iter__(self):
        return Fib._Fib_iter()

fib_amount = int(input('Введите положительное число - количество членов последовательности Фибоначчи:'))
fi = Fib()
for f in itertools.islice(fi, fib_amount):
    print(f)
    