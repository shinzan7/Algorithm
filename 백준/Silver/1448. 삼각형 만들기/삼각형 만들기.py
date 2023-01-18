import sys

input = sys.stdin.readline

N = int(input().strip())
lines = []

for i in range(N):
    a = int(input().strip())
    lines.append(a)

lines.sort(reverse=True)
answer = -1

for i in range(N-2):
    if lines[i] < lines[i+1] + lines[i+2]:
        answer = lines[i] + lines[i+1] + lines[i+2]
        break

print(answer)