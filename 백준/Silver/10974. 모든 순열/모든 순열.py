from sys import stdin

input = stdin.readline

N = int(input().strip())

def dfs(cnt, arr, visit):
    if cnt == N:
        print(*arr)
        return
    for i in range(1,N+1):
        if not visit[i]:
            arr.append(i)
            visit[i] = True
            dfs(cnt+1, arr, visit)
            arr.pop()
            visit[i] = False

a = []
v = [False for _ in range(N+1)]

dfs(0,a,v)