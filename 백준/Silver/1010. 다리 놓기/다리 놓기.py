def facto(x):
    num = 1
    for _ in range(x):
        num *= x
        x -= 1
    return num
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    result = facto(m) // facto(m-n) // facto(n)
    print(result)