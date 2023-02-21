from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] += arr[i-1]

answer = 0

for i in range(N):
    if arr[i] < M:
        continue
    elif arr[i] == M:
        answer += 1
        continue

    for j in range(i):
        num = arr[i] - arr[j]
        if num == M:
            answer += 1
            break
        elif num < M:
            break
    
print(answer)