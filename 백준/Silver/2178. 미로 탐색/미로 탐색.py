from sys import stdin
from collections import deque

input = stdin.readline
R,C = map(int, input().split())
mapp = []
visit = [[False for cols in range(C)] for rows in range(R)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]
for r in range(R):
    mapp.append(list(input().strip()))

q = deque()
q.append((0,0,1))
visit[0][0] = True

while q:
    cur = q.popleft()
    if cur[0] == R-1 and cur[1] == C-1:
        print(cur[2])
        break
    for i in range(4):
        nr = cur[0] + dr[i]
        nc = cur[1] + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not visit[nr][nc] and mapp[nr][nc] == '1':
            q.append((nr,nc,cur[2]+1))
            visit[nr][nc] = True