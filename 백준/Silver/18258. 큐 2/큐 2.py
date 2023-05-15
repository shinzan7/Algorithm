from sys import stdin
from collections import deque

input = stdin.readline

N = int(input().strip())
q = deque()
for _ in range(N):
    orders = list(input().split())
    o = orders[0]
    if o == 'push':
        q.append(int(orders[1]))
    elif o == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif o == 'size':
        print(len(q))
    elif o == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif o == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif o == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)