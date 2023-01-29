import sys

input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))
prefix = []
a = 0
for i in range(M):
    a += arr[i]
    prefix.append(a)

for i in range(N):
    start, end = map(int, input().split())
    if start == 1:
        print(prefix[end-1])
    else:
        print(prefix[end-1] - prefix[start-2])