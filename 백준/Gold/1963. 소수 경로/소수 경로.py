from sys import stdin
from collections import deque

input = stdin.readline

is_decimal = [True] * 10000
for i in range(2,100):
    if is_decimal[i] == True:
        for j in range(i*2, 10000, i):
            is_decimal[j] = False

def bfs(start, end):
    visit = [False] * 10000
    q = deque()
    q.append((start, 0))
    visit[start] = True
    is_arrive = False

    while q:
        cur, cnt = q.popleft()
        if cur == end:
            is_arrive = True
            break
        string = str(cur)
        for i in range(4):
            for n in range(10):
                temp_str = string[:i] + str(n) + string[i+1:]
                temp = int(temp_str)
                if temp >= 1000 and is_decimal[temp] and not visit[temp]:
                    q.append((temp, cnt+1))
                    visit[temp] = True
    
    if is_arrive:
        print(cnt)
    else:
        print('Impossible')

T = int(input().strip())
for _ in range(T):
    start, end = map(int, input().split())
    bfs(start, end)