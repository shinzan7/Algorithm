import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
div = []
for i in range(1, N+1):
    div = div + list(combinations(arr, i))
cnt = 0
for d in div:
    if sum(d) == S:
        cnt += 1
print(cnt)