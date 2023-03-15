from sys import stdin
from collections import deque

input = stdin.readline

a, b = map(int, input().split())

answer = -1
q = deque()
q.append((a,1))

while q:
    n, cnt = q.popleft()
    if n == b:
        answer = cnt
        break

    if n * 2 <= b:
        q.append((n*2, cnt+1))
    if n * 10 + 1 <= b:
        q.append((n*10+1, cnt+1))

print(answer)