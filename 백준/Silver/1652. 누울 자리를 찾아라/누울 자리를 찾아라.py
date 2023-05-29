from sys import stdin
input = stdin.readline

N = int(input().rstrip())
mapp = []
w = 0
h = 0
for _ in range(N):
    temp = list(input().strip())
    cnt = 0
    for i in range(N):
        if temp[i] == '.':
            cnt += 1
            if cnt == 2:
                w += 1
        else:
            cnt = 0
    mapp.append(temp)

for c in range(N):
    cnt = 0
    for r in range(N):
        if mapp[r][c] == '.':
            cnt += 1
            if cnt == 2:
                h += 1
        else:
            cnt = 0

print(w, h)