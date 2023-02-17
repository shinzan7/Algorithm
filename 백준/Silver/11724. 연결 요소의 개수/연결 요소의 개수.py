from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(i)

cnt = 0
for i in range(1, N+1):
    if not visit[i]:
        cnt += 1
        dfs(i)

print(cnt)