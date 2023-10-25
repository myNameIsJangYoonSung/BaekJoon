def dfs(x, y, water):
    safe_matrix[x][y] = 1
    
    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < n and ny >= 0 and ny < n and safe_matrix[nx][ny] == 0 and matrix[nx][ny] > water:
            dfs(nx, ny, water)
    
# txt 파일 입력받는 법 나중에 input()이라는 명령어에 자동으로 파일에서 한줄을 빼서 입력해줌 입력시간 짧아짐
import sys
#sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline

# 재귀 최대 수를 늘려줌
sys.setrecursionlimit(10**9)

n = int(input())
maxheight = 1
matrix = []
for i in range(n):
    tmp = list(map(int, input().split()))
    maxheight = max(tmp)
    matrix.append(tmp)
result = 0

for water in range(maxheight):
    count_safe = 0
    safe_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if safe_matrix[i][j] == 0 and matrix[i][j] > water:
                dfs(i, j, water)
                count_safe += 1
    result = max(result, count_safe)
print(result)
