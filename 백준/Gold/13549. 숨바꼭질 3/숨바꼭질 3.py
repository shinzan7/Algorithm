import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque()
MAX = 100001
visit = [False] * MAX
dist = [-1] * MAX

q.appendleft(N)
visit[N] = True
dist[N] = 0

while q:
    cur = q.pop()
    if cur == K:
        break

    if(cur*2 < MAX and not visit[cur*2]):
        q.append(cur*2)
        visit[cur*2] = True
        dist[cur*2] = dist[cur]
    if(cur+1 < MAX and not visit[cur+1]):
        q.appendleft(cur+1)
        visit[cur+1] = True
        dist[cur+1] = dist[cur] + 1
    if(cur-1 >= 0 and not visit[cur-1]):
        q.appendleft(cur-1)
        visit[cur-1] = True
        dist[cur-1] = dist[cur] + 1

print(dist[K])