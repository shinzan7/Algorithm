import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

sums = []

for i in range(1, N+1):
    a = combinations(arr, i)
    for j in a:
        sums.append(sum(j))

sums = list(set(sums))
sums.sort()
n, idx = 1,0

for i in sums:
    if i!=n:
        break
    n += 1

print(n)