from sys import stdin

input = stdin.readline

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input().strip()))

down = 1
up = max(arr)
answer = 1

while down <= up:
    mid = (down + up) // 2
    cnt = 0

    for lan in arr:
        cnt += (lan // mid)
    if cnt >= N:
        down = mid+1
        answer = max(answer, mid)
    else:
        up = mid-1

print(answer)