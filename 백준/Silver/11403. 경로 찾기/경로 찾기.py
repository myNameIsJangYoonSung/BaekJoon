import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for next in ans[cur]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)
    return
        

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = [[] for _ in range(N)]
# result = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans[i].append(j)

for i in range(N):
    visited = [0]*N
    bfs(i)
    # result[i] = visited
    print(*visited)

