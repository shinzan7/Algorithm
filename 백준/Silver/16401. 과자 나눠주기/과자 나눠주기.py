from sys import stdin

input = stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

up = max(snacks)
down = 1
answer = 0

while up >= down:
    count = 0
    mid = (up + down) // 2
    
    for s in snacks:
        if s >= mid:
            count += (s // mid)
    
    if count >= M:
        answer = mid
        down = mid + 1
    else:
        up = mid - 1

print(answer)