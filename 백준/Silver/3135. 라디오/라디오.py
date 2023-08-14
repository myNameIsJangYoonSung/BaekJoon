a, b = map(int, input().split())
n = int(input())
hz = [int(input()) for _ in range(n)]


mincnt = abs(a-b)
minidx = 0
minval = max(hz)
for i in range(len(hz)):
  if mincnt > abs(hz[i]-b):
    mincnt = abs(hz[i]-b) + 1
    minidx = i
print(mincnt)