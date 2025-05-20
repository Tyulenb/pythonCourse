def fact1(x):
    if x == 0:
        return 1
    return x*fact1(x-1)

print(fact1(5))

print((lambda fact: (lambda x: fact(fact, x)))(lambda fact, x: 1 if x == 0 else x * fact(fact, x - 1))(5))
