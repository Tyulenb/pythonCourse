def main(dct):
    b1 = format(dct['B1'], '03b')
    b2 = format(dct['B2'], '04b')
    b3 = format(dct['B3'], '04b')
    b4 = format(0, '07b')
    b5 = format(dct['B5'], '03b')
    b6 = format(dct['B6'], '08b')
    rs_str = b6 + b5 + b4 + b3 + b2 + b1
    return int(rs_str, 2)

print(main({'B1': 0, 'B2': 5, 'B3': 15, 'B5': 4, 'B6': 61}))
print(main({'B1': 7, 'B2': 8, 'B3': 9, 'B5': 6, 'B6': 7}))
print(main({'B1': 3, 'B2': 2, 'B3': 4, 'B5': 7, 'B6': 1}))
print(main({'B1': 1, 'B2': 15, 'B3': 0, 'B5': 1, 'B6': 132}))
