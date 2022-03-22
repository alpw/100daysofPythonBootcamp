def tottal(*args): #it's a tuple
    total = 0
    for x in args:
        total += x
    return total

print(tottal(1,2,3,4,5,6,7,8,9))

def calculator(n,**kwargs): #it's a dictionary
    n += kwargs["add"]
    n *= kwargs["mult"]
    return n

print(calculator(5, add=3, mult=5))

class Pc():
    def __init__(self, **kwargs):
        self.comp = kwargs.get("comp")
        self.model = kwargs.get("model")
    
    def info(self) -> str:
        print(self.comp, ", ", self.model)


abraA7 = Pc(comp="Monster", model="Abra A7 V12.1")

abraA7.info()