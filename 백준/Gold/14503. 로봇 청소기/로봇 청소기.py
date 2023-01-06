import sys

N, M = map(int, sys.stdin.readline().split())

mapp = [[0 for col in range(M)] for row in range(N)]

cr, cc, d = map(int, sys.stdin.readline().split())
# d : 0123 북동남서
dir = [(-1,0), (0,1), (1,0), (0,-1)]

for r in range(N):
    mapp[r] = list(map(int, sys.stdin.readline().split()))

clean = 0
check = 0

while(True):
    if(mapp[cr][cc] == 0):
        clean += 1
        mapp[cr][cc] = 2
    lr = cr + dir[d-1][0]
    lc = cc + dir[d-1][1]
    # 왼쪽방향이 청소하지 않은장소면
    if(check != 4 and mapp[lr][lc] == 0):
        check = 0
        d -= 1
        if(d == -1):
            d = 3
        cr = lr
        cc = lc
    # 청소했거나 벽이면
    elif(check != 4):
        check += 1
        d -= 1
        if(d == -1):
            d = 3
    # 4방향 모두 확인했다면
    else:
        check = 0
        nr = cr + dir[d-2][0]
        nc = cc + dir[d-2][1]
        # 뒤쪽이 벽이면 종료
        if(mapp[nr][nc] == 1):
            break
        else:
            cr = nr
            cc = nc

print(clean)