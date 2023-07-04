result = int(input())


if result <= 100 and result >= 90:
    hak = 'A'
elif result < 90 and result >= 80:
    hak = 'B'
elif result < 80 and result >= 70:
    hak = 'C'
elif result < 70 and result >= 60:
    hak = 'D'
else:
    hak = 'F'
print(hak)