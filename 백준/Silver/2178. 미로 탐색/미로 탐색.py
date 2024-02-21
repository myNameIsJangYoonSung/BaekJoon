from collections import deque

def bfs(x, y, cnt):
  queue = deque()
  queue.append((x, y))
  dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
  copy_miro[x][y] = cnt

  while len(queue) > 0:
    cx, cy = queue.popleft()
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if nx >= 0 and nx < N and ny >= 0 and ny < M and miro[nx][ny]==1 and copy_miro[nx][ny]==0:
        queue.append((nx, ny))
        copy_miro[nx][ny] = copy_miro[cx][cy]+1

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)] # strip() 함수는 입력 뒤의 개행문자, 공백을 제거해준다.

copy_miro = [[0]*M for i in range(N)]
bfs(0,0,1)

print(copy_miro[N-1][M-1])