from sys import stdin

input = stdin.readline

N = int(input().strip())
mapp = []
for _ in range(N):
    mapp.append(list(map(int, input().split())))

visit = [False]*N
answer = 1e6 * N
path = []

def dfs(cnt, cur, cost):
    global answer
    if cnt == N and cur == 0:
        answer = min(answer, cost)
        return
    for i in range(N):
        if not visit[i] and mapp[cur][i] != 0:
            visit[i] = True
            path.append(i)
            dfs(cnt+1, i, cost+mapp[cur][i])
            visit[i] = False
            path.pop()

path.append(0)
dfs(0, 0, 0)
print(answer)