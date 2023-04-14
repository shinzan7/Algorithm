from sys import stdin

input = stdin.readline

N = int(input().strip())
answer = 0

for i in range(1, N+1):
    answer += (N // i) * i

print(answer)