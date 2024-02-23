import sys
sys.setrecursionlimit(10**7) # 백준 제출 시 재귀 깊이 제한 늘리기

def dfs(c):
    visited[c] = True
    for nc in graph[c]:
        if not visited[nc]:
            dfs(nc)
    

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)