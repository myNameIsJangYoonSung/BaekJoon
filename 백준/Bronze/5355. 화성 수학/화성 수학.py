from collections import deque
t = int(input())
result = []
for i in range(t):
  exam = deque(input().split())
  number = float(exam.popleft())
  for j in range(len(exam)):
    unknown = exam[j]
    if unknown == "@":
      number *= 3
    elif unknown == "%":
      number += 5
    else:
      number -= 7
  result.append(number)
for i in range(len(result)):
  print(f'{result[i]:.2f}')