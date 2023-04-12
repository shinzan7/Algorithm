from sys import stdin

input = stdin.readline

N = int(input().strip())
arr = map(int, input().split())
answer = 0

for n in arr:
    e = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                e += 1
        if e == 0:
            answer += 1

print(answer)