n = int(input())
count = [0, 0, 0, 0, 0]
for i in range(n):
    x, y = map(int,input().split())
    if x == 0 or y == 0:
        count[4] += 1
    elif x > 0 and y > 0:
        count[0] += 1
    elif x < 0 and y > 0:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    else:
        count[3] += 1

for i in range(len(count)):
    if i == 4:
        print("AXIS: "+str(count[4]))
    else:
        print("Q"+str(i+1)+": "+str(count[i]))