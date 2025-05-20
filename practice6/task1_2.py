def person(name, age):
    Name = name
    Age = age
    def get(attr):
        if attr == "name":
            return Name
        elif attr == "age":
            return Age
    return get

def get(prsn, attr):
    return prsn(attr)

def replace(prsn, attr, val):
    if attr == "name":
        return person(name=val, age=get(prsn, "age"))
    elif attr == "age":
        return person(name=get(prsn, "name"), age=val)

p1 = person(name="Ivan", age=16)
print(get(p1,'name'))
p2 = replace(p1, 'age', 18)
print(get(p2, 'name'), get(p2, 'age'))
