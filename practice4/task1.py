class MyClass:
    static_var = 10
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Hello(self):
        print("Hello!")
    def sm(self):
        print(self.x+self.y)

cl = MyClass(3,4)
print([x for x in dir(cl) if '__' not in x and not callable(getattr(cl, x))])


def fnc(mth):
    methods = [x for x in dir(cl) if callable(getattr(cl, x)) and not '__' in x]
    if(mth in methods):
        method = getattr(cl, mth)
        method()

fnc("sm")
fnc("Hello")


get_inheritance = lambda obj: ''.join(list(map(lambda y: y+' -> ' if y != 'object' else y ,[x.__name__ for x in obj.mro()])))

print(get_inheritance(OSError))
