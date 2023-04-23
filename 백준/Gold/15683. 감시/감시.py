from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/15683

R, C = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(R)]
# 상우하좌 0123
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# cctv 감시 (after으로 origin을 덮어씌운다)
def cctv(r,c,d,origin, after):
    nr = r + dr[d]
    nc = c + dc[d]
    while 0 <= nr < R and 0 <= nc < C:
        if mapp[nr][nc] == 6:
            break
        elif mapp[nr][nc] == origin:
            mapp[nr][nc] = after
        
        nr += dr[d]
        nc += dc[d]

cctv_list = []
for r in range(R):
    for c in range(C):
        if 0 < mapp[r][c] < 6:
            cctv_list.append([r,c,mapp[r][c]])
NUM = len(cctv_list)

def count_blind():
    count = 0
    for r in range(R):
        for c in range(C):
            if mapp[r][c] == 0:
                count += 1
    return count

answer = 1e9

def dfs(idx):
    global answer
    if idx == NUM:
        answer = min(answer, count_blind())
        return
    cr, cc, num = cctv_list[idx]
    # cctv 번호대로 적용
    if num == 1:
        # 상,하,좌,우 4번
        for i in range(4):
            cctv(cr, cc, i, 0, -idx-1)
            dfs(idx + 1)
            cctv(cr, cc, i, -idx-1, 0)
    elif num == 2:
        # 상하,좌우 2번
        for i in range(2):
            cctv(cr, cc, i, 0, -idx-1)
            cctv(cr, cc, i+2, 0, -idx-1)
            dfs(idx + 1)
            cctv(cr, cc, i, -idx-1, 0)
            cctv(cr, cc, i+2, -idx-1, 0)
    elif num == 3:
        # 상우, 우하, 하좌, 좌상 4번
        for i in range(4):
            cctv(cr, cc, i, 0, -idx-1)
            cctv(cr, cc, (i+1)%4, 0, -idx-1)
            dfs(idx + 1)
            cctv(cr, cc, i, -idx-1, 0)
            cctv(cr, cc, (i+1)%4, -idx-1, 0)
    elif num == 4:
        # 상,하,좌,우 빼고 4번
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                cctv(cr, cc, j, 0, -idx-1)
            dfs(idx + 1)
            for j in range(4):
                if i == j:
                    continue
                cctv(cr, cc, j, -idx-1, 0)
    else:
        # 상하좌우 모든방향 1번
        for i in range(4):
            cctv(cr,cc,i,0,-idx-1)
        dfs(idx + 1)
        for i in range(4):
            cctv(cr,cc,i,-idx-1,0)

dfs(0)
print(answer)