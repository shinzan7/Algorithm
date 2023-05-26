from sys import stdin

input = stdin.readline

N,L = map(int, input().split())
water = []
for _ in range(N):
    water.append(list(map(int, input().split())))
water.sort()

water = sorted(water, key = lambda x : (x[0],-x[1]))
cur = 0
count = 0

for start, end in water:
    if cur > start:
        start = cur
    while start < end:
        start += L
        count += 1
    cur = start

print(count)