from sys import stdin

input = stdin.readline

N = int(input().strip())
M = int(input().strip())
point = list(map(int, input().split()))

cur = 0
diff = point[0]

for i in range(M-1):
    temp = point[i+1] - point[i]
    if temp % 2 == 0:
        temp = temp // 2
    else:
        temp = temp // 2 + 1

    diff = max(diff, temp)

diff = max(diff, N - point[-1])

print(diff)