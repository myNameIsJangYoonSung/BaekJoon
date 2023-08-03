first, second = 100, 100

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        second -= a
    elif b > a:
        first -= b
print(first)
print(second)