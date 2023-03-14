from sys import stdin

input = stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

M = int(input().strip())
arr = list(map(int, input().split()))

def is_exist(n):
    down = 0
    up = N-1
    
    while down <= up:
        mid = (down + up) // 2

        if A[mid] == n:
            return 1
        elif A[mid] < n:
            down = mid + 1
        else:
            up = mid - 1
    
    return 0

for a in arr:
    print(is_exist(a))