def main(n):
    if n == 0:
        return -0.13
    if n == 1:
        return -0.37
    elif n >= 2:
        return main(n - 2) / 47 - main(n - 1) ** 2


print(main(7))
print(main(8))
print(main(3))
print(main(5))
print(main(2))
