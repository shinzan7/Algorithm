import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    x = int(input().strip())
    house.append(x)
house.sort()

result = 0
down = 1
up = house[-1] - house[0]
while down <= up:
    mid = (down + up) // 2
    cnt = 1
    prev = house[0]
    
    for i in range(1,N):
        if house[i] - prev >= mid:
            cnt += 1
            prev = house[i]
    
    if cnt >= C:
        result = max(result, mid)
        down = mid + 1
    else:
        up = mid - 1

print(result)