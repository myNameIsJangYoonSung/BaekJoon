t = int(input())
for i in range(t):
    y, k = [], []
    for i in range(9):
        a, b = map(int, input().split())
        y.append(a)
        k.append(b)
    if sum(y) > sum(k):
        print("Yonsei")
    elif sum(k) > sum(y):
        print("Korea")
    else:
        print("Draw")