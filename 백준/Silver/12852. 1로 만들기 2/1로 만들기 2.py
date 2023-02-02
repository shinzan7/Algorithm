import sys
from collections import deque

input = sys.stdin.readline
visit = [0] * (int(1e6) + 1)
N = int(input().strip())
q = deque()

visit[N] = -1
q.append(N)

while q:
    cur = q.popleft()
    if cur % 3 == 0 and visit[cur//3] == 0:
        visit[cur//3] = cur
        q.append(cur//3)
    if cur % 2 == 0 and visit[cur//2] == 0:
        visit[cur//2] = cur
        q.append(cur//2)
    if cur > 1 and visit[cur-1] == 0:
        visit[cur-1] = cur
        q.append(cur-1)

result = []
idx = 1
while idx != N:
    result.append(idx)
    idx = visit[idx]
result.append(N)

print(len(result)-1)
print(*result[::-1])