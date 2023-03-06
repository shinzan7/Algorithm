from sys import stdin
from collections import deque
input = stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
parent[1] = 1
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
for i in graph[1]:
    q.append(i)
    parent[i] = 1

while q:
    cur = q.popleft()
    for i in graph[cur]:
        if parent[i] == 0:
            parent[i] = cur
            q.append(i)

for i in range(2, N+1):
    print(parent[i])