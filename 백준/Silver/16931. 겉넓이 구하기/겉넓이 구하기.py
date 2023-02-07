from sys import stdin

input = stdin.readline

mapp = []
dr = [0,0,1,-1]
dc = [1,-1,0,0]
answer = 0
R, C = map(int, input().split())

for r in range(R):
    mapp.append(list(map(int, input().split())))

for r in range(R):
    for c in range(C):
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if mapp[r][c] > mapp[nr][nc]:
                    answer += mapp[r][c] - mapp[nr][nc]
            else:
                answer += mapp[r][c]

answer += R*C*2

print(answer)