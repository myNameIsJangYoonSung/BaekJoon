import sys
sys.setrecursionlimit(10**7) # 백준 제출 시 재귀 깊이 제한 늘리기

def dfs_1(x, y, color):
    visited_1[x][y] = 1
    
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < N and ny >= 0 and ny < N and color_map[nx][ny] == color and visited_1[nx][ny] == 0:
            dfs_1(nx, ny, color)
    return

def dfs_2(x, y, color):
    visited_2[x][y] = 1
    
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited_2[nx][ny] == 0:
            if color == "R" and color_map_2[nx][ny] == "G" or color == "G" and color_map_2[nx][ny] == "R":
                dfs_2(nx, ny, color)
            elif color_map[nx][ny] == color:
                dfs_2(nx, ny, color)
    return

N = int(input())
color_map = [list(input().strip()) for _ in range(N)]
color_map_2 = color_map
visited_1 = [[0] * N for _ in range(N)]
visited_2 = [[0] * N for _ in range(N)]

cnt_1 = 0
cnt_2 = 0

for i in range(N):
    for j in range(N):
        if visited_1[i][j] == 0:
            dfs_1(i, j, color_map[i][j])
            cnt_1 += 1
        if visited_2[i][j] == 0:
            dfs_2(i, j, color_map_2[i][j])
            cnt_2 += 1

print(cnt_1, cnt_2)