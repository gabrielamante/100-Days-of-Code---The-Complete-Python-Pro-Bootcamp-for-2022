def add(*args):
    sumnumbers = 0
    for n in args:
        sumnumbers += n
    return sumnumbers

print(add(1,2,3,4,5,6,7,8,9,10))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    

    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw