import sys

input = sys.stdin.readline

N = int(input().strip())
k = int(input().strip())

def find_smaller(x:int):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, (x-1) // i)
    return cnt

def find_bigger(x:int):
    cnt = 0
    for i in range(1, N+1):
        cnt += N - min(N, x // i)
    return cnt

down = 1
up = min(N**2, 1e9)
num = -1

while down <= up:
    mid = (down + up) // 2
    if k-1 < find_smaller(mid):
        up = mid - 1
    elif N**2-k < find_bigger(mid):
        down = mid + 1
    else:
        num = mid
        break
print(int(num))