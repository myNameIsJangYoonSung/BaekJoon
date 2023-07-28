h, m = map(int, input().split())
take_time = int(input())
m += take_time
h = h + (m // 60)
m = m % 60
if h >= 24:
    h -= 24
print(h, m)