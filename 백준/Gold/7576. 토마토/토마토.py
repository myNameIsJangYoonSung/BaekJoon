from collections import deque

def bfs(queue, cnt):
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = cx+dx, cy+dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M and tomato_box[nx][ny] == 0:
                tomato_box[nx][ny] = tomato_box[cx][cy] + 1
                queue.append((nx, ny))
                cnt-=1
    if cnt != 0:
        return -1
    else:
        return tomato_box[cx][cy] - 1

queue = deque()
M, N = map(int, input().split()) # m:col, n:row
tomato_box = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for row in range(N):
    for col in range(M):
        if tomato_box[row][col] == 0:
            cnt += 1
        if tomato_box[row][col] == 1:
            queue.append((row, col))
print(bfs(queue, cnt))