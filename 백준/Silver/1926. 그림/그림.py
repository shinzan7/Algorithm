from sys import stdin
from collections import deque

input = stdin.readline

# https://www.acmicpc.net/problem/1926
R,C = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(R)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
paint_count = 0
largest = 0

def bfs(sr,sc):
    q = deque()
    mapp[sr][sc] = 2
    q.append((sr,sc))
    cnt = 1

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < R and 0 <= nc < C and mapp[nr][nc] == 1:
                mapp[nr][nc] = 2
                q.append((nr,nc))
                cnt += 1
    return cnt

for r in range(R):
    for c in range(C):
        if mapp[r][c] == 1:
            paint_count += 1
            largest = max(largest, bfs(r,c))

print(paint_count)
print(largest)