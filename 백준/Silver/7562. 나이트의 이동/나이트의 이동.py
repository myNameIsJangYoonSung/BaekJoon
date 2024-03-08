import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque
def bfs(x,y,cnt):
    queue = deque()
    queue.append((x,y,cnt))
    visited[x][y] = 1
    while queue:
        cx, cy, move = queue.popleft()
        if cx == t_x and cy == t_y:
            return move
        for dx, dy in [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]:
            nx, ny = cx+dx, cy+dy
            if nx >= 0 and nx < l and ny >= 0 and ny < l and visited[nx][ny]==0:
                queue.append((nx,ny,move+1))
                visited[nx][ny] = 1
t = int(input())

for _ in range(t):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    x, y = map(int, input().split())
    t_x, t_y = map(int, input().split())

    print(bfs(x,y,0))