from sys import stdin
from collections import deque

input = stdin.readline

F,S,G,U,D = map(int, input().split())
visit = [False] * (F+1)
visit[0] = True
q = deque()
q.append((S,0))
visit[S] = True
answer = 'use the stairs'

while q:
    cur, cnt = q.popleft()
    if cur == G:
        answer = cnt
        break
    up = cur + U
    down = cur - D
    if up <= F and not visit[up]:
        q.append((up, cnt+1))
        visit[up] = True
    if down >= 1 and not visit[down]:
        q.append((down, cnt+1))
        visit[down] = True

print(answer)