import sys
from collections import deque

N = int(sys.stdin.readline().strip())

mapp = [[0 for col in range(N)] for row in range(N)]
visit = [[False for col in range(N)] for row in range(N)]
result = 0
# 동남
dr = [0, 1]
dc = [1, 0]

for r in range(N):
    line = sys.stdin.readline().strip()
    for c in range(N):
        mapp[r][c] = line[c]

# 최대개수 행 검사
def find_row(row):
    global result
    cnt = 0
    a = ' '
    for c in range(N):
        if(a==mapp[row][c]):
            cnt += 1
        else:
            if(cnt > result):
                result = cnt
            cnt = 1
            a = mapp[row][c]
        if(cnt > result):
            result = cnt
# 최대개수 열 검사
def find_col(col):
    global result
    cnt = 0
    a = ' '
    for r in range(N):
        if(a==mapp[r][col]):
            cnt += 1
        else:
            if(cnt > result):
                result = cnt
            cnt = 1
            a = mapp[r][col]
        if(cnt > result):
            result = cnt
# 초기상태 최대개수 갱신
for r in range(N):
    find_row(r)
for c in range(N):
    find_col(c)

q = deque()
q.appendleft((0,0))

while(len(q) != 0):
    cnt = 0
    cur = q.pop()
    if(visit[cur[0]][cur[1]]):
        continue
    visit[cur[0]][cur[1]] = True
    for i in range(2):
        nr = cur[0] + dr[i]
        nc = cur[1] + dc[i]
        # 범위 안이고 방문하지 않으면 위치 바꿔보기
        if(nr>=0 and nr<N and nc>=0 and nc<N and not visit[nr][nc]):
            q.appendleft((nr, nc))
            if(mapp[cur[0]][cur[1]] == mapp[nr][nc]):
                continue
            origin_1 = mapp[cur[0]][cur[1]]
            origin_2 = mapp[nr][nc]
            mapp[nr][nc] = origin_1
            mapp[cur[0]][cur[1]] = origin_2

            # 좌우교환일때 최대개수 갱신
            if(i == 0):
                find_row(cur[0])
                find_col(cur[1])
                find_col(nc)
            # 상하교환일때 최대개수 갱신
            else:
                find_row(cur[0])
                find_row(nr)
                find_col(cur[1])

            if(result < cnt):
                result = cnt
            # 바꾼위치 원래대로
            mapp[nr][nc] = origin_2
            mapp[cur[0]][cur[1]] = origin_1

print(result)