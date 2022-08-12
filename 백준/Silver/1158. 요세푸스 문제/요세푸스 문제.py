n, target = map(int, input().split())
arr = [elem for elem in range(1,n+1)]
cnt = 0
jump = 1
newArr = []

while(arr):
    if target == jump:
        newArr.append(arr[cnt%len(arr)])
        arr.remove(arr[cnt%len(arr)])
        jump = 1
    else:
        cnt += 1
        jump += 1
    if cnt == len(arr):
        cnt = 0
print("<", end="") 
print(*newArr, sep=", ", end="")
print(">")