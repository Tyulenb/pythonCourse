from math import cos, acos, sin, exp, ceil, sqrt


def main(z, y):
    a = (53 * z ** 3) ** 4 / 58 - (ceil(y)) ** 3
    b = (sin(y)) ** 3 - 31 * (sqrt(y ** 2 - 84 * z ** 3 - y / 33)) ** 4
    c = ((z ** 3) - y ** 2 - 1) ** 5
    q = 33 * exp(38 * y + y ** 3 / 36 + 98 * z ** 2)
    d = 9 * (z ** 2 - 89 - z) ** 7 + 80 * (0.06 - 41 * z - y ** 3 / 38) ** 5
    e = sqrt((c - q) / d)
    f = a / b
    return f - e

print(main(-0.05, 0.76))
print(main(-0.18, -0.12))
print(main(-0.35, -0.32))
print(main(-0.02, 0.8))
print(main(-0.23, -0.8))
