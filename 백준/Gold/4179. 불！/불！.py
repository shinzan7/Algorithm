from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().split())

mapp = [[',' for col in range(C)] for row in range(R)]
visit = [[False for col in range(C)] for row in range(R)]
jq = deque()
fq = deque()

for r in range(R):
    strr = stdin.readline().strip()
    for c in range(C):
        mapp[r][c] = strr[c]
        if(strr[c] == 'J'):
            jq.appendleft((r,c))
            visit[r][c] = True
            mapp[r][c] = '.'
        elif(strr[c] == 'F'):
            fq.appendleft((r,c))

dr = [0,0,1,-1]
dc = [1,-1,0,0]
result = 0
arrive = False

def inside(r, c):
    return r>=0 and r<R and c>=0 and c<C

while jq:
    fq_size = len(fq)
    while(fq_size > 0):
        fire = fq.pop()
        fq_size -= 1

        for i in range(4):
            nr = fire[0] + dr[i]
            nc = fire[1] + dc[i]
            if(inside(nr, nc) and mapp[nr][nc] == '.'):
                mapp[nr][nc] = 'F'
                fq.appendleft((nr,nc))
        
    jq_size = len(jq)
    while(jq_size > 0):
        j = jq.pop()
        jq_size -= 1

        for i in range(4):
            nr = j[0] + dr[i]
            nc = j[1] + dc[i]
            if(not inside(nr, nc)):
                arrive = True
                break
            elif(mapp[nr][nc]=='.' and not visit[nr][nc]):
                jq.appendleft((nr,nc))
                visit[nr][nc] = True        
        if(arrive):
            break
    result += 1

    if(arrive):
        break

if(arrive):
    print(result)
else:
    print('IMPOSSIBLE')