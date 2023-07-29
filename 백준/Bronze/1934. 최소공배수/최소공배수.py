t = int(input())
result = 0
for i in range(t):
  a, b = map(int,input().split())

  # 유클리드 알고리즘 : 최대 공약수를 찾아줌 -> 나눠 0이되면 마지막에 나눈 수가 최대공약수
  aa, bb = a, b
  while bb != 0:
    aa = aa%bb
    aa, bb = bb, aa
  print(a*b//aa)