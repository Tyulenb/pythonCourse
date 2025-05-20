def io(input1, input2, input3, output):
    def decorator(func):
        def wrapper():
            x = input1()
            y = input2()
            z = input3()
            if x.isdigit() and y.isdigit() and z.isdigit():
                x = int(x)
                y = int(y)
                z = int(z)
            output(func(x, y, z))
        return wrapper
    return decorator


@io(input, input, input, print)
def f1(x, y, z):
    return (x + y + z)

f1()
