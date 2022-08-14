n = int(input())
arr = [input() for _ in range(n)]
cnt = 0

for idx, i in enumerate(arr):
    word = i[0]
    newstr = ""
    result = True
    if len(i) == 1:
        cnt += 1
        continue
    else:
        for j in range(1, len(i)):
            if i[j] != word:
                newstr += word
                word = i[j]
                if word in newstr:
                    result = False
    if result == True:
        cnt += 1
print(cnt)