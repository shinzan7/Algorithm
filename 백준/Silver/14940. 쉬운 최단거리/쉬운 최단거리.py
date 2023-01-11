from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().split())

mapp = [[0 for col in range(C)] for row in range(R)]
visit = [[False for col in range(C)] for row in range(R)]
start = (0,0,0)
found_start = False

for r in range(R):
    mapp[r] = list(map(int, stdin.readline().split()))

    # 출발지점 찾기
    if(not found_start):
        for c in range(C):
            if(mapp[r][c] == 2):
                found_start = True
                start = (r,c,0)

q = deque()
q.appendleft(start)
visit[start[0]][start[1]] = True
mapp[start[0]][start[1]] = start[2]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

while q:
    cur = q.pop()

    for i in range(4):
        nr = cur[0] + dr[i]
        nc = cur[1] + dc[i]
        if(nr>=0 and nr<R and nc>=0 and nc<C and not visit[nr][nc] and mapp[nr][nc] != 0):
            q.appendleft((nr, nc, cur[2]+1))
            visit[nr][nc] = True
            mapp[nr][nc] = cur[2]+1

for r in range(R):
    for c in range(C):
        if(not visit[r][c] and mapp[r][c] == 1):
            mapp[r][c] = -1

for r in range(R):
    for c in range(C):
        print(mapp[r][c], end=' ')
    print()