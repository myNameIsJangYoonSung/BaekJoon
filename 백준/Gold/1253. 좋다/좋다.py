n = int(input())
numlist = list(map(int, input().split()))
numlist.sort()

cnt = 0
result = []
for i in range(n):
  find_value = numlist[i]
  start = 0
  end = n-1
  while start < end:
    if numlist[start] + numlist[end] == find_value:
      if start != i and end != i:
        cnt += 1
        break
      elif start == i:
        start += 1
      elif end == i:
        end -= 1
    elif numlist[start] + numlist[end] > find_value:
      end -= 1
    elif numlist[start] + numlist[end] < find_value:
      start += 1
print(cnt)