t = int(input())

cnt = 0
time = [5*60, 1*60, 10]
timecnt = [0,0,0]
if t%10 != 0:
    print(-1)
else:
    for i in range(len(time)):
        while t-time[i]>= 0:
            t -= time[i]
            timecnt[i] += 1
    print(*timecnt)    