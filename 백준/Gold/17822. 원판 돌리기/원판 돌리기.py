from sys import stdin
from collections import deque

input = stdin.readline

# https://www.acmicpc.net/problem/17822

R,C,T = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(R)]

# 원판 x배수 k번 회전 (d방향)
def rotate(x, d, k):
    # global mapp
    kk = k % C
    idx = x

    #시계방향
    if d == 0:
        while idx <= R:
            for _ in range(kk):
                mapp[idx-1].insert(0, mapp[idx-1].pop(-1))
            idx += x
    #반시계방향
    else:
        while idx <= R:
            for _ in range(kk):
                mapp[idx-1].append(mapp[idx-1].pop(0))
            idx += x

dr = [1,-1,0,0]
dc = [0,0,1,-1]
# 지정위치에 인접하면서 같은 숫자 있는지 체크
def check_same(r, c):
    if mapp[r][c] == 0:
        return False
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R:
            if nc == C:
                nc = 0
            if mapp[r][c] == mapp[nr][nc]:
                return True
    return False    

# 원판 인접한 수 bfs로 모두 제거
def bfs(r,c):
    # global mapp
    q = deque()
    q.append((r,c,mapp[r][c]))
    mapp[r][c] = 0

    while q:
        cr, cc, num = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < R:
                if nc == C:
                    nc = 0
                elif nc == -1:
                    nc = C-1
                if mapp[nr][nc] == num:
                    q.append((nr, nc, num))
                    mapp[nr][nc] = 0

# 인접한 수가 없다면
def same_nothing():
    total = 0
    cnt = 0
    for r in range(R):
        for c in range(C):
            if mapp[r][c] != 0:
                total += mapp[r][c]
                cnt += 1
    if cnt == 0:
        return
    average = total / cnt
    for r in range(R):
        for c in range(C):
            if mapp[r][c] != 0:
                if mapp[r][c] > average:
                    mapp[r][c] -= 1
                elif mapp[r][c] < average:
                    mapp[r][c] += 1
    

# 전체 원판에서 지울 것 있는지 검사하여 규칙이행
def erase():
    # global mapp
    same_exist = False
    for r in range(R):
        for c in range(C):
            if check_same(r,c):
                same_exist = True
                bfs(r,c)
    if not same_exist:
        same_nothing()

for _ in range(T):
    # x 원판번호, d 0시계 1반시계, k번 회전
    x, d, k = map(int, input().split())
    rotate(x,d,k)
    erase()

answer = 0
for r in range(R):
    for c in range(C):
        answer += mapp[r][c]

print(answer)