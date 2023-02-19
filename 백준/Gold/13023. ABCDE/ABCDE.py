from sys import stdin

input = stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N)]
visit = [False] * N
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0

def dfs(idx, cnt):
    global answer
    if cnt == 5 or answer == 1:
        answer = 1
        return
    for g in graph[idx]:
        if not visit[g]:
            visit[g] = True
            dfs(g, cnt+1)
            visit[g] = False

for i in range(N):
    visit[i] = True
    dfs(i, 1)
    visit[i] = False
    
    if answer == 1:
        break
print(answer)