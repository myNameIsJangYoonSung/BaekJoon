import math
def is_prime_number(n):
  arr = [True] * (n+1)
  p_arr = []
  arr[0] = False
  arr[1] = False

  for i in range(2, n//2+1):
    if arr[i] == True:
      j = 2

      while i*j <= n:
        arr[i*j] = False
        j += 1
  for i in range(len(arr)):
    if arr[i] == True:
      p_arr.append(i)
  return p_arr

num = int(input())
result = []
prime_list = is_prime_number(num)
for i in prime_list:
  divide = i
  if num % divide == 0:
    while num % divide == 0:
      result.append(divide)
      num = num/divide
for i in range(len(result)):
  print(int(result[i]))   
