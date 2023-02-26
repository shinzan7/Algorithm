from sys import stdin
from collections import deque

input = stdin.readline

N,M = map(int, input().split())
mapp = [0 for _ in range(101)]
visit = [False for _ in range(101)]

for _ in range(N):
    a, b = map(int, input().split())
    mapp[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    mapp[a] = b

def bfs():
    q = deque()
    q.append((1,0))
    visit[1] = True

    while q:
        size = len(q)
        while size > 0:
            size -= 1
            cur, cnt = q.popleft()
            if cur == 100:
                return cnt
            for i in range(1,7):
                next = cur + i
                if next <= 100 and not visit[next]:
                    visit[next] = True
                    if mapp[next] == 0:
                        q.append((next, cnt+1))
                    else:
                        visit[mapp[next]] = True
                        q.append((mapp[next], cnt+1))

print(bfs())