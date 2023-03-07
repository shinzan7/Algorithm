from sys import stdin
from collections import deque

input = stdin.readline

C,R,H = map(int, input().split())
box = [[] for _ in range(H)]
new_tomatoes = 0
q = deque()

for h in range(H):
    for r in range(R):
        temp = list(map(int, input().split()))
        box[h].append(temp)
        for c in range(C):
            if temp[c] == 1:
                q.append((h,r,c))
            elif temp[c] == 0:
                new_tomatoes += 1

# 1익음 0안익음 -1없음
dir = [(0,0,1), (0,0,-1), (1,0,0), (-1,0,0), (0,1,0), (0,-1,0)]
day = 0

if new_tomatoes == 0:
    print(0)
else:
    while q:
        if new_tomatoes == 0:
            break
        size = len(q)
        while size > 0:
            size -= 1
            h,r,c = q.popleft()
            for i in range(6):
                nh = h + dir[i][0]
                nr = r + dir[i][1]
                nc = c + dir[i][2]

                if 0 <= nh < H and 0 <= nr < R and 0 <= nc < C and box[nh][nr][nc] == 0:
                    box[nh][nr][nc] = 1
                    new_tomatoes -= 1
                    q.append((nh,nr,nc))
        day += 1
    
    if new_tomatoes == 0:
        print(day)
    else:
        print(-1)