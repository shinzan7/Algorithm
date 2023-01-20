import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())
q = deque(range(1, n+1))

while len(q) > 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)

print(q[0])