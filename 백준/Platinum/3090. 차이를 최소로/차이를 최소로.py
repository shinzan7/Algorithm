import sys

input = sys.stdin.readline

N, T = map(int, input().split())
nums = list(map(int, input().split()))

def count_change(d, arr):
    cnt = 0
    for i in range(N-1):
        diff = arr[i+1] - arr[i]
        if diff > d:
            cnt += diff - d
            arr[i+1] = arr[i] + d
    for i in range(N-1, 0, -1):
        diff = arr[i-1] - arr[i]
        if diff > d:
            cnt += diff - d
            arr[i-1] = arr[i] + d
    return cnt

down = 0
up = max(nums)
result = []

while down <= up:
    mid = (down + up) // 2
    arr = nums[:]
    count = count_change(mid, arr)
    if T < count:
        down = mid + 1
    else:
        up = mid - 1
        result = arr[:]

for i in range(N):
    print(result[i], end=' ')