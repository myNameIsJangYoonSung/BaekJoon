t = int(input())
value = ""
result = []
for i in range(t):
  s, r = input().split()
  s = int(s)
  for j in range(len(r)):
    value += r[j]*s
  result.append(value)
  value = ""
for i in range(len(result)):
  print(result[i])