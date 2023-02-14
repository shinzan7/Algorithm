import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
V = int(input().strip())

graph = [[] for i in range(N+1)]
visit = [0 for i in range(N+1)]

for i in range(V):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
visit[1] = 1
q = deque([1])
while q:
    cur = q.popleft()
    for g in graph[cur]:
        if visit[g] == 0:
            q.append(g)
            visit[g] = 1
print(sum(visit)-1)