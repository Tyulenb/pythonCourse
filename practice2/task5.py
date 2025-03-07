#task 5.1
def ham_dist(a, b): 
    return bin(a^b).count("1")
    #return len([i for i in range(len(a)) if a[i] != b[i]])

print("0b10, 0b11: ", ham_dist(0b10, 0b11))
print("0b1100, 0b1101: ", ham_dist(0b1100, 0b1101))
print("0b1100, 0b0011: ", ham_dist(0b1100, 0b0011))

#task 5.2
def decode(num):
    bit8 = bin(num)[2:]
    while len(bit8) != 24:
        bit8 = "0" + bit8

    counter = 1
    lst = []
    for i in range(0, len(bit8), 3):
        if bit8[i:i+3].count("0") < bit8[i:i+3].count("1"):
            lst.append("1")
        else:
            lst.append("0")


    return "".join(lst) 


lst = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407, 6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903, 2067967, 2068456]

str = ""
for i in lst:
    str += chr(int(decode(i),2))
print("\n" + str, end = '\n\n')

#task 5.3
from functools import cache
@cache
def f(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i-1] == b[j-1]:
        return f(a,b,i-1,j-1)
    else:
        return 1 + min(f(a,b,i,j-1), f(a,b,i-1,j), f(a,b,i-1,j-1))


def lev_dist(a, b):
    return f(a, b, len(a), len(b))

print("lev_dist(слон, столб)", lev_dist('слон','столб'))
print("lev_dist(слоник, столб)", lev_dist('слоник','столб'))
print("lev_dist(слон, слон)", lev_dist('слон','слон'))
