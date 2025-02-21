import math

def main(y):
    if y < 26:
        return 68 * math.exp(y) - 23 - y ** 6
    elif 26 <= y < 80:
        return (42 * y ** 2 - 
                19 * math.tan(31 - y - 34 * y ** 2) ** 4 - 
                (3 * y ** 3 + y + 89 * y ** 2) ** 7)
    elif 80 <= y < 140:
        return ((0.03 - y ** 3 / 63 - 62 * y ** 2) ** 6 + 
                (y / 58 + y ** 2) ** 5 + 
                y ** 21)
    elif y >= 140:
        return y ** 7

print(main(70))
print(main(173))
print(main(137))
print(main(135))
print(main(74))


