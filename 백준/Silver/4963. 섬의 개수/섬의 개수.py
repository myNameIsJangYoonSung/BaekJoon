import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  test_case[x][y] = 2

  while queue:
    cx, cy = queue.popleft()
    for dx, dy in [(1,0), (0,-1), (-1,0), (0, 1), (-1,-1), (-1,1), (1,-1), (1,1)]:
        nx, ny = cx+dx, cy+dy
        if nx >= 0 and nx < m_row and ny >= 0 and ny < m_col and test_case[nx][ny] == 1:
            test_case[nx][ny] = 2
            queue.append((nx,ny))
  return

result = []
while True:
  m_col, m_row = map(int, input().split())
  if m_row == 0 and m_col == 0:
    break
  test_case = [list(map(int, input().split())) for _ in range(m_row)]

  cnt = 0
  for row in range(m_row):
    for col in range(m_col):
      if test_case[row][col] == 1:
        bfs(row, col)
        cnt += 1
  result.append(cnt)
print(*result, sep="\n")