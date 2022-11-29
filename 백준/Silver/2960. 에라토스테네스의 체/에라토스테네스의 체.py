import sys
import collections

N, K = map(int, sys.stdin.readline().split())

q = collections.deque(range(2,N+1))
count = 0
flag = False
result = 0

for _ in range(1,N):
    num = q.popleft()
    count += 1
    p = collections.deque([])
    if(count == K):
        flag = True
        result = num
        break
    
    for i in q:
        if(i % num != 0):
            p.append(i)
        else:
            count += 1
            if(count == K):
                flag = True
                result = i
                break
    if(flag):
        break
    q = p.copy()

print(result)