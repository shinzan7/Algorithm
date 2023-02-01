import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = []
dr = [0,0,-1,1]
dc = [1,-1,0,0]
visit = [[False for cols in range(C)] for rows in range(R)]
for r in range(R):
    arr.append(list(map(int, input().split())))
answer = 0

def dfs(cnt, r, c, summ):
    global answer
    if cnt == 4:
        answer = max(answer, summ)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not visit[nr][nc]:
            if cnt == 2:
                visit[nr][nc] = True
                dfs(cnt+1, r, c, summ + arr[nr][nc])
                visit[nr][nc] = False

            visit[nr][nc] = True
            dfs(cnt+1, nr, nc, summ + arr[nr][nc])
            visit[nr][nc] = False

for r in range(R):
    for c in range(C):
        visit[r][c] = True
        dfs(1, r, c, arr[r][c])
        visit[r][c] = False

print(answer)