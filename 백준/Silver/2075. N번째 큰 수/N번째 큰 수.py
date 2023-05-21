from sys import stdin
import heapq

input = stdin.readline

N = int(input().strip())
q = []
temp = list(map(int, input().split()))
for t in temp:
    heapq.heappush(q, t)

for _ in range(N-1):
    temp = list(map(int, input().split()))

    for t in temp:
        if q[0] < t:
            heapq.heapreplace(q, t)

print(heapq.heappop(q))