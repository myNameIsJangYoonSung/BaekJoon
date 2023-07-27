n = int(input())
i = 1
cnt = 0
while n > 0:
  n -= i
  i += 1
  cnt += 1
if cnt % 2 == 0:
  print(str(1+(cnt+n-1))+"/"+str(cnt-(cnt+n-1)))
else:
  print(str(cnt-(cnt+n-1))+"/"+str(1+(cnt+n-1)))