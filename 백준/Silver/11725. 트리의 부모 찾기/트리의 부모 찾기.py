import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        c_node = queue.popleft()
        for n_node in graph[c_node]:
            if parent_graph[n_node] == 0:
                parent_graph[n_node] = c_node
                queue.append(n_node)
    return

N = int(input())
graph = [[] for _ in range(N+1)]
parent_graph = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(*parent_graph[2:], sep="\n")