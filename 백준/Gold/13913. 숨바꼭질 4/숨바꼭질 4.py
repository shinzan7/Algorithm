import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
max = 100000
visit = [-1 for _ in range(max+1)]
path = []

def bfs(start, target):
    q = deque()
    q.append(n)
    visit[start] = start

    while q:
        cur = q.popleft()
        if cur == target:
            idx = cur
            while idx != start:
                path.append(idx)
                idx = visit[idx]
            path.append(start)
            return len(path) - 1
        if cur+1 <= max and visit[cur+1] == -1:
            q.append(cur+1)
            visit[cur+1] = cur
        if cur-1 >= 0 and visit[cur-1] == -1:
            q.append(cur-1)
            visit[cur-1] = cur
        if cur*2 <= max and visit[cur*2] == -1:
            q.append(cur*2)
            visit[cur*2] = cur

print(bfs(n,k))
print(*path[::-1])