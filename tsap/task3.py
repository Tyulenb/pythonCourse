import math


def main(a, n, b, p):
    s = 0
    for i in range(1, b+1):
        for k in range(1, n+1):
            for j in range(1, a+1):
                s += 95 * (math.ceil(j ** 2 - k ** 3)) ** 3\
                        - math.exp(i) - (0.01 - 20 * p ** 2) ** 6
    return s

print(main(6, 3, 4, 0.67))
print(main(3, 8, 7, 0.6))
print(main(3, 5, 3, -0.95))
print(main(6, 4, 3, 0.67))
print(main(8, 8, 3, -0.49))
