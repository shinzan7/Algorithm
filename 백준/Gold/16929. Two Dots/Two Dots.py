from sys import stdin

input = stdin.readline

R, C = map(int,input().split())
mapp = []
for _ in range(R):
    mapp.append(list(input().strip()))

dr = [0,0,1,-1]
dc = [1,-1,0,0]
visit = [[False for _ in range(C)] for _ in range(R)]
sr = 0
sc = 0
answer = 'No'

def dfs(r, c, cnt, color):
    global sr, sc, answer
    if answer == 'Yes':
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if cnt >= 4 and nr == sr and nc == sc:
            answer = 'Yes'
            return
        if 0 <= nr < R and 0 <= nc < C and not visit[nr][nc] and mapp[nr][nc] == color:
            visit[nr][nc] = True
            dfs(nr, nc, cnt+1, color)
            visit[nr][nc] = False

for r in range(R):
    for c in range(C):
        sr = r
        sc = c
        visit[r][c] = True
        dfs(r,c,1,mapp[r][c])
        visit[r][c] = False

print(answer)