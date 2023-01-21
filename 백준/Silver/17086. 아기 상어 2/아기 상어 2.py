import sys
from collections import deque

input = sys.stdin.readline
R,C = map(int, input().split())

mapp = []
q = deque()
for r in range(R):
    arr = list(map(int, input().split()))
    mapp.append(arr)
    for c in range(C):
        if mapp[r][c] == 1:
            q.append((r,c,1))

dr = [0,0,1,-1,-1,-1,1,1]
dc = [1,-1,0,0,-1,1,-1,1]

def bfs():
    while q:
        cr, cc, dist = q.popleft()

        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<= nr <R and 0 <= nc < C and mapp[nr][nc] == 0:
                q.append((nr, nc, dist+1))
                mapp[nr][nc] = dist+1
    return

bfs()

result = 1
for r in range(R):
    for c in range(C):
        result = max(result, mapp[r][c])

print(result - 1)