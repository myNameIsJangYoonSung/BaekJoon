dice = list(map(int, input().split()))
count = [0] * 6
for i in dice:
  count[i-1] += 1

if max(count) == 3:
  print(10000 + 1000*(count.index(max(count))+1))
elif max(count) == 2:
  print(1000 + 100*(count.index(max(count))+1))
else:
  print(100*max(dice))