import sys

input = sys.stdin.readline

N = int(input().strip())
city = list(map(int, input().split()))
maximum = int(input().strip())

down = 0
up = max(city)
result = -1

while down <= up:
    mid = (down + up) // 2
    current = 0

    for money in city:
        current += min(money, mid)
    
    if current <= maximum:
        down = mid + 1
        result = mid
    elif current > maximum:
        up = mid - 1

print(result)