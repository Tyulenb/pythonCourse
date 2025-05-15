def main(table):
    result = []
    for line in table:
        first_col = line[0].split('#')
        old_date = first_col[1].split('.')
        first = old_date[2]+"/"+old_date[1]+"/"+old_date[0]
        second = line[1].split('@')[1]
        third = "Выполнено"
        if first_col[0] == "false":
            third = "Не выполнено"
        result.append([first, second, third])
    return result

table = [
    ["false#04.08.22","bibman47@gmail.com"],
    ["true#00.04.24","rumitman45@yandex.ru"],
    ["false#04.02.20","doledli10@rambler.ru"],
    ["false#02.06.27", "rostislav77@yahoo.com"]
]
table1 = [
    ["true#03.04.23","lufonak47@yahoo.com"],
    ["true#04.12.07","matvej84@yahoo.com"],
    ["false#00.07.20","sazogidi19@yahoo.com"],
]
print(main(table))
print(main(table1))
