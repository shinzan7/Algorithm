from sys import stdin

N = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
arr = sorted(arr)
result = 0

for i in range(N):
    cur = arr[i]
    rest = arr[:i] + arr[i+1:]
    l = 0
    r = len(rest) - 1
    while l < r:
        summ = rest[l] + rest[r]
        if cur == summ:
            result += 1
            break
        elif cur > summ:
            l += 1
        else:
            r -= 1

print(result)