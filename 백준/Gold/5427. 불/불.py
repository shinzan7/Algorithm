from sys import stdin
from collections import deque

input = stdin.readline

T = int(input().strip())
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def is_in(r,c):
    return 0 <= r < R and 0 <= c < C

# 불과 상근이의 큐를 2개 돌리면서 탈출구를 찾는다
def escape(fq, q):
    time = 0
    while q:
        time += 1
        size = len(fq)
        while size > 0:
            size -= 1
            fr, fc = fq.popleft()
            for i in range(4):
                nr = fr + dr[i]
                nc = fc + dc[i]
                if is_in(nr,nc) and mapp[nr][nc] == '.':
                    fq.append((nr,nc))
                    mapp[nr][nc] = '*'
        size = len(q)
        while size > 0:
            size -= 1
            cr, cc = q.popleft()
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if is_in(nr,nc) and mapp[nr][nc] == '.':
                    q.append((nr,nc))
                    mapp[nr][nc] = '@'
                elif not is_in(nr,nc):
                    return time
    
    return 'IMPOSSIBLE'

for _ in range(T):
    C,R = map(int, input().split())
    mapp = []
    fire = []
    sr, sc = 0,0
    for r in range(R):
        temp = list(input().strip())
        for c in range(C):
            if temp[c] == '.' or temp[c] == '#':
                continue
            elif temp[c] == '*':
                fire.append((r,c))
            else:
                sr = r
                sc = c

        mapp.append(temp)
    
    fq = deque()
    for fr,fc in fire:
        fq.append((fr,fc))
    q = deque()
    q.append((sr,sc))
    print(escape(fq,q))