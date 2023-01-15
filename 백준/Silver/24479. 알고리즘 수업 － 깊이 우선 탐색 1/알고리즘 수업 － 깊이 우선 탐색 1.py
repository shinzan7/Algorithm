import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visit = [0] * (N+1)
cnt = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global cnt
    visit[v] = cnt
    graph[v].sort()

    for i in graph[v]:
        if visit[i] == 0:
            cnt += 1
            dfs(i)

dfs(R)

for i in range(1, N+1):
    print(visit[i])