def f1(x):
    if x[0] == 1998:
        return 0
    if x[0] == 1984:
        return 1


def f2(x):
    if x[2] == 'SHELL':
        return 2
    if x[2] == 'HTML':
        return 3
    if x[2] == 'OCAML':
        return 4


def f3(x):
    if x[2] == 'SHELL':
        return 5
    if x[2] == 'HTML':
        return 6
    if x[2] == 'OCAML':
        return 7


def f4(x):
    if x[2] == 'SHELL':
        return 8
    if x[2] == 'HTML':
        return 9
    if x[2] == 'OCAML':
        return 10


def f5(x):
    if x[3] == 1968:
        return f1(x)
    if x[3] == 1973:
        return f2(x)
    if x[3] == 1963:
        return f3(x)
    

def f6(x):
    if x[3] == 1968:
        return f4(x)
    if x[3] == 1973:
        return 11
    if x[3] == 1963:
        return 12


def main(x):
    if x[1] == 'D':
        return f5(x)
    if x[1] == 'TCL':
        return f6(x)
    if x[1] == 'SWIFT':
        return 13

print(main([1984, 'SWIFT', 'SHELL', 1963]))
print(main([1984, 'TCL', 'SHELL', 1968]))
print(main([1984, 'TCL', 'OCAML', 1963]))
print(main([1984, 'TCL', 'SHELL', 1973]))
print(main([1998, 'TCL', 'HTML', 1968]))

