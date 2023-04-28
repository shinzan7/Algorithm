from sys import stdin
from collections import deque

input = stdin.readline

# https://www.acmicpc.net/problem/16946
R, C = map(int, input().split())
mapp = [list(map(int, input().strip())) for _ in range(R)]

# 빈칸의 집합의 개수를 세고 집합마다 개수 저장
visited = [[False for _ in range(C)] for _ in range(R)]
group = [[[0,0] for _ in range(C)] for _ in range(R)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

# 빈칸에 대해서 bfs를 탐색하고 같은 영역인 방의 위치들을 group에 저장한다
def bfs(r,c, num):
    q = deque()
    arr = [(r,c)]
    q.append((r,c))
    visited[r][c] = True

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < R and 0 <= nc < C and mapp[nr][nc] == 0 and not visited[nr][nc]:
                arr.append((nr,nc))
                q.append((nr,nc))
                visited[nr][nc] = True
    
    count = len(arr)
    # 그룹의 요소에 대하여 모두 [그룹번호, 개수]를 저장해준다
    for gr, gc in arr:
        group[gr][gc] = [num, count]

num = 1
for r in range(R):
    for c in range(C):
        if mapp[r][c] == 0 and group[r][c][0] == 0:
            bfs(r,c, num)
            num += 1

answer = [[0]*C for _ in range(R)]
# 벽마다 사방탐색을 하여 빈칸이라면 그룹번호와 개수를 추가한다.
# 이미 추가한 그룹번호의 경우는 건너뛴다.
for r in range(R):
    for c in range(C):
        if mapp[r][c] == 1:
            groups = []
            # 현재위치의 방도 개수에 추가
            cnt = 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and mapp[nr][nc] == 0 and group[nr][nc][0] not in groups:
                   # 그룹번호와 개수 저장
                   groups.append(group[nr][nc][0])
                   cnt += group[nr][nc][1]
            answer[r][c] = cnt % 10

for r in range(R):
    print(''.join(map(str, answer[r])))