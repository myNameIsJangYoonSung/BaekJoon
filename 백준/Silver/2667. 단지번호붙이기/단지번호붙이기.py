from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    apt_width = 1
    copy_apt[x][y] = 1
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while len(queue) > 0:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and apt[nx][ny] == 1 and copy_apt[nx][ny] == 0:
                apt_width += 1
                copy_apt[nx][ny] = 1
                queue.append((nx, ny))
    return apt_width

N = int(input())
apt = [list(map(int, input().strip())) for _ in range(N)]
copy_apt = [[0] * N for _ in range(N)]
apt_widths = []
cnt = 0

for i in range(N):
    for j in range(N):
        if apt[i][j] == 1 and copy_apt[i][j] == 0:
            cnt += 1
            apt_widths.append(bfs(i, j))
print(cnt, *sorted(apt_widths), sep="\n")