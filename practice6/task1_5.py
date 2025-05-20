def collect(cls):
    def get_objects():
        return cls.lst
    cls.get_objects = get_objects
    cls.lst = []

    def __init__(self):
        cls.lst.append(self)
    cls.__init__ = __init__
    return cls



@collect
class C1:
    pass

a = C1()
b = C1()
c = C1()

print(C1.get_objects())
