import sys

n = int(sys.stdin.readline().strip())

arr = map(int, sys.stdin.readline().split())

arr = sorted(arr)
minn = arr[0] + arr[-1]

for i in range(n):
    team = arr[i] + arr[2*n - 1 - i]
    if(minn > team):
        minn = team

print(minn)