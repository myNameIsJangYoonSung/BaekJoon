n = int(input())
arr = [input() for _ in range(n)]
cnt = 0

for i in arr:
    word = i[0]
    newstr = ""
    result = True
    
    for j in range(1, len(i)):
        if i[j] != word:
            newstr += word
            word = i[j]
            if word in newstr:
                result = False
    if result == True:
        cnt += 1
print(cnt)