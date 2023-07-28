t = int(input())
point = [input() for _ in range(t)]
result = 0
for i in range(len(point)):
    x, y = map(int, point[i].split())
    length = y-x
    cnt = 0
    sec = 1
    while length > 0:
        length -= sec
        cnt += 1
        if cnt % 2 == 0:
            sec += 1
    
    print(cnt)