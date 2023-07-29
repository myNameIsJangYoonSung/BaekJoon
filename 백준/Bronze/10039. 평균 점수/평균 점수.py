jumsu = [int(input()) for _ in range(5)]
sum_val = 0
mean_val = 0
for i in range(len(jumsu)):
  if jumsu[i] < 40:
    jumsu[i] = 40
  sum_val += jumsu[i]
  mean_val = sum_val/5
print(int(mean_val))