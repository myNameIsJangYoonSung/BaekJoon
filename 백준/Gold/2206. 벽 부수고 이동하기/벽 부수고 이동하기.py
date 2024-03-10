import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque
def bfs(x, y, cnt, crashed):
    queue = deque()
    queue.append((x,y,cnt,crashed))
    move_map[x][y] = 1
    while queue:
        cx, cy, count, crash = queue.popleft()
        if cx == N-1 and cy == M-1:
            return count
        for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if crash == True and move_map[nx][ny] == 0 and crash_map[nx][ny] == 0:
                    move_map[nx][ny] = 2
                    queue.append((nx,ny,count+1,True))
                elif crash == False:
                    if crash_map[nx][ny] == 1 and move_map[nx][ny] == 0:
                        queue.append((nx,ny,count+1,True))
                    elif crash_map[nx][ny] == 0 and move_map[nx][ny] != 1:
                        move_map[nx][ny] = 1
                        queue.append((nx,ny,count+1,False))
    return -1

N, M = map(int, input().split())
crash_map = [list(map(int, input().strip())) for _ in range(N)]
move_map = [[0]*M for _ in range(N)]

print(bfs(0, 0, 1, False))