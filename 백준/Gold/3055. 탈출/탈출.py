import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

mapp = [[0 for col in range(C)] for row in range(R)]
visit = [[False for col in range(C)] for row in range(R)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

water = -1
goal = (0,0)
bb = (0,0)
result = 0
is_arrive = False

q_bb = deque()
q_water = deque()

for r in range(R):
    line = sys.stdin.readline().strip()
    for c in range(C):
        mapp[r][c] = line[c]
        if(line[c] == 'D'):
            goal = (r,c)
        elif(line[c] == '*'):
            q_water.appendleft((r,c))
        elif(line[c] == 'S'):
            bb = (r,c)
            mapp[r][c] = '.'

q_bb.appendleft(bb)
visit[bb[0]][bb[1]] = True

while(len(q_bb) != 0):
    size_water = len(q_water)
    size_bb = len(q_bb)

    # 홍수 확장
    while(size_water > 0):
        size_water -= 1
        w = q_water.pop()

        for i in range(4):
            wr = w[0] + dr[i]
            wc = w[1] + dc[i]
            if(wr>=0 and wr<R and wc>=0 and wc<C and mapp[wr][wc] == '.'):
                q_water.appendleft((wr,wc))
                mapp[wr][wc] = '*'

    # 고슴도치 사방탐색
    while(size_bb > 0):
        size_bb -= 1
        cur = q_bb.pop()
        # 도착한 경우
        if(mapp[cur[0]][cur[1]] == 'D'):
            is_arrive = True
            break

        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if(nr>=0 and nr<R and nc>=0 and nc<C and not visit[nr][nc] and (mapp[nr][nc] == '.' or mapp[nr][nc] == 'D')):
                q_bb.appendleft((nr,nc))
                visit[nr][nc] = True

    if(is_arrive):
        break
    
    # 1분 경과
    result += 1

if(not is_arrive):
    result = 'KAKTUS'

print(result)