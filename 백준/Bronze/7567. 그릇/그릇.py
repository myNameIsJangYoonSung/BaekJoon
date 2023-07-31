bowl = input()

length = 0
last = 0
for i in range(len(bowl)):
    if i == 0:
        length += 10
        continue
    elif bowl[last] == bowl[i]:
        length += 5
        last = i
    else:
        length += 10
        last = i
print(length)
