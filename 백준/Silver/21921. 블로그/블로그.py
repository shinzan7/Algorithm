from sys import stdin

input = stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

answer = sum(arr[:X])
cur = answer
count = 1

for i in range(X, N):
    cur -= arr[i-X]
    cur += arr[i]
    if cur > answer:
        count = 1
        answer = cur
    elif cur == answer:
        count += 1

if answer == 0:
    print('SAD')
else:
    print(answer)
    print(count)