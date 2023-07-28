h, m, s = map(int, input().split())
take_sec = int(input())
s += take_sec
m = m + s//60
s = s%60
h = h + m//60
m = m%60
if h > 23:
    h = h%24
print(h,m,s)