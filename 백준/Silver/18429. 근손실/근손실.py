from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
kit = list(map(int,input().split()))
visited = [False] * N
answer = 0

def dfs(cnt, weight):
    global answer
    if weight < 500:
        return

    if cnt == N:
        answer += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, weight - K + kit[i])
            visited[i] = False

dfs(0,500)

print(answer)