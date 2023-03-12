from sys import stdin

input = stdin.readline

N = int(input().strip())
prefer = []
for _ in range(N*N):
    prefer.append(list(map(int, input().split())))

mapp = [[0 for _ in range(N)] for _ in range(N)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]
def count_near(r,c,idx):
    favorite = prefer[idx][1:]
    fav_cnt = 0
    empty_cnt = 4
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if mapp[nr][nc] in favorite:
                fav_cnt += 1
                empty_cnt -= 1
            elif mapp[nr][nc] != 0:
                empty_cnt -= 1

        else:
            empty_cnt -= 1
    return (fav_cnt, empty_cnt)

def sitting(idx):
    cr, cc, count, ept_count = -1, -1, -1, -1

    for r in range(N):
        for c in range(N):
            fav, empty = count_near(r,c,idx)
            if mapp[r][c] == 0:
                if fav > count:
                    cr,cc,count,ept_count = r,c,fav,empty
                elif fav == count and empty > ept_count:
                    cr,cc,count,ept_count = r,c,fav,empty
    
    mapp[cr][cc] = prefer[idx][0]

for i in range(N**2):
    sitting(i)

prefer.sort()

def calcul(r,c):
    cnt = 0
    student_idx = mapp[r][c] - 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and mapp[nr][nc] in prefer[student_idx]:
            cnt += 1
    if cnt == 0:
        return 0
    else:
        return 10 ** (cnt-1)

answer = 0
for r in range(N):
    for c in range(N):
        answer += calcul(r,c)

print(answer)