from math import floor
from itertools import product


def main(i_set):
    E_set = {floor(i / 7) + i * i for i in i_set if (i >= 78 or i < 35)}
    o_set = {i + e * e for i in i_set for e in E_set if i > e}
    F_set = E_set.union(o_set)
    o_sq = 0
    o_mod = 0
    for i in o_set:
        o_sq += i * i
    for i in product(o_set, F_set):
        o_mod *= (i[0] % 3 + i[1] % 2)
    return o_sq-o_mod

print(main({-30, 5, 27, -48, 49, 84, 86, -10, -5, -68}))
print(main({1, -54, 91, -20, -81, 51, 22, -5, 60}))
