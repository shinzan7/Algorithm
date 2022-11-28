import sys
import collections

start, end = map(int, sys.stdin.readline().split())

q = collections.deque([])
is_visit = [False] * 100001
count = 0
flag = False
q.append(start)
is_visit[start] = True

while(start != end):
    size = len(q)

    while(size > 0): # 한바퀴 돌기
        cur = q.popleft()
        size -= 1

        if(cur == end):
            flag = True
            break
        #왼쪽
        if(cur>0 and not is_visit[cur - 1]):
            q.append(cur - 1)
            is_visit[cur - 1] = True
        #오른쪽
        if(cur<100000 and not is_visit[cur + 1]):
            q.append(cur + 1)
            is_visit[cur + 1] = True
        #순간이동
        if(cur<=50000 and not is_visit[cur * 2]):
            q.append(cur * 2)
            is_visit[cur * 2] = True
    
    if(flag):
        break
    else:
        count += 1

print(count)