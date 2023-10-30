import collections as col
import sys

def bfs(c):
    global result
    deque = col.deque()
    deque.append(c)
    visited[c] = 1
    
    while deque:
        nc = deque.popleft()
        for next in computer[nc]:
            if visited[next] == 0:
                visited[next] = 1
                deque.append(next)
                result += 1

# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

n = int(input())
edge = int(input())
computer = [[] for _ in range (n+1)]
visited = [0] * (n+1)
result = 0
# graph 입력받기
for _ in range(edge):
    a, b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)

for i in range(len(computer)):
    computer[i].sort()

bfs(1)
print(result)