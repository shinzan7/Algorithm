from sys import stdin
from collections import deque

input = stdin.readline

N = int(input().strip())
r1, c1, r2, c2 = map(int, input().split())

dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]
visit = [[False for _ in range(N)] for _ in range(N)]

q = deque()
q.append((r1,c1, 0))
visit[r1][c1] = True
is_arrive = False

while q:
    cr, cc, count = q.popleft()
    if cr == r2 and cc == c2:
        is_arrive = True
        print(count)
        break
    for i in range(6):
        nr = cr + dr[i]
        nc = cc + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
            q.append((nr,nc,count+1))
            visit[nr][nc] = True

if not is_arrive:
    print(-1)