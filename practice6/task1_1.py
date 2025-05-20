def deravativ(func):
    def deriv_func(x):
        x0 = x
        dx = 1e-12
        dy = func(x+dx) - func(x-dx)
        drv = dy/(2*dx)
        return drv
    return deriv_func

print(deravativ(lambda x: x ** 3)(5))

