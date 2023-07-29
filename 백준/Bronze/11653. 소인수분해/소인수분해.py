num = int(input())
for i in range(2,num+1):
  if num % i == 0:
    while num % i == 0:
      num = num/i
      print(i)