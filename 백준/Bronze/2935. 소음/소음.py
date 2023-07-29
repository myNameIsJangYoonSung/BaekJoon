result = 0
numlist = [input() for _ in range(3)]
if numlist[1] == "*":
  result = int(numlist[0]) * int(numlist[2])
else:
  result = int(numlist[0]) + int(numlist[2])
print(result)