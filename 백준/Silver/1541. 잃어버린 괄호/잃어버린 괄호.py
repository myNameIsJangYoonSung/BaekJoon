solve = input()
minus = list(solve.split('-'))
result = 0
plus = ''
for i in range(len(minus)):
    if '+' in minus[i]:
        plus = minus.pop(i)
        minus.insert(i, str(sum(list(map(int, plus.split('+'))))))

result += int(minus[0])
for i in range(1, len(minus)):
        result -= int(minus[i])
print(result)