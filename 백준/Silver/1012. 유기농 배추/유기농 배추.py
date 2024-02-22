from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    farm[x][y] = 2 # 0:배추x, 1:배추o, 2:방문o
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while len(queue) > 0:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N and farm[nx][ny] == 1:
                queue.append((nx, ny))
                farm[nx][ny] = 2
    return

T = int(input())
answer = []

for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*N for _ in range(M)]
    worms = 0
    for _ in range(K): # 배추 심기
        x, y = map(int, input().split())
        farm[x][y] = 1
    
    for row in range(M):
        for col in range(N):
            if farm[row][col] == 1:
                worms += 1
                bfs(row, col)
    print(worms)