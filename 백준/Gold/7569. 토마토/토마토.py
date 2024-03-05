from collections import deque

def bfs(queue):
    global cnt
    while queue:
        ch, cx, cy, day  = queue.popleft()
        for dx, dy, dh in [(0,1,0), (1,0,0), (0,-1,0), (-1,0,0), (0,0,1), (0,0,1), (0,0,-1), (0,0,-1)]:
            nh, nx, ny = ch+dh, cx+dx, cy+dy
            if nh >= 0 and nh < H and nx >= 0 and nx < N and ny >= 0 and ny < M and tomato_box[nh][nx][ny] == 0:
                tomato_box[nh][nx][ny] = 1
                queue.append((nh, nx, ny, day+1))
                cnt-=1
    return day
M, N, H = map(int, input().split())
tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
cnt = M*N*H
queue = deque()
for height in range(H):
    for row in range(N):
        for col in range(M):
            if tomato_box[height][row][col] == -1:
                cnt-=1
            elif tomato_box[height][row][col] == 1:
                queue.append((height, row, col, 0))
                cnt-=1

if queue:
    result = bfs(queue)

if cnt != 0:
    print(-1)
else:
    print(result)