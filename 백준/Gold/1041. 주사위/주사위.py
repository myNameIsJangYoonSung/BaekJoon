n = int(input())

a, b, c, d, e, f = map(int, input().split())

if n == 1:
    dice = min(a+b+c+d+e, b+a+c+d+f, c+e+a+b+f, d+e+a+b+f, e+a+c+d+f, f+b+c+d+e)
    print(dice)
elif n == 2:
    corner = min(d+a+b, d+b+f, d+f+e, d+e+a, c+a+b, c+b+f, c+f+e, c+e+a)
    bottom = min(d+a, d+b, d+f, d+e, c+a, c+b, c+f, c+e, a+b, b+f, f+e, e+a)
    print(corner * 4 + bottom * 4)
else:
    corner = min(d+a+b, d+b+f, d+f+e, d+e+a, c+a+b, c+b+f, c+f+e, c+e+a)
    side_corner = min(d+a, d+b, d+f, d+e, c+a, c+b, c+f, c+e, a+b, b+f, f+e, e+a)
    plane = min(a,b,c,d,e,f)
    print(corner*4 + side_corner*(n-2)*4 + side_corner*(n-1)*4 + plane*(n*n-4-(n-2)*4) + plane*(n*n-n-(n-1)*2)*4) # 코너 + 탑 사이드들 4개 + 사이드 기둥 4개 + 탑 면 + 사이드 면