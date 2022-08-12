def changeList(arr):
    cnt = 0
    minNum = min(arr)
    newArr = arr.copy()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if minNum == arr[j]:
                if newArr[j] == arr[j]:
                    arr[j] = cnt
                    cnt += 1
                    newArr[j] = max(arr) + 1
        minNum = min(newArr)

n = int(input())
arr = list(map(int, input().split()))
changeList(arr)
print(*arr)