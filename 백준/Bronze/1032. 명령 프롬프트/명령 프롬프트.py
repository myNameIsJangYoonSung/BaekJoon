n = int(input())
arr = [input() for _ in range(n)]

findapp = ""
if len(arr) == 1:
    findapp += arr[0]
else:
    for i in range(len(arr[0])):
        start = arr[0][i]
        for j in range(1, len(arr)):
            if start != arr[j][i]:
                findapp += '?'
                break
            if len(arr)-1 == j:
                findapp += start
print(findapp)