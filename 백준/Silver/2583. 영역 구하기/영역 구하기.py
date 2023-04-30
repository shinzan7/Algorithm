from sys import stdin
from collections import deque

input = stdin.readline

# https://www.acmicpc.net/problem/2583

R, C, K = map(int,input().split())
mapp = [[0] * C for _ in range(R)]
# 빈칸 0, 직사각형 구간 1
def fill(a,b,x,y):
    # x,y는 모눈종이임을 고려해서 -1씩 하여 배열과 같게 한다
    x -= 1
    y -= 1
    for r in range(b,y+1):
        for c in range(a,x+1):
            mapp[r][c] = 1

for _ in range(K):
    a,b,x,y = map(int, input().split())
    fill(a,b,x,y)

answer = []
dr = [0,0,1,-1]
dc = [1,-1,0,0]

# 빈칸이지만 이미 방문한 곳은 2로 바꾼다
def bfs(r,c):
    q = deque()
    count = 1
    q.append((r,c))
    mapp[r][c] = 2

    while q:
        cr, cc = q.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < R and 0 <= nc < C and mapp[nr][nc] == 0:
                count += 1
                q.append((nr,nc))
                mapp[nr][nc] = 2
    return count

for r in range(R):
    for c in range(C):
        if mapp[r][c] == 0:
            answer.append(bfs(r,c))
answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))