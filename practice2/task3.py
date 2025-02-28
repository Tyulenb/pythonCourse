import random

s = ["20", "20", "20", "21", "22", "23", "100000"]
print([int(x) for x in s]) #task3.1
print(sum(s.count(x) for x in s)) #task3.2
print(s[::-1]) #task3.3
print([x for x in range(len(s)) if s[x]=="20"]) #task3.4
print([int(x) + sum([int(y) for y in s[0:len(s):2]]) for x in s]) #task3.5
print(max([len(x) for x in s])) #task3.6
print([int(x)%sum([int(y) for y in x]) == 0 for x in s]) #task3.7

alph = "abcdefghijklmnopqrstuvwxyz"
print("".join([random.choice(alph) for _ in range(20)])) #task3.8
